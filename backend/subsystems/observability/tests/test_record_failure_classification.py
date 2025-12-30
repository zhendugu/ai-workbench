"""
Unit tests for C-OBS-3: Record Failure Classification

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.observability.failure_classification import record_failure_classification


def test_record_failure_classification_success():
    """Test successful failure classification recording (C-OBS-3)."""
    task_id = "test_task_123"
    failure_reason = "Task execution timeout"
    failure_category = "timeout"
    
    result = record_failure_classification(
        task_id=task_id,
        failure_reason=failure_reason,
        failure_category=failure_category,
    )
    
    # Verify success response structure
    assert "classification_id" in result
    assert "task_id" in result
    assert "classified_at" in result
    assert "error" not in result
    
    # Verify classification ID and task ID
    assert result["task_id"] == task_id
    assert isinstance(result["classification_id"], str)
    assert isinstance(result["classified_at"], str)
    
    # Verify classification file was created
    classification_file = Path(f"backend/subsystems/observability/classifications/{result['classification_id']}.json")
    assert classification_file.exists()


def test_record_failure_classification_failure():
    """Test failure classification recording failure path (C-OBS-3)."""
    # Test with empty task_id
    task_id = ""  # Empty task_id should fail
    failure_reason = "Test failure reason"
    failure_category = "system_error"
    
    result = record_failure_classification(
        task_id=task_id,
        failure_reason=failure_reason,
        failure_category=failure_category,
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "ValueError"


if __name__ == "__main__":
    print("Running C-OBS-3 unit tests...")
    
    try:
        test_record_failure_classification_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_record_failure_classification_failure()
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
    
    print("✅ All C-OBS-3 tests passed")

