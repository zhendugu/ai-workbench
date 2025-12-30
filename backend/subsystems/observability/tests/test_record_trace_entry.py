"""
Unit tests for C-OBS-2: Record Trace Entry

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.observability.tracing import record_trace_entry


def test_record_trace_entry_success():
    """Test successful trace entry recording (C-OBS-2)."""
    task_id = "test_task_123"
    decision_point = "Test decision point"
    tool_call = {
        "tool_name": "test_tool",
        "parameters": {"param1": "value1"},
    }
    handoff_document = "test_doc_123"
    
    result = record_trace_entry(
        task_id=task_id,
        decision_point=decision_point,
        tool_call=tool_call,
        handoff_document=handoff_document,
    )
    
    # Verify success response structure
    assert "trace_id" in result
    assert "task_id" in result
    assert "timestamp" in result
    assert "error" not in result
    
    # Verify trace ID and task ID
    assert result["task_id"] == task_id
    assert isinstance(result["trace_id"], str)
    assert isinstance(result["timestamp"], str)
    
    # Verify trace file was created
    trace_file = Path(f"backend/subsystems/observability/traces/{result['trace_id']}.json")
    assert trace_file.exists()


def test_record_trace_entry_failure():
    """Test trace entry recording failure path (C-OBS-2)."""
    # Test with invalid tool_call (not a dict)
    task_id = "test_task_456"
    decision_point = "Test decision point"
    tool_call = "invalid_tool_call"  # Should be a dict
    handoff_document = None
    
    result = record_trace_entry(
        task_id=task_id,
        decision_point=decision_point,
        tool_call=tool_call,
        handoff_document=handoff_document,
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
    print("Running C-OBS-2 unit tests...")
    
    try:
        test_record_trace_entry_success()
        print("✅ Success test passed")
    except Exception as e:
        print(f"❌ Success test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    try:
        test_record_trace_entry_failure()
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
    
    print("✅ All C-OBS-2 tests passed")

