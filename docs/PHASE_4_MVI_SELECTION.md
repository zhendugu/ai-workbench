# Phase-4 Minimal Viable Implementation (MVI) Selection

**Document Status**: **SELECTION ONLY**  
**Date**: 2025-12-26  
**Phase**: Phase-4 Gate A  
**Purpose**: Select and define exactly ONE Phase-4 MVI candidate

---

## Critical Declaration

**This document is SELECTION ONLY.**

**This document does NOT authorize Phase-4 implementation.**

**This document does NOT modify Phase-3 code or documents.**

**This document proposes MVI candidates and selects ONE for future consideration.**

**Implementation requires a separate authorization work order.**

---

## Selection Criteria

### Required Properties

**Any Phase-4 MVI candidate MUST**:
1. ✅ Be minimal (smallest possible extension)
2. ✅ Touch only ONE subsystem
3. ✅ Introduce NO execution, routing, triggering, enforcement
4. ✅ Be removable without affecting system behavior
5. ✅ Comply with Phase-4 Gate A constraints
6. ✅ Respect READ-ONLY FOREVER structures
7. ✅ Not modify Phase-3 L1 code or documents

---

## Candidate MVI Options

### Option 1: Human-Initiated Task Force Status Query

**Subsystem**: Task Force (Subsystem 4)

#### What It Does

**This MVI adds a single read-only capability**:
- `C-TF-4: Query Task Force Status Summary`
  - Accepts: `task_force_id` (string)
  - Returns: Structured summary of Task Force definition (read-only aggregation)
  - Behavior: Pure read-only query, no state changes, no evaluation

**Capability Details**:
- Reads Task Force definition (C-TF-3)
- Aggregates descriptive information:
  - Task Force name
  - Number of members
  - Number of goals
  - Number of dissolution conditions (as count, not evaluation)
  - Created date
  - Created by
- Returns structured summary object
- Records observability (C-OBS-1)

**No evaluation, no enforcement, no behavior influence.**

---

#### What It Explicitly Does NOT Do

**This MVI explicitly does NOT**:
- ❌ Evaluate dissolution_conditions
- ❌ Check success_criteria
- ❌ Extract or coordinate capabilities
- ❌ Create or modify Task Forces
- ❌ Trigger any actions
- ❌ Make any decisions
- ❌ Influence system behavior
- ❌ Read Cell-State or Role Management
- ❌ Perform any validation beyond type safety

**This is a pure read-only aggregation query.**

---

#### Phase-3 Structures It Touches (Read-Only)

**Read-Only Access**:
- ✅ `TaskForceDefinition` (via C-TF-3)
  - Reads: `task_force_id`, `name`, `members`, `goals`, `dissolution_conditions`, `created_by`, `created_at`
  - Does NOT evaluate: `dissolution_conditions` (counts only)
  - Does NOT evaluate: `success_criteria` (counts only)
  - Does NOT use: `capability_contribution` (counts only)

**No writes, no evaluation, no behavior.**

---

#### Risk Analysis

**Risk Level**: **LOW**

**Potential Violations**:
1. ⚠️ **Risk**: Accidentally evaluating `dissolution_conditions` or `success_criteria`
   - **Mitigation**: Explicitly count only, never evaluate or check
   - **Protection**: Code review must verify no conditional logic on these fields

2. ⚠️ **Risk**: Accidentally using `capability_contribution` for extraction
   - **Mitigation**: Count only, never extract or coordinate
   - **Protection**: Code review must verify no capability extraction logic

3. ⚠️ **Risk**: Accidentally creating dependencies on other subsystems
   - **Mitigation**: No cross-subsystem calls except Observability (C-OBS-1)
   - **Protection**: Code review must verify no Cell-State or Role Management calls

**Canonical Test**: "If this capability is removed, system behavior remains identical. Only the summary query disappears."

**Verdict**: **SAFE** - Pure read-only aggregation, no evaluation, no behavior.

---

### Option 2: Human-Initiated AI Usage Report Generator

**Subsystem**: AI Resource Governance (Subsystem 10)

#### What It Does

**This MVI adds a single read-only capability**:
- `C-AI-GOV-3: Generate AI Usage Report`
  - Accepts: `time_range_start`, `time_range_end`, `scope` (all optional)
  - Returns: Formatted human-readable report (text/markdown)
  - Behavior: Pure read-only report generation, no enforcement, no blocking

**Capability Details**:
- Reads AI usage data (C-AI-GOV-2)
- Formats aggregated data into human-readable report:
  - Summary statistics
  - Breakdown by model
  - Breakdown by caller
  - Time range information
- Returns formatted report string
- Records observability (C-OBS-1)

**No evaluation, no enforcement, no behavior influence.**

---

#### What It Explicitly Does NOT Do

**This MVI explicitly does NOT**:
- ❌ Enforce budget limits
- ❌ Block operations
- ❌ Throttle calls
- ❌ Evaluate `max_tokens` or `max_cost`
- ❌ Make enforcement decisions
- ❌ Trigger alerts
- ❌ Influence system behavior
- ❌ Read or modify budget policies

**This is a pure read-only report formatter.**

---

#### Phase-3 Structures It Touches (Read-Only)

**Read-Only Access**:
- ✅ `AICallRecord` (via C-AI-GOV-2)
  - Reads: `call_id`, `model`, `provider`, `total_tokens`, `estimated_cost`, `currency`, `caller`, `purpose`, `created_at`
  - Does NOT enforce: Any limits
  - Does NOT block: Any operations

- ✅ `AIBudgetPolicy` (read-only, if available)
  - Reads: `scope`, `period`, `currency`, `max_tokens`, `max_cost` (informational only)
  - Does NOT enforce: `max_tokens` or `max_cost`
  - Does NOT block: Any operations

**No writes, no enforcement, no behavior.**

---

#### Risk Analysis

**Risk Level**: **LOW**

**Potential Violations**:
1. ⚠️ **Risk**: Accidentally enforcing budget limits
   - **Mitigation**: Report only, never enforce or block
   - **Protection**: Code review must verify no enforcement logic

2. ⚠️ **Risk**: Accidentally using `max_*` fields for blocking
   - **Mitigation**: Display only, never compare or block
   - **Protection**: Code review must verify no comparison logic

3. ⚠️ **Risk**: Accidentally triggering alerts or notifications
   - **Mitigation**: Report generation only, no triggers
   - **Protection**: Code review must verify no alert/notification logic

**Canonical Test**: "If this capability is removed, system behavior remains identical. Only the report generation disappears."

**Verdict**: **SAFE** - Pure read-only report formatting, no enforcement, no behavior.

---

### Option 3: Human-Initiated Cell State History Query

**Subsystem**: Cell-State (Cell Composition Subsystem)

#### What It Does

**This MVI adds a single read-only capability**:
- `C-CELL-6: Query Cell State History`
  - Accepts: `cell_id` (string), `limit` (optional integer)
  - Returns: List of historical CellState records (read-only)
  - Behavior: Pure read-only history query, no state changes, no evaluation

**Capability Details**:
- Reads Cell state history from storage
- Returns list of historical CellState records:
  - Ordered by `updated_at` (descending)
  - Limited by `limit` parameter (if provided)
  - Each record: `cell_id`, `state`, `updated_by`, `updated_at`
- Returns structured list
- Records observability (C-OBS-1)

**No evaluation, no enforcement, no behavior influence.**

---

#### What It Explicitly Does NOT Do

**This MVI explicitly does NOT**:
- ❌ Evaluate state values
- ❌ Validate state transitions
- ❌ Enforce state rules
- ❌ Infer behavior from state
- ❌ Trigger actions based on state
- ❌ Modify Cell state
- ❌ Influence system behavior
- ❌ Read other subsystems

**This is a pure read-only history query.**

---

#### Phase-3 Structures It Touches (Read-Only)

**Read-Only Access**:
- ✅ `CellState` (DS-CELL-2)
  - Reads: `cell_id`, `state`, `updated_by`, `updated_at`
  - Does NOT evaluate: `state` values
  - Does NOT validate: State transitions
  - Does NOT infer: Behavior from state

**No writes, no evaluation, no behavior.**

---

#### Risk Analysis

**Risk Level**: **LOW-MEDIUM**

**Potential Violations**:
1. ⚠️ **Risk**: Accidentally evaluating state values
   - **Mitigation**: Return raw state values only, no evaluation
   - **Protection**: Code review must verify no conditional logic on state values

2. ⚠️ **Risk**: Accidentally inferring behavior from state history
   - **Mitigation**: Return history only, no inference
   - **Protection**: Code review must verify no inference logic

3. ⚠️ **Risk**: Accidentally validating state transitions
   - **Mitigation**: Return history only, no validation
   - **Protection**: Code review must verify no validation logic

**Canonical Test**: "If this capability is removed, system behavior remains identical. Only the history query disappears."

**Verdict**: **SAFE** - Pure read-only history query, no evaluation, no behavior.

---

## Recommended MVI Selection

### Selected Option: **Option 1 - Human-Initiated Task Force Status Query**

**Subsystem**: Task Force (Subsystem 4)  
**Capability**: `C-TF-4: Query Task Force Status Summary`

---

### Justification: Why It Is the Safest

**1. Pure Read-Only Aggregation**:
- ✅ Only reads existing Task Force definitions (C-TF-3)
- ✅ Only counts fields, never evaluates
- ✅ No writes, no state changes, no side effects
- ✅ No cross-subsystem dependencies (except Observability)

**2. Clear Boundaries**:
- ✅ Explicitly does NOT evaluate `dissolution_conditions`
- ✅ Explicitly does NOT evaluate `success_criteria`
- ✅ Explicitly does NOT extract `capability_contribution`
- ✅ Clear separation between counting and evaluating

**3. Minimal Risk of Scope Expansion**:
- ✅ Single capability, single purpose
- ✅ No behavioral logic
- ✅ No decision-making
- ✅ No workflow or orchestration

**4. Well-Defined Canonical Test**:
- ✅ "If this capability is removed, system behavior remains identical"
- ✅ Only the summary query disappears
- ✅ No impact on system behavior

---

### Justification: Why It Is the Most Informative

**1. Demonstrates Phase-4 Pattern**:
- ✅ Shows how to add read-only capabilities
- ✅ Shows how to respect READ-ONLY FOREVER structures
- ✅ Shows how to aggregate without evaluation
- ✅ Shows how to maintain observability

**2. Provides Useful Functionality**:
- ✅ Human-readable Task Force summaries
- ✅ Quick overview of Task Force structure
- ✅ No behavioral implications
- ✅ Pure information display

**3. Establishes Precedent**:
- ✅ Sets pattern for future Phase-4 read-only capabilities
- ✅ Demonstrates compliance with Gate A
- ✅ Shows how to extend Phase-3 L1 without violating constraints

---

### Justification: Why It Is the Least Likely to Expand Scope

**1. Single Purpose**:
- ✅ One capability, one purpose
- ✅ No multiple goals
- ✅ No workflow or orchestration
- ✅ No decision-making

**2. Clear Non-Goals**:
- ✅ Explicitly does NOT evaluate conditions
- ✅ Explicitly does NOT check criteria
- ✅ Explicitly does NOT extract capabilities
- ✅ Explicitly does NOT trigger actions

**3. Minimal Surface Area**:
- ✅ Single input: `task_force_id`
- ✅ Single output: Summary object
- ✅ No complex parameters
- ✅ No conditional logic

**4. No Behavioral Dependencies**:
- ✅ No dependencies on other subsystems (except Observability)
- ✅ No dependencies on execution or routing
- ✅ No dependencies on enforcement or automation
- ✅ No dependencies on exception detection

---

## Selected MVI Specification

### Capability: C-TF-4: Query Task Force Status Summary

**Subsystem**: Task Force (Subsystem 4)  
**Type**: Read-Only Query  
**Status**: **SELECTED FOR CONSIDERATION** (NOT AUTHORIZED)

---

#### Input

```python
task_force_id: str  # Required: Task Force identifier
```

---

#### Output

```python
{
    "task_force_id": str,
    "status": "found" | "not_found",
    "summary": {
        "name": str,
        "member_count": int,
        "goal_count": int,
        "dissolution_condition_count": int,  # Count only, not evaluation
        "created_by": str,
        "created_at": str,  # ISO8601
    } | None,
    "queried_at": str  # ISO8601
}
```

**Or error dict**:
```python
{
    "error": str,
    "error_type": str
}
```

---

#### Behavior

1. **Read Task Force Definition**:
   - Calls `C-TF-3: Query Task Force Definition` (read-only)
   - If not found, returns `status: "not_found"`

2. **Aggregate Descriptive Information**:
   - Counts `members` (list length)
   - Counts `goals` (list length)
   - Counts `dissolution_conditions` (list length)
   - Extracts: `name`, `created_by`, `created_at`

3. **Return Summary**:
   - Returns structured summary object
   - No evaluation, no checking, no validation

4. **Record Observability**:
   - Calls `C-OBS-1: Record Task Log` (observability only)

---

#### Explicit Constraints

**This capability MUST**:
- ✅ Only read Task Force definitions (C-TF-3)
- ✅ Only count fields, never evaluate
- ✅ Only return descriptive information
- ✅ Record observability (C-OBS-1)

**This capability MUST NOT**:
- ❌ Evaluate `dissolution_conditions`
- ❌ Check `success_criteria`
- ❌ Extract or coordinate `capability_contribution`
- ❌ Read Cell-State or Role Management
- ❌ Trigger any actions
- ❌ Make any decisions
- ❌ Influence system behavior

---

#### Canonical Test

**Question**: "If this capability is removed, does system behavior change?"

**Answer**: ✅ **NO** - System behavior remains IDENTICAL.

**Canonical Statement**:
"If C-TF-4 is removed, system behavior remains identical. Only the Task Force status summary query disappears. No other capabilities are affected."

---

## Implementation Authorization

### Current Status

**MVI Selection**: ✅ **COMPLETE**

**Implementation Authorization**: ❌ **NOT AUTHORIZED**

**This document selects ONE MVI candidate for future consideration.**

**Implementation requires a separate authorization work order.**

---

### Next Steps

**Before implementation authorization**:
1. Review this MVI selection
2. Review Phase-4 Gate A constraints
3. Review READ-ONLY FOREVER structures
4. Review canonical test requirements

**For implementation authorization**:
- Submit separate work order: `WO-PHASE4-MVI-IMPLEMENTATION-C-TF-4`
- Include explicit authorization for C-TF-4
- Include verification of canonical test
- Include verification of READ-ONLY FOREVER compliance

---

## Reference Documents

**This selection is based on**:

1. **Phase-4 Gate A Definition**:
   - `docs/PHASE_4_GATE_A_DEFINITION.md`

2. **Phase-4 Allowed Semantics Matrix**:
   - `docs/PHASE_4_ALLOWED_SEMANTICS_MATRIX.md`

3. **Phase-4 Implementation Stop Rules**:
   - `docs/PHASE_4_IMPLEMENTATION_STOP_RULES.md`

4. **Phase-3 L1 Global Freeze Summary**:
   - `docs/PHASE_3_L1_GLOBAL_FREEZE_SUMMARY.md`

5. **Phase-3 L1 READ-ONLY FOREVER List**:
   - `docs/PHASE_3_L1_READ_ONLY_FOREVER_LIST.md`

**These documents are authoritative and must be referenced for all Phase-4 work.**

---

## Summary

**Selected MVI**: **Option 1 - Human-Initiated Task Force Status Query**

**Capability**: `C-TF-4: Query Task Force Status Summary`

**Subsystem**: Task Force (Subsystem 4)

**Justification**:
- ✅ Safest (pure read-only aggregation)
- ✅ Most informative (demonstrates Phase-4 pattern)
- ✅ Least likely to expand scope (single purpose, clear boundaries)

**Status**: **SELECTED FOR CONSIDERATION** (NOT AUTHORIZED)

**Implementation requires a separate authorization work order.**

---

## Implementation Status

**C-TF-4 Implementation**: ✅ **COMPLETE**

**C-TF-4 has been implemented and designated as Phase-4 Gate A reference implementation.**

**Reference Document**: `docs/PHASE_4_GATE_A_REFERENCE_IMPLEMENTATION_C_TF_4.md`

---

**END OF PHASE-4 MVI SELECTION**

**This document is SELECTION ONLY and does NOT authorize implementation.**

