"""
C-TF-4: Query Task Force Status Summary

Phase-4 MVI: Human-Initiated, Read-Only Aggregation

This capability provides a read-only summary of Task Force definition.
It aggregates descriptive information only, without evaluation or behavior.

Phase-4 Constraints:
- Read-only query (no writes, no state changes)
- Aggregation only (counts, no evaluation)
- Does NOT evaluate dissolution_conditions
- Does NOT evaluate success_criteria
- Does NOT extract or coordinate capability_contribution
- Does NOT introduce lifecycle/status semantics
- Does NOT call Cell-State capabilities
- Removal-safe (canonical test must pass)
"""

import uuid
from datetime import datetime
from typing import Any, Dict

from backend.subsystems.observability.logging import record_task_log
from .query_task_force import query_task_force_definition


def query_task_force_summary(
    task_force_id: str, requested_by: str
) -> Dict[str, Any]:
    """
    C-TF-4: Query Task Force Status Summary

    Returns a read-only summary of Task Force definition.
    This is a pure aggregation query with no evaluation or behavior.

    Phase-4 Constraints:
    - Read-only (no writes, no state changes)
    - Aggregation only (counts, no evaluation)
    - Does NOT evaluate dissolution_conditions (counts only)
    - Does NOT evaluate success_criteria (counts only)
    - Does NOT extract or coordinate capability_contribution (counts only)
    - Does NOT introduce lifecycle/status semantics
    - Does NOT call Cell-State capabilities
    - Removal-safe (canonical test: removing this capability changes nothing except this query)

    Args:
        task_force_id: Unique identifier for the Task Force.
        requested_by: Human identifier who initiated the query.

    Returns:
        Dict with:
        - task_force_id: str
        - status: "found" / "not_found"
        - summary: Dict (if found) containing:
            - name: str
            - members_count: int
            - goals_count: int
            - dissolution_condition_count: int (count only, not evaluation)
            - created_by: str
            - created_at: str (ISO8601)
        - queried_at: str (ISO8601)

        Or error dict with:
        - error: str
        - error_type: str
    """
    start_time = datetime.utcnow()
    task_log_id = str(uuid.uuid4())
    goal = f"Query Task Force Summary (C-TF-4): {task_force_id}"

    try:
        if not isinstance(task_force_id, str) or not task_force_id.strip():
            raise ValueError("task_force_id must be a non-empty string.")

        # Source data ONLY via existing C-TF-3 (read-only query)
        task_force_result = query_task_force_definition(
            task_force_id=task_force_id,
            requested_by=requested_by
        )

        queried_at = datetime.utcnow().isoformat()

        # Check if Task Force was found
        if task_force_result.get("status") == "not_found":
            end_time = datetime.utcnow()
            duration = (end_time - start_time).total_seconds() * 1000

            record_task_log(
                task_id=task_log_id,
                goal=goal,
                input_data={"task_force_id": task_force_id, "requested_by": requested_by},
                output_data={"status": "not_found", "task_force_id": task_force_id},
                status="not_found",
                duration=duration,
                cost_estimate=1,
            )

            return {
                "task_force_id": task_force_id,
                "status": "not_found",
                "summary": None,
                "queried_at": queried_at,
            }

        # Extract Task Force definition from C-TF-3 result
        task_force_definition = task_force_result.get("task_force_definition")
        if not task_force_definition:
            raise ValueError("Task Force definition not found in C-TF-3 result.")

        # Aggregate descriptive information (counts only, no evaluation)
        name = task_force_definition.get("name", "")
        members = task_force_definition.get("members", [])
        goals = task_force_definition.get("goals", [])
        dissolution_conditions = task_force_definition.get("dissolution_conditions", [])
        created_by = task_force_definition.get("created_by", "")
        created_at = task_force_definition.get("created_at", "")

        # Count only (no evaluation, no checking, no validation)
        members_count = len(members) if isinstance(members, list) else 0
        goals_count = len(goals) if isinstance(goals, list) else 0
        dissolution_condition_count = len(dissolution_conditions) if isinstance(dissolution_conditions, list) else 0

        # Build summary (descriptive only, no evaluation)
        summary = {
            "name": name,
            "members_count": members_count,
            "goals_count": goals_count,
            "dissolution_condition_count": dissolution_condition_count,  # Count only, NOT evaluation
            "created_by": created_by,
            "created_at": created_at,
        }

        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds() * 1000

        record_task_log(
            task_id=task_log_id,
            goal=goal,
            input_data={"task_force_id": task_force_id, "requested_by": requested_by},
            output_data={
                "status": "found",
                "task_force_id": task_force_id,
                "summary": summary,
            },
            status="success",
            duration=duration,
            cost_estimate=1,
        )

        return {
            "task_force_id": task_force_id,
            "status": "found",
            "summary": summary,
            "queried_at": queried_at,
        }

    except Exception as e:
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds() * 1000
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        record_task_log(
            task_id=task_log_id,
            goal=goal,
            input_data={"task_force_id": task_force_id, "requested_by": requested_by},
            output_data=error_response,
            status="failure",
            duration=duration,
            cost_estimate=1,
        )
        return error_response

