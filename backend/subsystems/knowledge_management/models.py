"""
Data models for Knowledge Management Subsystem.

DS-KM-1: Document Record (as defined in MVP_RUNTIME_SURFACE.md)
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class DocumentRecord:
    """
    DS-KM-1: Document Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - document_id: Unique identifier
    - content: Document content (text/binary)
    - metadata: Document metadata (title, author, category, tags)
    - version_number: Integer version number
    - created_at: Timestamp
    - updated_at: Timestamp
    - access_control_rules: List of access control rules
    """
    document_id: str
    content: str
    metadata: Dict[str, Any]
    version_number: int
    created_at: datetime
    updated_at: datetime
    access_control_rules: List[Dict[str, Any]]
