"""
Unit tests for C-KM-3: Check Access Permission

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.knowledge_management.storage import (
    store_document,
    check_access_permission,
)


def test_check_access_permission_success():
    """Test successful access permission check (C-KM-3)."""
    # First, store a document
    content = "Test document content for access check"
    metadata = {
        "title": "Test Document for Access Check",
        "author": "Test Author",
    }
    
    store_result = store_document(content, metadata)
    document_id = store_result["document_id"]
    
    # Test with no access control rules - should return denied
    result = check_access_permission(document_id, "test_requester", "read")
    
    # Verify success response structure
    assert "permission_status" in result
    assert "permission_reason" in result
    assert "error" not in result
    
    # Verify permission status is valid
    assert result["permission_status"] in ["read_allowed", "write_allowed", "denied"]
    assert isinstance(result["permission_reason"], str)
    
    # With no rules, should return denied (no default allow behavior)
    assert result["permission_status"] == "denied"
    assert "No access control rule found" in result["permission_reason"]


def test_check_access_permission_failure():
    """Test access permission check failure path (C-KM-3)."""
    # Test with non-existent document_id
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    
    result = check_access_permission(non_existent_id, "test_requester", "read")
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "FileNotFoundError"


if __name__ == "__main__":
    print("Running C-KM-3 unit tests...")
    
    try:
        test_check_access_permission_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_check_access_permission_failure()
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
    
    print("✅ All C-KM-3 tests passed")

