"""
Unit tests for C-HANDOFF-1: Validate Handoff Document

Test Requirements:
- Valid document
- Missing required fields
- Invalid structure
- Optional document_type handling
- Deterministic output (same input == same output)
"""

import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.handoff_protocol.validation import validate_handoff_document


def test_validate_handoff_document_valid():
    """Test valid handoff document validation."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "This is a valid handoff document content.",
        "created_at": "2025-12-26T15:30:00.000000",
        "source_role": "role-1",
        "target_role": "role-2",
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is True
    assert "details" in result
    assert result["details"]["document_id"] == "doc-123"
    assert result["details"]["document_type"] == "work_state"
    assert result["details"]["content_length"] > 0
    assert result["details"]["has_source_role"] is True
    assert result["details"]["has_target_role"] is True
    assert "errors" not in result


def test_validate_handoff_document_valid_presentation_state():
    """Test valid presentation_state document."""
    handoff_doc = {
        "document_id": "doc-456",
        "document_type": "presentation_state",
        "content": "Presentation content",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is True
    assert result["details"]["document_type"] == "presentation_state"
    assert result["details"]["has_source_role"] is False
    assert result["details"]["has_target_role"] is False


def test_validate_handoff_document_missing_required_fields():
    """Test missing required fields."""
    handoff_doc = {
        "document_id": "doc-123",
        # Missing document_type, content, created_at
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert len(result["errors"]) > 0
    assert any("document_type" in error.lower() for error in result["errors"])
    assert any("content" in error.lower() for error in result["errors"])
    assert any("created_at" in error.lower() for error in result["errors"])


def test_validate_handoff_document_missing_document_id():
    """Test missing document_id."""
    handoff_doc = {
        "document_type": "work_state",
        "content": "Content",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("document_id" in error.lower() for error in result["errors"])


def test_validate_handoff_document_invalid_document_type():
    """Test invalid document_type."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "invalid_type",
        "content": "Content",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("document_type" in error.lower() and "work_state" in error.lower() or "presentation_state" in error.lower() for error in result["errors"])


def test_validate_handoff_document_empty_content():
    """Test empty content."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("content" in error.lower() and "empty" in error.lower() for error in result["errors"])


def test_validate_handoff_document_invalid_created_at():
    """Test invalid created_at format."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "Content",
        "created_at": "invalid-date",
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("created_at" in error.lower() for error in result["errors"])


def test_validate_handoff_document_document_type_parameter():
    """Test document_type provided as parameter."""
    handoff_doc = {
        "document_id": "doc-123",
        "content": "Content",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = validate_handoff_document(handoff_doc, document_type="work_state")
    
    assert result["valid"] is True
    assert result["details"]["document_type"] == "work_state"


def test_validate_handoff_document_string_input():
    """Test string input (minimal validation)."""
    result = validate_handoff_document("This is a string document", document_type="work_state")
    
    assert result["valid"] is True
    assert result["details"]["content_length"] > 0
    assert result["details"]["document_type"] == "work_state"


def test_validate_handoff_document_empty_string():
    """Test empty string input."""
    result = validate_handoff_document("")
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("empty" in error.lower() for error in result["errors"])


def test_validate_handoff_document_invalid_input_type():
    """Test invalid input type."""
    result = validate_handoff_document(123)  # Not dict or string
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("dict or str" in error.lower() for error in result["errors"])


def test_validate_handoff_document_deterministic():
    """Test deterministic output (same input == same output)."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "Content",
        "created_at": "2025-12-26T15:30:00.000000",
    }
    
    result1 = validate_handoff_document(handoff_doc)
    result2 = validate_handoff_document(handoff_doc)
    
    assert result1 == result2
    assert result1["valid"] == result2["valid"]
    if "details" in result1:
        assert result1["details"] == result2["details"]


def test_validate_handoff_document_optional_fields():
    """Test optional fields (source_role, target_role, metadata)."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "Content",
        "created_at": datetime.utcnow().isoformat(),
        "source_role": None,
        "target_role": None,
        "metadata": None,
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is True
    assert result["details"]["has_source_role"] is False
    assert result["details"]["has_target_role"] is False


def test_validate_handoff_document_invalid_optional_fields():
    """Test invalid optional field types."""
    handoff_doc = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "Content",
        "created_at": datetime.utcnow().isoformat(),
        "source_role": 123,  # Invalid type
        "metadata": "not-a-dict",  # Invalid type
    }
    
    result = validate_handoff_document(handoff_doc)
    
    assert result["valid"] is False
    assert "errors" in result
    assert any("source_role" in error.lower() or "metadata" in error.lower() for error in result["errors"])

