"""
Data models for Cell Composition Subsystem.

DS-CELL-1: Cell Definition Structure (as defined for C-CELL-1)

Phase-2 Semantic Reduction: Cell is a static declarative composition, not a runtime entity.
Cell has no state, no lifecycle, no execution semantics in Phase-2.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CellDefinition:
    """
    DS-CELL-1: Cell Definition Structure (Phase-2 Reduced)
    
    Minimal structure for Cell registration (C-CELL-1).
    
    Cell is a STATIC DECLARATION, not a runtime entity.
    This defines what Roles form a Cell and its external interface contract.
    
    Phase-2 Reduction:
    - NO state fields (active, idle, executing, dissolved)
    - NO lifecycle fields
    - NO execution semantics
    - NO state transitions
    - NO runtime information
    
    Required fields:
    - cell_id: Unique identifier for the cell
    - role_ids: List of role identifiers (read-only references to Role definitions)
    - input_contract: External input contract structure (dict)
    - output_format: External output format structure (dict)
    
    Forbidden fields (Phase-2):
    - state, status, lifecycle, state_transitions, execution_history, runtime_info
    - Any execution-related metadata
    """
    cell_id: str
    role_ids: List[str]
    input_contract: Dict
    output_format: Dict
