"""
Unit tests for C-HANDOFF-2: Format Handoff Document

Test Requirements:
- work_state formatting
- presentation_state formatting
- deterministic output
- invalid target_format handling
- no mutation of input object
"""

import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.handoff_protocol.formatter import format_handoff_document


def test_format_handoff_document_work_state():
    """Test work_state formatting."""
    document = {
        "document_id": "doc-123",
        "document_type": "work_state",
        "content": "Work state content",
        "created_at": "2025-12-26T15:30:00.000000",
        "source_role": "role-1",
        "target_role": "role-2",
    }
    
    result = format_handoff_document(document, "work_state")
    
    assert "formatted_document" in result
    assert result["format_type"] == "work_state"
    assert result["formatted_document"]["document_id"] == "doc-123"
    assert result["formatted_document"]["document_type"] == "work_state"
    assert result["formatted_document"]["content"] == "Work state content"
    assert "error" not in result


def test_format_handoff_document_presentation_state():
    """Test presentation_state formatting."""
    document = {
        "document_id": "doc-456",
        "document_type": "work_state",
        "content": "Original content",
        "created_at": "2025-12-26T15:30:00.000000",
    }
    
    result = format_handoff_document(document, "presentation_state")
    
    assert "formatted_document" in result
    assert result["format_type"] == "presentation_state"
    assert result["formatted_document"]["document_type"] == "presentation_state"
    assert result["formatted_document"]["content"] == "Original content"
    assert "error" not in result


def test_format_handoff_document_deterministic():
    """Test deterministic output (same input == same output)."""
    document = {
        "document_id": "doc-123",
        "content": "Test content",
        "created_at": "2025-12-26T15:30:00.000000",
    }
    
    result1 = format_handoff_document(document, "work_state")
    result2 = format_handoff_document(document, "work_state")
    
    # Compare structure (created_at may differ if not provided)
    assert result1["format_type"] == result2["format_type"]
    assert result1["formatted_document"]["document_id"] == result2["formatted_document"]["document_id"]
    assert result1["formatted_document"]["document_type"] == result2["formatted_document"]["document_type"]
    assert result1["formatted_document"]["content"] == result2["formatted_document"]["content"]


def test_format_handoff_document_invalid_target_format():
    """Test invalid target_format handling."""
    document = {
        "document_id": "doc-123",
        "content": "Content",
    }
    
    result = format_handoff_document(document, "invalid_format")
    
    assert "error" in result
    assert result["error_type"] == "InvalidFormat"
    assert "work_state" in result["error"] or "presentation_state" in result["error"]
    assert "formatted_document" not in result


def test_format_handoff_document_no_mutation():
    """Test that input object is not mutated."""
    original_doc = {
        "document_id": "doc-123",
        "content": "Original content",
        "created_at": "2025-12-26T15:30:00.000000",
        "metadata": {"key": "value"},
    }
    
    # Create a copy for comparison
    original_copy = {
        "document_id": "doc-123",
        "content": "Original content",
        "created_at": "2025-12-26T15:30:00.000000",
        "metadata": {"key": "value"},
    }
    
    result = format_handoff_document(original_doc, "work_state")
    
    # Verify original document is unchanged
    assert original_doc == original_copy
    assert original_doc["document_id"] == "doc-123"
    assert original_doc["content"] == "Original content"
    assert original_doc["metadata"]["key"] == "value"
    
    # Verify formatted document is different object
    assert result["formatted_document"] is not original_doc


def test_format_handoff_document_string_input():
    """Test string input formatting."""
    result = format_handoff_document("Simple string content", "work_state")
    
    assert "formatted_document" in result
    assert result["format_type"] == "work_state"
    assert result["formatted_document"]["content"] == "Simple string content"
    assert result["formatted_document"]["document_type"] == "work_state"
    assert result["formatted_document"]["document_id"] is None


def test_format_handoff_document_missing_fields():
    """Test formatting with missing fields (should add defaults)."""
    document = {
        "content": "Content only",
    }
    
    result = format_handoff_document(document, "presentation_state")
    
    assert "formatted_document" in result
    assert result["formatted_document"]["content"] == "Content only"
    assert result["formatted_document"]["document_type"] == "presentation_state"
    assert "document_id" in result["formatted_document"]
    assert "created_at" in result["formatted_document"]
    assert result["formatted_document"]["source_role"] is None
    assert result["formatted_document"]["target_role"] is None


def test_format_handoff_document_alternative_content_fields():
    """Test formatting with alternative content field names."""
    # Test with "text" field
    doc1 = {"text": "Text content"}
    result1 = format_handoff_document(doc1, "work_state")
    assert result1["formatted_document"]["content"] == "Text content"
    
    # Test with "body" field
    doc2 = {"body": "Body content"}
    result2 = format_handoff_document(doc2, "work_state")
    assert result2["formatted_document"]["content"] == "Body content"
    
    # Test with "message" field
    doc3 = {"message": "Message content"}
    result3 = format_handoff_document(doc3, "work_state")
    assert result3["formatted_document"]["content"] == "Message content"


def test_format_handoff_document_datetime_object():
    """Test formatting with datetime object in created_at."""
    document = {
        "content": "Content",
        "created_at": datetime(2025, 12, 26, 15, 30, 0),
    }
    
    result = format_handoff_document(document, "work_state")
    
    assert "formatted_document" in result
    # created_at should be converted to ISO string
    assert isinstance(result["formatted_document"]["created_at"], str)
    assert "2025-12-26" in result["formatted_document"]["created_at"]


def test_format_handoff_document_none_input():
    """Test formatting with None input."""
    result = format_handoff_document(None, "work_state")
    
    assert "formatted_document" in result
    assert result["formatted_document"]["content"] == ""
    assert result["formatted_document"]["document_type"] == "work_state"


def test_format_handoff_document_preserves_metadata():
    """Test that metadata is preserved during formatting."""
    document = {
        "content": "Content",
        "metadata": {"key1": "value1", "key2": "value2"},
    }
    
    result = format_handoff_document(document, "work_state")
    
    assert "formatted_document" in result
    assert result["formatted_document"]["metadata"] == {"key1": "value1", "key2": "value2"}


def test_format_handoff_document_type_conversion():
    """Test that document_type is updated to target_format."""
    document = {
        "document_id": "doc-123",
        "document_type": "work_state",  # Original type
        "content": "Content",
    }
    
    result = format_handoff_document(document, "presentation_state")
    
    assert result["formatted_document"]["document_type"] == "presentation_state"
    # Original document should be unchanged
    assert document["document_type"] == "work_state"

