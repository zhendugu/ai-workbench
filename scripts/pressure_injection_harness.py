#!/usr/bin/env python3
"""
Pressure Injection Harness for J8 Testing

This script provides a minimal viable pressure injection toolchain
for testing frontend and backend behavior under stress conditions.

Usage:
    python3 pressure_injection_harness.py --profile P1
    python3 pressure_injection_harness.py --profile P2 --duration 60
    python3 pressure_injection_harness.py --profile P6 --duration 120

Dependencies:
    - Python 3.7+
    - flask (for mock backend server)
    - requests (for concurrent request injection)
"""

import argparse
import time
import random
import threading
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import sys

# Pressure profile configurations
PRESSURE_PROFILES = {
    "P0": {
        "latency": (0, 0.1),
        "jitter": 0,
        "error_rate": 0.0,
        "rate_limit": False,
        "concurrency": 5,
    },
    "P1": {
        "latency": (5.0, 5.0),  # Fixed 5 seconds
        "jitter": 0,
        "error_rate": 0.0,
        "rate_limit": False,
        "concurrency": 5,
    },
    "P2": {
        "latency": (0.1, 8.0),  # Variable 100ms - 8s
        "jitter": 2.0,  # ±2 seconds
        "error_rate": 0.0,
        "rate_limit": False,
        "concurrency": 5,
    },
    "P3": {
        "latency": (0, 0.1),
        "jitter": 0,
        "error_rate": 0.5,  # 50% error rate
        "rate_limit": False,
        "concurrency": 5,
    },
    "P4": {
        "latency": (0, 0.1),
        "jitter": 0,
        "error_rate": 1.0,  # 100% error rate (429)
        "rate_limit": True,
        "concurrency": 5,
    },
    "P5": {
        "latency": (0, 0.1),
        "jitter": 0,
        "error_rate": 0.0,
        "rate_limit": False,
        "concurrency": 50,  # High concurrency
    },
    "P6": {
        "latency": (1.0, 6.0),  # Variable 1s - 6s
        "jitter": 1.5,  # ±1.5 seconds
        "error_rate": 0.3,  # 30% error rate
        "rate_limit": 0.2,  # 20% rate limit
        "concurrency": 40,  # High concurrency
    },
}

# Mock backend data
MOCK_CAPABILITIES = [
    {"id": "C-MD-HTML-001", "name": "Markdown to HTML Conversion", "description": "Converts Markdown document to HTML format"},
    {"id": "C-TEXT-SUM-001", "name": "Text Summarization", "description": "Summarizes text document"},
    {"id": "C-LANG-TRANS-001", "name": "Language Translation", "description": "Translates text between languages"},
    {"id": "C-DATA-VAL-001", "name": "Data Validation", "description": "Validates data structure"},
    {"id": "C-FORMAT-NORM-001", "name": "Format Normalization", "description": "Normalizes data format"},
]

MOCK_PATTERNS = [
    {"id": "P-MD-CONV-001", "name": "Markdown Conversion Pattern", "description": "Pattern for Markdown conversion", "capabilityId": "C-MD-HTML-001"},
    {"id": "P-TEXT-SUM-001", "name": "Text Summarization Pattern", "description": "Pattern for text summarization", "capabilityId": "C-TEXT-SUM-001"},
    {"id": "P-LANG-TRANS-001", "name": "Language Translation Pattern", "description": "Pattern for language translation", "capabilityId": "C-LANG-TRANS-001"},
]


class PressureInjectionHandler(BaseHTTPRequestHandler):
    """HTTP request handler with pressure injection"""
    
    def __init__(self, *args, profile=None, **kwargs):
        self.profile = profile
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests with pressure injection"""
        parsed_path = urlparse(self.path)
        
        # Apply latency
        if self.profile:
            latency_min, latency_max = self.profile["latency"]
            jitter = self.profile["jitter"]
            
            # Calculate delay
            base_delay = random.uniform(latency_min, latency_max)
            jitter_delay = random.uniform(-jitter, jitter) if jitter > 0 else 0
            total_delay = max(0, base_delay + jitter_delay)
            
            time.sleep(total_delay)
        
        # Apply error rate
        if self.profile and self.profile["error_rate"] > 0:
            if random.random() < self.profile["error_rate"]:
                # Rate limit (429)
                if self.profile.get("rate_limit") and random.random() < self.profile.get("rate_limit", 0):
                    self.send_response(429)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Backend returned error: 429 Too Many Requests"}).encode())
                    return
                # Other errors (500, 502, 503)
                error_code = random.choice([500, 502, 503])
                self.send_response(error_code)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Backend returned error: HTTP {error_code}"}).encode())
                return
        
        # Normal response
        if parsed_path.path == "/api/capabilities":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"capabilities": MOCK_CAPABILITIES}).encode())
        elif parsed_path.path == "/api/patterns":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"patterns": MOCK_PATTERNS}).encode())
        elif parsed_path.path == "/api/capabilities/execute":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "execution_not_supported",
                "message": "Backend returned: Execution requires parameters. Parameters not supported in current Stage 5 constraints."
            }).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Backend returned error: 404 Not Found"}).encode())
    
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass


def create_handler(profile):
    """Create request handler with profile"""
    def handler(*args, **kwargs):
        return PressureInjectionHandler(*args, profile=profile, **kwargs)
    return handler


def run_pressure_server(profile_name, port=8000, duration=60):
    """Run mock backend server with pressure injection"""
    profile = PRESSURE_PROFILES.get(profile_name)
    if not profile:
        print(f"Error: Unknown profile {profile_name}")
        sys.exit(1)
    
    handler = create_handler(profile)
    server = HTTPServer(("localhost", port), handler)
    
    print(f"Starting pressure injection server (Profile: {profile_name})")
    print(f"  Latency: {profile['latency']}s")
    print(f"  Jitter: {profile['jitter']}s")
    print(f"  Error Rate: {profile['error_rate']*100}%")
    print(f"  Rate Limit: {profile.get('rate_limit', False)}")
    print(f"  Concurrency: {profile['concurrency']}")
    print(f"  Duration: {duration}s")
    print(f"  Server: http://localhost:{port}")
    print()
    
    # Run server in background thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for duration
    time.sleep(duration)
    
    # Shutdown server
    server.shutdown()
    print(f"Pressure injection server stopped (Profile: {profile_name})")


def inject_concurrent_requests(profile_name, url, duration=60):
    """Inject concurrent requests (for P5/P6)"""
    try:
        import requests
    except ImportError:
        print("Error: requests library not installed. Install with: pip install requests")
        sys.exit(1)
    
    profile = PRESSURE_PROFILES.get(profile_name)
    if not profile:
        print(f"Error: Unknown profile {profile_name}")
        sys.exit(1)
    
    concurrency = profile["concurrency"]
    end_time = time.time() + duration
    
    print(f"Injecting {concurrency} concurrent requests to {url}")
    print(f"Duration: {duration}s")
    print()
    
    def make_request():
        while time.time() < end_time:
            try:
                requests.get(url, timeout=10)
            except:
                pass
            time.sleep(0.1)
    
    threads = []
    for i in range(concurrency):
        thread = threading.Thread(target=make_request)
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()


def main():
    parser = argparse.ArgumentParser(description="Pressure Injection Harness for J8 Testing")
    parser.add_argument("--profile", required=True, choices=list(PRESSURE_PROFILES.keys()),
                       help="Pressure profile (P0-P6)")
    parser.add_argument("--port", type=int, default=8000,
                       help="Backend server port (default: 8000)")
    parser.add_argument("--duration", type=int, default=60,
                       help="Test duration in seconds (default: 60)")
    parser.add_argument("--mode", choices=["server", "client"], default="server",
                       help="Mode: server (run mock backend) or client (inject concurrent requests)")
    parser.add_argument("--url", default="http://localhost:8000/api/capabilities",
                       help="URL for client mode (default: http://localhost:8000/api/capabilities)")
    
    args = parser.parse_args()
    
    if args.mode == "server":
        run_pressure_server(args.profile, args.port, args.duration)
    else:
        inject_concurrent_requests(args.profile, args.url, args.duration)


if __name__ == "__main__":
    main()

