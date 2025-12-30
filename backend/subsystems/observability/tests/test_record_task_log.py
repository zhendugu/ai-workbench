"""
Unit tests for C-OBS-1: Record Task Log

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.observability.logging import record_task_log


def test_record_task_log_success():
    """Test successful task log recording (C-OBS-1)."""
    task_id = "test_task_123"
    goal = "Test task goal"
    input_data = {"test": "input"}
    output_data = {"test": "output"}
    status = "success"
    duration = 100
    cost_estimate = 50
    
    result = record_task_log(
        task_id=task_id,
        goal=goal,
        input_data=input_data,
        output_data=output_data,
        status=status,
        duration=duration,
        cost_estimate=cost_estimate,
    )
    
    # Verify success response structure
    assert "log_id" in result
    assert "task_id" in result
    assert "created_at" in result
    assert "error" not in result
    
    # Verify log ID and task ID
    assert result["task_id"] == task_id
    assert isinstance(result["log_id"], str)
    assert isinstance(result["created_at"], str)
    
    # Verify log file was created
    log_file = Path(f"backend/subsystems/observability/logs/{result['log_id']}.json")
    assert log_file.exists()


def test_record_task_log_failure():
    """Test task log recording failure path (C-OBS-1)."""
    # Test with invalid status
    task_id = "test_task_456"
    goal = "Test task goal"
    input_data = {"test": "input"}
    output_data = {"test": "output"}
    status = "invalid_status"  # Invalid status
    duration = 100
    cost_estimate = 50
    
    result = record_task_log(
        task_id=task_id,
        goal=goal,
        input_data=input_data,
        output_data=output_data,
        status=status,
        duration=duration,
        cost_estimate=cost_estimate,
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
    print("Running C-OBS-1 unit tests...")
    
    try:
        test_record_task_log_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_record_task_log_failure()
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
    
    print("✅ All C-OBS-1 tests passed")

