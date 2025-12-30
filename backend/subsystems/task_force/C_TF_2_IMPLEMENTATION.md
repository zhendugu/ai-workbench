# C-TF-2: Validate Task Force Completeness - Implementation Summary

**Capability**: C-TF-2  
**Subsystem**: Task Force (Subsystem 4)  
**Phase**: Phase-3 Level 1  
**Status**: IMPLEMENTATION COMPLETE

---

## Implementation Overview

**C-TF-2** validates that a Task Force definition is complete per schema rules.

**Phase-3 Level 1**: This capability is a **PURE VALIDATION FUNCTION**. It does NOT perform I/O, mutate state, or influence behavior.

---

## Function Signature

```python
def validate_task_force_completeness(
    task_force_definition: Any,
    strict: bool = True,
) -> Dict[str, Any]:
```

---

## Behavior

### Input Acceptance

1. **Accepts Both Types**:
   - Dict (raw Task Force definition)
   - TaskForceDefinition instance (model)

2. **Strict Mode**:
   - `strict=True` (default): Requires all required fields present and non-empty
   - `strict=False`: Allows empty lists but still requires keys present

### Validation Rules

1. **Required Fields Check**:
   - `task_force_id`: Must be non-empty string
   - `name`: Must be non-empty string
   - `members`: Must be list (non-empty in strict mode)
   - `goals`: Must be list (non-empty in strict mode)
   - `dissolution_conditions`: Must be list

2. **Type Checks**:
   - Validates types for all fields
   - Validates nested structures (members, goals)

3. **Member Validation**:
   - Each member must have: `member_id`, `role_id`, `cell_id`, `capability_contribution`
   - `capability_contribution` must be a list

4. **Goal Validation**:
   - Each goal must have: `goal_id`, `description`, `expected_output`, `success_criteria`
   - `success_criteria` must be a list

5. **Forbidden Fields Check**:
   - Explicitly checks for forbidden fields (state, status, lifecycle, etc.)
   - Adds error if forbidden fields detected

### Output

**Valid**:
```python
{
    "valid": True,
    "errors": [],
    "warnings": [],
    "normalized": None,
}
```

**Invalid**:
```python
{
    "valid": False,
    "errors": [
        {
            "field": str,
            "code": str,
            "message": str,
        },
        ...
    ],
    "warnings": [],
    "normalized": None,
}
```

**Error Ordering**: Deterministic (stable sort by field then code)

---

## Constraints Adherence

### Phase-3 Level 1 Constraints

✅ **Pure Function**:
- No I/O operations
- No state mutation
- No global state access
- Deterministic output for same input

✅ **No Cross-Subsystem Dependencies**:
- Does NOT import Cell-State modules
- Does NOT call C-CELL-4 or C-CELL-5
- Does NOT read from other subsystems

✅ **No Permission/Authority Inference**:
- Does NOT infer permissions
- Does NOT infer authority
- Does NOT infer execution rights

✅ **No Normalization**:
- Does NOT normalize Task Force definitions
- Does NOT auto-fill missing fields
- Does NOT repair Task Force definitions

✅ **Observability Handled by Wrapper**:
- Function itself stays pure
- Observability recorded by wrapper (C-EXEC-1) only

---

## Canonical Test

**Question**: "If this capability is removed, does system behavior change?"

**Answer**: ✅ **NO** - System behavior remains IDENTICAL.

**What Happens If Removed**:
- ✅ System continues to function identically
- ✅ All subsystems continue to operate
- ❌ Only Task Force validation fails
- ❌ Only Task Force completeness checks unavailable

**This Test Must Always Pass**: If removing C-TF-2 changes system behavior, it violates the descriptive-only principle.

---

## Implementation Files

- **Implementation**: `backend/subsystems/task_force/validate_task_force.py`
- **Model**: `backend/subsystems/task_force/models.py`
- **Tests**: `backend/subsystems/task_force/tests/test_validate_task_force.py`

---

## Test Coverage

✅ **Valid Task Force**: Passes validation  
✅ **Missing Required Fields**: Returns errors  
✅ **Forbidden Fields**: Rejects forbidden fields  
✅ **Empty Lists (Strict)**: Rejects empty lists in strict mode  
✅ **Deterministic**: Same input produces same output  
✅ **Pure Function**: No I/O, no state mutation

---

## Related Capabilities

- **C-TF-1**: Register Task Force Definition (registration)
- **C-TF-3**: Query Task Force Definition (query)

---

**END OF C-TF-2 IMPLEMENTATION SUMMARY**

