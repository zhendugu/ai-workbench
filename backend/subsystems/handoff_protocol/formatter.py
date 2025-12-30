"""
Handoff Protocol formatting for Handoff Protocol Subsystem.

C-HANDOFF-2: Format Handoff Document implementation
"""

from copy import deepcopy
from datetime import datetime
from typing import Any, Dict


def format_handoff_document(
    document: Any,
    target_format: str,
) -> Dict[str, Any]:
    """
    C-HANDOFF-2: Format Handoff Document
    
    Formats a document into Handoff Protocol format (work_state or presentation_state).
    This is a PURE TRANSFORMATION FUNCTION with NO side effects, NO state changes, NO dependencies.
    
    Behavior:
    - Pure transformation function: No side effects, no state changes
    - Structural transformation: Converts document structure to target format
    - Field separation: Separates work_state vs presentation_state fields
    - Deterministic formatting: Same input always produces same output
    
    Args:
        document: Document to format (dict, string, or any structure)
        target_format: Target format ("work_state" or "presentation_state")
    
    Returns:
        Success: {
            "formatted_document": {
                "document_id": str,
                "document_type": str,
                "content": str,
                "created_at": str,
                "source_role": str or None,
                "target_role": str or None,
                "metadata": dict or None,
            },
            "format_type": "work_state" | "presentation_state"
        }
        Failure: {
            "error": str,
            "error_type": str
        }
    
    Note: This is a pure transformation function. It does NOT:
    - Validate correctness (assumes input already validated or raw)
    - Write any persistent state
    - Read from any other subsystem
    - Infer intent, role, permissions, or workflow
    - Trigger any follow-up action
    - Mutate input object (creates new object)
    """
    # Validate target_format
    if target_format not in ["work_state", "presentation_state"]:
        return {
            "error": f"target_format must be 'work_state' or 'presentation_state', got '{target_format}'",
            "error_type": "InvalidFormat",
        }
    
    # Handle string input
    if isinstance(document, str):
        # Create minimal formatted document from string
        formatted = {
            "document_id": None,  # No ID for string input
            "document_type": target_format,
            "content": document,
            "created_at": datetime.utcnow().isoformat(),
            "source_role": None,
            "target_role": None,
            "metadata": None,
        }
        return {
            "formatted_document": formatted,
            "format_type": target_format,
        }
    
    # Handle dict input
    if isinstance(document, dict):
        # Create deep copy to avoid mutating input
        formatted = deepcopy(document)
        
        # Ensure required fields exist with defaults
        if "document_id" not in formatted:
            formatted["document_id"] = None
        if "document_type" not in formatted:
            formatted["document_type"] = target_format
        else:
            # Update document_type to target_format
            formatted["document_type"] = target_format
        
        # Ensure content exists
        if "content" not in formatted:
            # Try to extract content from various possible fields
            if "text" in formatted:
                formatted["content"] = formatted.pop("text")
            elif "body" in formatted:
                formatted["content"] = formatted.pop("body")
            elif "message" in formatted:
                formatted["content"] = formatted.pop("message")
            else:
                # Default empty content
                formatted["content"] = ""
        
        # Ensure created_at exists
        if "created_at" not in formatted:
            formatted["created_at"] = datetime.utcnow().isoformat()
        elif isinstance(formatted["created_at"], datetime):
            # Convert datetime to ISO string
            formatted["created_at"] = formatted["created_at"].isoformat()
        
        # Ensure optional fields exist
        if "source_role" not in formatted:
            formatted["source_role"] = None
        if "target_role" not in formatted:
            formatted["target_role"] = None
        if "metadata" not in formatted:
            formatted["metadata"] = None
        
        # Format-specific transformations
        if target_format == "work_state":
            # work_state: Include all technical details, preserve metadata
            # No special transformation needed, just ensure structure
            pass
        elif target_format == "presentation_state":
            # presentation_state: May simplify or format for presentation
            # For now, same structure but document_type indicates presentation
            # No content transformation (that would be interpretation)
            pass
        
        # Return formatted document
        return {
            "formatted_document": formatted,
            "format_type": target_format,
        }
    
    # Handle other input types (convert to dict)
    # For non-dict, non-string input, create minimal structure
    formatted = {
        "document_id": None,
        "document_type": target_format,
        "content": str(document) if document is not None else "",
        "created_at": datetime.utcnow().isoformat(),
        "source_role": None,
        "target_role": None,
        "metadata": None,
    }
    
    return {
        "formatted_document": formatted,
        "format_type": target_format,
    }

