# Pressure Injection Harness - Usage Guide

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Tool Usage Guide  
**Date**: 2025-12-27  
**Work Order**: WO-J8-REAL-LOAD-CONCURRENCY-LATENCY-PRESSURE-TEST-AND-NEUTRALITY-REGRESSION

---

## Purpose

This document provides usage instructions for the pressure injection harness used in J8 testing.

---

## Dependencies

**Required**:
- Python 3.7+
- Standard library only (http.server, threading, etc.)

**Optional** (for client mode):
- `requests` library: `pip install requests`

---

## Quick Start

### 1. Make Script Executable

```bash
chmod +x scripts/pressure_injection_harness.py
```

### 2. Run Pressure Server

```bash
# P0: Baseline (no pressure)
python3 scripts/pressure_injection_harness.py --profile P0 --duration 60

# P1: Fixed high latency (5 seconds)
python3 scripts/pressure_injection_harness.py --profile P1 --duration 60

# P2: Latency jitter (variable 100ms - 8s)
python3 scripts/pressure_injection_harness.py --profile P2 --duration 60

# P3: High error rate (50%)
python3 scripts/pressure_injection_harness.py --profile P3 --duration 60

# P4: Rate limiting (429)
python3 scripts/pressure_injection_harness.py --profile P4 --duration 60

# P5: High concurrency (requires separate client)
python3 scripts/pressure_injection_harness.py --profile P5 --mode client --duration 60

# P6: Chaos mix (all conditions)
python3 scripts/pressure_injection_harness.py --profile P6 --duration 120
```

---

## Usage Modes

### Server Mode (Default)

Runs a mock backend server with pressure injection.

**Command**:
```bash
python3 scripts/pressure_injection_harness.py --profile P1 --port 8000 --duration 60
```

**Parameters**:
- `--profile`: Pressure profile (P0-P6)
- `--port`: Server port (default: 8000)
- `--duration`: Test duration in seconds (default: 60)

**Endpoints**:
- `GET /api/capabilities` - Returns capability list
- `GET /api/patterns` - Returns pattern list
- `GET /api/capabilities/execute` - Returns execution not supported message

### Client Mode

Injects concurrent requests to an existing backend.

**Command**:
```bash
python3 scripts/pressure_injection_harness.py --profile P5 --mode client --url http://localhost:8000/api/capabilities --duration 60
```

**Parameters**:
- `--profile`: Pressure profile (P5 or P6 for high concurrency)
- `--mode`: Set to "client"
- `--url`: Target URL
- `--duration`: Test duration in seconds (default: 60)

---

## Pressure Profiles

See `docs/PRESSURE_PROFILE_DEFINITION.md` for detailed profile specifications.

**Summary**:
- **P0**: Baseline (no pressure)
- **P1**: Fixed high latency (5s)
- **P2**: Latency jitter (variable 100ms - 8s)
- **P3**: High error rate (50%)
- **P4**: Rate limiting (429)
- **P5**: High concurrency (50 concurrent requests)
- **P6**: Chaos mix (all conditions combined)

---

## Environment Variables

**None required** - All configuration via command-line arguments.

---

## Port Configuration

**Default**: Port 8000

**Change port**:
```bash
python3 scripts/pressure_injection_harness.py --profile P1 --port 8080
```

**Frontend configuration**: Update `API_BASE_URL` in frontend HTML files if port changes.

---

## Reproducible Test Execution

### Single Profile Test

```bash
# Start pressure server
python3 scripts/pressure_injection_harness.py --profile P1 --duration 60 &

# Access frontend in browser
# http://localhost:8000/frontend_app/capabilities.html

# Wait for duration, then stop server
```

### Multiple Profile Test

```bash
# Test all profiles sequentially
for profile in P0 P1 P2 P3 P4 P6; do
    echo "Testing profile: $profile"
    python3 scripts/pressure_injection_harness.py --profile $profile --duration 60
    sleep 10  # Wait between tests
done
```

### Concurrent Request Test (P5)

```bash
# Terminal 1: Start backend (normal or pressure server)
python3 scripts/pressure_injection_harness.py --profile P0 --duration 120 &

# Terminal 2: Inject concurrent requests
python3 scripts/pressure_injection_harness.py --profile P5 --mode client --duration 60

# Terminal 3: Access frontend in browser
# Observe behavior under concurrent load
```

---

## Troubleshooting

### Port Already in Use

**Error**: `Address already in use`

**Solution**: Change port or stop existing server
```bash
python3 scripts/pressure_injection_harness.py --profile P1 --port 8001
```

### Import Error (requests)

**Error**: `ImportError: No module named 'requests'`

**Solution**: Install requests (only needed for client mode)
```bash
pip install requests
```

### Frontend Cannot Connect

**Error**: Frontend shows connection error

**Solution**: 
1. Verify server is running: `curl http://localhost:8000/api/capabilities`
2. Check frontend `API_BASE_URL` matches server port
3. Check CORS if accessing from different origin

---

## Output

**Server Mode**:
- Prints profile configuration on startup
- Runs silently (no request logging)
- Stops after duration

**Client Mode**:
- Prints concurrent request injection status
- Runs silently (no response logging)

---

## Notes

- **No persistence**: Server does not persist state between requests
- **No caching**: Server does not cache responses
- **No retry**: Server does not retry failed requests
- **No optimization**: Server does not optimize based on request patterns
- **Factual only**: Server returns responses as configured, no interpretation

---

**END OF PRESSURE INJECTION HARNESS README**

