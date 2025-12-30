# DS-TF-1: TaskForceDefinition Structure

**Data Structure**: DS-TF-1  
**Subsystem**: Task Force (Subsystem 4)  
**Phase**: Phase-3 Level 1  
**Status**: IMPLEMENTED

---

## Purpose

**DS-TF-1** represents a Task Force definition structure for structural purposes only.

**Phase-3 Level 1**: This structure is **DESCRIPTIVE ONLY**, not prescriptive. It does NOT execute tasks, orchestrate workflows, or influence behavior.

---

## Structure

```python
@dataclass
class TaskForceDefinition:
    task_force_id: str
    name: str
    members: List[TaskForceMember]
    goals: List[TaskForceGoal]
    dissolution_conditions: List[str]
    created_by: str
    created_at: str  # ISO8601 timestamp
```

---

## Required Fields

### `task_force_id: str`
- Unique identifier for the Task Force
- Must be non-empty string
- Used for querying and referencing

### `name: str`
- Human-readable name for the Task Force
- Must be non-empty string

### `members: List[TaskForceMember]`
- List of Task Force members (DS-TF-2)
- Must be non-empty list in strict validation mode
- Each member references a Role (Phase-2) and Cell (Phase-2)

### `goals: List[TaskForceGoal]`
- List of Task Force goals (DS-TF-3)
- Must be non-empty list in strict validation mode
- Each goal describes an expected outcome (descriptive only)

### `dissolution_conditions: List[str]`
- List of dissolution condition descriptions (descriptive only)
- Human-readable descriptions of when Task Force should dissolve
- **NOT prescriptive** - does NOT trigger dissolution

### `created_by: str`
- Human identifier who created the Task Force
- Must be non-empty string

### `created_at: str`
- ISO8601 timestamp of creation
- Format: `YYYY-MM-DDTHH:MM:SS`

---

## Forbidden Fields (Phase-3 Level 1)

**The following fields are EXPLICITLY FORBIDDEN**:

- ❌ `state` - No state tracking
- ❌ `status` - No status tracking
- ❌ `lifecycle` - No lifecycle management
- ❌ `execution_history` - No execution tracking
- ❌ `runtime_info` - No runtime information
- ❌ `execution_status` - No execution status
- ❌ `task_assignments` - No task assignment
- ❌ `workload` - No workload tracking
- ❌ `availability` - No availability tracking
- ❌ `progress` - No progress tracking
- ❌ `completion_date` - No completion tracking
- ❌ `execution_plan` - No execution planning

**Any field that implies execution, orchestration, or behavior is FORBIDDEN.**

---

## Constraints

### Phase-3 Level 1 Constraints

1. **Structural Only**:
   - Defines structure, does not execute
   - Descriptive only, not prescriptive

2. **No Execution Semantics**:
   - Does NOT trigger execution
   - Does NOT orchestrate workflows
   - Does NOT manage lifecycle

3. **No Cell-State Dependency**:
   - MUST NOT read Cell-State
   - MUST NOT query Cell state (C-CELL-4, C-CELL-5)
   - MAY reference Cell definitions (Phase-2) for structure only

4. **No Behavior Influence**:
   - Does NOT influence system behavior
   - Does NOT trigger actions
   - Does NOT coordinate subsystems

---

## Canonical Test

**Question**: "If this data structure is removed, does system behavior change?"

**Answer**: ✅ **NO** - System behavior remains IDENTICAL.

**What Happens If Removed**:
- ✅ System continues to function identically
- ✅ All subsystems continue to operate
- ❌ Only Task Force definitions disappear
- ❌ Only Task Force queries fail

**This Test Must Always Pass**: If removing TaskForceDefinition changes system behavior, it violates the descriptive-only principle.

---

## Usage

### Registration (C-TF-1)

```python
task_force_def = {
    "task_force_id": "tf-1",
    "name": "Example Task Force",
    "members": [...],
    "goals": [...],
    "dissolution_conditions": [...],
}

result = register_task_force_definition(task_force_def, requested_by="human-1")
```

### Validation (C-TF-2)

```python
result = validate_task_force_completeness(task_force_def)
assert result["valid"] is True
```

### Query (C-TF-3)

```python
result = query_task_force_definition("tf-1", requested_by="human-1")
assert result["status"] == "found"
```

---

## Implementation Location

- **Model**: `backend/subsystems/task_force/models.py`
- **Registration**: `backend/subsystems/task_force/register_task_force.py`
- **Validation**: `backend/subsystems/task_force/validate_task_force.py`
- **Query**: `backend/subsystems/task_force/query_task_force.py`

---

## Related Data Structures

- **DS-TF-2**: TaskForceMember (member structure)
- **DS-TF-3**: TaskForceGoal (goal structure)
- **DS-TF-4**: TaskForceDissolutionRecord (dissolution record structure)

---

**END OF DS-TF-1 DOCUMENTATION**

