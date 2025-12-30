"""
Task Force querying for Task Force Subsystem.

C-TF-3: Query Task Force Definition implementation

Phase-3 Level 1: Read-only query capability.
Provides read-only access to Task Force definitions.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from backend.subsystems.observability.logging import record_task_log
from .models import TaskForceDefinition, TaskForceMember, TaskForceGoal

# Access in-memory storage from register_task_force module
def _get_task_forces():
    """Get in-memory Task Force records from register_task_force module"""
    try:
        from backend.subsystems.task_force import register_task_force
        return register_task_force._task_forces
    except (ImportError, AttributeError):
        # Fallback to empty dict if module not loaded
        return {}


def _load_task_force_from_disk(task_force_id: str) -> TaskForceDefinition:
    """
    Load Task Force definition from disk storage.
    
    File naming: task_forces/{task_force_id}.json
    
    Returns:
        TaskForceDefinition if found, None if not found.
    """
    task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    task_force_file = task_forces_dir / f"{task_force_id}.json"
    
    if not task_force_file.exists():
        return None
    
    with open(task_force_file, "r") as f:
        tf_dict = json.load(f)
    
    # Verify no forbidden fields are present
    forbidden_fields = ["state", "status", "lifecycle", "execution_history", "runtime_info",
                       "execution_status", "task_assignments", "workload", "availability",
                       "progress", "completion_date", "execution_plan"]
    for field in forbidden_fields:
        if field in tf_dict:
            raise ValueError(f"Forbidden field '{field}' detected in stored Task Force. Phase-3 Level 1 Task Force definitions must not contain execution or behavior-related fields.")
    
    # Reconstruct TaskForceDefinition
    members = [
        TaskForceMember(
            member_id=m["member_id"],
            role_id=m["role_id"],
            cell_id=m["cell_id"],
            capability_contribution=m["capability_contribution"],
        )
        for m in tf_dict["members"]
    ]
    
    goals = [
        TaskForceGoal(
            goal_id=g["goal_id"],
            description=g["description"],
            expected_output=g["expected_output"],
            success_criteria=g["success_criteria"],
        )
        for g in tf_dict["goals"]
    ]
    
    return TaskForceDefinition(
        task_force_id=tf_dict["task_force_id"],
        name=tf_dict["name"],
        members=members,
        goals=goals,
        dissolution_conditions=tf_dict["dissolution_conditions"],
        created_by=tf_dict["created_by"],
        created_at=tf_dict["created_at"],
    )


def query_task_force_definition(
    task_force_id: str,
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-TF-3: Query Task Force Definition
    
    Queries a Task Force definition by task_force_id.
    
    Phase-3 Level 1 Constraints:
    - Read-only operation (no mutations)
    - No repair, inference, or normalization
    - No history return
    - No cross-subsystem aggregation
    - MUST NOT read Cell-State
    - MUST record Observability entry (before / after)
    
    Args:
        task_force_id: Unique identifier for the Task Force
        requested_by: Human identifier who requested the query
    
    Returns:
        Dict with:
        - task_force_id: str
        - name: str
        - members: List[Dict]
        - goals: List[Dict]
        - dissolution_conditions: List[str]
        - created_by: str
        - created_at: ISO8601 timestamp
        - status: "found"
        
        Or:
        - task_force_id: str
        - status: "not_found"
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"query_task_force_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        record_task_log(
            task_id=task_id,
            goal="Query Task Force Definition (C-TF-3)",
            input_data={
                "task_force_id": task_force_id,
                "requested_by": requested_by,
            },
            output_data=None,
            status="in_progress",
            duration=0,
            cost_estimate=0,
        )
        
        # Input validation
        if not isinstance(task_force_id, str) or not task_force_id.strip():
            raise ValueError("task_force_id must be a non-empty string")
        
        if not isinstance(requested_by, str) or not requested_by.strip():
            raise ValueError("requested_by must be a non-empty string")
        
        # Try in-memory cache first
        task_force = _get_task_forces().get(task_force_id)
        
        # If not in memory, try disk
        if task_force is None:
            task_force = _load_task_force_from_disk(task_force_id)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        if task_force is None:
            # Not found
            result = {
                "task_force_id": task_force_id,
                "status": "not_found",
            }
            
            # Observability: Exit record (not_found)
            record_task_log(
                task_id=task_id,
                goal="Query Task Force Definition (C-TF-3)",
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
        
        # Found - convert to dict for return
        result = {
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
            "status": "found",
        }
        
        # Observability: Exit record (found)
        record_task_log(
            task_id=task_id,
            goal="Query Task Force Definition (C-TF-3)",
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
            goal="Query Task Force Definition (C-TF-3)",
            input_data={
                "task_force_id": task_force_id,
                "requested_by": requested_by,
            },
            output_data=error_response,
            status="failure",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        return error_response

