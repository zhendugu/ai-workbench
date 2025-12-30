"""
Cell state update for Cell Composition Subsystem.

C-CELL-4: Update Cell State implementation

Phase-3 Level 1: Minimal, passive, human-controlled Cell State.
State is descriptive data only and MUST NOT influence any system behavior.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .cell_state_models import CellState


# Simple in-memory storage for MVP
_cell_states: Dict[str, CellState] = {}


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
        "cost_estimate": 0,
        "created_at": datetime.utcnow().isoformat(),
        "completed_at": datetime.utcnow().isoformat(),
    }
    
    log_file = log_dir / f"{task_id}.json"
    with open(log_file, "w") as f:
        json.dump(log_entry, f, indent=2)


def _persist_cell_state(cell_state: CellState) -> None:
    """
    Persist cell state to disk as JSON.
    
    File naming: cell_states/{cell_id}.json
    Overwrite allowed (human decision).
    
    Phase-3 Level 1: Only stores descriptive state, no behavior triggers.
    """
    states_dir = Path("backend/subsystems/cell_composition/cell_states")
    states_dir.mkdir(parents=True, exist_ok=True)
    
    state_file = states_dir / f"{cell_state.cell_id}.json"
    
    state_dict = {
        "cell_id": cell_state.cell_id,
        "state": cell_state.state,
        "updated_by": cell_state.updated_by,
        "updated_at": cell_state.updated_at,
    }
    
    # Explicitly verify no forbidden fields are present
    forbidden_fields = ["previous_state", "transition", "reason", "metadata",
                       "lifecycle", "execution_history", "runtime_info"]
    for field in forbidden_fields:
        if field in state_dict:
            raise ValueError(f"Forbidden field '{field}' detected. Phase-3 Level 1 Cell State must not contain behavior-related fields.")
    
    with open(state_file, "w") as f:
        json.dump(state_dict, f, indent=2)


def update_cell_state(
    cell_id: str,
    state: str,
    updated_by: str,
) -> Dict[str, Any]:
    """
    C-CELL-4: Update Cell State
    
    Updates the descriptive state of a Cell.
    
    Phase-3 Level 1 Constraints:
    - Explicit human invocation only
    - Overwrite allowed (human decision)
    - MUST NOT trigger execution
    - MUST NOT trigger validation, handoff, or orchestration
    - MUST record Observability entry (before / after)
    
    Args:
        cell_id: Unique identifier for the cell
        state: Descriptive state value (human-controlled)
        updated_by: Human identifier who updated the state
    
    Returns:
        Dict with:
        - cell_id: str
        - state: str
        - updated_at: ISO8601 timestamp
        - status: "updated"
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    start_time = datetime.utcnow()
    task_id = f"update_cell_state_{uuid.uuid4()}"
    
    try:
        # Observability: Entry record
        _record_observability(
            task_id=task_id,
            goal="Update Cell State (C-CELL-4)",
            status="in_progress",
            input_data={
                "cell_id": cell_id,
                "state": state,
                "updated_by": updated_by,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Input validation
        if not isinstance(cell_id, str) or not cell_id.strip():
            raise ValueError("cell_id must be a non-empty string")
        
        if not isinstance(state, str) or not state.strip():
            raise ValueError("state must be a non-empty string")
        
        if not isinstance(updated_by, str) or not updated_by.strip():
            raise ValueError("updated_by must be a non-empty string")
        
        # Create CellState
        updated_at = datetime.utcnow().isoformat()
        cell_state = CellState(
            cell_id=cell_id,
            state=state,
            updated_by=updated_by,
            updated_at=updated_at,
        )
        
        # Store in memory
        _cell_states[cell_id] = cell_state
        
        # Persist to disk
        _persist_cell_state(cell_state)
        
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        result = {
            "cell_id": cell_id,
            "state": state,
            "updated_at": updated_at,
            "status": "updated",
        }
        
        # Observability: Exit record (success)
        _record_observability(
            task_id=task_id,
            goal="Update Cell State (C-CELL-4)",
            status="success",
            input_data={
                "cell_id": cell_id,
                "state": state,
                "updated_by": updated_by,
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
            goal="Update Cell State (C-CELL-4)",
            status="failure",
            input_data={
                "cell_id": cell_id,
                "state": state,
                "updated_by": updated_by,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response

