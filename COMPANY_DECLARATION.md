# Company Declaration

**Document Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Purpose**: Declare a Company-level semantic anchor object for human cognition and frontend navigation.

**Authority**: AI_Virtual_Company_Organizational_GCD_v2.md, FE_FACT_ENTITY_MAP.md

---

## Company Semantic Object

### Company ID

**company_id**: `ai-workbench-v1`

**Stability**: This ID is stable and human-readable. It does not change unless the company instance is replaced.

---

### Company Properties

#### company_name

**Value**: `AI Workbench`

**Type**: String (human-readable)

**Purpose**: Human-facing company name for navigation and identification.

---

#### creation_timestamp

**Value**: `2025-12-28T00:00:00Z` (approximate, based on project inception)

**Type**: ISO 8601 timestamp

**Purpose**: Declarative timestamp for company instance creation. This is a declaration, not an execution record.

---

#### current_phase

**Value**: `Phase R` (CLOSED)

**Type**: Phase identifier (string)

**Purpose**: Declare the current phase state for human navigation.

**Evidence**:
- `phase_q/PHASE_R_STATUS.md`: Phase R status document
- `phase_q/PHASE_R_CLOSURE_SUMMARY.md`: Phase R CLOSED
- `CURRENT_STATE_SNAPSHOT.md`: `ACTIVE_STAGE: 6-A`

**Note**: This is a declarative statement of current phase, not an execution state.

---

#### frozen_design_refs

**Value**: List of frozen design document references

**Type**: Array of document paths (strings)

**Purpose**: Declare references to frozen design documents for human navigation and audit.

**References**:
- `docs/GCD.md`: AI Virtual Company Organizational GCD (authority document)
- `phase_q/PARADIGM_FREEZE_DECLARATION.md`: Epoch-based Time-Fractured Intelligence System (FROZEN)
- `phase_q/LIMITS_OF_VALIDITY.md`: Q4-2 validity boundaries
- `DESIGN_COMPLIANCE_AUDIT.md`: Design compliance audit report
- `docs/ENGINE_V1_FREEZE.md`: Engine v1 freeze declaration
- `docs/EXECUTION_CONTRACT.md`: Execution contract (frozen)
- `docs/WORKFLOW_RULES.md`: Workflow rules (frozen)

**Note**: These are read-only references. No modification capability.

---

#### description

**Value**: Human-facing summary of the company instance

**Type**: String (markdown-compatible)

**Content**:
```
AI Workbench is a governance framework and execution system for AI-driven virtual company structures.

The system implements:
- Role-based organizational structure (GCD_v2)
- Cell composition and Task Force coordination
- Epoch-based time-fractured intelligence paradigm (Phase Q, FROZEN)
- Constitutional compliance and audit mechanisms
- Read-only operator interface (Phase S)

Current state:
- Phase R: CLOSED (Red Team validation complete)
- Active Stage: 6-A (Implementation not authorized)
- Active Blueprint: ai-virtual-company-org

The system is read-only at the frontend layer. All execution requires human authorization.
```

**Purpose**: Provide human-readable context for navigation and understanding.

---

## Company Rules

### Rule 1: No Execution Authority

**Statement**: Company does not own execution authority.

**Enforcement**: Company is a declarative object only. It does not trigger, execute, or modify any system behavior.

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 1: "Frontend MUST NOT execute work orders, trigger scripts, or invoke Python scripts."

---

### Rule 2: No Decision Authority

**Statement**: Company does not own decision authority.

**Enforcement**: Company is a declarative object only. It does not make decisions, approve actions, or replace human judgment.

**Evidence**: `FE_FACT_FRONTEND_BOUNDARIES.md` Section 5: "Frontend MUST NOT make decisions, approve actions, or replace human judgment."

---

### Rule 3: Semantic Anchor Only

**Statement**: Company is only a semantic anchor for human cognition and frontend navigation.

**Enforcement**: Company serves as a reference point for:
- Human understanding of system scope
- Frontend navigation structure
- Audit and traceability context

**Evidence**: `FE_FACT_ENTITY_MAP.md` Section 1: "Company (公司) - Existence: NO" (no Company entity exists, this declaration creates the semantic anchor).

---

## Company Indexing

### Global Index Entry

**Location**: To be added to global index (read-only)

**Format**: 
```json
{
  "entity_type": "company",
  "entity_id": "ai-workbench-v1",
  "declaration_file": "COMPANY_DECLARATION.md",
  "read_only": true,
  "non_executable": true
}
```

**Purpose**: Enable frontend to discover and reference the Company object.

---

## Company Relationships

### Referenced By

- Workflow declarations (if any)
- Methodology declarations (if any)
- Frontend semantic contract

### References

- Frozen design documents (listed in `frozen_design_refs`)
- Current phase (Phase R)
- Active blueprint (ai-virtual-company-org)

---

## Modification Protocol

### This Declaration Is

- **DECLARATIVE**: Describes what exists, not how to execute
- **READ-ONLY**: Cannot be modified by frontend or automated processes
- **NON-EXECUTABLE**: Does not trigger, execute, or modify any system behavior

### Modification Authority

Only human authorization can modify this declaration. Modification requires:
1. Explicit human approval
2. Version tracking
3. Update to global index
4. No retroactive changes to frozen references

---

## Audit Trail

**Declaration Created**: 2025-12-28

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Authority**: FE_FACT_ENTITY_MAP.md, FE_FACT_FRONTEND_BOUNDARIES.md

**Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

---

**END OF COMPANY DECLARATION**

