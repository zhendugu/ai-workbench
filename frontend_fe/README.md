# Frontend FE (Frozen Requirements Implementation)

**Status**: IMPLEMENTATION IN PROGRESS

**Work Order**: WO-FE-FREEZE-AND-IMPLEMENT-0

**Authority**: `docs/frontend/FE_REQ_FROZEN_1.md` (FROZEN)

---

## Purpose

This frontend implements the frozen frontend requirements (FE_REQ_FROZEN_1.md) as a read-only cognitive interface.

**This frontend is NOT**:
- A control system
- An execution interface
- A recommendation system
- An intelligent assistant

**This frontend IS**:
- A read-only cognitive interface
- A structural fact display system
- A human decision point visibility system
- An evidence backtracking system

---

## Architecture

**Technology Stack**: Vanilla JavaScript + HTML + CSS (no frameworks)

**Rationale**: Minimal dependencies, explicit control, no implicit behaviors

**Data Source**: Read-only file system access (direct JSON/Markdown file reading or backend API)

---

## Implementation Status

- [x] Freeze requirements document
- [x] Create constitutional constraint
- [x] Create frontend structure
- [x] Interface A: Company anchor view
- [x] Interface B: Cell responsibility structure view
- [x] Interface C: Declarative topology view
- [ ] Interface D: Task Force collaboration view (pending - needs Task Force data source)
- [x] Interface E: Methodology perspective switcher
- [x] Interface F: Human decision point view
- [x] Interface G: Evidence backtracking view
- [x] Navigation structure
- [ ] Hard constraint verification (pending - needs full data integration)

---

## Hard Constraints

This frontend MUST NOT contain:

1. Execution, running, triggering operations
2. Creation or modification of structural objects
3. AI calls, agents, or automatic suggestions
4. Intelligent recommendations, sorting, or predictions
5. Progress bars, execution status, or health indicators
6. Color coding (red/yellow/green) that implies state
7. Default selections or auto-fill
8. Any elements that imply "system is working"

---

## Self-Check Rules

Before marking any interface COMPLETE, verify:

1. Does this interface make humans feel "the system is running"?
   - Answer must be NO

2. Does this interface make humans feel "one click can complete something"?
   - Answer must be NO

3. Does this interface imply recommendations, execution, or intelligent judgment anywhere?
   - Answer must be NO

---

## Data Integration

**Current Status**: Using example data

**Next Steps**: Integrate with actual data sources:
- Company data: `COMPANY_DECLARATION.md`
- Cell data: `backend/subsystems/cell_composition/cells/*.json`
- Role data: `backend/subsystems/role_management/roles/*.json`
- Workflow data: `WORKFLOW_DECLARATION.md`
- Methodology data: `METHODOLOGY_DECLARATION.md`
- Decision data: `FINAL_*_DECISION.md` files
- Evidence data: Evidence pack directories

---

**END OF FRONTEND FE README**

