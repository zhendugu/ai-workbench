"""
Storage interface for Knowledge Management Subsystem.

C-KM-1: Store Document implementation
C-KM-2: Retrieve Document implementation
C-KM-3: Check Access Permission implementation
C-KM-4: Detect Knowledge Conflict implementation
C-KM-5: Record Document Version implementation
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import DocumentRecord, AccessControlRule, ConflictDetectionResult, DocumentVersionRecord


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


def retrieve_document(
    document_id: str,
    requester_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-KM-2: Retrieve Document
    
    Accepts document identifier, retrieves document, and returns document content and metadata.
    
    Args:
        document_id: Document identifier (UUID string)
        requester_id: Optional requester identifier for access control (not implemented in C-KM-2)
    
    Returns:
        Success: {
            "document_id": str,
            "content": str,
            "metadata": dict,
            "version_number": int,
            "created_at": str,
            "updated_at": str
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    """
    start_time = datetime.utcnow()
    task_id = f"retrieve_document_{uuid.uuid4()}"
    
    try:
        # Validate document_id
        if not document_id or not isinstance(document_id, str):
            raise ValueError("document_id must be a non-empty string")
        
        # Step 2: Check access permission (minimal - document existence check)
        # C-KM-3 (Check Access Permission) is not implemented, so we do minimal check:
        # document must exist in storage
        if document_id not in _documents:
            raise FileNotFoundError(f"Document not found: {document_id}")
        
        # Step 4: Retrieve document record from persistent storage
        document = _documents[document_id]
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Step 6: Record document retrieval in Observability (task log)
        _record_observability(
            task_id=task_id,
            goal="Retrieve Document (C-KM-2)",
            status="success",
            input_data={"document_id": document_id, "requester_id": requester_id},
            output_data={
                "document_id": document.document_id,
                "version_number": document.version_number,
                "content_length": len(document.content),
            },
            duration_ms=duration_ms,
        )
        
        # Step 5: Return document content, metadata, and version information
        return {
            "document_id": document.document_id,
            "content": document.content,
            "metadata": document.metadata,
            "version_number": document.version_number,
            "created_at": document.created_at.isoformat(),
            "updated_at": document.updated_at.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {"document_id": document_id},
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Retrieve Document (C-KM-2)",
            status="failure",
            input_data={"document_id": document_id, "requester_id": requester_id},
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response


def check_access_permission(
    document_id: str,
    requester_id: str,
    permission_type: str = "read",
) -> Dict[str, Any]:
    """
    C-KM-3: Check Access Permission
    
    Accepts document identifier and requester identifier, checks access permission,
    and returns permission status and reason.
    
    Args:
        document_id: Document identifier (UUID string)
        requester_id: Requester identifier (Role identifier or system component)
        permission_type: Permission type to check ("read", "write", "delete")
    
    Returns:
        Success: {
            "permission_status": str,  # "read_allowed", "write_allowed", "denied"
            "permission_reason": str,
            "rule_id": str (if rule found)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    """
    start_time = datetime.utcnow()
    task_id = f"check_access_permission_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not document_id or not isinstance(document_id, str):
            raise ValueError("document_id must be a non-empty string")
        if not requester_id or not isinstance(requester_id, str):
            raise ValueError("requester_id must be a non-empty string")
        if permission_type not in ["read", "write", "delete"]:
            raise ValueError(f"permission_type must be 'read', 'write', or 'delete', got '{permission_type}'")
        
        # Check if document exists
        if document_id not in _documents:
            raise FileNotFoundError(f"Document not found: {document_id}")
        
        document = _documents[document_id]
        
        # Check access control rules (DS-KM-2)
        # Look for matching rule in document's access_control_rules
        matching_rule = None
        for rule_dict in document.access_control_rules:
            if (rule_dict.get("requester_type") == requester_id and
                rule_dict.get("permission_type") == permission_type):
                matching_rule = rule_dict
                break
        
        # Determine permission status
        if matching_rule:
            granted = matching_rule.get("granted", False)
            reason = matching_rule.get("reason", "Rule-based decision")
            rule_id = matching_rule.get("rule_id", "unknown")
            
            if granted:
                if permission_type == "read":
                    permission_status = "read_allowed"
                elif permission_type == "write":
                    permission_status = "write_allowed"
                else:  # delete
                    permission_status = "denied"  # Delete not explicitly allowed in MVP
                    reason = "Delete permission not granted in MVP"
            else:
                permission_status = "denied"
        else:
            # No matching rule found - return denied (no default allow behavior)
            rule_id = None
            permission_status = "denied"
            reason = f"No access control rule found for requester '{requester_id}' and permission type '{permission_type}'"
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record in Observability (minimal)
        _record_observability(
            task_id=task_id,
            goal="Check Access Permission (C-KM-3)",
            status="success",
            input_data={
                "document_id": document_id,
                "requester_id": requester_id,
                "permission_type": permission_type,
            },
            output_data={
                "permission_status": permission_status,
                "permission_reason": reason,
            },
            duration_ms=duration_ms,
        )
        
        # Return permission status and reason
        result = {
            "permission_status": permission_status,
            "permission_reason": reason,
        }
        if rule_id:
            result["rule_id"] = rule_id
        
        return result
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "document_id": document_id,
                "requester_id": requester_id,
                "permission_type": permission_type,
            },
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Check Access Permission (C-KM-3)",
            status="failure",
            input_data={
                "document_id": document_id,
                "requester_id": requester_id,
                "permission_type": permission_type,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response


# Simple in-memory storage for conflict detection results
_conflict_results: Dict[str, ConflictDetectionResult] = {}


def detect_knowledge_conflict(
    document_content: str,
    existing_document_id: str,
) -> Dict[str, Any]:
    """
    C-KM-4: Detect Knowledge Conflict
    
    Accepts document content and existing document identifier, compares content for conflicts,
    and returns conflict detection result.
    
    Args:
        document_content: New document content to compare
        existing_document_id: Existing document identifier to compare against
    
    Returns:
        Success: {
            "conflict_detected": bool,
            "conflict_id": str (if conflict detected),
            "conflict_type": str (if conflict detected),
            "conflicting_fields": List[str] (if conflict detected),
            "conflicting_values": List[Any] (if conflict detected),
            "detected_at": str (if conflict detected)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Does NOT auto-resolve conflicts, does NOT escalate, does NOT modify documents.
    Only returns structured conflict detection result.
    """
    start_time = datetime.utcnow()
    task_id = f"detect_knowledge_conflict_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not document_content or not isinstance(document_content, str):
            raise ValueError("document_content must be a non-empty string")
        if not existing_document_id or not isinstance(existing_document_id, str):
            raise ValueError("existing_document_id must be a non-empty string")
        
        # Step 2: Retrieve existing document from Knowledge Management
        if existing_document_id not in _documents:
            raise FileNotFoundError(f"Existing document not found: {existing_document_id}")
        
        existing_document = _documents[existing_document_id]
        
        # Step 3: Compare new document content with existing document content
        # Step 4: Identify conflicting fields and values
        conflicting_fields = []
        conflicting_values = []
        
        # Simple content comparison (minimal implementation)
        if document_content != existing_document.content:
            conflicting_fields.append("content")
            conflicting_values.append({
                "existing": existing_document.content,
                "new": document_content,
            })
        
        # Step 5: If conflicts detected, create conflict detection result record
        conflict_detected = len(conflicting_fields) > 0
        
        if conflict_detected:
            conflict_id = str(uuid.uuid4())
            now = datetime.utcnow()
            
            conflict_result = ConflictDetectionResult(
                conflict_id=conflict_id,
                document_id=existing_document_id,
                conflict_type="content_conflict",
                conflicting_fields=conflicting_fields,
                conflicting_values=conflicting_values,
                detected_at=now,
            )
            
            # Step 6: Store conflict detection result in persistent storage
            _conflict_results[conflict_id] = conflict_result
            
            # Calculate duration
            duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            # Step 7: Record conflict detection in Observability (task log)
            _record_observability(
                task_id=task_id,
                goal="Detect Knowledge Conflict (C-KM-4)",
                status="success",
                input_data={
                    "existing_document_id": existing_document_id,
                    "content_length": len(document_content),
                },
                output_data={
                    "conflict_detected": True,
                    "conflict_id": conflict_id,
                    "conflict_type": "content_conflict",
                },
                duration_ms=duration_ms,
            )
            
            # Step 8: Return conflict detection result and conflict details
            return {
                "conflict_detected": True,
                "conflict_id": conflict_id,
                "conflict_type": "content_conflict",
                "conflicting_fields": conflicting_fields,
                "conflicting_values": conflicting_values,
                "detected_at": now.isoformat(),
            }
        else:
            # No conflict detected
            duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            # Record in Observability
            _record_observability(
                task_id=task_id,
                goal="Detect Knowledge Conflict (C-KM-4)",
                status="success",
                input_data={
                    "existing_document_id": existing_document_id,
                    "content_length": len(document_content),
                },
                output_data={
                    "conflict_detected": False,
                },
                duration_ms=duration_ms,
            )
            
            # Return no conflict result
            return {
                "conflict_detected": False,
            }
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "existing_document_id": existing_document_id,
                "content_length": len(document_content) if document_content else 0,
            },
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Detect Knowledge Conflict (C-KM-4)",
            status="failure",
            input_data={
                "existing_document_id": existing_document_id,
                "content_length": len(document_content) if document_content else 0,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response


# Simple in-memory storage for document version records
_version_records: Dict[str, DocumentVersionRecord] = {}


def record_document_version(
    document_id: str,
    new_version_content: str,
    created_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-KM-5: Record Document Version
    
    Accepts document identifier and new version content, creates new version record,
    preserves previous version, and records version timestamp.
    
    Args:
        document_id: Document identifier (UUID string)
        new_version_content: New version content to record
        created_by: Creator identifier (optional)
    
    Returns:
        Success: {
            "version_id": str,
            "document_id": str,
            "version_number": int,
            "created_at": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Does NOT perform conflict detection, does NOT resolve conflicts,
    does NOT introduce version strategy or merge logic.
    Only records new version and preserves previous version.
    """
    start_time = datetime.utcnow()
    task_id = f"record_document_version_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not document_id or not isinstance(document_id, str):
            raise ValueError("document_id must be a non-empty string")
        if not new_version_content or not isinstance(new_version_content, str):
            raise ValueError("new_version_content must be a non-empty string")
        
        # Check if document exists
        if document_id not in _documents:
            raise FileNotFoundError(f"Document not found: {document_id}")
        
        existing_document = _documents[document_id]
        
        # Preserve previous version: create version record for current content
        version_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        # Create version record for previous version (preserve old version)
        previous_version_record = DocumentVersionRecord(
            version_id=version_id,
            document_id=document_id,
            version_number=existing_document.version_number,
            content=existing_document.content,  # Preserve old content
            created_at=now,
            created_by=created_by,
        )
        
        # Store previous version record
        _version_records[version_id] = previous_version_record
        
        # Update document with new version
        new_version_number = existing_document.version_number + 1
        existing_document.content = new_version_content
        existing_document.version_number = new_version_number
        existing_document.updated_at = now
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record in Observability (minimal)
        _record_observability(
            task_id=task_id,
            goal="Record Document Version (C-KM-5)",
            status="success",
            input_data={
                "document_id": document_id,
                "new_version_content_length": len(new_version_content),
                "previous_version_number": existing_document.version_number - 1,
            },
            output_data={
                "version_id": version_id,
                "version_number": new_version_number,
            },
            duration_ms=duration_ms,
        )
        
        # Return new version information
        return {
            "version_id": version_id,
            "document_id": document_id,
            "version_number": new_version_number,
            "created_at": now.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error and record in Observability
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "document_id": document_id,
                "new_version_content_length": len(new_version_content) if new_version_content else 0,
            },
        }
        
        # Record failure in Observability
        _record_observability(
            task_id=task_id,
            goal="Record Document Version (C-KM-5)",
            status="failure",
            input_data={
                "document_id": document_id,
                "new_version_content_length": len(new_version_content) if new_version_content else 0,
            },
            output_data=error_response,
            duration_ms=duration_ms,
        )
        
        return error_response
