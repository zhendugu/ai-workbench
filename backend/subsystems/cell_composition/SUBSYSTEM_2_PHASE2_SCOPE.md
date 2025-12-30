# Cell Composition Subsystem (Subsystem 2) - Phase-2 Scope Declaration

**Status**: FROZEN  
**Effective Date**: 2025-12-26  
**Work Order**: WO-PHASE2-CELL-SEMANTIC-REDUCTION-001  
**Stage**: 6-B (Implementation Authorization)  
**Phase**: Phase-2 (Core Execution)

---

## Purpose

This document defines the **hard limits** for Cell Composition Subsystem in Phase-2.  
This document is **FROZEN** and may not be modified without invalidating Phase-2 gate approval.

**Any stateful Cell semantics are deferred to Phase-3.**

---

## Phase-2 Semantic Reduction Declaration

### Core Principle

**Cell is a static declarative composition, not a runtime entity.**

**Cell has no state, no lifecycle, no execution semantics in Phase-2.**

### What Was Removed (Phase-2 Semantic Reduction)

The following semantics have been **explicitly removed** from Phase-2:

1. ❌ **Cell state structure** (active, idle, executing, dissolved)
2. ❌ **Cell state transition structure**
3. ❌ **Cell lifecycle management**
4. ❌ **Cell runtime state**
5. ❌ **Cell activation / deactivation**
6. ❌ **Cell execution semantics**
7. ❌ **Cell orchestration**
8. ❌ **Cell workflow semantics**

**All of the above are deferred to Phase-3.**

---

## Phase-2 Allowed Capabilities

### Authorized Capabilities (Design-Time Only)

The following capabilities are **authorized for Phase-2 implementation**:

#### C-CELL-1: Register Cell Definition (STATIC, NO STATE)

**Purpose**: Store a Cell definition as a static, declarative composition specification.

**Allowed Behavior**:
- Store Cell definition with:
  - `cell_id`: Unique identifier
  - `role_ids`: List of role identifiers (read-only references to Role definitions)
  - `input_contract`: External input contract structure
  - `output_format`: External output format structure
- Overwrite existing Cell definition with same `cell_id`
- Persist to storage (JSON file pattern, like Role Management)

**Forbidden Behavior**:
- ❌ Store Cell state (active, idle, executing, dissolved)
- ❌ Store Cell status or lifecycle information
- ❌ Store Cell state transitions
- ❌ Store Cell execution history
- ❌ Store Cell runtime information

#### C-CELL-2: Query Cell Definition (READ-ONLY)

**Purpose**: Retrieve an existing Cell definition by `cell_id`.

**Allowed Behavior**:
- Load Cell definition from in-memory cache (if present)
- Load Cell definition from disk storage
- Return "not_found" if Cell definition does not exist
- Return structured error for invalid input

**Forbidden Behavior**:
- ❌ Return Cell state information
- ❌ Return Cell status or lifecycle information
- ❌ Return Cell execution history
- ❌ Return Cell runtime information
- ❌ Create default Cell definition
- ❌ Fix or normalize stored Cell definition

#### C-CELL-3: Validate Cell Completeness (PURE VALIDATION)

**Purpose**: Validate that a Cell definition is complete per schema rules.

**Allowed Behavior**:
- Validate required fields exist: `cell_id`, `role_ids`, `input_contract`, `output_format`
- Validate field types: strings, lists, dictionaries
- Validate non-empty checks (strict mode)
- Validate `role_ids` references (read-only check via C-ROLE-2)
- Return structured errors/warnings

**Forbidden Behavior**:
- ❌ Validate Cell state structure
- ❌ Validate Cell state transitions
- ❌ Validate Cell lifecycle rules
- ❌ Validate Cell execution semantics
- ❌ Auto-fix or normalize Cell definition
- ❌ Write or modify Cell definition

---

## Phase-2 Explicitly Forbidden Capabilities

The following capabilities are **explicitly forbidden** in Phase-2:

1. ❌ **Cell Execution**: Execute a Cell or trigger Cell execution
2. ❌ **Cell Activation**: Activate or deactivate a Cell
3. ❌ **Cell State Management**: Manage Cell runtime state
4. ❌ **Cell State Transitions**: Manage Cell state transitions
5. ❌ **Cell Lifecycle Management**: Manage Cell lifecycle (creation, activation, dissolution)
6. ❌ **Cell Orchestration**: Orchestrate multiple Cells
7. ❌ **Cell Workflow Semantics**: Define or manage Cell workflow
8. ❌ **Cell Runtime Monitoring**: Monitor Cell runtime behavior
9. ❌ **Cell Status Queries**: Query Cell status or state
10. ❌ **Cell Coordination**: Coordinate between Cells

**All of the above are deferred to Phase-3.**

---

## Data Model Reduction

### Phase-2 Cell Definition Model (Reduced)

**Allowed Fields** (Phase-2 only):

```python
CellDefinition {
    cell_id: str                    # Unique identifier
    role_ids: List[str]            # List of role identifiers (read-only references)
    input_contract: Dict          # External input contract structure
    output_format: Dict            # External output format structure
}
```

### Forbidden Fields (Phase-2)

The following fields are **explicitly forbidden** in Phase-2:

- ❌ `state`: Cell state (active, idle, executing, dissolved)
- ❌ `status`: Cell status information
- ❌ `lifecycle`: Cell lifecycle information
- ❌ `state_transitions`: Cell state transition structure
- ❌ `execution_history`: Cell execution history
- ❌ `runtime_info`: Cell runtime information
- ❌ `activation_time`: Cell activation timestamp
- ❌ `deactivation_time`: Cell deactivation timestamp
- ❌ `current_state`: Current Cell state
- ❌ `previous_state`: Previous Cell state

**All of the above are deferred to Phase-3.**

---

## Implementation Constraints

### Hard Constraints (Must Hold)

1. ❌ **No State Machine**: Must not introduce state machine
2. ❌ **No Lifecycle**: Must not introduce lifecycle
3. ❌ **No Cross-Subsystem Runtime Coordination**: Must not coordinate with other subsystems at runtime
4. ❌ **No Role Permission/Execution Semantics**: Must not depend on Role's permission or execution semantics
5. ✅ **C-EXEC-1 Compatible**: Must be executable as single action via C-EXEC-1
6. ✅ **Manual Rollback**: Must be manually recoverable (JSON file pattern)
7. ❌ **No Implicit Process**: Must not introduce implicit process or automatic progression

### Allowed Dependencies

- ✅ **Read Role Definitions**: Can read Role definitions via C-ROLE-2 (read-only)
- ✅ **No Execution Dependency**: Does not require Role execution or permission semantics

### Forbidden Dependencies

- ❌ **Cell Execution**: Must not depend on Cell execution capabilities
- ❌ **Cell State Management**: Must not depend on Cell state management
- ❌ **Cell Lifecycle**: Must not depend on Cell lifecycle management

---

## Implementation Pattern

### Follow Subsystem 1 (Role Management) Pattern

**Similarities**:
- Static declaration (like Role)
- No state machine (unlike original Cell definition)
- No lifecycle (unlike original Cell definition)
- Only composition and interface contract definitions
- JSON file persistence pattern
- In-memory cache pattern

**Differences**:
- Cell references multiple Roles (via `role_ids`)
- Cell has external interface contract (input/output)
- Cell does not have state (Phase-2 reduction)

---

## Verification Checklist

Before authorizing any Cell Composition capability implementation, verify:

- [ ] Cell definition model does NOT contain state fields
- [ ] Cell definition model does NOT contain lifecycle fields
- [ ] Capability does NOT manage Cell state
- [ ] Capability does NOT manage Cell lifecycle
- [ ] Capability does NOT trigger Cell execution
- [ ] Capability does NOT coordinate with other subsystems at runtime
- [ ] Capability is C-EXEC-1 compatible (single action, single subsystem)
- [ ] Capability allows manual rollback (JSON file pattern)
- [ ] Capability follows Subsystem 1 (Role Management) pattern

---

## Freeze Declaration

**This document is FROZEN.**

- Any modification invalidates Phase-2 gate approval
- Any implementation exceeding this scope is a violation
- Violations automatically revoke Phase-2 status

**Effective Date**: 2025-12-26  
**Frozen By**: WO-PHASE2-CELL-SEMANTIC-REDUCTION-001

---

## Phase-3 Deferral Statement

**Any stateful Cell semantics are deferred to Phase-3.**

Phase-3 may authorize:
- Cell state structure (active, idle, executing, dissolved)
- Cell state transition structure
- Cell lifecycle management
- Cell execution capabilities
- Cell orchestration capabilities

**Phase-3 authorization requires a new gate and a new scope document.**

---

**END OF PHASE-2 SCOPE DECLARATION**

