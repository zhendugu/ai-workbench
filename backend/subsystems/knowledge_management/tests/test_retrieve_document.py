"""
Unit tests for C-KM-2: Retrieve Document

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.knowledge_management.storage import store_document, retrieve_document


def test_retrieve_document_success():
    """Test successful document retrieval (C-KM-2)."""
    # First, store a document to retrieve
    content = "Test document content for retrieval"
    metadata = {
        "title": "Test Document for Retrieval",
        "author": "Test Author",
        "category": "test",
    }
    
    store_result = store_document(content, metadata)
    assert "document_id" in store_result
    document_id = store_result["document_id"]
    
    # Now retrieve the document
    result = retrieve_document(document_id)
    
    # Verify success response structure
    assert "document_id" in result
    assert "content" in result
    assert "metadata" in result
    assert "version_number" in result
    assert "created_at" in result
    assert "updated_at" in result
    assert "error" not in result
    
    # Verify content matches
    assert result["document_id"] == document_id
    assert result["content"] == content
    assert result["metadata"] == metadata
    assert result["version_number"] == 1


def test_retrieve_document_failure():
    """Test document retrieval failure path (C-KM-2)."""
    # Test with non-existent document_id
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    
    result = retrieve_document(non_existent_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "FileNotFoundError"


if __name__ == "__main__":
    print("Running C-KM-2 unit tests...")
    
    try:
        test_retrieve_document_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_retrieve_document_failure()
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
    
    print("✅ All C-KM-2 tests passed")

