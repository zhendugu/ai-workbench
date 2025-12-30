# Semantic Object Index

**Document Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Purpose**: Global index of semantic objects for frontend consumption and human navigation.

**Authority**: WO-FE-SEMANTIC-ALIGN-0 deliverables, FE_SEMANTIC_CONTRACT.md

---

## Index Structure

This index provides a read-only registry of all semantic objects declared in the system.

**Format**: JSON-compatible structure (read-only)

**Purpose**: Enable frontend to discover and reference semantic objects.

---

## Semantic Objects

### Company

```json
{
  "entity_type": "company",
  "entity_id": "ai-workbench-v1",
  "declaration_file": "COMPANY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true
}
```

---

### Workflow

```json
{
  "entity_type": "workflow",
  "entity_id": "ai-workbench-main-workflow",
  "declaration_file": "WORKFLOW_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "workflow_type": "declarative-topology"
}
```

---

### Methodology

```json
{
  "entity_type": "methodology",
  "entity_id": "work-order-structure",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "status": "active",
  "scope": "company"
}
```

```json
{
  "entity_type": "methodology",
  "entity_id": "execution-pattern",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "status": "active",
  "scope": "execution"
}
```

```json
{
  "entity_type": "methodology",
  "entity_id": "phase-based-organization",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "status": "active",
  "scope": "company"
}
```

```json
{
  "entity_type": "methodology",
  "entity_id": "epoch-based-time-fractured-intelligence",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "status": "frozen",
  "scope": "paradigm",
  "frozen_ref": "phase_q/PARADIGM_FREEZE_DECLARATION.md"
}
```

```json
{
  "entity_type": "methodology",
  "entity_id": "constitutional-compliance-audit",
  "declaration_file": "METHODOLOGY_DECLARATION.md",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "status": "active",
  "scope": "audit"
}
```

---

### Cell

```json
{
  "entity_type": "cell",
  "entity_id": "<cell_id>",
  "declaration_location": "backend/subsystems/cell_composition/cells/*.json",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "note": "Cell definitions exist as JSON files. Frontend must query backend API or read JSON files."
}
```

---

### Role

```json
{
  "entity_type": "role",
  "entity_id": "<role_id>",
  "declaration_location": "backend/subsystems/role_management/roles/*.json",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": true,
  "note": "Role definitions exist as JSON files. Frontend must query backend API or read JSON files."
}
```

---

### Work Order

```json
{
  "entity_type": "work_order",
  "entity_id": "<work_order_id>",
  "declaration_location": "FINAL_*_DECISION.md files, phase directories",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": false,
  "note": "Work Orders are PARTIAL. Only work orders with FINAL_*_DECISION.md files are guaranteed to exist."
}
```

---

### Execution

```json
{
  "entity_type": "execution",
  "entity_id": "<execution_id>",
  "declaration_location": "EXECUTION_STATUS*.md files, EXECUTION_LOG_ARCHIVE_*/",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": false,
  "note": "Executions are PARTIAL. Only executions with EXECUTION_STATUS*.md files are guaranteed to exist."
}
```

---

### Decision

```json
{
  "entity_type": "decision",
  "entity_id": "<decision_id>",
  "declaration_location": "FINAL_*_DECISION.md files",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": false,
  "note": "Decisions are PARTIAL. Only decisions with FINAL_*_DECISION.md files are guaranteed to exist."
}
```

---

### Evidence

```json
{
  "entity_type": "evidence",
  "entity_id": "<evidence_pack_id>",
  "declaration_location": "audit_evidence/*/, phase_*/*/PASS_EVIDENCE_PACK_*/",
  "read_only": true,
  "non_executable": true,
  "stable_id": true,
  "guaranteed_existence": false,
  "note": "Evidence packs are PARTIAL. Only evidence packs with directories are guaranteed to exist."
}
```

---

## Index Rules

### Rule 1: Read-Only

**Statement**: This index is read-only.

**Enforcement**: No modifications allowed without human authorization.

---

### Rule 2: Non-Executable

**Statement**: This index does not trigger, execute, or modify any system behavior.

**Enforcement**: Index is declarative only. It describes what exists, not how to execute.

---

### Rule 3: Guaranteed Existence

**Statement**: Objects with `guaranteed_existence: true` are guaranteed to exist. Objects with `guaranteed_existence: false` are PARTIAL (may or may not exist).

**Enforcement**: Frontend must check for existence before displaying PARTIAL objects.

---

## Index Modification

### This Index Is

- **DECLARATIVE**: Describes semantic object registry, not implementation
- **READ-ONLY**: Cannot be modified by frontend or automated processes
- **NON-EXECUTABLE**: Does not trigger, execute, or modify any system behavior

### Modification Authority

Only human authorization can modify this index. Modification requires:
1. Explicit human approval
2. Version tracking
3. Update to all referenced declarations
4. No retroactive changes to frozen entries

---

## Audit Trail

**Index Created**: 2025-12-28

**Work Order**: WO-FE-SEMANTIC-ALIGN-0

**Authority**: FE_SEMANTIC_CONTRACT.md, WO-FE-SEMANTIC-ALIGN-0 deliverables

**Status**: DECLARATIVE / READ-ONLY / NON-EXECUTABLE

---

**END OF SEMANTIC OBJECT INDEX**

