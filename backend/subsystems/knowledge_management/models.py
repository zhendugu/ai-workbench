"""
Data models for Knowledge Management Subsystem.

DS-KM-1: Document Record (as defined in MVP_RUNTIME_SURFACE.md)
DS-KM-2: Access Control Rule (as defined in MVP_RUNTIME_SURFACE.md)
DS-KM-3: Conflict Detection Result (as defined in MVP_RUNTIME_SURFACE.md)
DS-KM-4: Document Version Record (as defined in MVP_RUNTIME_SURFACE.md)
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


@dataclass
class AccessControlRule:
    """
    DS-KM-2: Access Control Rule
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - rule_id: Unique identifier
    - document_id: Reference to document
    - requester_type: Type of requester (Role identifier, system component)
    - permission_type: Permission type (read, write, delete)
    - granted: Boolean (true/false)
    - reason: Permission grant/deny reason
    """
    rule_id: str
    document_id: str
    requester_type: str
    permission_type: str  # "read", "write", "delete"
    granted: bool
    reason: str


@dataclass
class ConflictDetectionResult:
    """
    DS-KM-3: Conflict Detection Result
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - conflict_id: Unique identifier
    - document_id: Reference to document
    - conflict_type: Type of conflict (content conflict, version conflict)
    - conflicting_fields: List of field names with conflicts
    - conflicting_values: List of conflicting values
    - detected_at: Timestamp
    """
    conflict_id: str
    document_id: str
    conflict_type: str  # "content_conflict", "version_conflict"
    conflicting_fields: List[str]
    conflicting_values: List[Any]
    detected_at: datetime


@dataclass
class DocumentVersionRecord:
    """
    DS-KM-4: Document Version Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - version_id: Unique identifier
    - document_id: Reference to document
    - version_number: Integer version number
    - content: Version content
    - created_at: Timestamp
    - created_by: Creator identifier
    """
    version_id: str
    document_id: str
    version_number: int
    content: str
    created_at: datetime
    created_by: Optional[str]
