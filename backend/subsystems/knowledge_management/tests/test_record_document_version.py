"""
Unit tests for C-KM-5: Record Document Version

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.knowledge_management.storage import (
    store_document,
    record_document_version,
    retrieve_document,
)


def test_record_document_version_success():
    """Test successful document version recording (C-KM-5)."""
    # First, store a document
    content = "Original document content"
    metadata = {
        "title": "Original Document",
        "author": "Original Author",
    }
    
    store_result = store_document(content, metadata)
    document_id = store_result["document_id"]
    
    # Record a new version
    new_content = "Updated document content version 2"
    result = record_document_version(document_id, new_content, created_by="test_user")
    
    # Verify success response structure
    assert "version_id" in result
    assert "document_id" in result
    assert "version_number" in result
    assert "created_at" in result
    assert "error" not in result
    
    # Verify version information
    assert result["document_id"] == document_id
    assert result["version_number"] == 2  # Should be version 2 (original was version 1)
    assert isinstance(result["version_id"], str)
    assert isinstance(result["created_at"], str)
    
    # Verify document was updated with new content
    retrieved = retrieve_document(document_id)
    assert retrieved["content"] == new_content
    assert retrieved["version_number"] == 2


def test_record_document_version_failure():
    """Test document version recording failure path (C-KM-5)."""
    # Test with non-existent document_id
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    new_content = "New version content"
    
    result = record_document_version(non_existent_id, new_content)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "FileNotFoundError"


if __name__ == "__main__":
    print("Running C-KM-5 unit tests...")
    
    try:
        test_record_document_version_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_record_document_version_failure()
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
    
    print("✅ All C-KM-5 tests passed")

