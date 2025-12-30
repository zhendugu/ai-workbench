"""
Cell query for Cell Composition Subsystem.

C-CELL-2: Query Cell Definition implementation

Phase-2 Semantic Reduction: Cell is a static declarative composition, not a runtime entity.
Cell has no state, no lifecycle, no execution semantics in Phase-2.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .models import CellDefinition
from .register_cell import _cells, _record_observability


def query_cell_definition(
    cell_id: str,
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-CELL-2: Query Cell Definition (READ-ONLY, NO STATE)
    
    Retrieves an existing CellDefinition by cell_id.
    This is a READ-ONLY operation with NO writes, NO mutation, NO auto-repair.
    
    THIS IS NOT EXECUTION
    THIS IS NOT STATE MANAGEMENT
    THIS IS NOT LIFECYCLE MANAGEMENT
    
    Phase-2 Semantic Reduction:
    - Cell has no state, no lifecycle, no execution semantics
    - Returns only static composition definition
    
    Behavior:
    - READ-ONLY operation: No writes, no mutation, no auto-repair
    - Load from in-memory cache if present
    - Else load from disk cells/{cell_id}.json
    - Return "not_found" if missing
    - Return structured error for invalid input
    - Records observability BEFORE and AFTER execution (even for "not_found")
    
    Args:
        cell_id: Cell identifier to query
        requested_by: Human identifier who requested the query
    
    Returns:
        Found: {
            "cell_id": str,
            "status": "found",
            "cell_definition": {
                "cell_id": str,
                "role_ids": List[str],
                "input_contract": Dict,
                "output_format": Dict
            },
            "timestamp": str (ISO format)
        }
        Not Found: {
            "cell_id": str,
            "status": "not_found",
            "timestamp": str (ISO format)
        }
        Failure: {
            "error": str,
            "error_type": str
        }
    
    Note: This function does NOT:
    - Create default cell
    - Fix/normalize stored cell
    - List cells (out of scope)
    - Search/fuzzy matching (out of scope)
    - Return Cell state information
    - Return Cell status or lifecycle information
    - Return Cell execution history
    - Return Cell runtime information
    - Reference Cell execution or orchestration
    """
    start_time = datetime.utcnow()
    task_id = f"query_cell_{uuid.uuid4()}"
    
    try:
        # Record observability BEFORE execution
        _record_observability(
            task_id=task_id,
            goal="Query Cell Definition (C-CELL-2)",
            status="in_progress",
            input_data={
                "cell_id": cell_id,
                "requested_by": requested_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Validate inputs
        if not isinstance(cell_id, str) or not cell_id.strip():
            raise ValueError("cell_id must be a non-empty string")
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Try to load from in-memory cache first
        cell = _cells.get(cell_id)
        
        # If not in memory, try to load from disk
        if cell is None:
            cells_dir = Path("backend/subsystems/cell_composition/cells")
            cell_file = cells_dir / f"{cell_id}.json"
            
            if cell_file.exists():
                # Load from disk
                with open(cell_file, "r") as f:
                    cell_dict = json.load(f)
                
                # Explicitly verify no forbidden fields in stored data
                forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                                 "execution_history", "runtime_info", "activation_time",
                                 "deactivation_time", "current_state", "previous_state"]
                for field in forbidden_fields:
                    if field in cell_dict:
                        raise ValueError(f"Forbidden field '{field}' detected in stored Cell definition. Phase-2 Cell definitions must not contain state or lifecycle fields.")
                
                # Reconstruct CellDefinition object
                cell = CellDefinition(
                    cell_id=cell_dict["cell_id"],
                    role_ids=cell_dict["role_ids"],
                    input_contract=cell_dict["input_contract"],
                    output_format=cell_dict["output_format"],
                )
                
                # Cache in memory for future queries
                _cells[cell_id] = cell
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        timestamp = datetime.utcnow().isoformat()
        
        # Handle result
        if cell is None:
            # Not found
            result = {
                "cell_id": cell_id,
                "status": "not_found",
                "timestamp": timestamp,
            }
            
            # Record observability AFTER execution (not found)
            _record_observability(
                task_id=task_id,
                goal="Query Cell Definition (C-CELL-2)",
                status="success",  # Query operation succeeded, cell just not found
                input_data={
                    "cell_id": cell_id,
                    "requested_by": requested_by,
                },
                output_data=result,
                duration_ms=duration_ms,
            )
            
            return result
        else:
            # Found
            result = {
                "cell_id": cell_id,
                "status": "found",
                "cell_definition": {
                    "cell_id": cell.cell_id,
                    "role_ids": cell.role_ids,
                    "input_contract": cell.input_contract,
                    "output_format": cell.output_format,
                },
                "timestamp": timestamp,
            }
            
            # Record observability AFTER execution (found)
            _record_observability(
                task_id=task_id,
                goal="Query Cell Definition (C-CELL-2)",
                status="success",
                input_data={
                    "cell_id": cell_id,
                    "requested_by": requested_by,
                },
                output_data={
                    "cell_id": cell_id,
                    "status": "found",
                    "role_ids_count": len(cell.role_ids),
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
            goal="Query Cell Definition (C-CELL-2)",
            status="failure",
            input_data={
                "cell_id": cell_id if isinstance(cell_id, str) else str(cell_id),
                "requested_by": requested_by,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

