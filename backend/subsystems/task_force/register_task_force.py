"""
Task Force registration for Task Force Subsystem.

C-TF-1: Register Task Force Definition implementation

Phase-3 Level 1: Structural only, descriptive definitions.
Task Force is a conceptual structure, not an executable entity.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from backend.subsystems.observability.logging import record_task_log
from .models import TaskForceDefinition, TaskForceMember, TaskForceGoal


# Simple in-memory storage for MVP
_task_forces: Dict[str, TaskForceDefinition] = {}


def _persist_task_force_definition(task_force: TaskForceDefinition) -> None:
    """
    Persist Task Force definition to disk as JSON.
    
    File naming: task_forces/{task_force_id}.json
    For observability and querying purposes only.
    """
    task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    task_forces_dir.mkdir(parents=True, exist_ok=True)
    
    task_force_file = task_forces_dir / f"{task_force.task_force_id}.json"
    
    # Convert to dict for JSON serialization
    task_force_dict = {
        "task_force_id": task_force.task_force_id,
        "name": task_force.name,
        "members": [
            {
                "member_id": m.member_id,
                "role_id": m.role_id,
                "cell_id": m.cell_id,
                "capability_contribution": m.capability_contribution,
            }
            for m in task_force.members
        ],
        "goals": [
            {
                "goal_id": g.goal_id,
                "description": g.description,
                "expected_output": g.expected_output,
                "success_criteria": g.success_criteria,
            }
            for g in task_force.goals
        ],
        "dissolution_conditions": task_force.dissolution_conditions,
        "created_by": task_force.created_by,
        "created_at": task_force.created_at,
    }
    
    # Explicitly verify no forbidden fields are present
    forbidden_fields = ["state", "status", "lifecycle", "execution_history", "runtime_info",
                       "execution_status", "task_assignments", "workload", "availability",
                       "progress", "completion_date", "execution_plan"]
    for field in forbidden_fields:
        if field in task_force_dict:
            raise ValueError(f"Forbidden field '{field}' detected. Phase-3 Level 1 Task Force definitions must not contain execution or behavior-related fields.")
    
    with open(task_force_file, "w") as f:
        json.dump(task_force_dict, f, indent=2)


def register_task_force_definition(
    task_force_definition: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-TF-1: Register Task Force Definition
    
    Registers a Task Force definition for structural purposes only.
    
    Phase-3 Level 1 Constraints:
    - Structural only (defines structure, does not execute)
    - Descriptive only (does not trigger behavior)
    - No execution, orchestration, or automation
    - MUST NOT read Cell-State
    - MUST NOT trigger any behavior
    
    Args:
        task_force_definition: Dict containing Task Force definition
        requested_by: Human identifier who requested the registration
    
    Returns:
        Dict with:
        - task_force_id: str
        - status: "registered"
        - created_at: ISO8601 timestamp
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"register_task_force_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        record_task_log(
            task_id=task_id,
            goal="Register Task Force Definition (C-TF-1)",
            input_data={
                "task_force_id": task_force_definition.get("task_force_id"),
                "requested_by": requested_by,
            },
            output_data=None,
            status="in_progress",
            duration=0,
            cost_estimate=0,
        )
        
        # Input validation
        if not isinstance(task_force_definition, dict):
            raise ValueError(f"task_force_definition must be a dict, got {type(task_force_definition).__name__}")
        
        required_fields = ["task_force_id", "name", "members", "goals", "dissolution_conditions"]
        for field in required_fields:
            if field not in task_force_definition:
                raise ValueError(f"Missing required field: '{field}'")
        
        # Validate forbidden fields
        forbidden_fields = ["state", "status", "lifecycle", "execution_history", "runtime_info",
                           "execution_status", "task_assignments", "workload", "availability",
                           "progress", "completion_date", "execution_plan"]
        for field in forbidden_fields:
            if field in task_force_definition:
                raise ValueError(f"Forbidden field '{field}' detected. Phase-3 Level 1 Task Force definitions must not contain execution or behavior-related fields.")
        
        task_force_id = task_force_definition["task_force_id"]
        if not isinstance(task_force_id, str) or not task_force_id.strip():
            raise ValueError("task_force_id must be a non-empty string")
        
        name = task_force_definition["name"]
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        
        # Validate members
        members_data = task_force_definition["members"]
        if not isinstance(members_data, list):
            raise ValueError("members must be a list")
        
        members = []
        for i, member_data in enumerate(members_data):
            if not isinstance(member_data, dict):
                raise ValueError(f"members[{i}] must be a dict")
            
            member_required = ["member_id", "role_id", "cell_id", "capability_contribution"]
            for field in member_required:
                if field not in member_data:
                    raise ValueError(f"members[{i}] missing required field: '{field}'")
            
            members.append(TaskForceMember(
                member_id=member_data["member_id"],
                role_id=member_data["role_id"],
                cell_id=member_data["cell_id"],
                capability_contribution=member_data["capability_contribution"],
            ))
        
        # Validate goals
        goals_data = task_force_definition["goals"]
        if not isinstance(goals_data, list):
            raise ValueError("goals must be a list")
        
        goals = []
        for i, goal_data in enumerate(goals_data):
            if not isinstance(goal_data, dict):
                raise ValueError(f"goals[{i}] must be a dict")
            
            goal_required = ["goal_id", "description", "expected_output", "success_criteria"]
            for field in goal_required:
                if field not in goal_data:
                    raise ValueError(f"goals[{i}] missing required field: '{field}'")
            
            goals.append(TaskForceGoal(
                goal_id=goal_data["goal_id"],
                description=goal_data["description"],
                expected_output=goal_data["expected_output"],
                success_criteria=goal_data["success_criteria"],
            ))
        
        # Validate dissolution_conditions
        dissolution_conditions = task_force_definition["dissolution_conditions"]
        if not isinstance(dissolution_conditions, list):
            raise ValueError("dissolution_conditions must be a list")
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Create TaskForceDefinition
        created_at = datetime.utcnow().isoformat()
        task_force = TaskForceDefinition(
            task_force_id=task_force_id,
            name=name,
            members=members,
            goals=goals,
            dissolution_conditions=dissolution_conditions,
            created_by=requested_by,
            created_at=created_at,
        )
        
        # Store in memory
        _task_forces[task_force_id] = task_force
        
        # Persist to disk
        _persist_task_force_definition(task_force)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        result = {
            "task_force_id": task_force_id,
            "status": "registered",
            "created_at": created_at,
        }
        
        # Observability: Exit record (success)
        record_task_log(
            task_id=task_id,
            goal="Register Task Force Definition (C-TF-1)",
            input_data={
                "task_force_id": task_force_id,
                "requested_by": requested_by,
            },
            output_data=result,
            status="success",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        return result
        
    except Exception as e:
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        # Observability: Exit record (failure)
        record_task_log(
            task_id=task_id,
            goal="Register Task Force Definition (C-TF-1)",
            input_data={
                "task_force_id": task_force_definition.get("task_force_id") if isinstance(task_force_definition, dict) else None,
                "requested_by": requested_by,
            },
            output_data=error_response,
            status="failure",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        return error_response

