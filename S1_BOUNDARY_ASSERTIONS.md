# S1 Boundary Assertions

**Work Order**: WO-S-1

**Document Status**: BOUNDARY-ASSERTIONS / NON-CANONICAL

**Date**: 2025-12-28

---

## Purpose

This document explicitly lists all things the S1 Operator UI **CANNOT** do, and maps them to code locations that enforce these boundaries.

---

## Hard Prohibitions

### 1. No File Writes

**Prohibition**: The UI must never write to disk.

**Enforcement Locations**:

- `s1_data_indexer.py`:
  - No `open(file, 'w')` calls
  - No `open(file, 'a')` calls
  - No `os.remove()` calls
  - No `shutil` write operations

- `s1_server.py`:
  - All file operations use `read_text()` only
  - No file write endpoints (only GET endpoints)
  - No POST, PUT, DELETE, PATCH endpoints

**Verification**:
```bash
grep -r "open.*['\"]w" s1_ui/
grep -r "open.*['\"]a" s1_ui/
grep -r "os.remove" s1_ui/
```

**Expected Result**: No matches.

---

### 2. No Execution Operations

**Prohibition**: The UI must never execute scripts, commands, or subprocesses.

**Enforcement Locations**:

- `s1_server.py`:
  - No `subprocess` imports
  - No `os.system()` calls
  - No `exec()` or `eval()` calls

- `s1_ui/static/js/*.js`:
  - No `fetch()` calls to execution endpoints
  - No button handlers that trigger scripts
  - No "Run", "Execute", "Approve", "Fix", "Optimize" buttons

**Verification**:
```bash
grep -r "subprocess" s1_ui/
grep -r "os.system" s1_ui/
grep -r "exec\|eval" s1_ui/
grep -r "Run\|Execute\|Approve\|Fix\|Optimize" s1_ui/static/js/
```

**Expected Result**: No matches (except in comments/documentation).

---

### 3. No Network Operations

**Prohibition**: The UI must never make external network calls.

**Enforcement Locations**:

- `s1_server.py`:
  - No `requests` library imports
  - No `urllib` network calls
  - No external API calls
  - Server binds to `127.0.0.1` only (not `0.0.0.0`)

- `s1_ui/static/js/*.js`:
  - All `fetch()` calls use relative URLs (no external domains)
  - No external API integrations

**Verification**:
```bash
grep -r "requests\|urllib" s1_ui/
grep -r "http://\|https://" s1_ui/static/js/ | grep -v "localhost\|127.0.0.1"
```

**Expected Result**: No matches.

---

### 4. No State Persistence

**Prohibition**: The UI must not persist state across server restarts.

**Enforcement Locations**:

- `s1_data_indexer.py`:
  - Index built in-memory only
  - No caching to disk
  - No database connections

- `s1_server.py`:
  - No session storage (beyond browser default)
  - No database connections
  - Index rebuilt on each server start

**Verification**:
```bash
grep -r "sqlite\|database\|cache.*disk\|pickle.*dump" s1_ui/
```

**Expected Result**: No matches.

---

### 5. No Recommendations or Suggestions

**Prohibition**: The UI must not infer, suggest, or recommend actions.

**Enforcement Locations**:

- `s1_ui/static/js/*.js`:
  - No "suggested next steps" displays
  - No "recommended actions" sections
  - No auto-detection of "improvements"
  - No risk summaries or warnings

- `s1_server.py`:
  - No inference logic in API handlers
  - No "next steps" calculations
  - No recommendation generation

**Verification**:
```bash
grep -r "recommend\|suggest\|next step\|should\|improve" s1_ui/static/js/ s1_server.py
```

**Expected Result**: No matches (except in error messages or documentation).

---

### 6. No Decision Assistance

**Prohibition**: The UI must not assist in decision-making.

**Enforcement Locations**:

- `s1_ui/static/js/decision-viewer.js`:
  - Displays decisions only (read-only)
  - No decision creation forms
  - No decision editing capability
  - No "approve" or "reject" buttons

- `s1_server.py`:
  - No decision writing endpoints
  - No decision modification endpoints

**Verification**:
```bash
grep -r "create.*decision\|edit.*decision\|approve\|reject" s1_ui/
```

**Expected Result**: No matches.

---

### 7. No Evidence Creation

**Prohibition**: The UI must not create or modify evidence packs.

**Enforcement Locations**:

- `s1_ui/static/js/evidence-browser.js`:
  - Displays evidence only (read-only)
  - No evidence creation forms
  - No evidence editing capability

- `s1_server.py`:
  - No evidence writing endpoints
  - No evidence modification endpoints

**Verification**:
```bash
grep -r "create.*evidence\|edit.*evidence\|write.*evidence" s1_ui/
```

**Expected Result**: No matches.

---

## Code-Level Enforcement Summary

### Python Files

**File**: `s1_data_indexer.py`
- **Lines**: All
- **Enforcement**: Read-only file operations only
- **Methods**: `index_all()`, `_index_phases()`, `_index_work_orders()`, etc.
- **Pattern**: All use `read_text()` or `readlines()`, no write operations

**File**: `s1_server.py`
- **Lines**: All
- **Enforcement**: GET endpoints only, read-only file access
- **Methods**: All route handlers
- **Pattern**: All use `read_text()`, no write operations, no subprocess calls

### JavaScript Files

**Files**: `s1_ui/static/js/*.js`
- **Enforcement**: Display-only, no execution triggers
- **Pattern**: All use `fetch()` for GET requests only, no POST/PUT/DELETE

---

## Runtime Enforcement

### File Permissions Test

**Test**: Make all repository files read-only at OS level.

**Expected Behavior**: UI should still function (all operations are read-only).

**Test Command**:
```bash
chmod -R a-w /path/to/repo
python3 s1_ui/s1_server.py
# UI should function normally
```

### Missing File Test

**Test**: Remove a phase status file.

**Expected Behavior**: UI should handle gracefully (404 response), no crash.

**Test Command**:
```bash
mv phase_q/PHASE_R_STATUS.md phase_q/PHASE_R_STATUS.md.bak
python3 s1_ui/s1_server.py
# Navigate to Phase R
# Should show "No status file available" message
```

### No Execution Test

**Test**: Verify no buttons trigger scripts.

**Expected Behavior**: No buttons with execution-related text, no subprocess calls.

**Manual Verification**: Inspect UI, verify no "Run", "Execute", "Approve" buttons.

---

## Static Analysis Checklist

Before marking WO-S-1 COMPLETE, verify:

- [ ] No `open(file, 'w')` or `open(file, 'a')` calls
- [ ] No `subprocess` imports or calls
- [ ] No `os.system()` calls
- [ ] No `exec()` or `eval()` calls
- [ ] No `requests` or `urllib` network calls
- [ ] No database connections
- [ ] No file caching to disk
- [ ] No "Run", "Execute", "Approve", "Fix", "Optimize" buttons
- [ ] No recommendation or suggestion displays
- [ ] All endpoints are GET only
- [ ] Server binds to `127.0.0.1` only

---

## Boundary Violation Response

**If a boundary violation is detected**:

1. **Immediate**: Remove violating code
2. **Document**: Record violation in this file
3. **Verify**: Re-run static analysis
4. **Test**: Re-run runtime tests

**No exceptions allowed.**

---

**END OF BOUNDARY ASSERTIONS**

