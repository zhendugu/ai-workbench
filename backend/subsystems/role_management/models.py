"""
Data models for Role Management Subsystem.

DS-ROLE-1: Role Definition Structure (as defined for C-ROLE-1)
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class RoleDefinition:
    """
    DS-ROLE-1: Role Definition Structure
    
    Minimal structure for Role registration (C-ROLE-1).
    
    Role is a STATIC DECLARATION, not a runtime entity.
    This defines what a Role is, not what it can do or who can use it.
    
    Required fields:
    - role_id: Unique identifier for the role
    - purpose: What problem this role exists to solve
    - inputs: List of input types this role accepts
    - outputs: List of output types this role must deliver
    - boundaries: List of things this role is explicitly forbidden to do
    
    Optional fields:
    - notes: Additional notes or context
    """
    role_id: str
    purpose: str
    inputs: List[str]
    outputs: List[str]
    boundaries: List[str]
    notes: Optional[str] = None
