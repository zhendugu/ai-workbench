# C-TF-3: Query Task Force Definition - Implementation Summary

**Capability**: C-TF-3  
**Subsystem**: Task Force (Subsystem 4)  
**Phase**: Phase-3 Level 1  
**Status**: IMPLEMENTATION COMPLETE

---

## Implementation Overview

**C-TF-3** queries a Task Force definition by `task_force_id`.

**Phase-3 Level 1**: This capability is **READ-ONLY**. It does NOT mutate state, repair definitions, or influence behavior.

---

## Function Signature

```python
def query_task_force_definition(
    task_force_id: str,
    requested_by: str,
) -> Dict[str, Any]:
```

---

## Behavior

### Query Strategy

1. **In-Memory Cache First**:
   - Checks in-memory `_task_forces` dict
   - Fast lookup if Task Force recently registered

2. **Disk Fallback**:
   - If not in memory, loads from disk
   - File: `backend/subsystems/task_force/task_forces/{task_force_id}.json`

3. **Forbidden Fields Check**:
   - Verifies stored Task Force does NOT contain forbidden fields
   - Raises error if forbidden fields detected

### Input Validation

1. **task_force_id**:
   - Must be non-empty string
   - Returns error if invalid

2. **requested_by**:
   - Must be non-empty string
   - Used for observability only

### Output

**Found**:
```python
{
    "task_force_id": str,
    "name": str,
    "members": [
        {
            "member_id": str,
            "role_id": str,
            "cell_id": str,
            "capability_contribution": List[str],
        },
        ...
    ],
    "goals": [
        {
            "goal_id": str,
            "description": str,
            "expected_output": str,
            "success_criteria": List[str],
        },
        ...
    ],
    "dissolution_conditions": List[str],
    "created_by": str,
    "created_at": str,  # ISO8601 timestamp
    "status": "found",
}
```

**Not Found**:
```python
{
    "task_force_id": str,
    "status": "not_found",
}
```

**Failure**:
```python
{
    "error": str,
    "error_type": str,
}
```

---

## Constraints Adherence

### Phase-3 Level 1 Constraints

✅ **Read-Only Operation**:
- No mutations
- No repairs
- No inference
- No normalization

✅ **No Repair/Inference**:
- Does NOT create default Task Forces
- Does NOT repair missing fields
- Does NOT infer default values
- Does NOT normalize Task Force definitions

✅ **No Cross-Subsystem Dependencies**:
- Does NOT import Cell-State modules
- Does NOT call C-CELL-4 or C-CELL-5
- Does NOT read Cell state

✅ **No History Return**:
- Returns current Task Force definition only
- Does NOT return history or changes

✅ **Observability**:
- Records entry via C-OBS-1 (before query)
- Records exit via C-OBS-1 (after query)
- Records success/failure/not_found status

---

## Canonical Test

**Question**: "If this capability is removed, does system behavior change?"

**Answer**: ✅ **NO** - System behavior remains IDENTICAL.

**What Happens If Removed**:
- ✅ System continues to function identically
- ✅ All subsystems continue to operate
- ❌ Only Task Force queries fail
- ❌ Only Task Force definitions cannot be retrieved

**This Test Must Always Pass**: If removing C-TF-3 changes system behavior, it violates the descriptive-only principle.

---

## Implementation Files

- **Implementation**: `backend/subsystems/task_force/query_task_force.py`
- **Model**: `backend/subsystems/task_force/models.py`
- **Tests**: `backend/subsystems/task_force/tests/test_query_task_force.py`

---

## Test Coverage

✅ **Found in Memory**: Queries from in-memory cache  
✅ **Found on Disk**: Queries from disk storage  
✅ **Not Found**: Returns not_found status  
✅ **Invalid Input**: Returns error for invalid input  
✅ **Read-Only**: Verifies no mutations  
✅ **No Repair/Inference**: Verifies no repair or inference  
✅ **No Cell-State Dependency**: Verifies no Cell-State reads

---

## Observability Integration

- **Entry Record**: Recorded via C-OBS-1 before query
- **Exit Record**: Recorded via C-OBS-1 after query
- **Status**: Success/failure/not_found recorded
- **Duration**: Query duration recorded

---

## Related Capabilities

- **C-TF-1**: Register Task Force Definition (registration)
- **C-TF-2**: Validate Task Force Completeness (validation)

---

**END OF C-TF-3 IMPLEMENTATION SUMMARY**

