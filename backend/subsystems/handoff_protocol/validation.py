"""
Handoff Protocol validation for Handoff Protocol Subsystem.

C-HANDOFF-1: Validate Handoff Document implementation
"""

from datetime import datetime
from typing import Any, Dict, List, Optional


def validate_handoff_document(
    handoff_document: Any,
    document_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-HANDOFF-1: Validate Handoff Document
    
    Validates that a handoff document conforms to the Handoff Protocol format.
    This is a PURE FUNCTION with NO side effects, NO state changes, NO dependencies.
    
    Behavior:
    - Pure validation function: No side effects, no state changes
    - Schema validation: Checks required fields and structure
    - Structural checks: Validates document type, content format
    - Clear error reporting: Returns structured validation results
    
    Args:
        handoff_document: Document to validate (dict or string)
        document_type: Optional document type hint ("work_state" or "presentation_state")
    
    Returns:
        Success: {
            "valid": True,
            "details": {
                "document_id": str,
                "document_type": str,
                "content_length": int,
                "has_source_role": bool,
                "has_target_role": bool,
            }
        }
        Failure: {
            "valid": False,
            "errors": List[str],
            "details": {
                "document_type": str or None,
                "validation_errors": List[str],
            }
        }
    
    Note: This is a pure function. It does NOT:
    - Write any persistent state
    - Read from any other subsystem
    - Infer roles, permissions, or intent
    - Trigger any follow-up action
    - Store validation results
    """
    errors: List[str] = []
    details: Dict[str, Any] = {}
    
    # Validate input type
    if not isinstance(handoff_document, (dict, str)):
        return {
            "valid": False,
            "errors": [f"handoff_document must be dict or str, got {type(handoff_document).__name__}"],
            "details": {
                "document_type": document_type,
                "validation_errors": [f"Invalid input type: {type(handoff_document).__name__}"],
            },
        }
    
    # If string, try to parse as dict (minimal JSON-like structure)
    if isinstance(handoff_document, str):
        # For string input, validate it's non-empty
        if not handoff_document.strip():
            return {
                "valid": False,
                "errors": ["handoff_document string is empty"],
                "details": {
                    "document_type": document_type,
                    "validation_errors": ["Empty document content"],
                },
            }
        # String is valid as content, but we need structure
        # For minimal validation, accept string as valid content
        details["content_length"] = len(handoff_document)
        details["document_type"] = document_type or "unknown"
        
        # Validate document_type if provided
        if document_type:
            if document_type not in ["work_state", "presentation_state"]:
                errors.append(f"document_type must be 'work_state' or 'presentation_state', got '{document_type}'")
        
        if errors:
            return {
                "valid": False,
                "errors": errors,
                "details": {
                    "document_type": document_type,
                    "validation_errors": errors,
                },
            }
        
        return {
            "valid": True,
            "details": {
                "document_id": None,  # String input has no ID
                "document_type": document_type or "unknown",
                "content_length": len(handoff_document),
                "has_source_role": False,
                "has_target_role": False,
            },
        }
    
    # Validate dict structure
    if not isinstance(handoff_document, dict):
        return {
            "valid": False,
            "errors": [f"handoff_document must be dict, got {type(handoff_document).__name__}"],
            "details": {
                "document_type": document_type,
                "validation_errors": [f"Invalid input type: {type(handoff_document).__name__}"],
            },
        }
    
    # Required fields validation (document_type can be provided as parameter)
    required_fields = ["document_id", "content", "created_at"]
    for field in required_fields:
        if field not in handoff_document:
            errors.append(f"Missing required field: '{field}'")
    
    # document_type is required but can be in document or parameter
    if "document_type" not in handoff_document and not document_type:
        errors.append("document_type is required (either in document or as parameter)")
    
    # Validate document_id
    if "document_id" in handoff_document:
        doc_id = handoff_document["document_id"]
        if not isinstance(doc_id, str) or not doc_id.strip():
            errors.append("document_id must be a non-empty string")
        else:
            details["document_id"] = doc_id
    
    # Validate document_type
    if "document_type" in handoff_document:
        doc_type = handoff_document["document_type"]
        if not isinstance(doc_type, str):
            errors.append("document_type must be a string")
        elif doc_type not in ["work_state", "presentation_state"]:
            errors.append(f"document_type must be 'work_state' or 'presentation_state', got '{doc_type}'")
        else:
            details["document_type"] = doc_type
    elif document_type:
        # Use provided document_type if not in document
        if document_type not in ["work_state", "presentation_state"]:
            errors.append(f"document_type parameter must be 'work_state' or 'presentation_state', got '{document_type}'")
        else:
            details["document_type"] = document_type
    else:
        # document_type is required for dict input
        errors.append("document_type is required (either in document or as parameter)")
    
    # Validate content
    if "content" in handoff_document:
        content = handoff_document["content"]
        if not isinstance(content, str):
            errors.append("content must be a string")
        elif not content.strip():
            errors.append("content must be non-empty")
        else:
            details["content_length"] = len(content)
    else:
        errors.append("Missing required field: 'content'")
    
    # Validate created_at
    if "created_at" in handoff_document:
        created_at = handoff_document["created_at"]
        if isinstance(created_at, str):
            # Try to parse ISO format
            try:
                datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                errors.append("created_at must be a valid ISO format datetime string")
        elif isinstance(created_at, datetime):
            # datetime object is valid
            pass
        else:
            errors.append("created_at must be a datetime object or ISO format string")
    
    # Optional fields validation
    if "source_role" in handoff_document:
        source_role = handoff_document["source_role"]
        if source_role is not None and not isinstance(source_role, str):
            errors.append("source_role must be a string or None")
        else:
            details["has_source_role"] = source_role is not None and bool(source_role)
    else:
        details["has_source_role"] = False
    
    if "target_role" in handoff_document:
        target_role = handoff_document["target_role"]
        if target_role is not None and not isinstance(target_role, str):
            errors.append("target_role must be a string or None")
        else:
            details["has_target_role"] = target_role is not None and bool(target_role)
    else:
        details["has_target_role"] = False
    
    if "metadata" in handoff_document:
        metadata = handoff_document["metadata"]
        if metadata is not None and not isinstance(metadata, dict):
            errors.append("metadata must be a dict or None")
    
    # Return validation result
    if errors:
        return {
            "valid": False,
            "errors": errors,
            "details": {
                "document_type": details.get("document_type"),
                "validation_errors": errors,
            },
        }
    
    # Success: all validations passed
    return {
        "valid": True,
        "details": {
            "document_id": details.get("document_id"),
            "document_type": details.get("document_type"),
            "content_length": details.get("content_length", 0),
            "has_source_role": details.get("has_source_role", False),
            "has_target_role": details.get("has_target_role", False),
        },
    }

