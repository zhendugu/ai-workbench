"""
Cell registration for Cell Composition Subsystem.

C-CELL-1: Register Cell Definition implementation

Phase-2 Semantic Reduction: Cell is a static declarative composition, not a runtime entity.
Cell has no state, no lifecycle, no execution semantics in Phase-2.
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .models import CellDefinition


# Simple in-memory storage for MVP
# In production, this would be replaced with proper persistence
_cells: Dict[str, CellDefinition] = {}


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
    
    This is a minimal implementation for C-CELL-1 only.
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


def _persist_cell_definition(cell: CellDefinition) -> None:
    """
    Persist cell definition to disk as JSON.
    
    File naming: cells/{cell_id}.json
    Overwrite allowed, no versioning (yet).
    
    Phase-2: Only stores static composition, no state or lifecycle.
    """
    cells_dir = Path("backend/subsystems/cell_composition/cells")
    cells_dir.mkdir(parents=True, exist_ok=True)
    
    cell_file = cells_dir / f"{cell.cell_id}.json"
    
    cell_dict = {
        "cell_id": cell.cell_id,
        "role_ids": cell.role_ids,
        "input_contract": cell.input_contract,
        "output_format": cell.output_format,
        "registered_at": datetime.utcnow().isoformat(),
    }
    
    # Explicitly verify no forbidden fields are present
    forbidden_fields = ["state", "status", "lifecycle", "state_transitions", 
                       "execution_history", "runtime_info"]
    for field in forbidden_fields:
        if field in cell_dict:
            raise ValueError(f"Forbidden field '{field}' detected in Cell definition")
    
    with open(cell_file, "w") as f:
        json.dump(cell_dict, f, indent=2)


def register_cell_definition(
    cell_definition: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-CELL-1: Register Cell Definition (STATIC, NO STATE)
    
    Registers a Cell Definition as a static, declarative composition specification.
    
    THIS IS NOT EXECUTION
    THIS IS NOT STATE MANAGEMENT
    THIS IS NOT LIFECYCLE MANAGEMENT
    
    Cell is a STATIC DECLARATION, not a runtime entity.
    This function stores what Roles form a Cell and its external interface contract.
    
    Phase-2 Semantic Reduction:
    - Cell has no state, no lifecycle, no execution semantics
    - Any stateful Cell semantics are deferred to Phase-3
    
    Behavior:
    - Stores cell definition as explicit data (manual rollback possible)
    - Overwrites existing cell definition with same cell_id
    - Records observability BEFORE and AFTER execution
    - No state logic, no lifecycle logic, no execution linkage
    
    Args:
        cell_definition: Cell definition dict with required fields:
            - cell_id: str (unique identifier)
            - role_ids: List[str] (list of role identifiers, read-only references)
            - input_contract: Dict (external input contract structure)
            - output_format: Dict (external output format structure)
        requested_by: Human identifier who requested the registration
    
    Returns:
        Success: {
            "cell_id": str,
            "status": "registered",
            "timestamp": str (ISO format)
        }
        Failure: {
            "error": str,
            "error_type": str
        }
    
    Note: This function does NOT:
    - Handle Cell state (active, idle, executing, dissolved)
    - Handle Cell lifecycle (activation, deactivation, dissolution)
    - Handle Cell execution semantics
    - Handle Cell orchestration or workflow
    - Auto-fix or normalize input
    - Coordinate with other subsystems at runtime
    """
    start_time = datetime.utcnow()
    task_id = f"register_cell_{uuid.uuid4()}"
    
    try:
        # Record observability BEFORE execution
        _record_observability(
            task_id=task_id,
            goal="Register Cell Definition (C-CELL-1)",
            status="in_progress",
            input_data={
                "cell_id": cell_definition.get("cell_id"),
                "role_ids": cell_definition.get("role_ids"),
                "requested_by": requested_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Validate inputs
        if not isinstance(cell_definition, dict):
            raise ValueError(f"cell_definition must be a dict, got {type(cell_definition).__name__}")
        
        # Validate required fields
        required_fields = ["cell_id", "role_ids", "input_contract", "output_format"]
        for field in required_fields:
            if field not in cell_definition:
                raise ValueError(f"Missing required field: '{field}'")
        
        cell_id = cell_definition["cell_id"]
        if not isinstance(cell_id, str) or not cell_id.strip():
            raise ValueError("cell_id must be a non-empty string")
        
        role_ids = cell_definition["role_ids"]
        if not isinstance(role_ids, list):
            raise ValueError("role_ids must be a list")
        if not all(isinstance(item, str) for item in role_ids):
            raise ValueError("role_ids must be a list of strings")
        if len(role_ids) == 0:
            raise ValueError("role_ids must contain at least one role identifier")
        
        input_contract = cell_definition["input_contract"]
        if not isinstance(input_contract, dict):
            raise ValueError("input_contract must be a dict")
        
        output_format = cell_definition["output_format"]
        if not isinstance(output_format, dict):
            raise ValueError("output_format must be a dict")
        
        # Explicitly check for forbidden fields
        forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                          "execution_history", "runtime_info", "activation_time",
                          "deactivation_time", "current_state", "previous_state"]
        for field in forbidden_fields:
            if field in cell_definition:
                raise ValueError(f"Forbidden field '{field}' detected. Phase-2 Cell definitions must not contain state or lifecycle fields.")
        
        # Validate requested_by
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Create CellDefinition object
        cell = CellDefinition(
            cell_id=cell_id,
            role_ids=role_ids,
            input_contract=input_contract,
            output_format=output_format,
        )
        
        # Store in memory (overwrite if exists)
        _cells[cell_id] = cell
        
        # Persist to disk
        _persist_cell_definition(cell)
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        timestamp = datetime.utcnow().isoformat()
        
        # Record observability AFTER execution (success)
        _record_observability(
            task_id=task_id,
            goal="Register Cell Definition (C-CELL-1)",
            status="success",
            input_data={
                "cell_id": cell_id,
                "role_ids": role_ids,
                "requested_by": requested_by,
            },
            output_data={
                "cell_id": cell_id,
                "status": "registered",
                "timestamp": timestamp,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "cell_id": cell_id,
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
        
        # Extract cell_id safely for observability
        cell_id_for_log = None
        if isinstance(cell_definition, dict):
            cell_id_for_log = cell_definition.get("cell_id")
        elif hasattr(cell_definition, "cell_id"):
            cell_id_for_log = getattr(cell_definition, "cell_id", None)
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Register Cell Definition (C-CELL-1)",
            status="failure",
            input_data={
                "cell_id": cell_id_for_log,
                "requested_by": requested_by,
                "input_type": type(cell_definition).__name__,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

