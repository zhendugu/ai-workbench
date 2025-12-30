"""
Role registration for Role Management Subsystem.

C-ROLE-1: Register Role Definition implementation
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .models import RoleDefinition


# Simple in-memory storage for MVP
# In production, this would be replaced with proper persistence
_roles: Dict[str, RoleDefinition] = {}


def _record_observability(
    task_id: str,
    goal: str,
    status: str,
    input_data: Any,
    output_data: Any,
    duration_ms: int,
) -> None:
    """
    Minimal Observability recording point.
    Records task log with minimum required fields (DS-OBS-1).
    
    This is a minimal implementation for C-ROLE-1 only.
    Does not implement full Observability capabilities.
    """
    log_dir = Path("backend/subsystems/observability/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_entry = {
        "log_id": str(uuid.uuid4()),
        "task_id": task_id,
        "goal": goal,
        "input": str(input_data),
        "output": str(output_data),
        "status": status,
        "duration": duration_ms,
        "cost_estimate": 0,  # Minimal field
        "created_at": datetime.utcnow().isoformat(),
        "completed_at": datetime.utcnow().isoformat(),
    }
    
    log_file = log_dir / f"{task_id}.json"
    with open(log_file, "w") as f:
        json.dump(log_entry, f, indent=2)


def _persist_role_definition(role: RoleDefinition) -> None:
    """
    Persist role definition to disk as JSON.
    
    File naming: roles/{role_id}.json
    Overwrite allowed, no versioning (yet).
    """
    roles_dir = Path("backend/subsystems/role_management/roles")
    roles_dir.mkdir(parents=True, exist_ok=True)
    
    role_file = roles_dir / f"{role.role_id}.json"
    
    role_dict = {
        "role_id": role.role_id,
        "purpose": role.purpose,
        "inputs": role.inputs,
        "outputs": role.outputs,
        "boundaries": role.boundaries,
        "notes": role.notes,
        "registered_at": datetime.utcnow().isoformat(),
    }
    
    with open(role_file, "w") as f:
        json.dump(role_dict, f, indent=2)


def register_role_definition(
    role_definition: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-ROLE-1: Register Role Definition
    
    Registers a Role Definition as a static, declarative specification.
    
    THIS IS NOT PERMISSION SYSTEM
    THIS IS NOT EXECUTION
    THIS IS NOT INFERENCE
    
    Role is a STATIC DECLARATION, not a runtime entity.
    This function stores what a Role is, not what it can do or who can use it.
    
    Behavior:
    - Stores role definition as explicit data (manual rollback possible)
    - Overwrites existing role definition with same role_id
    - Records observability BEFORE and AFTER execution
    - No permission logic, no inference, no execution linkage
    
    Args:
        role_definition: Role definition dict with required fields:
            - role_id: str (unique identifier)
            - purpose: str (what problem this role exists to solve)
            - inputs: List[str] (input types this role accepts)
            - outputs: List[str] (output types this role must deliver)
            - boundaries: List[str] (things this role is forbidden to do)
            - notes: Optional[str] (additional notes)
        requested_by: Human identifier who requested the registration
    
    Returns:
        Success: {
            "role_id": str,
            "status": "registered",
            "timestamp": str (ISO format)
        }
        Failure: {
            "error": str,
            "error_type": str
        }
    
    Note: This function does NOT:
    - Infer permissions, authority, or execution rights
    - Trigger or reference Cell Composition
    - Coordinate with other Roles
    - Auto-link to Handoff or Execution
    - Implement permission logic
    - Create role hierarchy or inheritance
    - Infer capabilities
    """
    start_time = datetime.utcnow()
    task_id = f"register_role_{uuid.uuid4()}"
    
    try:
        # Record observability BEFORE execution
        _record_observability(
            task_id=task_id,
            goal="Register Role Definition (C-ROLE-1)",
            status="in_progress",
            input_data={
                "role_id": role_definition.get("role_id"),
                "purpose": role_definition.get("purpose"),
                "requested_by": requested_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Validate inputs
        if not isinstance(role_definition, dict):
            raise ValueError(f"role_definition must be a dict, got {type(role_definition).__name__}")
        
        # Validate required fields
        required_fields = ["role_id", "purpose", "inputs", "outputs", "boundaries"]
        for field in required_fields:
            if field not in role_definition:
                raise ValueError(f"Missing required field: '{field}'")
        
        role_id = role_definition["role_id"]
        if not isinstance(role_id, str) or not role_id.strip():
            raise ValueError("role_id must be a non-empty string")
        
        purpose = role_definition["purpose"]
        if not isinstance(purpose, str) or not purpose.strip():
            raise ValueError("purpose must be a non-empty string")
        
        inputs = role_definition["inputs"]
        if not isinstance(inputs, list):
            raise ValueError("inputs must be a list")
        if not all(isinstance(item, str) for item in inputs):
            raise ValueError("inputs must be a list of strings")
        
        outputs = role_definition["outputs"]
        if not isinstance(outputs, list):
            raise ValueError("outputs must be a list")
        if not all(isinstance(item, str) for item in outputs):
            raise ValueError("outputs must be a list of strings")
        
        boundaries = role_definition["boundaries"]
        if not isinstance(boundaries, list):
            raise ValueError("boundaries must be a list")
        if not all(isinstance(item, str) for item in boundaries):
            raise ValueError("boundaries must be a list of strings")
        
        notes = role_definition.get("notes")
        if notes is not None and not isinstance(notes, str):
            raise ValueError("notes must be a string or None")
        
        # Validate requested_by
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Create RoleDefinition object
        role = RoleDefinition(
            role_id=role_id,
            purpose=purpose,
            inputs=inputs,
            outputs=outputs,
            boundaries=boundaries,
            notes=notes,
        )
        
        # Store in memory (overwrite if exists)
        _roles[role_id] = role
        
        # Persist to disk
        _persist_role_definition(role)
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        timestamp = datetime.utcnow().isoformat()
        
        # Record observability AFTER execution (success)
        _record_observability(
            task_id=task_id,
            goal="Register Role Definition (C-ROLE-1)",
            status="success",
            input_data={
                "role_id": role_id,
                "purpose": purpose,
                "requested_by": requested_by,
            },
            output_data={
                "role_id": role_id,
                "status": "registered",
                "timestamp": timestamp,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "role_id": role_id,
            "status": "registered",
            "timestamp": timestamp,
        }
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        # Extract role_id safely for observability
        role_id_for_log = None
        if isinstance(role_definition, dict):
            role_id_for_log = role_definition.get("role_id")
        elif hasattr(role_definition, "role_id"):
            role_id_for_log = getattr(role_definition, "role_id", None)
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Register Role Definition (C-ROLE-1)",
            status="failure",
            input_data={
                "role_id": role_id_for_log,
                "requested_by": requested_by,
                "input_type": type(role_definition).__name__,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

