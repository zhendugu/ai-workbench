"""
Unit tests for C-OBS-5: Calculate Basic Metrics

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.observability.logging import record_task_log
from backend.subsystems.observability.metrics import calculate_basic_metrics


def test_calculate_basic_metrics_success():
    """Test successful basic metrics calculation (C-OBS-5)."""
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
    
    record_task_log(
        task_id="test_task_3",
        goal="Test goal 3",
        input_data={"test": "input3"},
        output_data={"test": "output3"},
        status="success",
        duration=150,
        cost_estimate=75,
    )
    
    # Calculate metrics
    result = calculate_basic_metrics(time_window=10)
    
    # Verify success response structure
    assert "time_range_start" in result
    assert "time_range_end" in result
    assert "total_count" in result
    assert "success_count" in result
    assert "failure_count" in result
    assert "success_rate" in result
    assert "avg_duration_ms" in result
    assert "time_window_desc" in result
    assert "generated_at" in result
    assert "error" not in result
    
    # Verify metrics are descriptive (not analysis)
    assert isinstance(result["total_count"], int)
    assert isinstance(result["success_count"], int)
    assert isinstance(result["failure_count"], int)
    assert isinstance(result["success_rate"], float)
    assert isinstance(result["avg_duration_ms"], float)
    assert result["total_count"] >= 0
    assert result["success_count"] >= 0
    assert result["failure_count"] >= 0
    assert 0.0 <= result["success_rate"] <= 1.0


def test_calculate_basic_metrics_failure():
    """Test basic metrics calculation failure path (C-OBS-5)."""
    # Test with invalid time_window
    result = calculate_basic_metrics(time_window=-1)  # Invalid time_window
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    
    # Verify it's a structured error, not a crash
    assert isinstance(result["error"], str)
    assert isinstance(result["error_type"], str)
    assert result["error_type"] == "ValueError"


if __name__ == "__main__":
    print("Running C-OBS-5 unit tests...")
    
    try:
        test_calculate_basic_metrics_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_calculate_basic_metrics_failure()
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
    
    print("✅ All C-OBS-5 tests passed")

