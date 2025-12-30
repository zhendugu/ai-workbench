"""
Data models for Handoff Protocol Subsystem.

DS-HANDOFF-1: Handoff Document Structure (as defined for C-HANDOFF-1)
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class HandoffDocument:
    """
    DS-HANDOFF-1: Handoff Document Structure
    
    Minimal structure for Handoff Protocol validation (C-HANDOFF-1).
    
    Required fields:
    - document_id: Unique identifier for the handoff document
    - document_type: "work_state" or "presentation_state"
    - content: Document content (text/markdown)
    - created_at: Timestamp
    
    Optional fields:
    - source_role: Source role identifier (optional)
    - target_role: Target role identifier (optional)
    - metadata: Additional metadata (optional)
    """
    document_id: str
    document_type: str  # "work_state" or "presentation_state"
    content: str
    created_at: datetime
    source_role: Optional[str] = None
    target_role: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
