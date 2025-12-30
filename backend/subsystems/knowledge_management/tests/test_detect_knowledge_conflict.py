"""
Unit tests for C-KM-4: Detect Knowledge Conflict

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.knowledge_management.storage import (
    store_document,
    detect_knowledge_conflict,
)


def test_detect_knowledge_conflict_success():
    """Test successful knowledge conflict detection (C-KM-4)."""
    # First, store a document
    content = "Original document content"
    metadata = {
        "title": "Original Document",
        "author": "Original Author",
    }
    
    store_result = store_document(content, metadata)
    document_id = store_result["document_id"]
    
    # Test with conflicting content
    new_content = "Modified document content"
    result = detect_knowledge_conflict(new_content, document_id)
    
    # Verify success response structure
    assert "conflict_detected" in result
    assert "error" not in result
    
    # Verify conflict was detected
    assert result["conflict_detected"] is True
    assert "conflict_id" in result
    assert "conflict_type" in result
    assert "conflicting_fields" in result
    assert "conflicting_values" in result
    assert "detected_at" in result
    
    # Verify conflict details
    assert result["conflict_type"] == "content_conflict"
    assert "content" in result["conflicting_fields"]
    assert len(result["conflicting_values"]) > 0


def test_detect_knowledge_conflict_failure():
    """Test knowledge conflict detection failure path (C-KM-4)."""
    # Test with non-existent document_id
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    content = "Test content"
    
    result = detect_knowledge_conflict(content, non_existent_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "FileNotFoundError"


if __name__ == "__main__":
    print("Running C-KM-4 unit tests...")
    
    try:
        test_detect_knowledge_conflict_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_detect_knowledge_conflict_failure()
        print("✅ Failure test passed")
    except AssertionError as e:
        print(f"❌ Failure test assertion failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failure test failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("✅ All C-KM-4 tests passed")

