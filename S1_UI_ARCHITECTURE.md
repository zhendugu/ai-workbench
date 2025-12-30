# S1 Operator Read-Only Control Surface Architecture

**Work Order**: WO-S-1

**Document Status**: ARCHITECTURE / NON-CANONICAL

**Date**: 2025-12-28

---

## Purpose

This document defines the architecture for a local, read-only operator interface that exposes system state, structure, and artifacts in a navigable form.

**This is a CONTROL SURFACE, not a control system.**

---

## Architecture Overview

### Technology Stack

**Choice**: Python + Flask (minimal web server) + Vanilla JavaScript (frontend)

**Rationale**:
- Python: Easy file system access, markdown parsing
- Flask: Minimal dependencies, local-only deployment
- Vanilla JS: No build step, direct file serving, explicit control

**Alternative Considered**: Node.js + Express
- Rejected: More dependencies, less explicit file system control

---

## Component Architecture

### 1. Data Indexer (`s1_data_indexer.py`)

**Purpose**: Scan repository and build in-memory index of all navigable structures.

**Input**: Repository root directory

**Output**: In-memory data structures (no persistence)

**Indexed Entities**:
- Phases (from `phase_*/` directories and `*_STATUS.md` files)
- Work Orders (from directory names and markdown files)
- Executions (from `EXECUTION_STATUS*.md` files)
- Evidence Packs (from `audit_evidence/` and `*_EVIDENCE_PACK_*/` directories)
- Decisions (from `FINAL_*_DECISION.md` files)
- Traceability (from `TRACEABILITY_INDEX_*.md` files)

**Read Operations Only**:
- `os.listdir()` - directory listing
- `open(file, 'r')` - file reading
- `os.path.exists()` - existence checks
- `os.path.isdir()` - directory checks

**No Write Operations**:
- No file creation
- No file modification
- No caching to disk
- No state persistence

---

### 2. Flask Backend (`s1_server.py`)

**Purpose**: Serve read-only API endpoints and static files.

**Endpoints**:

```
GET /api/phases
  → Returns: List of phases with status

GET /api/phases/<phase_id>
  → Returns: Phase details, work orders, closure summary

GET /api/work-orders
  → Returns: List of all work orders

GET /api/work-orders/<wo_id>
  → Returns: Work order details, related artifacts

GET /api/executions
  → Returns: List of execution runs

GET /api/executions/<execution_id>
  → Returns: Execution details, status, logs

GET /api/evidence
  → Returns: List of evidence packs

GET /api/evidence/<pack_id>
  → Returns: Evidence pack file tree

GET /api/evidence/<pack_id>/file/<path>
  → Returns: File content (markdown rendered as HTML)

GET /api/decisions
  → Returns: List of decision documents

GET /api/decisions/<decision_id>
  → Returns: Decision content

GET /api/traceability
  → Returns: List of traceability indexes

GET /api/traceability/<index_id>
  → Returns: Traceability mappings
```

**Read-Only Enforcement**:
- All endpoints are GET only
- No POST, PUT, DELETE, PATCH endpoints
- No file write operations in handlers
- No subprocess calls
- No shell execution

---

### 3. Frontend Modules

**Location**: `s1_ui/static/` and `s1_ui/templates/`

**Structure**:

```
s1_ui/
  static/
    js/
      phase-view.js
      work-order-list.js
      execution-viewer.js
      evidence-browser.js
      decision-viewer.js
      traceability-view.js
      app.js (main router)
    css/
      styles.css
  templates/
    index.html (main app shell)
    phase-view.html
    work-order-list.html
    execution-viewer.html
    evidence-browser.html
    decision-viewer.html
    traceability-view.html
```

**Module Responsibilities**:

#### PhaseView
- Display phase list
- Show phase status (OPEN/CLOSED/FROZEN)
- Link to phase closure summaries
- Display phase work orders

#### WorkOrderList
- List all work orders
- Show work order status
- Link to related executions and evidence
- No execution buttons

#### ExecutionViewer
- Display execution runs
- Show run status (completed/failed/pending)
- Link to execution logs (read-only)
- Timeline view

#### EvidenceBrowser
- Navigate evidence pack directory tree
- Render markdown files (read-only)
- Display JSON files (read-only)
- No editing capability

#### DecisionViewer
- Display decision documents
- Show questions and answers
- Highlight human signature status
- No decision creation or editing

#### TraceabilityView
- Visual navigation of traceability indexes
- Click-through from claim to evidence
- Display evidence file paths
- No modification

---

## Data Flow

### 1. Initialization

```
Human launches server
  → Server starts
  → Data Indexer scans repository
  → In-memory index built
  → Server ready
```

### 2. Page Load

```
Human opens browser → localhost:5000
  → Frontend loads
  → Frontend requests /api/phases
  → Backend reads from index (no file I/O)
  → JSON response
  → Frontend renders
```

### 3. Navigation

```
Human clicks "Phase Q"
  → Frontend requests /api/phases/Q
  → Backend reads phase status file (read-only)
  → JSON response
  → Frontend renders phase details
```

### 4. Evidence Viewing

```
Human clicks evidence pack
  → Frontend requests /api/evidence/<pack_id>
  → Backend reads directory structure (read-only)
  → JSON response (file tree)
  → Human clicks file
  → Frontend requests /api/evidence/<pack_id>/file/<path>
  → Backend reads file (read-only)
  → Markdown rendered to HTML
  → Frontend displays
```

---

## Read-Only Guarantees

### Code-Level Enforcement

1. **No Write Operations**:
   - No `open(file, 'w')` or `open(file, 'a')` calls
   - No `os.remove()` calls
   - No `shutil` write operations
   - Static analysis check: grep for write patterns

2. **No Execution Operations**:
   - No `subprocess` calls
   - No `os.system()` calls
   - No `exec()` or `eval()` calls
   - Static analysis check: grep for execution patterns

3. **No Network Operations**:
   - No `requests` library
   - No `urllib` network calls
   - No external API calls
   - Static analysis check: grep for network patterns

4. **No State Persistence**:
   - No database connections
   - No file caching
   - No session storage (beyond browser default)
   - Index rebuilt on each server start

### Runtime Enforcement

1. **File Permissions**:
   - UI should function if files are read-only at OS level
   - UI should crash safely if files are missing (no recovery attempts)

2. **Error Handling**:
   - Missing files → 404 response
   - Permission errors → 403 response
   - No retry logic
   - No auto-recovery

---

## Security Model

**Single-User, Local-Only**:
- No authentication required
- No authorization checks
- No network exposure
- No external access

**Attack Surface**: Minimal
- Only reads local files
- No user input processing (beyond navigation)
- No code execution
- No data modification

---

## Deployment

### Local Development

```bash
cd s1_ui/
python3 s1_server.py
# Server starts on localhost:5000
```

### Production (Local)

Same as development. No cloud deployment.

---

## File Structure

```
s1_ui/
  s1_data_indexer.py      # Repository scanner
  s1_server.py            # Flask server
  static/
    js/                   # Frontend modules
    css/                  # Styles
  templates/              # HTML templates
  README.md               # Operator instructions
```

---

## Dependencies

**Python**:
- Flask (minimal web server)
- markdown (markdown rendering)
- pygments (code highlighting, optional)

**No External Services**:
- No databases
- No cloud services
- No APIs
- No authentication systems

---

## Performance Considerations

**Index Building**:
- Scans repository on server start
- In-memory only
- No caching across restarts
- Acceptable delay: <10 seconds for full scan

**File Reading**:
- On-demand file reading
- No pre-loading
- Acceptable delay: <1 second per file

**No Optimization Required**:
- This is a read-only interface
- Performance is secondary to correctness
- No caching complexity needed

---

## Testing Strategy

### Manual Verification

1. **Read-Only Check**:
   - Make all files read-only at OS level
   - Verify UI still functions
   - Verify no write errors

2. **Missing File Check**:
   - Remove a phase status file
   - Verify UI handles gracefully (404)
   - Verify no crash

3. **No Execution Check**:
   - Verify no buttons trigger scripts
   - Verify no subprocess calls in code
   - Verify no shell execution

### Static Analysis

```bash
# Check for write operations
grep -r "open.*['\"]w" s1_ui/
grep -r "open.*['\"]a" s1_ui/

# Check for execution operations
grep -r "subprocess" s1_ui/
grep -r "os.system" s1_ui/

# Check for network operations
grep -r "requests" s1_ui/
grep -r "urllib" s1_ui/
```

---

## Future Extensions (NOT IN SCOPE)

**Explicitly Forbidden**:
- Adding write capabilities
- Adding execution capabilities
- Adding recommendation systems
- Adding decision assistance
- Adding external integrations

**This UI is FROZEN at read-only operator interface.**

---

**END OF ARCHITECTURE DOCUMENT**

