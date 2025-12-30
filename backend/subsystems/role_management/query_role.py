"""
Role query for Role Management Subsystem.

C-ROLE-2: Query Role Definition implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import RoleDefinition
from .register_role import _roles, _record_observability


def query_role_definition(
    role_id: str,
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-ROLE-2: Query Role Definition
    
    Retrieves an existing RoleDefinition by role_id.
    This is a READ-ONLY operation with NO writes, NO mutation, NO auto-repair.
    
    THIS IS NOT PERMISSION SYSTEM
    THIS IS NOT EXECUTION
    THIS IS NOT INFERENCE
    
    Behavior:
    - READ-ONLY operation: No writes, no mutation, no auto-repair
    - Load from in-memory cache if present
    - Else load from disk roles/{role_id}.json
    - Return "not_found" if missing
    - Return structured error for invalid input
    - Records observability BEFORE and AFTER execution
    
    Args:
        role_id: Role identifier to query
        requested_by: Human identifier who requested the query
    
    Returns:
        Found: {
            "role_id": str,
            "status": "found",
            "role_definition": {
                "role_id": str,
                "purpose": str,
                "inputs": List[str],
                "outputs": List[str],
                "boundaries": List[str],
                "notes": Optional[str]
            },
            "timestamp": str (ISO format)
        }
        Not Found: {
            "role_id": str,
            "status": "not_found",
            "timestamp": str (ISO format)
        }
        Failure: {
            "error": str,
            "error_type": str
        }
    
    Note: This function does NOT:
    - Create default role
    - Fix/normalize stored role
    - List roles (out of scope)
    - Search/fuzzy matching (out of scope)
    - Reference Cell Composition / Handoff / Execution
    - Infer permissions, authority, or execution rights
    """
    start_time = datetime.utcnow()
    task_id = f"query_role_{uuid.uuid4()}"
    
    try:
        # Record observability BEFORE execution
        _record_observability(
            task_id=task_id,
            goal="Query Role Definition (C-ROLE-2)",
            status="in_progress",
            input_data={
                "role_id": role_id,
                "requested_by": requested_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Validate inputs
        if not isinstance(role_id, str) or not role_id.strip():
            raise ValueError("role_id must be a non-empty string")
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Try to load from in-memory cache first
        role = _roles.get(role_id)
        
        # If not in memory, try to load from disk
        if role is None:
            roles_dir = Path("backend/subsystems/role_management/roles")
            role_file = roles_dir / f"{role_id}.json"
            
            if role_file.exists():
                # Load from disk
                with open(role_file, "r") as f:
                    role_dict = json.load(f)
                
                # Reconstruct RoleDefinition object
                role = RoleDefinition(
                    role_id=role_dict["role_id"],
                    purpose=role_dict["purpose"],
                    inputs=role_dict["inputs"],
                    outputs=role_dict["outputs"],
                    boundaries=role_dict["boundaries"],
                    notes=role_dict.get("notes"),
                )
                
                # Cache in memory for future queries
                _roles[role_id] = role
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        timestamp = datetime.utcnow().isoformat()
        
        # Handle result
        if role is None:
            # Not found
            result = {
                "role_id": role_id,
                "status": "not_found",
                "timestamp": timestamp,
            }
            
            # Record observability AFTER execution (not found)
            _record_observability(
                task_id=task_id,
                goal="Query Role Definition (C-ROLE-2)",
                status="success",  # Query operation succeeded, role just not found
                input_data={
                    "role_id": role_id,
                    "requested_by": requested_by,
                },
                output_data=result,
                duration_ms=duration_ms,
            )
            
            return result
        else:
            # Found
            result = {
                "role_id": role_id,
                "status": "found",
                "role_definition": {
                    "role_id": role.role_id,
                    "purpose": role.purpose,
                    "inputs": role.inputs,
                    "outputs": role.outputs,
                    "boundaries": role.boundaries,
                    "notes": role.notes,
                },
                "timestamp": timestamp,
            }
            
            # Record observability AFTER execution (found)
            _record_observability(
                task_id=task_id,
                goal="Query Role Definition (C-ROLE-2)",
                status="success",
                input_data={
                    "role_id": role_id,
                    "requested_by": requested_by,
                },
                output_data={
                    "role_id": role_id,
                    "status": "found",
                    "purpose": role.purpose,
                },
                duration_ms=duration_ms,
            )
            
            return result
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Query Role Definition (C-ROLE-2)",
            status="failure",
            input_data={
                "role_id": role_id if isinstance(role_id, str) else str(role_id),
                "requested_by": requested_by,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

