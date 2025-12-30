# Frontend Entity Fact Map

**Work Order**: WO-FE-FACT-0

**Document Status**: FACT-AUDIT / READ-ONLY

**Purpose**: Enumerate stable entities that frontend must perceive, based on current code and frozen documents.

**Authority**: AI_Virtual_Company_Organizational_GCD_v2.md, frozen Phase Q/R documents, DESIGN_COMPLIANCE_AUDIT.md

---

## Entity Fact Table

### 1. Company (公司)

**Existence**: NO

**Fact**: No "Company" entity exists in current codebase.

**Evidence**:
- No `company` or `company_management` subsystem in `backend/subsystems/`
- GCD_v2 Section 1 states: "AI 公司不应照抄人类公司的部门制与层级制结构"
- GCD_v2 Section 7 states: "本结构不是'公司架构'"

**Conclusion**: Frontend must NOT assume a "Company" entity exists.

---

### 2. Cell (责任最小单元)

**Existence**: YES

**Stable ID**: YES (`cell_id`)

**Lifecycle State**: PARTIAL

**Fact**: Cell exists as static declaration, not runtime entity (Phase-2 semantic reduction).

**Evidence**:
- `backend/subsystems/cell_composition/models.py`: `CellDefinition` dataclass exists
- `backend/subsystems/cell_composition/README.md`: "Cell is a static declarative composition, not a runtime entity"
- `backend/subsystems/cell_composition/cells/`: Contains JSON files with cell definitions (e.g., `test-cell-1.json`, `test-cell-2.json`)

**Fields**:
- `cell_id`: Unique identifier (string)
- `role_ids`: List of role identifiers (read-only references)
- `input_contract`: External input contract structure (dict)
- `output_format`: External output format structure (dict)

**State Information Location**:
- Cell definitions: `backend/subsystems/cell_composition/cells/*.json`
- Cell state (if exists): `backend/subsystems/cell_composition/cell_states/*.json`
- Registration: `backend/subsystems/cell_composition/register_cell.py`
- Query: `backend/subsystems/cell_composition/query_cell.py`

**Read-Only vs Human Confirmation**:
- Cell definition: Read-only (static declaration)
- Cell state: Not verified (Phase-2 reduction removed state)

**Frontend Visibility**: Frontend can read cell definitions, but cannot modify them.

---

### 3. Role (约束描述)

**Existence**: YES

**Stable ID**: YES (`role_id`)

**Lifecycle State**: PARTIAL

**Fact**: Role exists as static declaration with Purpose, Inputs, Outputs, Boundaries.

**Evidence**:
- `backend/subsystems/role_management/models.py`: `RoleDefinition` dataclass exists
- `backend/subsystems/role_management/roles/`: Contains JSON files with role definitions (13 files)
- `backend/subsystems/role_management/README.md`: "Role is a STATIC DECLARATION, not a runtime entity"

**Fields**:
- `role_id`: Unique identifier (string)
- `purpose`: What problem this role exists to solve (string)
- `inputs`: List of input types (List[str])
- `outputs`: List of output types (List[str])
- `boundaries`: List of forbidden actions (List[str])
- `notes`: Optional notes (Optional[str])

**State Information Location**:
- Role definitions: `backend/subsystems/role_management/roles/*.json`
- Registration: `backend/subsystems/role_management/register_role.py`
- Query: `backend/subsystems/role_management/query_role.py`

**Read-Only vs Human Confirmation**:
- Role definition: Read-only (static declaration)
- Task Log: Not explicitly implemented (per DESIGN_COMPLIANCE_AUDIT.md Section 2.1)

**Frontend Visibility**: Frontend can read role definitions, but cannot modify them.

---

### 4. Task / Work Order

**Existence**: YES

**Stable ID**: YES (Work Order ID pattern: `WO-*`)

**Lifecycle State**: YES (implicit from Decision documents)

**Fact**: Work Orders exist as markdown documents with structured IDs.

**Evidence**:
- 31+ `FINAL_*_DECISION.md` files across phases
- Work Order IDs follow pattern: `WO-C1A`, `WO-J1`, `WO-Q-4-2-0`, `WO-R-2E-0`, `WO-S-0`, `WO-S-1`
- Work Orders referenced in phase directories: `phase_q/`, `phase_k_a/`, `phase_m/`, `phase_n/`, etc.

**Fields** (from Decision documents):
- Work Order ID: Pattern `WO-<Phase>-<Number>` or `WO-<Phase>-<Sub>-<Number>`
- Phase: Associated phase identifier
- Title: Work order title
- Status: Implicit from `FINAL_*_DECISION.md` existence (COMPLETE if decision exists)
- Objective: Stated in Decision document

**State Information Location**:
- Decision documents: `FINAL_*_DECISION.md` files (31+ files)
- Phase directories: `phase_*/` directories
- Execution artifacts: `EXECUTION_STATUS*.md` files
- Evidence packs: `*_EVIDENCE_PACK_*/` directories

**Read-Only vs Human Confirmation**:
- Work Order definition: Read-only (frozen documents)
- Work Order completion: Requires human sign-off (per Decision documents)
- Work Order execution: Read-only (execution logs archived)

**Frontend Visibility**: Frontend can read work order definitions and execution status, but cannot create or modify work orders.

---

### 5. Task Force / Working Group

**Existence**: YES

**Stable ID**: YES (`task_force_id`)

**Lifecycle State**: YES (descriptive only, Phase-3 Level 1)

**Fact**: Task Force exists as conceptual structure, not executable entity.

**Evidence**:
- `backend/subsystems/task_force/models.py`: `TaskForceDefinition`, `TaskForceMember`, `TaskForceGoal`, `TaskForceDissolutionRecord` dataclasses exist
- `backend/subsystems/task_force/README.md`: "Task Force is a conceptual structure, not an executable entity"
- GCD_v2 Section 3.4: Task Force must have explicit goal, output, dissolution condition

**Fields**:
- `task_force_id`: Unique identifier (string)
- `goal`: TaskForceGoal structure
- `members`: List of TaskForceMember structures
- `dissolution_condition`: Explicit dissolution condition (string)
- `methodology_recovery`: Post-completion recovery structure

**State Information Location**:
- Task Force definitions: `backend/subsystems/task_force/` (structure only)
- Registration: `backend/subsystems/task_force/register_task_force.py`
- Query: `backend/subsystems/task_force/query_task_force.py`

**Read-Only vs Human Confirmation**:
- Task Force definition: Read-only (descriptive only)
- Task Force dissolution: Not verified (per DESIGN_COMPLIANCE_AUDIT.md Section 11.3)

**Frontend Visibility**: Frontend can read task force definitions, but cannot create or modify task forces.

---

### 6. Execution / Run

**Existence**: YES

**Stable ID**: YES (`run_id`)

**Lifecycle State**: YES

**Fact**: Executions exist as archived run logs with structured IDs.

**Evidence**:
- `phase_q/Q4-1/EXECUTION_STATUS.md`: Execution status document
- `phase_q/Q4-2/EXECUTION_STATUS_Q4-2.md`: Execution status document
- `phase_q/R2/EXECUTION_STATUS_R2E.md`: Execution status document
- Execution archives: `RUN_LOG_ARCHIVE_*/`, `EXECUTION_LOG_ARCHIVE_*/` directories

**Fields** (from Execution Status documents):
- Execution ID: Derived from run_id (e.g., `Q4-1`, `Q4-2`, `R2E`)
- Phase: Associated phase identifier
- Work Order: Associated work order ID
- Status: COMPLETED, FAILED, PENDING
- Expected Runs: Integer count
- Completed Runs: Integer count
- Archive Path: Path to execution archive directory

**State Information Location**:
- Execution status: `EXECUTION_STATUS*.md` files (3 files found)
- Execution archives: `RUN_LOG_ARCHIVE_*/`, `EXECUTION_LOG_ARCHIVE_*/` directories
- Run logs: `*.log` files in archive directories
- Run configs: `run_configs/*.json` files

**Read-Only vs Human Confirmation**:
- Execution logs: Read-only (archived)
- Execution status: Read-only (frozen documents)
- Execution triggering: Requires human action (command-line scripts)

**Frontend Visibility**: Frontend can read execution status and logs, but cannot trigger executions.

---

### 7. Decision

**Existence**: YES

**Stable ID**: YES (Decision ID pattern: `FINAL_*_DECISION.md`)

**Lifecycle State**: YES (FINAL status)

**Fact**: Decisions exist as markdown documents with structured format.

**Evidence**:
- 31+ `FINAL_*_DECISION.md` files across phases
- Decision format: Questions, Answers, Human sign-off section
- Decision location: Phase directories or `docs/` directory

**Fields** (from Decision documents):
- Decision ID: Derived from filename (e.g., `FINAL_Q4-2-0_DECISION.md` → `Q4-2-0`)
- Phase: Associated phase identifier
- Work Order: Associated work order ID
- Questions: List of questions (extracted via regex pattern `Q\d+`)
- Answers: List of answers (extracted via regex pattern `Answer:`)
- Human Signed: Boolean (presence of "Human Reviewer" and "Signature" in content)

**State Information Location**:
- Decision documents: `FINAL_*_DECISION.md` files (31+ files)
- Phase directories: `phase_*/` directories
- Docs directory: `docs/FINAL_*_DECISION.md` files

**Read-Only vs Human Confirmation**:
- Decision document: Read-only (frozen)
- Decision creation: Requires human sign-off
- Decision modification: Forbidden (frozen documents)

**Frontend Visibility**: Frontend can read decision documents, but cannot create or modify decisions.

---

### 8. Audit / Evidence

**Existence**: YES

**Stable ID**: YES (Evidence Pack ID pattern: `*_EVIDENCE_PACK_*` or `audit_evidence/*`)

**Lifecycle State**: YES (PASS/FAIL type)

**Fact**: Evidence packs exist as directories with structured naming.

**Evidence**:
- `audit_evidence/`: 66+ evidence pack directories
- `phase_q/Q4-1/PASS_EVIDENCE_PACK_Q4-1/`: Evidence pack directory
- `phase_q/Q4-2/EVIDENCE_PACK_Q4-2-0/`: Evidence pack directory
- Evidence pack naming: `*_pass/`, `*_fail/`, `*_EVIDENCE_PACK_*`

**Fields** (from Evidence Pack structure):
- Evidence Pack ID: Directory name
- Type: PASS or FAIL (derived from directory name)
- Phase: Associated phase identifier (inferred from path)
- Work Order: Associated work order ID (inferred from path)
- Files: List of files in evidence pack directory

**State Information Location**:
- Evidence packs: `audit_evidence/*/` directories (66+ directories)
- Phase evidence: `phase_*/*/PASS_EVIDENCE_PACK_*/`, `phase_*/*/FAIL_EVIDENCE_PACK_*/` directories
- Evidence files: Markdown and JSON files within evidence pack directories

**Read-Only vs Human Confirmation**:
- Evidence pack: Read-only (archived)
- Evidence pack creation: Requires human action (scripts or manual)
- Evidence pack modification: Forbidden (archived)

**Frontend Visibility**: Frontend can read evidence pack contents, but cannot create or modify evidence packs.

---

### 9. Knowledge / Memory / Document

**Existence**: YES (partial)

**Stable ID**: YES (`document_id`, `knowledge_id`)

**Lifecycle State**: PARTIAL (versioning exists, but not fully verified)

**Fact**: Knowledge Management subsystem exists with Memory, Document Center, Knowledge Base structures.

**Evidence**:
- `backend/subsystems/knowledge_management/models.py`: `DocumentRecord`, `AccessControlRule`, `ConflictDetectionResult`, `DocumentVersionRecord` dataclasses exist
- `backend/subsystems/knowledge_management/README.md`: Defines Memory, Document Center, Knowledge Base structures
- GCD_v2 Section 8.2: Defines Memory, Document Center, Knowledge Base infrastructure

**Fields** (from models):
- `document_id`: Unique identifier (string)
- `content`: Document content (string)
- `metadata`: Document metadata (dict)
- `version_number`: Integer version number
- `created_at`: Timestamp
- `updated_at`: Timestamp
- `access_control_rules`: List of access control rules

**State Information Location**:
- Knowledge Management: `backend/subsystems/knowledge_management/` (structure only)
- Storage: `backend/subsystems/knowledge_management/storage.py` (implementation)
- Versioning: `backend/subsystems/knowledge_management/versioning.py` (implementation)

**Read-Only vs Human Confirmation**:
- Document read: Read-only (Role read-controlled)
- Document write: Requires access control (Role write-controlled)
- Document versioning: Not fully verified (per DESIGN_COMPLIANCE_AUDIT.md Section 3.2)

**Frontend Visibility**: Frontend can read documents (subject to access control), but write operations require backend enforcement.

---

## Summary Table

| Entity | Exists | Stable ID | Lifecycle State | Read-Only | Human Confirmation Required |
|--------|--------|-----------|-----------------|-----------|----------------------------|
| Company | NO | N/A | N/A | N/A | N/A |
| Cell | YES | YES | PARTIAL | YES | NO |
| Role | YES | YES | PARTIAL | YES | NO |
| Task/Work Order | YES | YES | YES | YES | YES (completion) |
| Task Force | YES | YES | YES | YES | NO |
| Execution/Run | YES | YES | YES | YES | YES (triggering) |
| Decision | YES | YES | YES | YES | YES (creation) |
| Audit/Evidence | YES | YES | YES | YES | YES (creation) |
| Knowledge/Memory/Document | YES | YES | PARTIAL | PARTIAL | YES (write) |

---

**END OF FRONTEND ENTITY FACT MAP**

