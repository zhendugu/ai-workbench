# Phase-4 Allowed Semantics Matrix

**Document Status**: **AUTHORITATIVE FOR PHASE-4**  
**Date**: 2025-12-26  
**Phase**: Phase-4 Gate A  
**Purpose**: Define allowed and forbidden usage of Phase-3 L1 structures in Phase-4

---

## Critical Declaration

**This document is AUTHORITATIVE for Phase-4.**

**This document does NOT authorize Phase-4 implementation.**

**This document defines semantic boundaries only.**

**This document does NOT modify Phase-3 code or documents.**

---

## Matrix Structure

**For each Phase-3 L1 structure, this matrix defines**:
- ✅ **Allowed Usage**: What Phase-4 MAY do with the structure
- ❌ **Forbidden Usage**: What Phase-4 MUST NOT do with the structure

**All structures are READ-ONLY FOREVER unless explicitly stated otherwise.**

---

## Phase-3 L1 Structures Matrix

### 1. TriggerCondition (Catalyst Hub)

**Structure**: `TriggerCondition`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query TriggerCondition (read-only) | ❌ Evaluate TriggerCondition.condition_type |
| **Store** | ✅ Register TriggerCondition (storage only) | ❌ Use TriggerCondition to trigger actions |
| **Return** | ✅ Return TriggerCondition in queries | ❌ Use TriggerCondition for decision-making |
| **Evaluate** | ❌ **NEVER** | ❌ Evaluate TriggerCondition.condition_type |
| **Trigger** | ❌ **NEVER** | ❌ Use TriggerCondition to trigger actions |
| **Create Task Force** | ❌ **NEVER** | ❌ Use TriggerCondition to create Task Forces |
| **Behavior** | ❌ **NEVER** | ❌ Use TriggerCondition to influence behavior |

**Explicit Statement**: "TriggerCondition is a descriptive label only. It is never evaluated, never used for triggering, and never influences behavior."

---

### 2. RoutingHint (Catalyst Hub)

**Structure**: `RoutingHint`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query RoutingHint (read-only) | ❌ Use RoutingHint.suggested_cell_ids for routing |
| **Store** | ✅ Register RoutingHint (storage only) | ❌ Use RoutingHint to make routing decisions |
| **Return** | ✅ Return RoutingHint in queries | ❌ Use RoutingHint.reasoning for routing logic |
| **Route** | ❌ **NEVER** | ❌ Use RoutingHint to route requirements |
| **Decision** | ❌ **NEVER** | ❌ Use RoutingHint to make routing decisions |
| **Evaluate** | ❌ **NEVER** | ❌ Evaluate RoutingHint.suggested_cell_ids |
| **Behavior** | ❌ **NEVER** | ❌ Use RoutingHint to influence behavior |

**Explicit Statement**: "RoutingHint is a descriptive label only. It is never used for routing, never makes routing decisions, and never influences behavior."

---

### 3. ExceptionType (Catalyst Hub)

**Structure**: `ExceptionType` (Enum)  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query ExceptionType (read-only) | ❌ Use ExceptionType for exception detection |
| **Store** | ✅ Register ExceptionType (storage only) | ❌ Use ExceptionType.DEAD_LOOP to detect dead loops |
| **Return** | ✅ Return ExceptionType in queries | ❌ Use ExceptionType.INVALID_STATE to detect invalid states |
| **Detect** | ❌ **NEVER** | ❌ Use ExceptionType to detect exceptions |
| **Evaluate** | ❌ **NEVER** | ❌ Use ExceptionType values for detection logic |
| **Behavior** | ❌ **NEVER** | ❌ Use ExceptionType to influence behavior |

**Explicit Statement**: "ExceptionType is a descriptive label only. It is never used for detection, contains no detection logic, and never influences behavior."

---

### 4. dissolution_conditions (Task Force)

**Structure**: `TaskForceDefinition.dissolution_conditions`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query dissolution_conditions (read-only) | ❌ Evaluate dissolution_conditions |
| **Store** | ✅ Store dissolution_conditions (registration only) | ❌ Use dissolution_conditions to trigger dissolution |
| **Return** | ✅ Return dissolution_conditions in queries | ❌ Check dissolution_conditions |
| **Evaluate** | ❌ **NEVER** | ❌ Evaluate dissolution_conditions |
| **Trigger** | ❌ **NEVER** | ❌ Use dissolution_conditions to trigger dissolution |
| **Check** | ❌ **NEVER** | ❌ Check dissolution_conditions |
| **Behavior** | ❌ **NEVER** | ❌ Use dissolution_conditions to influence behavior |

**Explicit Statement**: "dissolution_conditions are descriptive text only. They are never evaluated, never checked, and never influence behavior."

---

### 5. success_criteria (Task Force)

**Structure**: `TaskForceGoal.success_criteria`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query success_criteria (read-only) | ❌ Evaluate success_criteria |
| **Store** | ✅ Store success_criteria (registration only) | ❌ Use success_criteria to determine success |
| **Return** | ✅ Return success_criteria in queries | ❌ Check success_criteria |
| **Evaluate** | ❌ **NEVER** | ❌ Evaluate success_criteria |
| **Determine** | ❌ **NEVER** | ❌ Use success_criteria to determine success |
| **Check** | ❌ **NEVER** | ❌ Check success_criteria |
| **Behavior** | ❌ **NEVER** | ❌ Use success_criteria to influence behavior |

**Explicit Statement**: "success_criteria are descriptive text only. They are never evaluated, never checked, and never influence behavior."

---

### 6. WorkflowStateSnapshot.cell_states (Catalyst Hub)

**Structure**: `WorkflowStateSnapshot.cell_states`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query cell_states (read-only) | ❌ Read Cell-State based on cell_states |
| **Store** | ✅ Store cell_states (registration only) | ❌ Query Cell state (C-CELL-4, C-CELL-5) based on cell_states |
| **Return** | ✅ Return cell_states in queries | ❌ Use cell_states to affect behavior |
| **Read Cell-State** | ❌ **NEVER** | ❌ Read Cell-State subsystem based on cell_states |
| **Query Cell State** | ❌ **NEVER** | ❌ Query Cell state (C-CELL-4, C-CELL-5) based on cell_states |
| **Infer** | ❌ **NEVER** | ❌ Infer Cell state from cell_states |
| **Behavior** | ❌ **NEVER** | ❌ Use cell_states to affect behavior |

**Explicit Statement**: "cell_states in WorkflowStateSnapshot are descriptive values only. They are never read from Cell-State subsystem and never influence behavior."

---

### 7. AIBudgetPolicy.max_tokens, max_cost (AI Resource Governance)

**Structure**: `AIBudgetPolicy.max_tokens`, `AIBudgetPolicy.max_cost`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query max_* fields (read-only) | ❌ Enforce max_tokens limits |
| **Store** | ✅ Store max_* fields (registration only) | ❌ Enforce max_cost limits |
| **Return** | ✅ Return max_* fields in queries | ❌ Block operations based on max_* fields |
| **Enforce** | ❌ **NEVER** | ❌ Enforce max_tokens or max_cost limits |
| **Block** | ❌ **NEVER** | ❌ Block operations based on max_* fields |
| **Throttle** | ❌ **NEVER** | ❌ Throttle operations based on max_* fields |
| **Behavior** | ❌ **NEVER** | ❌ Use max_* fields to influence behavior |

**Explicit Statement**: "max_tokens and max_cost are informational values only. They are never enforced, never block operations, and never influence behavior."

---

### 8. capability_contribution (Task Force)

**Structure**: `TaskForceMember.capability_contribution`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query capability_contribution (read-only) | ❌ Extract capabilities based on capability_contribution |
| **Store** | ✅ Store capability_contribution (registration only) | ❌ Coordinate capabilities based on capability_contribution |
| **Return** | ✅ Return capability_contribution in queries | ❌ Use capability_contribution for execution |
| **Extract** | ❌ **NEVER** | ❌ Extract capabilities based on capability_contribution |
| **Coordinate** | ❌ **NEVER** | ❌ Coordinate capabilities based on capability_contribution |
| **Execute** | ❌ **NEVER** | ❌ Use capability_contribution for execution |
| **Behavior** | ❌ **NEVER** | ❌ Use capability_contribution to influence behavior |

**Explicit Statement**: "capability_contribution is a list of identifiers only. It never extracts capabilities, never coordinates capabilities, and never influences behavior."

---

### 9. CellState.state (Cell-State)

**Structure**: `CellState.state`  
**Status**: **READ-ONLY FOREVER**

| Usage Type | Allowed | Forbidden |
|------------|---------|-----------|
| **Read** | ✅ Query state (read-only) | ❌ Infer behavior from state values |
| **Update** | ✅ Update state (human-initiated only, descriptive only) | ❌ Validate state values |
| **Return** | ✅ Return state in queries | ❌ Enforce state transitions |
| **Infer** | ❌ **NEVER** | ❌ Infer behavior from state values |
| **Validate** | ❌ **NEVER** | ❌ Validate state values (beyond type safety) |
| **Transition** | ❌ **NEVER** | ❌ Enforce state transitions |
| **Behavior** | ❌ **NEVER** | ❌ Use state to influence behavior |

**Explicit Statement**: "state is an arbitrary string value. It has no semantic meaning, never implies transitions, and never influences behavior."

---

## Universal Rules

### Rule 1: READ-ONLY FOREVER Structures

**All structures listed in `PHASE_3_L1_READ_ONLY_FOREVER_LIST.md` are READ-ONLY FOREVER.**

**Phase-4 MUST NOT:**
- ❌ Evaluate these structures
- ❌ Enforce based on these structures
- ❌ Use these structures for routing, triggering, detection, or execution
- ❌ Modify the semantics of these structures

**Phase-4 MAY:**
- ✅ Read these structures (query only)
- ✅ Store these structures (registration only)
- ✅ Return these structures in queries

---

### Rule 2: Descriptive Labels Only

**All structure names, field names, and enum values are descriptive labels only.**

**Phase-4 MUST NOT:**
- ❌ Infer behavior from structure names
- ❌ Infer enforcement from field names
- ❌ Infer detection from enum values

**Phase-4 MUST:**
- ✅ Treat all names as descriptive labels only
- ✅ Check freeze declarations for authoritative statements
- ✅ Apply canonical tests to verify descriptive-only nature

---

### Rule 3: No Implied Semantics

**No structure or field implies any semantics.**

**Phase-4 MUST NOT:**
- ❌ Assume structures have implied behavior
- ❌ Assume fields have implied enforcement
- ❌ Assume enums have implied detection

**Phase-4 MUST:**
- ✅ Explicitly check freeze declarations
- ✅ Explicitly verify descriptive-only nature
- ✅ Explicitly request authorization for any behavioral use

---

## Reference Documents

**This matrix is based on**:

1. **Phase-3 L1 READ-ONLY FOREVER List**:
   - `docs/PHASE_3_L1_READ_ONLY_FOREVER_LIST.md`

2. **Phase-3 L1 Semantic Interpretation Guide**:
   - `docs/PHASE_3_L1_SEMANTIC_INTERPRETATION_GUIDE.md`

3. **Phase-3 Global Review and Risk Scan**:
   - `docs/PHASE_3_GLOBAL_REVIEW_AND_RISK_SCAN.md`

**These documents are authoritative and must be referenced for all Phase-4 work.**

---

## Summary

**All Phase-3 L1 structures listed in this matrix are READ-ONLY FOREVER.**

**Phase-4 MUST NOT:**
- ❌ Evaluate, enforce, or use these structures for behavior
- ❌ Modify the semantics of these structures
- ❌ Add behavior to these structures

**Phase-4 MAY:**
- ✅ Read these structures (query only)
- ✅ Store these structures (registration only)
- ✅ Return these structures in queries

**This matrix is AUTHORITATIVE for Phase-4.**

---

**END OF PHASE-4 ALLOWED SEMANTICS MATRIX**

**This document is AUTHORITATIVE and does NOT modify Phase-3 code or documents.**

