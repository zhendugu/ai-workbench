"""
Unit tests for C-OBS-4: Query Task Log

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.observability.logging import (
    record_task_log,
    query_task_log,
)


def test_query_task_log_success():
    """Test successful task log query (C-OBS-4)."""
    # First, create some task logs
    record_task_log(
        task_id="test_task_1",
        goal="Test goal 1",
        input_data={"test": "input1"},
        output_data={"test": "output1"},
        status="success",
        duration=100,
        cost_estimate=50,
    )
    
    record_task_log(
        task_id="test_task_2",
        goal="Test goal 2",
        input_data={"test": "input2"},
        output_data={"test": "output2"},
        status="failure",
        duration=200,
        cost_estimate=100,
    )
    
    # Query by task_id
    result = query_task_log(task_id="test_task_1")
    
    # Verify success response structure
    assert "task_logs" in result
    assert "count" in result
    assert "error" not in result
    
    # Verify query results
    assert isinstance(result["task_logs"], list)
    assert result["count"] >= 1
    assert len(result["task_logs"]) == result["count"]
    
    # Verify log content (raw, unprocessed)
    if result["task_logs"]:
        log = result["task_logs"][0]
        assert "log_id" in log
        assert "task_id" in log
        assert log["task_id"] == "test_task_1"
    
    # Query by status
    result_status = query_task_log(status="failure")
    assert result_status["count"] >= 1
    assert all(log["status"] == "failure" for log in result_status["task_logs"])


def test_query_task_log_failure():
    """Test task log query failure path (C-OBS-4)."""
    # Test with invalid limit
    result = query_task_log(limit=-1)  # Invalid limit
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "ValueError"


if __name__ == "__main__":
    print("Running C-OBS-4 unit tests...")
    
    try:
        test_query_task_log_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_query_task_log_failure()
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
    
    print("✅ All C-OBS-4 tests passed")

