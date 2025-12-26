"""
Storage interface for Knowledge Management Subsystem.

C-KM-1: Store Document implementation
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import DocumentRecord


# Simple in-memory storage for MVP
# In production, this would be replaced with proper persistence
_documents: Dict[str, DocumentRecord] = {}


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
    
    This is a minimal implementation for C-KM-1 only.
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


def store_document(
    content: str,
    metadata: Dict[str, Any],
    requester_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-KM-1: Store Document
    
    Accepts document content and metadata, stores document, and returns document identifier.
    
    Args:
        content: Document content (text)
        metadata: Document metadata (title, author, category, tags)
        requester_id: Optional requester identifier for access control (not implemented in C-KM-1)
    
    Returns:
        Success: { "document_id": str, "version_number": int, "created_at": str }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    """
    start_time = datetime.utcnow()
    task_id = f"store_document_{uuid.uuid4()}"
    
    try:
        # Validate inputs (minimal validation for failure path testing)
        if not isinstance(metadata, dict):
            raise ValueError(f"metadata must be a dict, got {type(metadata).__name__}")
        
        # Generate unique document identifier
        document_id = str(uuid.uuid4())
        
        # Create Document Record (DS-KM-1) with version=1
        now = datetime.utcnow()
        document = DocumentRecord(
            document_id=document_id,
            content=content,
            metadata=metadata,
            version_number=1,
            created_at=now,
            updated_at=now,
            access_control_rules=[],  # Empty for C-KM-1 (access control not implemented)
        )
        
        # Persist document (simple in-memory storage)
        _documents[document_id] = document
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record in Observability (minimal)
        _record_observability(
            task_id=task_id,
            goal="Store Document (C-KM-1)",
            status="success",
            input_data={"content_length": len(content), "metadata": metadata},
            output_data={"document_id": document_id, "version_number": 1},
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "document_id": document_id,
            "version_number": 1,
            "created_at": now.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {"content_length": len(content) if content else 0},
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Store Document (C-KM-1)",
            status="failure",
            input_data={"content_length": len(content) if content else 0, "metadata": metadata},
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response
