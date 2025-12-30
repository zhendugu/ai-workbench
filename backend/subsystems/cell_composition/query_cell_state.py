"""
Cell state query for Cell Composition Subsystem.

C-CELL-5: Query Cell State implementation

Phase-3 Level 1: Minimal, passive, human-controlled Cell State.
State is descriptive data only and MUST NOT influence any system behavior.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .cell_state_models import CellState
from .update_cell_state import _cell_states, _record_observability


def _load_cell_state_from_disk(cell_id: str) -> CellState:
    """
    Load cell state from disk storage.
    
    File naming: cell_states/{cell_id}.json
    
    Returns:
        CellState if found, None if not found.
    """
    states_dir = Path("backend/subsystems/cell_composition/cell_states")
    state_file = states_dir / f"{cell_id}.json"
    
    if not state_file.exists():
        return None
    
    with open(state_file, "r") as f:
        state_dict = json.load(f)
    
    # Verify no forbidden fields are present
    forbidden_fields = ["previous_state", "transition", "reason", "metadata",
                       "lifecycle", "execution_history", "runtime_info"]
    for field in forbidden_fields:
        if field in state_dict:
            raise ValueError(f"Forbidden field '{field}' detected in stored state. Phase-3 Level 1 Cell State must not contain behavior-related fields.")
    
    return CellState(
        cell_id=state_dict["cell_id"],
        state=state_dict["state"],
        updated_by=state_dict["updated_by"],
        updated_at=state_dict["updated_at"],
    )


def query_cell_state(
    cell_id: str,
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-CELL-5: Query Cell State
    
    Queries the descriptive state of a Cell.
    
    Phase-3 Level 1 Constraints:
    - Read-only operation
    - No repair, inference, or normalization
    - No history return
    - No cross-subsystem aggregation
    - MUST record Observability entry (before / after)
    
    Args:
        cell_id: Unique identifier for the cell
        requested_by: Human identifier who requested the query
    
    Returns:
        Dict with:
        - cell_id: str
        - state: str
        - updated_by: str
        - updated_at: ISO8601 timestamp
        - status: "found"
        
        Or:
        - cell_id: str
        - status: "not_found"
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"query_cell_state_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        _record_observability(
            task_id=task_id,
            goal="Query Cell State (C-CELL-5)",
            status="in_progress",
            input_data={
                "cell_id": cell_id,
                "requested_by": requested_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Input validation
        if not isinstance(cell_id, str) or not cell_id.strip():
            raise ValueError("cell_id must be a non-empty string")
        
        if not isinstance(requested_by, str) or not requested_by.strip():
            raise ValueError("requested_by must be a non-empty string")
        
        # Try in-memory cache first
        cell_state = _cell_states.get(cell_id)
        
        # If not in memory, try disk
        if cell_state is None:
            cell_state = _load_cell_state_from_disk(cell_id)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        if cell_state is None:
            # Not found
            result = {
                "cell_id": cell_id,
                "status": "not_found",
            }
            
            # Observability: Exit record (not_found)
            _record_observability(
                task_id=task_id,
                goal="Query Cell State (C-CELL-5)",
                status="success",
                input_data={
                    "cell_id": cell_id,
                    "requested_by": requested_by,
                },
                output_data=result,
                duration_ms=duration_ms,
            )
            
            return result
        
        # Found
        result = {
            "cell_id": cell_state.cell_id,
            "state": cell_state.state,
            "updated_by": cell_state.updated_by,
            "updated_at": cell_state.updated_at,
            "status": "found",
        }
        
        # Observability: Exit record (found)
        _record_observability(
            task_id=task_id,
            goal="Query Cell State (C-CELL-5)",
            status="success",
            input_data={
                "cell_id": cell_id,
                "requested_by": requested_by,
            },
            output_data=result,
            duration_ms=duration_ms,
        )
        
        return result
        
    except Exception as e:
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        # Observability: Exit record (failure)
        _record_observability(
            task_id=task_id,
            goal="Query Cell State (C-CELL-5)",
            status="failure",
            input_data={
                "cell_id": cell_id,
                "requested_by": requested_by,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

