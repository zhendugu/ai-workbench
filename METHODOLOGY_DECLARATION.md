# Methodology Declaration

**Document Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Purpose**: Declare methodology adoption as a declarative choice, not an implementation.

**Authority**: AI_Virtual_Company_Organizational_GCD_v2.md, FE_FACT_METHODOLOGY_WORKFLOW_STATE.md, DESIGN_COMPLIANCE_AUDIT.md

---

## Methodology Semantic Objects

### Methodology Registry

**Format**: Declarative list of methodology declarations

**Type**: Array of methodology objects (read-only)

**Purpose**: Declare which methodologies are adopted, without implementing them.

---

## Methodology Declarations

### Methodology 1: Work Order Structure

**methodology_id**: `work-order-structure`

**methodology_name**: `Work Order Structure`

**description**: 
```
Implicit workflow pattern observed in the system:
- Work Orders follow pattern: WO-<Phase>-<Number>
- Work Orders have phases: phase_q/, phase_k_a/, phase_m/, etc.
- Work Orders have execution artifacts: EXECUTION_STATUS*.md, FINAL_*_DECISION.md
- Work Orders have evidence packs: *_EVIDENCE_PACK_* directories

This is an IMPLICIT methodology, not an explicit template.
```

**scope**: `company`

**status**: `active`

**evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Q3: "Workflow is implicit in Work Order structure (phase → work order → execution → decision → evidence)"

**non_executable**: true

---

### Methodology 2: Execution Pattern

**methodology_id**: `execution-pattern`

**methodology_name**: `Execution Pattern`

**description**:
```
Implicit execution pattern observed in the system:
- generate_*_run_configs.py → run_*_matrix.sh → collect_hashes_*.py → detect_*.py

This pattern is observed in:
- Phase Q4-1: generate_run_configs_q4_1.py → run_q4_1_matrix.sh → collect_hashes.py → detect_leakage.py
- Phase Q4-2: generate_run_configs_q4_2.py → run_q4_2_matrix.sh → collect_hashes_q4_2.py → detect_leakage_q4_2.py
- Phase R2E: (similar pattern)

This is an IMPLICIT methodology, not an explicit template.
```

**scope**: `execution`

**status**: `active`

**evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Q4: "Execution habits form implicit workflows, but these are not explicitly structured as reusable methodologies."

**non_executable**: true

---

### Methodology 3: Phase-Based Organization

**methodology_id**: `phase-based-organization`

**methodology_name**: `Phase-Based Organization`

**description**:
```
Organizational structure based on phases:
- Phases are named: Phase C, D, E, F, G, H, I, J, K, L, M, N, Q, R, S
- Phases have status: OPEN, CLOSED, FROZEN
- Phases have closure summaries: PHASE_*_CLOSURE_SUMMARY.md
- Phases have traceability: TRACEABILITY_INDEX_*.md

This is an IMPLICIT methodology, not an explicit template.
```

**scope**: `company`

**status**: `active`

**evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Q7: "Phase structures are named and saved (as directories and documents), but not explicitly as reusable methodology templates."

**non_executable**: true

---

### Methodology 4: Epoch-Based Time-Fractured Intelligence (FROZEN)

**methodology_id**: `epoch-based-time-fractured-intelligence`

**methodology_name**: `Epoch-Based Time-Fractured Intelligence System`

**description**:
```
Paradigm frozen in Phase Q:
- Epoch boundaries as hard structural breaks
- State destruction at epoch end
- No cross-epoch state inheritance
- AI operations contained within epochs

This methodology is FROZEN and REFERENCE-ONLY.
```

**scope**: `paradigm`

**status**: `frozen`

**evidence**: 
- `phase_q/PARADIGM_FREEZE_DECLARATION.md`: Paradigm FROZEN
- `phase_q/LIMITS_OF_VALIDITY.md`: Validity boundaries
- `phase_q/PHASE_Q_CLOSURE_SUMMARY.md`: Phase Q CLOSED

**non_executable**: true

**frozen_ref**: `phase_q/PARADIGM_FREEZE_DECLARATION.md`

---

### Methodology 5: Constitutional Compliance Audit

**methodology_id**: `constitutional-compliance-audit`

**methodology_name**: `Constitutional Compliance Audit`

**description**:
```
Audit methodology for verifying system compliance with design documents:
- Compare implementation against GCD_v2
- Identify deviations and gaps
- Document compliance status
- Provide evidence-based assessment

This methodology is used in DESIGN_COMPLIANCE_AUDIT.md.
```

**scope**: `audit`

**status**: `active`

**evidence**: `DESIGN_COMPLIANCE_AUDIT.md`: Design compliance audit report

**non_executable**: true

---

## Methodology Rules

### Rule 1: Methodology Does Not Change System Behavior

**Statement**: Methodology declaration does not change system behavior.

**Enforcement**: Methodology is a declarative choice only. It does not:
- Generate tasks
- Trigger executions
- Modify system state
- Implement logic

**Evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Summary: "Methodologies/workflows exist only as implicit patterns in Work Order structure and execution habits."

---

### Rule 2: Methodology Is For Context Only

**Statement**: Methodology declaration is used only for:
- Human cognitive framework
- Frontend display information
- Audit context

**Enforcement**: Methodology serves as a reference point for:
- Understanding system approach
- Displaying methodology adoption
- Providing audit context

**Evidence**: `FE_FACT_METHODOLOGY_WORKFLOW_STATE.md` Q1: "No structured methodology representation exists. Workflow rules exist as documents, but not as structured data."

---

### Rule 3: Methodology Status

**Allowed Status Values**:
- `active`: Methodology is currently in use (implicitly or explicitly)
- `deprecated`: Methodology is no longer recommended but may still be referenced
- `experimental`: Methodology is under evaluation
- `frozen`: Methodology is frozen and cannot be modified

**Enforcement**: Methodology status is declarative only. It does not trigger any system behavior.

---

## Methodology Indexing

### Global Index Entry

**Location**: To be added to global index (read-only)

**Format**:
```json
{
  "entity_type": "methodology",
  "entity_id": "<methodology_id>",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "status": "<active|deprecated|experimental|frozen>",
  "scope": "<company|workflow|task-force|execution|audit|paradigm>"
}
```

**Purpose**: Enable frontend to discover and reference Methodology objects.

---

## Methodology Relationships

### Referenced By

- Company declaration (if methodology is company-scoped)
- Workflow declaration (if workflow uses methodologies)
- Frontend semantic contract

### References

- Frozen design documents (for frozen methodologies)
- Phase documents (for phase-based methodologies)
- Audit documents (for audit methodologies)

---

## Modification Protocol

### This Declaration Is

- **DECLARATIVE**: Describes methodology adoption, not implementation
- **READ-ONLY**: Cannot be modified by frontend or automated processes
- **NON-EXECUTABLE**: Does not trigger, execute, or modify any system behavior

### Modification Authority

Only human authorization can modify this declaration. Modification requires:
1. Explicit human approval
2. Version tracking
3. Update to global index
4. No retroactive changes to frozen methodologies

---

## Audit Trail

**Declaration Created**: 2025-12-28

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Authority**: FE_FACT_METHODOLOGY_WORKFLOW_STATE.md, DESIGN_COMPLIANCE_AUDIT.md

**Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

---

**END OF METHODOLOGY DECLARATION**

