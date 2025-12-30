"""
Structure registration for Catalyst Hub Subsystem.

C-CH-1: Register Structure implementation

Phase-3 Level 1: Structural only, descriptive definitions.
Catalyst Hub structures are descriptive, not prescriptive or execution-oriented.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from backend.subsystems.observability.logging import record_task_log
from .models import (
    RequirementEnvelope,
    RoutingHint,
    WorkflowStateSnapshot,
    TriggerCondition,
    HealthCheckRecord,
    CostBudgetSnapshot,
)


# Simple in-memory storage for MVP
_structures: Dict[str, Dict[str, Any]] = {}


def _persist_structure(structure_type: str, structure_id: str, structure_dict: Dict[str, Any]) -> None:
    """
    Persist structure to disk as JSON.
    
    File naming: structures/{structure_type}/{structure_id}.json
    For observability and querying purposes only.
    """
    structures_dir = Path(f"backend/subsystems/catalyst_hub/structures/{structure_type}")
    structures_dir.mkdir(parents=True, exist_ok=True)
    
    structure_file = structures_dir / f"{structure_id}.json"
    
    # Explicitly verify no forbidden fields are present
    forbidden_fields = [
        "routing_decision", "target_cell_id", "execution_status",
        "trigger_action", "task_force_creation", "enforcement_status",
        "blocking_status", "alert_triggers", "actions_taken", "recovery_actions",
        "analysis", "detection_results"
    ]
    for field in forbidden_fields:
        if field in structure_dict:
            raise ValueError(
                f"Forbidden field '{field}' detected. Phase-3 Level 1 Catalyst Hub structures "
                f"must not contain execution, decision-making, or behavior-related fields."
            )
    
    with open(structure_file, "w") as f:
        json.dump(structure_dict, f, indent=2)


def register_structure(
    structure_type: str,
    structure_data: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-CH-1: Register Structure
    
    Registers a Catalyst Hub structure for structural purposes only.
    
    Phase-3 Level 1 Constraints:
    - Structural only (defines structure, does not execute)
    - Descriptive only (does not trigger behavior)
    - No execution, routing, detection, triggering, or orchestration
    - MUST NOT read Cell-State to affect behavior
    - MUST NOT create Task Forces
    - MUST NOT enforce budgets or policies
    
    Supported structure types:
    - requirement_envelope
    - routing_hint
    - workflow_state_snapshot
    - trigger_condition
    - health_check_record
    - cost_budget_snapshot
    
    Args:
        structure_type: Type of structure to register
        structure_data: Dict containing structure data
        requested_by: Human identifier who requested the registration
    
    Returns:
        Dict with:
        - structure_id: str
        - structure_type: str
        - status: "registered"
        - created_at: ISO8601 timestamp
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"register_structure_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        record_task_log(
            task_id=task_id,
            goal="Register Structure (C-CH-1)",
            input_data={
                "structure_type": structure_type,
                "requested_by": requested_by,
            },
            output_data=None,
            status="in_progress",
            duration=0,
            cost_estimate=0,
        )
        
        # Input validation
        if not isinstance(structure_type, str) or not structure_type.strip():
            raise ValueError("structure_type must be a non-empty string")
        
        if not isinstance(structure_data, dict):
            raise ValueError(f"structure_data must be a dict, got {type(structure_data).__name__}")
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Validate structure_type
        valid_types = [
            "requirement_envelope",
            "routing_hint",
            "workflow_state_snapshot",
            "trigger_condition",
            "health_check_record",
            "cost_budget_snapshot",
        ]
        if structure_type not in valid_types:
            raise ValueError(
                f"Invalid structure_type: '{structure_type}'. "
                f"Valid types: {', '.join(valid_types)}"
            )
        
        # Get structure_id from structure_data or generate one
        structure_id = structure_data.get("requirement_id") or \
                      structure_data.get("hint_id") or \
                      structure_data.get("snapshot_id") or \
                      structure_data.get("condition_id") or \
                      structure_data.get("check_id") or \
                      str(uuid.uuid4())
        
        if not structure_id:
            raise ValueError("structure_id must be present in structure_data or generated")
        
        # Validate forbidden fields
        forbidden_fields = [
            "routing_decision", "target_cell_id", "execution_status",
            "trigger_action", "task_force_creation", "enforcement_status",
            "blocking_status", "alert_triggers", "actions_taken", "recovery_actions",
            "analysis", "detection_results"
        ]
        for field in forbidden_fields:
            if field in structure_data:
                raise ValueError(
                    f"Forbidden field '{field}' detected. Phase-3 Level 1 Catalyst Hub structures "
                    f"must not contain execution, decision-making, or behavior-related fields."
                )
        
        # Create structure dict with metadata
        structure_dict = {
            **structure_data,
            "structure_type": structure_type,
            "structure_id": structure_id,
            "created_by": requested_by,
            "created_at": datetime.utcnow().isoformat(),
        }
        
        # Store in memory
        storage_key = f"{structure_type}:{structure_id}"
        _structures[storage_key] = structure_dict
        
        # Persist to disk
        _persist_structure(structure_type, structure_id, structure_dict)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        result = {
            "structure_id": structure_id,
            "structure_type": structure_type,
            "status": "registered",
            "created_at": structure_dict["created_at"],
        }
        
        # Observability: Exit record (success)
        record_task_log(
            task_id=task_id,
            goal="Register Structure (C-CH-1)",
            input_data={
                "structure_type": structure_type,
                "structure_id": structure_id,
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
            goal="Register Structure (C-CH-1)",
            input_data={
                "structure_type": structure_type if isinstance(structure_type, str) else None,
                "requested_by": requested_by,
            },
            output_data=error_response,
            status="failure",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        return error_response


def query_structure(
    structure_type: str,
    structure_id: str,
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-CH-2: Query Structure
    
    Queries a Catalyst Hub structure by structure_type and structure_id.
    
    Phase-3 Level 1 Constraints:
    - Read-only operation (no mutations)
    - No repair, inference, or normalization
    - MUST NOT read Cell-State to affect behavior
    - MUST NOT trigger actions
    - MUST record Observability entry/exit
    
    Args:
        structure_type: Type of structure to query
        structure_id: Unique identifier for the structure
        requested_by: Human identifier who requested the query
    
    Returns:
        Dict with structure data and status: "found"
        
        Or:
        - structure_id: str
        - structure_type: str
        - status: "not_found"
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"query_structure_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        record_task_log(
            task_id=task_id,
            goal="Query Structure (C-CH-2)",
            input_data={
                "structure_type": structure_type,
                "structure_id": structure_id,
                "requested_by": requested_by,
            },
            output_data=None,
            status="in_progress",
            duration=0,
            cost_estimate=0,
        )
        
        # Input validation
        if not isinstance(structure_type, str) or not structure_type.strip():
            raise ValueError("structure_type must be a non-empty string")
        
        if not isinstance(structure_id, str) or not structure_id.strip():
            raise ValueError("structure_id must be a non-empty string")
        
        if not isinstance(requested_by, str) or not requested_by.strip():
            raise ValueError("requested_by must be a non-empty string")
        
        # Try in-memory cache first
        storage_key = f"{structure_type}:{structure_id}"
        structure = _structures.get(storage_key)
        
        # If not in memory, try disk
        if structure is None:
            structure_file = Path(
                f"backend/subsystems/catalyst_hub/structures/{structure_type}/{structure_id}.json"
            )
            if structure_file.exists():
                with open(structure_file, "r") as f:
                    structure = json.load(f)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        if structure is None:
            # Not found
            result = {
                "structure_id": structure_id,
                "structure_type": structure_type,
                "status": "not_found",
            }
            
            # Observability: Exit record (not_found)
            record_task_log(
                task_id=task_id,
                goal="Query Structure (C-CH-2)",
                input_data={
                    "structure_type": structure_type,
                    "structure_id": structure_id,
                    "requested_by": requested_by,
                },
                output_data=result,
                status="success",
                duration=duration_ms,
                cost_estimate=0,
            )
            
            return result
        
        # Found
        result = {
            **structure,
            "status": "found",
        }
        
        # Observability: Exit record (found)
        record_task_log(
            task_id=task_id,
            goal="Query Structure (C-CH-2)",
            input_data={
                "structure_type": structure_type,
                "structure_id": structure_id,
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
            goal="Query Structure (C-CH-2)",
            input_data={
                "structure_type": structure_type if isinstance(structure_type, str) else None,
                "structure_id": structure_id if isinstance(structure_id, str) else None,
                "requested_by": requested_by,
            },
            output_data=error_response,
            status="failure",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        return error_response

