#!/usr/bin/env python3
"""
Frontend FE Static File Server

Simple HTTP server to serve the read-only cognitive interface.

READ-ONLY OPERATIONS ONLY.
No file writes, no execution, no modifications.
"""

import os
import sys
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()
PUBLIC_DIR = SCRIPT_DIR / 'public'
STATIC_DIR = SCRIPT_DIR / 'static'

class FrontendRequestHandler(SimpleHTTPRequestHandler):
    """Custom request handler for frontend static files"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC_DIR), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def translate_path(self, path):
        # Handle static file requests
        if path.startswith('/static/'):
            static_path = path.replace('/static/', '')
            full_path = STATIC_DIR / static_path
            if full_path.exists():
                return str(full_path)
        
        # Handle root and other paths
        if path == '/' or path == '/index.html':
            return str(PUBLIC_DIR / 'index.html')
        
        # Default to public directory
        return super().translate_path(path)
    
    def log_message(self, format, *args):
        # Suppress default logging, or customize as needed
        pass


def find_free_port(start_port=8000, max_port=8100):
    """Find a free port starting from start_port"""
    for port in range(start_port, max_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        if result != 0:
            return port
    return None


if __name__ == '__main__':
    # Find free port
    port = find_free_port(8000, 8100)
    if port is None:
        print("Error: Could not find a free port between 8000-8100")
        sys.exit(1)
    
    # Change to script directory
    os.chdir(SCRIPT_DIR)
    
    # Create server
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, FrontendRequestHandler)
    
    print(f"Starting Frontend FE server...")
    print(f"Server running at: http://127.0.0.1:{port}")
    print(f"Press Ctrl+C to stop")
    print()
    print("Note: This is a read-only cognitive interface.")
    print("No execution, modification, or automation capabilities.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

