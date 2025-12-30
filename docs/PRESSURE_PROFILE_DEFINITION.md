# Pressure Profile Definition

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Pressure Test Profile Specification  
**Date**: 2025-12-27  
**Work Order**: WO-J8-REAL-LOAD-CONCURRENCY-LATENCY-PRESSURE-TEST-AND-NEUTRALITY-REGRESSION

---

## Purpose

This document defines pressure profiles for testing frontend and backend behavior under various stress conditions.

All profiles are factual descriptions only. No recommendations. No optimization suggestions.

---

## Pressure Profile P0: Baseline (No Pressure)

**Profile ID**: P0  
**Description**: Baseline condition with no artificial pressure injection  
**Purpose**: Establish baseline behavior for comparison

**Parameters**:
- Latency: Normal (0-100ms)
- Jitter: None (0ms)
- Error Rate: 0%
- Rate Limit: None
- Concurrency: Normal (1-5 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: No injection (normal operation)

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# No injection needed - normal operation
# Start backend normally
# Access frontend normally
```

**Expected Behavior**: Normal operation, all requests succeed, responses in normal time.

---

## Pressure Profile P1: Fixed High Latency

**Profile ID**: P1  
**Description**: Fixed high latency on all backend responses  
**Purpose**: Test frontend behavior under consistent high latency

**Parameters**:
- Latency: Fixed 5000ms (5 seconds) on all responses
- Jitter: None (0ms)
- Error Rate: 0%
- Rate Limit: None
- Concurrency: Normal (1-5 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Backend delay injection or proxy delay

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# Option 1: Backend delay (if supported)
# Set BACKEND_DELAY_MS=5000

# Option 2: Proxy delay (using mitmproxy or similar)
# mitmproxy --set delay=5

# Option 3: Network delay (using tc on Linux)
# tc qdisc add dev lo root netem delay 5000ms
```

**Expected Behavior**: All requests take ~5 seconds, no errors, timeout not triggered.

**Verification Points**:
- Frontend displays timeout error if request exceeds 10 seconds? (Should be NO - 5s < 10s timeout)
- Frontend automatically retries? (Should be NO)
- Frontend shows "loading" state? (Factual display only, no interpretation)

---

## Pressure Profile P2: Latency Jitter

**Profile ID**: P2  
**Description**: Variable latency with high jitter  
**Purpose**: Test frontend behavior under unpredictable latency

**Parameters**:
- Latency: Variable (100ms - 8000ms, random)
- Jitter: High (random variation ±2000ms)
- Error Rate: 0%
- Rate Limit: None
- Concurrency: Normal (1-5 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Backend jitter injection or proxy jitter

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# Option 1: Backend jitter (if supported)
# Set BACKEND_JITTER_MS=2000

# Option 2: Proxy jitter (using mitmproxy)
# mitmproxy --set delay=3000ms --set jitter=2000ms

# Option 3: Network jitter (using tc on Linux)
# tc qdisc add dev lo root netem delay 3000ms 2000ms
```

**Expected Behavior**: Requests take variable time (100ms - 8000ms), some may timeout (>10s), responses arrive in unpredictable order.

**Verification Points**:
- Frontend handles variable latency without interpretation? (Should be YES)
- Frontend displays responses in order received? (Should be YES - registration order)
- Frontend interprets fast responses as "preferred"? (Should be NO)

---

## Pressure Profile P3: High Error Rate

**Profile ID**: P3  
**Description**: High error rate on backend responses  
**Purpose**: Test frontend behavior under high failure rate

**Parameters**:
- Latency: Normal (0-100ms)
- Jitter: None (0ms)
- Error Rate: 50% (random 500 Internal Server Error)
- Rate Limit: None
- Concurrency: Normal (1-5 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Backend error injection or proxy error injection

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# Option 1: Backend error injection (if supported)
# Set BACKEND_ERROR_RATE=0.5
# Set BACKEND_ERROR_CODE=500

# Option 2: Proxy error injection (using mitmproxy)
# mitmproxy --set error_rate=0.5 --set error_code=500

# Option 3: Backend mock server with error injection
# python mock_backend.py --error-rate 0.5 --error-code 500
```

**Expected Behavior**: ~50% of requests return 500 errors, ~50% succeed.

**Verification Points**:
- Frontend displays errors verbatim? (Should be YES)
- Frontend automatically retries on error? (Should be NO)
- Frontend converts errors to suggestions? (Should be NO)
- Frontend shows different UI for errors vs success? (Should be NO - same UI, different content)

---

## Pressure Profile P4: Rate Limiting (429)

**Profile ID**: P4  
**Description**: Backend returns 429 Too Many Requests  
**Purpose**: Test frontend behavior under rate limiting

**Parameters**:
- Latency: Normal (0-100ms)
- Jitter: None (0ms)
- Error Rate: 100% (all requests return 429)
- Rate Limit: 429 Too Many Requests
- Concurrency: Normal (1-5 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Backend rate limit injection or proxy rate limit

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# Option 1: Backend rate limit (if supported)
# Set BACKEND_RATE_LIMIT=true
# Set BACKEND_RATE_LIMIT_CODE=429

# Option 2: Proxy rate limit (using mitmproxy)
# mitmproxy --set rate_limit=true --set rate_limit_code=429

# Option 3: Backend mock server with rate limit
# python mock_backend.py --rate-limit --rate-limit-code 429
```

**Expected Behavior**: All requests return 429 errors.

**Verification Points**:
- Frontend displays 429 errors verbatim? (Should be YES)
- Frontend automatically retries after delay? (Should be NO)
- Frontend suggests "try again later"? (Should be NO)
- Frontend interprets 429 as "too many requests, wait"? (Should be NO - display verbatim)

---

## Pressure Profile P5: High Concurrency

**Profile ID**: P5  
**Description**: High concurrent request load  
**Purpose**: Test frontend behavior under concurrent request pressure

**Parameters**:
- Latency: Normal (0-100ms)
- Jitter: None (0ms)
- Error Rate: 0%
- Rate Limit: None
- Concurrency: High (20-50 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Concurrent request injection (script or tool)

**Duration**: 60 seconds

**Reproducible Command**:
```bash
# Option 1: Concurrent requests script
# python concurrent_requests.py --count 50 --duration 60

# Option 2: Apache Bench (ab)
# ab -n 1000 -c 50 http://localhost:8000/api/capabilities

# Option 3: wrk
# wrk -t 4 -c 50 -d 60s http://localhost:8000/api/capabilities
```

**Expected Behavior**: Multiple concurrent requests, responses may arrive out of order, some may timeout.

**Verification Points**:
- Frontend handles concurrent requests without state corruption? (Should be YES)
- Frontend displays responses in order received? (Should be YES - registration order)
- Frontend interprets first response as "preferred"? (Should be NO)
- Frontend merges or deduplicates responses? (Should be NO)

---

## Pressure Profile P6: Chaos Mix (Optional)

**Profile ID**: P6  
**Description**: Mixed pressure conditions (latency + jitter + errors + rate limit + concurrency)  
**Purpose**: Test frontend behavior under combined stress conditions

**Parameters**:
- Latency: Variable (1000ms - 6000ms, random)
- Jitter: High (random variation ±1500ms)
- Error Rate: 30% (random 500/502/503 errors)
- Rate Limit: 20% (random 429 errors)
- Concurrency: High (30-50 concurrent requests)
- Timeout: 10 seconds (default)

**Injection Method**: Combined injection (all methods)

**Duration**: 120 seconds

**Reproducible Command**:
```bash
# Combined injection script
# python chaos_injection.py \
#   --latency-min 1000 --latency-max 6000 \
#   --jitter 1500 \
#   --error-rate 0.3 --error-codes 500,502,503 \
#   --rate-limit-rate 0.2 \
#   --concurrency 40 \
#   --duration 120
```

**Expected Behavior**: Highly unpredictable: variable latency, random errors, rate limits, concurrent requests, responses arrive out of order.

**Verification Points**:
- Frontend maintains neutrality under chaos? (Should be YES)
- Frontend does not introduce any optimization? (Should be YES)
- Frontend does not cache or retry? (Should be YES)
- Frontend displays all responses/errors verbatim? (Should be YES)

---

## Pressure Injection Configuration

### Backend Configuration (if supported)

**Environment Variables**:
```bash
BACKEND_DELAY_MS=5000          # Fixed delay (P1)
BACKEND_JITTER_MS=2000         # Jitter (P2)
BACKEND_ERROR_RATE=0.5         # Error rate (P3)
BACKEND_ERROR_CODE=500         # Error code (P3)
BACKEND_RATE_LIMIT=true        # Rate limit (P4)
BACKEND_RATE_LIMIT_CODE=429    # Rate limit code (P4)
```

### Proxy Configuration (mitmproxy example)

**mitmproxy Script**:
```python
# pressure_injection.py
def request(flow):
    # P1: Fixed delay
    if PRESSURE_PROFILE == "P1":
        import time
        time.sleep(5)
    
    # P2: Jitter
    elif PRESSURE_PROFILE == "P2":
        import random
        delay = random.uniform(0.1, 8.0)
        time.sleep(delay)
    
    # P3: Error rate
    elif PRESSURE_PROFILE == "P3":
        import random
        if random.random() < 0.5:
            flow.response = http.HTTPResponse.make(500)
    
    # P4: Rate limit
    elif PRESSURE_PROFILE == "P4":
        flow.response = http.HTTPResponse.make(429)
```

### Network Configuration (Linux tc example)

**Network Delay**:
```bash
# Add delay
tc qdisc add dev lo root netem delay 5000ms

# Add jitter
tc qdisc add dev lo root netem delay 3000ms 2000ms

# Remove delay
tc qdisc del dev lo root
```

---

## Pressure Profile Summary

| Profile | Latency | Jitter | Error Rate | Rate Limit | Concurrency | Duration |
|---------|---------|--------|------------|------------|-------------|----------|
| P0      | Normal  | None   | 0%         | None       | Normal      | 60s      |
| P1      | 5000ms  | None   | 0%         | None       | Normal      | 60s      |
| P2      | Variable| High   | 0%         | None       | Normal      | 60s      |
| P3      | Normal  | None   | 50%        | None       | Normal      | 60s      |
| P4      | Normal  | None   | 100% (429) | 429        | Normal      | 60s      |
| P5      | Normal  | None   | 0%         | None       | High        | 60s      |
| P6      | Variable| High   | 30%        | 20%        | High        | 120s     |

---

## Verification Checklist

For each pressure profile, verify:

- [ ] Frontend does not automatically retry
- [ ] Frontend does not cache responses
- [ ] Frontend does not fall back to mock/cached data
- [ ] Frontend displays errors verbatim
- [ ] Frontend does not convert errors to suggestions
- [ ] Frontend does not change UI based on response timing
- [ ] Frontend displays responses in registration order (as received)
- [ ] Frontend does not interpret fast/slow responses as preference
- [ ] Frontend does not merge or deduplicate responses
- [ ] Frontend maintains constant UI behavior regardless of pressure

---

**END OF PRESSURE PROFILE DEFINITION**

