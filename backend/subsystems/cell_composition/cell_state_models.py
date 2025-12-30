"""
Data models for Cell State (Phase-3 Level 1).

DS-CELL-2: CellState Structure

Phase-3 Level 1: Minimal, passive, human-controlled Cell State.
State is descriptive data only and MUST NOT influence any system behavior.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class CellState:
    """
    DS-CELL-2: Cell State Structure (Phase-3 Level 1)
    
    Minimal structure for Cell state (C-CELL-4, C-CELL-5).
    
    Cell State is DESCRIPTIVE ONLY, not prescriptive.
    State does NOT trigger execution, validation, handoff, or orchestration.
    
    Phase-3 Level 1 Constraints:
    - NO previous_state field
    - NO transition field
    - NO reason / metadata fields
    - NO lifecycle fields
    - NO execution-related fields
    - NO implicit semantics
    
    Required fields:
    - cell_id: Unique identifier for the cell
    - state: Descriptive state value (human-controlled)
    - updated_by: Human identifier who updated the state
    - updated_at: ISO8601 timestamp of the update
    
    Forbidden fields (Phase-3 Level 1):
    - previous_state, transition, reason, metadata
    - lifecycle, execution_history, runtime_info
    - Any field that implies behavior or semantics
    """
    cell_id: str
    state: str
    updated_by: str
    updated_at: str  # ISO8601 timestamp

