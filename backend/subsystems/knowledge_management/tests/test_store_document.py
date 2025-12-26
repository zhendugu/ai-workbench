"""
Unit tests for C-KM-1: Store Document

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.knowledge_management.storage import store_document


def test_store_document_success():
    """Test successful document storage (C-KM-1)."""
    content = "Test document content"
    metadata = {
        "title": "Test Document",
        "author": "Test Author",
        "category": "test",
        "tags": ["test", "unit-test"],
    }
    
    result = store_document(content, metadata)
    
    # Verify success response structure
    assert "document_id" in result
    assert "version_number" in result
    assert "created_at" in result
    assert result["version_number"] == 1
    assert "error" not in result
    
    # Verify document_id is a valid UUID format
    assert len(result["document_id"]) == 36  # UUID format length
    assert result["document_id"].count("-") == 4


def test_store_document_failure():
    """Test document storage failure path (C-KM-1)."""
    # Test failure path by passing invalid metadata type
    # This should trigger an exception that is caught and returned as structured error
    
    content = "Valid content"
    # Pass invalid metadata type (not a dict) - this should cause a TypeError
    # when trying to create DocumentRecord
    metadata = None  # None is not a valid dict
    
    result = store_document(content, metadata)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)


if __name__ == "__main__":
    print("Running C-KM-1 unit tests...")
    
    try:
        test_store_document_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        sys.exit(1)
    
    try:
        test_store_document_failure()
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
    
    print("✅ All C-KM-1 tests passed")

