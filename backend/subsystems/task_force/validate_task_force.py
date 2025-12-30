"""
Task Force validation for Task Force Subsystem.

C-TF-2: Validate Task Force Completeness implementation

Phase-3 Level 1: Pure validation function.
Validates Task Force definition completeness per schema rules.
"""

from typing import Any, Dict

from .models import TaskForceDefinition, TaskForceMember, TaskForceGoal


def validate_task_force_completeness(
    task_force_definition: Any,
    strict: bool = True,
) -> Dict[str, Any]:
    """
    C-TF-2: Validate Task Force Completeness
    
    Validates that a Task Force definition is complete per schema rules.
    
    Phase-3 Level 1 Constraints:
    - Pure validation function (no I/O, no state mutation)
    - No permission/authority inference
    - No cross-subsystem imports/calls (Cell-State forbidden)
    - Deterministic output for same input
    - Observability handled by wrapper only (this function stays pure)
    
    Args:
        task_force_definition: Dict or TaskForceDefinition instance
        strict: bool (default True) - strict mode requires all required fields present and non-empty
    
    Returns:
        Dict with:
        - valid: bool
        - errors: List[Dict] with { "field": str, "code": str, "message": str }
        - warnings: List[Dict] (empty in L1)
        - normalized: None (no normalization in L1)
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    errors = []
    
    # Accept both dict and TaskForceDefinition instance
    if isinstance(task_force_definition, TaskForceDefinition):
        tf_dict = {
            "task_force_id": task_force_definition.task_force_id,
            "name": task_force_definition.name,
            "members": [
                {
                    "member_id": m.member_id,
                    "role_id": m.role_id,
                    "cell_id": m.cell_id,
                    "capability_contribution": m.capability_contribution,
                }
                for m in task_force_definition.members
            ],
            "goals": [
                {
                    "goal_id": g.goal_id,
                    "description": g.description,
                    "expected_output": g.expected_output,
                    "success_criteria": g.success_criteria,
                }
                for g in task_force_definition.goals
            ],
            "dissolution_conditions": task_force_definition.dissolution_conditions,
            "created_by": task_force_definition.created_by,
            "created_at": task_force_definition.created_at,
        }
    elif isinstance(task_force_definition, dict):
        tf_dict = task_force_definition
    else:
        return {
            "valid": False,
            "errors": [
                {
                    "field": "task_force_definition",
                    "code": "invalid_type",
                    "message": f"task_force_definition must be a dict or TaskForceDefinition, got {type(task_force_definition).__name__}",
                }
            ],
            "warnings": [],
            "normalized": None,
        }
    
    # Required fields check
    required_fields = ["task_force_id", "name", "members", "goals", "dissolution_conditions"]
    for field in required_fields:
        if field not in tf_dict:
            errors.append({
                "field": field,
                "code": "missing_required",
                "message": f"Missing required field: '{field}'",
            })
            continue
        
        # Type checks
        if field == "task_force_id":
            if not isinstance(tf_dict[field], str):
                errors.append({
                    "field": field,
                    "code": "invalid_type",
                    "message": f"'{field}' must be a string",
                })
            elif strict and not tf_dict[field].strip():
                errors.append({
                    "field": field,
                    "code": "empty_value",
                    "message": f"'{field}' must be non-empty",
                })
        
        elif field == "name":
            if not isinstance(tf_dict[field], str):
                errors.append({
                    "field": field,
                    "code": "invalid_type",
                    "message": f"'{field}' must be a string",
                })
            elif strict and not tf_dict[field].strip():
                errors.append({
                    "field": field,
                    "code": "empty_value",
                    "message": f"'{field}' must be non-empty",
                })
        
        elif field == "members":
            if not isinstance(tf_dict[field], list):
                errors.append({
                    "field": field,
                    "code": "invalid_type",
                    "message": f"'{field}' must be a list",
                })
            elif strict and len(tf_dict[field]) == 0:
                errors.append({
                    "field": field,
                    "code": "empty_list",
                    "message": f"'{field}' must be non-empty",
                })
            else:
                # Validate each member
                for i, member in enumerate(tf_dict[field]):
                    if not isinstance(member, dict):
                        errors.append({
                            "field": f"{field}[{i}]",
                            "code": "invalid_type",
                            "message": f"members[{i}] must be a dict",
                        })
                        continue
                    
                    member_required = ["member_id", "role_id", "cell_id", "capability_contribution"]
                    for mf in member_required:
                        if mf not in member:
                            errors.append({
                                "field": f"{field}[{i}].{mf}",
                                "code": "missing_required",
                                "message": f"members[{i}] missing required field: '{mf}'",
                            })
                        elif mf == "capability_contribution":
                            if not isinstance(member[mf], list):
                                errors.append({
                                    "field": f"{field}[{i}].{mf}",
                                    "code": "invalid_type",
                                    "message": f"members[{i}].{mf} must be a list",
                                })
        
        elif field == "goals":
            if not isinstance(tf_dict[field], list):
                errors.append({
                    "field": field,
                    "code": "invalid_type",
                    "message": f"'{field}' must be a list",
                })
            elif strict and len(tf_dict[field]) == 0:
                errors.append({
                    "field": field,
                    "code": "empty_list",
                    "message": f"'{field}' must be non-empty",
                })
            else:
                # Validate each goal
                for i, goal in enumerate(tf_dict[field]):
                    if not isinstance(goal, dict):
                        errors.append({
                            "field": f"{field}[{i}]",
                            "code": "invalid_type",
                            "message": f"goals[{i}] must be a dict",
                        })
                        continue
                    
                    goal_required = ["goal_id", "description", "expected_output", "success_criteria"]
                    for gf in goal_required:
                        if gf not in goal:
                            errors.append({
                                "field": f"{field}[{i}].{gf}",
                                "code": "missing_required",
                                "message": f"goals[{i}] missing required field: '{gf}'",
                            })
                        elif gf == "success_criteria":
                            if not isinstance(goal[gf], list):
                                errors.append({
                                    "field": f"{field}[{i}].{gf}",
                                    "code": "invalid_type",
                                    "message": f"goals[{i}].{gf} must be a list",
                                })
        
        elif field == "dissolution_conditions":
            if not isinstance(tf_dict[field], list):
                errors.append({
                    "field": field,
                    "code": "invalid_type",
                    "message": f"'{field}' must be a list",
                })
    
    # Check for forbidden fields
    forbidden_fields = ["state", "status", "lifecycle", "execution_history", "runtime_info",
                       "execution_status", "task_assignments", "workload", "availability",
                       "progress", "completion_date", "execution_plan"]
    for field in forbidden_fields:
        if field in tf_dict:
            errors.append({
                "field": field,
                "code": "forbidden_field",
                "message": f"Forbidden field '{field}' detected. Phase-3 Level 1 Task Force definitions must not contain execution or behavior-related fields.",
            })
    
    # Deterministic error ordering (stable sort by field then code)
    errors.sort(key=lambda e: (e["field"], e["code"]))
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": [],
        "normalized": None,
    }

