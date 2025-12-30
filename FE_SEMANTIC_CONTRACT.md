# Frontend Semantic Consumption Contract

**Document Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Purpose**: Define a contract that frontend can depend on for semantic object existence, stability, and read-only guarantees.

**Authority**: FE_FACT_ENTITY_MAP.md, FE_FACT_HUMAN_DECISION_POINTS.md, FE_FACT_FRONTEND_BOUNDARIES.md, WO-FE-SEMANTIC-ALIGN-0 deliverables

---

## Contract Scope

This contract defines:
- Which objects are guaranteed to exist
- Which objects have stable IDs
- Which objects are read-only
- Which objects should not be assumed to exist

**This contract does NOT**:
- Define UI/UX design
- Define execution capabilities
- Define automation rules
- Define business logic

---

## Semantic Object Guarantees

### 1. Company

**Guaranteed Existence**: YES (via COMPANY_DECLARATION.md)

**Stable ID**: YES (`company_id: ai-workbench-v1`)

**Read-Only**: YES

**Modification Authority**: Human only (explicit approval required)

**Declaration File**: `COMPANY_DECLARATION.md`

**Frontend Can**:
- Read company properties (name, phase, frozen refs, description)
- Display company information
- Reference company as semantic anchor

**Frontend Cannot**:
- Modify company properties
- Create new company instances
- Delete company instance

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 1: "Company (公司) - Existence: NO" (declaration creates semantic anchor)

---

### 2. Cell

**Guaranteed Existence**: YES (via backend/subsystems/cell_composition/)

**Stable ID**: YES (`cell_id`)

**Read-Only**: YES (static declaration, Phase-2 semantic reduction)

**Modification Authority**: Human only (via backend registration)

**Declaration Location**: `backend/subsystems/cell_composition/cells/*.json`

**Frontend Can**:
- Read cell definitions (cell_id, role_ids, input_contract, output_format)
- Display cell information
- Reference cells in workflow visualization

**Frontend Cannot**:
- Modify cell definitions
- Create new cells
- Delete cells
- Trigger cell execution

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 2: "Cell exists as static declaration, not runtime entity"

---

### 3. Role

**Guaranteed Existence**: YES (via backend/subsystems/role_management/)

**Stable ID**: YES (`role_id`)

**Read-Only**: YES (static declaration)

**Modification Authority**: Human only (via backend registration)

**Declaration Location**: `backend/subsystems/role_management/roles/*.json`

**Frontend Can**:
- Read role definitions (role_id, purpose, inputs, outputs, boundaries)
- Display role information
- Reference roles in cell composition visualization

**Frontend Cannot**:
- Modify role definitions
- Create new roles
- Delete roles
- Trigger role execution

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 3: "Role exists as static declaration with Purpose, Inputs, Outputs, Boundaries"

---

### 4. Workflow

**Guaranteed Existence**: YES (via WORKFLOW_DECLARATION.md)

**Stable ID**: YES (`workflow_id: ai-workbench-main-workflow`)

**Read-Only**: YES

**Modification Authority**: Human only (explicit approval required)

**Declaration File**: `WORKFLOW_DECLARATION.md`

**Frontend Can**:
- Read workflow topology (nodes, edges, relationship types)
- Display workflow visualization
- Reference workflow in navigation

**Frontend Cannot**:
- Modify workflow topology
- Create new workflows
- Delete workflows
- Trigger workflow execution

**Evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Q8: "No structured workflow definitions exist" (declaration creates semantic object)

---

### 5. Methodology

**Guaranteed Existence**: YES (via METHODOLOGY_DECLARATION.md)

**Stable ID**: YES (`methodology_id`)

**Read-Only**: YES

**Modification Authority**: Human only (explicit approval required)

**Declaration File**: `METHODOLOGY_DECLARATION.md`

**Frontend Can**:
- Read methodology declarations (methodology_id, name, description, scope, status)
- Display methodology adoption
- Reference methodologies in context

**Frontend Cannot**:
- Modify methodology declarations
- Create new methodologies
- Delete methodologies
- Trigger methodology execution

**Evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Summary: "No explicit, structured, reusable methodology representation exists" (declaration creates semantic object)

---

### 6. Work Order

**Guaranteed Existence**: PARTIAL (not all work orders exist, but work order structure exists)

**Stable ID**: YES (Work Order ID pattern: `WO-*`)

**Read-Only**: YES (frozen documents)

**Modification Authority**: Human only (via decision documents)

**Declaration Location**: `FINAL_*_DECISION.md` files, phase directories

**Frontend Can**:
- Read work order definitions (ID, phase, title, status, objective)
- Display work order information
- Reference work orders in navigation

**Frontend Cannot**:
- Modify work order definitions
- Create new work orders
- Delete work orders
- Trigger work order execution

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 4: "Work Orders exist as markdown documents with structured IDs"

**Note**: Frontend should NOT assume all work orders exist. Only work orders with `FINAL_*_DECISION.md` files are guaranteed to exist.

---

### 7. Execution / Run

**Guaranteed Existence**: PARTIAL (not all executions exist, but execution structure exists)

**Stable ID**: YES (`run_id`)

**Read-Only**: YES (archived logs)

**Modification Authority**: Human only (via command-line scripts)

**Declaration Location**: `EXECUTION_STATUS*.md` files, `RUN_LOG_ARCHIVE_*/`, `EXECUTION_LOG_ARCHIVE_*/`

**Frontend Can**:
- Read execution status (execution_id, phase, work_order, status, expected_runs, completed_runs)
- Display execution information
- Reference executions in audit trails

**Frontend Cannot**:
- Modify execution logs
- Create new executions
- Delete executions
- Trigger executions

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 6: "Executions exist as archived run logs with structured IDs"

**Note**: Frontend should NOT assume all executions exist. Only executions with `EXECUTION_STATUS*.md` files are guaranteed to exist.

---

### 8. Decision

**Guaranteed Existence**: PARTIAL (not all decisions exist, but decision structure exists)

**Stable ID**: YES (Decision ID pattern: `FINAL_*_DECISION.md`)

**Read-Only**: YES (frozen documents)

**Modification Authority**: Human only (via sign-off)

**Declaration Location**: `FINAL_*_DECISION.md` files (31+ files)

**Frontend Can**:
- Read decision documents (decision_id, phase, work_order, questions, answers, human_signed)
- Display decision information
- Reference decisions in audit trails

**Frontend Cannot**:
- Modify decision documents
- Create new decisions
- Delete decisions
- Trigger decision creation

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 7: "Decisions exist as markdown documents with structured format"

**Note**: Frontend should NOT assume all decisions exist. Only decisions with `FINAL_*_DECISION.md` files are guaranteed to exist.

---

### 9. Evidence / Audit

**Guaranteed Existence**: PARTIAL (not all evidence packs exist, but evidence structure exists)

**Stable ID**: YES (Evidence Pack ID pattern: `*_EVIDENCE_PACK_*` or `audit_evidence/*`)

**Read-Only**: YES (archived)

**Modification Authority**: Human only (via scripts or manual)

**Declaration Location**: `audit_evidence/*/`, `phase_*/*/PASS_EVIDENCE_PACK_*/`, `phase_*/*/FAIL_EVIDENCE_PACK_*/`

**Frontend Can**:
- Read evidence pack contents (evidence_pack_id, type, phase, work_order, files)
- Display evidence information
- Reference evidence in audit trails

**Frontend Cannot**:
- Modify evidence packs
- Create new evidence packs
- Delete evidence packs
- Trigger evidence creation

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 8: "Evidence packs exist as directories with structured naming"

**Note**: Frontend should NOT assume all evidence packs exist. Only evidence packs with directories are guaranteed to exist.

---

## Object Existence Guarantees

### Guaranteed to Exist

| Object | Guarantee | Declaration File/Location |
|--------|-----------|--------------------------|
| Company | YES | `COMPANY_DECLARATION.md` |
| Cell | YES | `backend/subsystems/cell_composition/cells/*.json` |
| Role | YES | `backend/subsystems/role_management/roles/*.json` |
| Workflow | YES | `WORKFLOW_DECLARATION.md` |
| Methodology | YES | `METHODOLOGY_DECLARATION.md` |

### Not Guaranteed to Exist (Partial)

| Object | Guarantee | Declaration File/Location |
|--------|-----------|--------------------------|
| Work Order | PARTIAL | `FINAL_*_DECISION.md` files (only if decision exists) |
| Execution | PARTIAL | `EXECUTION_STATUS*.md` files (only if execution exists) |
| Decision | PARTIAL | `FINAL_*_DECISION.md` files (only if decision exists) |
| Evidence | PARTIAL | Evidence pack directories (only if evidence exists) |

**Frontend Implication**: Frontend should check for existence before displaying. Use existence checks, not assumptions.

---

## Read-Only Guarantees

### All Objects Are Read-Only

**Statement**: All semantic objects declared in this contract are read-only.

**Enforcement**: 
- No write operations allowed
- No modification capabilities
- No creation capabilities (except via human authorization)
- No deletion capabilities

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 2: "Frontend MUST NOT modify files, write to disk, or update markdown documents"

---

## Stable ID Guarantees

### All Objects Have Stable IDs

**Statement**: All semantic objects have stable, human-readable IDs.

**Enforcement**:
- IDs do not change unless object is replaced
- IDs are human-readable (not opaque hashes)
- IDs follow naming patterns (documented in this contract)

**Evidence**: `FE_FACT_ENTITY_MAP.md` Summary Table: All objects have "Stable ID: YES"

---

## Frontend Consumption Rules

### Rule 1: Existence Checks

**Statement**: Frontend must check for object existence before displaying.

**Enforcement**: 
- Use existence checks (file system, API queries)
- Do not assume objects exist
- Handle missing objects gracefully

**Evidence**: `FE_FACT_ENTITY_MAP.md` Summary: Some objects are "PARTIAL" (not guaranteed to exist)

---

### Rule 2: Read-Only Operations

**Statement**: Frontend must only perform read operations.

**Enforcement**:
- No write operations
- No modification operations
- No creation operations
- No deletion operations

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 2: "Frontend MUST NOT modify files, write to disk, or update markdown documents"

---

### Rule 3: No Execution Capabilities

**Statement**: Frontend must not trigger executions or modify system state.

**Enforcement**:
- No execution triggers
- No script invocations
- No state mutations
- No automation

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 1: "Frontend MUST NOT execute work orders, trigger scripts, or invoke Python scripts"

---

### Rule 4: No Recommendations

**Statement**: Frontend must not suggest actions or recommend decisions.

**Enforcement**:
- No recommendation logic
- No suggestion displays
- No "next step" inference
- No decision assistance

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 4: "Frontend MUST NOT suggest actions, recommend decisions, or infer 'next steps'"

---

## Contract Modification

### This Contract Is

- **DECLARATIVE**: Describes semantic guarantees, not implementation
- **READ-ONLY**: Cannot be modified by frontend or automated processes
- **NON-EXECUTABLE**: Does not trigger, execute, or modify any system behavior

### Modification Authority

Only human authorization can modify this contract. Modification requires:
1. Explicit human approval
2. Version tracking
3. Update to all referenced declarations
4. No retroactive changes to frozen guarantees

---

## Audit Trail

**Contract Created**: 2025-12-28

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Authority**: FE_FACT_ENTITY_MAP.md, FE_FACT_HUMAN_DECISION_POINTS.md, FE_FACT_FRONTEND_BOUNDARIES.md

**Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

**Referenced Declarations**:
- `COMPANY_DECLARATION.md`
- `WORKFLOW_DECLARATION.md`
- `METHODOLOGY_DECLARATION.md`

---

**END OF FRONTEND SEMANTIC CONSUMPTION CONTRACT**

