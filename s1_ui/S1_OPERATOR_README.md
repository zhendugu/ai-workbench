# S1 Operator Read-Only Control Surface

**Work Order**: WO-S-1

**Status**: OPERATOR-INTERFACE / READ-ONLY

**Date**: 2025-12-28

---

## What This Is

A local, read-only operator interface for navigating system state, phases, work orders, executions, evidence packs, decisions, and traceability indexes.

**This is a CONTROL SURFACE, not a control system.**

---

## What This Is NOT

- **NOT** an execution interface (cannot run scripts)
- **NOT** an editing interface (cannot modify files)
- **NOT** a recommendation system (does not suggest actions)
- **NOT** a decision assistant (does not help make decisions)
- **NOT** a production system (local-only, single-user)

---

## Prerequisites

- Python 3.7+
- Flask (`pip install flask flask-cors markdown`)
- Local repository access

---

## Launch Instructions

### 1. Navigate to UI Directory

```bash
cd s1_ui/
```

### 2. Install Dependencies (if needed)

**If using virtual environment** (recommended):
```bash
# Activate venv first
source .venv/bin/activate  # or: .venv/bin/python -m pip install ...

# Then install
pip install flask flask-cors markdown
```

**If using system Python**:
```bash
pip install flask flask-cors markdown
```

### 3. Start Server

**Using virtual environment** (if dependencies installed there):
```bash
.venv/bin/python s1_ui/s1_server.py
```

**Using system Python**:
```bash
python3 s1_ui/s1_server.py
```

**Default**: Server starts on `http://localhost:5000`

**Custom Repository Root**:
```bash
python3 s1_ui/s1_server.py /path/to/repository
```

### 4. Open Browser

Navigate to: `http://localhost:5000`

---

## Usage

### Navigation

The UI provides 6 main views:

1. **Phases**: Overview of all phases (K, M, N, Q, R, S)
2. **Work Orders**: Registry of all work orders
3. **Executions**: Execution history and status
4. **Evidence**: Evidence pack browser
5. **Decisions**: Decision document viewer
6. **Traceability**: Traceability index navigator

### Viewing Details

- Click on any item to view details
- Use "← Back" buttons to return to list views
- Markdown files are rendered as HTML
- JSON files are displayed as formatted JSON

### File Viewing

- Evidence pack files can be viewed by clicking on file names
- Markdown files are rendered with syntax highlighting
- JSON files are displayed with formatting

---

## What You Can Do

✅ **View** phase status and closure summaries  
✅ **Browse** work order registry  
✅ **View** execution history and status  
✅ **Navigate** evidence packs and view files  
✅ **Read** decision documents  
✅ **Explore** traceability indexes  

---

## What You Cannot Do

❌ **Execute** work orders or scripts  
❌ **Modify** any files  
❌ **Create** new evidence packs  
❌ **Write** decision documents  
❌ **Trigger** any actions  
❌ **Get** recommendations or suggestions  

---

## Troubleshooting

### Server Won't Start

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**: Install dependencies:
```bash
pip install flask flask-cors markdown
```

### No Data Appears

**Possible Causes**:
- Repository root path incorrect
- Files are read-only (this is OK, UI should still work)
- Indexer failed to scan (check server logs)

**Solution**: Check server console output for errors.

### Files Not Loading

**Possible Causes**:
- File path contains special characters
- File is missing or moved
- Permission error (should still work if read-only)

**Solution**: Check server console output for 404 or 500 errors.

---

## Architecture

### Components

- **Data Indexer** (`s1_data_indexer.py`): Scans repository, builds in-memory index
- **Flask Server** (`s1_server.py`): Serves API endpoints and static files
- **Frontend Modules** (`static/js/*.js`): UI view modules
- **Styles** (`static/css/styles.css`): UI styling

### Data Flow

1. Server starts → Indexer scans repository
2. Browser loads → Frontend requests data from API
3. API reads from index → Returns JSON
4. Frontend renders → User navigates

### Read-Only Guarantees

- All file operations are read-only
- No write operations in code
- No execution operations
- No network calls (except localhost)
- No state persistence

---

## Security

**Local-Only**: Server binds to `127.0.0.1` only (not accessible from network)

**Single-User**: No authentication required (local operator only)

**Read-Only**: No modification capabilities

**No External Access**: No network calls, no cloud services

---

## Limitations

- **Performance**: Index built on each server start (acceptable delay: <10 seconds)
- **File Count**: Evidence pack file lists limited to 100 files (for performance)
- **No Search**: No search functionality (navigate by structure only)
- **No Filtering**: No filtering or sorting (display as indexed)

---

## Support

**For Issues**: Check server console output for errors.

**For Questions**: Refer to `S1_UI_ARCHITECTURE.md` and `S1_BOUNDARY_ASSERTIONS.md`.

**For Verification**: Run static analysis checks in `S1_BOUNDARY_ASSERTIONS.md`.

---

## End of README

