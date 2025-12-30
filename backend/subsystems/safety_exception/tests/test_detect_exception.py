"""
Unit tests for C-SAFE-3: Detect Exception

Minimal unit tests: success case (exception detected, no exception) and failure case.
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.exception_detection import detect_exception


def test_detect_exception_no_exception():
    """Test exception detection with no exception (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    execution_state = {
        "operation_count": 5,
        "max_operations": 100,
        "state": "valid_state",
        "valid_states": ["valid_state", "another_state"],
    }
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify success response structure
    assert "exception_detected" in result
    assert result["exception_detected"] is False
    assert result["component_id"] == component_id
    assert result["operation_type"] == operation_type
    assert "detected_at" in result
    assert "error" not in result


def test_detect_exception_dead_loop():
    """Test exception detection for dead loop (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    execution_state = {
        "operation_count": 150,
        "max_operations": 100,
        "recent_operations": ["op1", "op1", "op1"],
    }
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify exception detected
    assert "exception_detected" in result
    assert result["exception_detected"] is True
    assert result["exception_type"] == "dead_loop"
    assert "exception_id" in result
    assert "exception_details" in result
    assert "error" not in result


def test_detect_exception_invalid_state():
    """Test exception detection for invalid state (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    execution_state = {
        "state": "invalid_state",
        "valid_states": ["valid_state", "another_state"],
    }
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify exception detected
    assert "exception_detected" in result
    assert result["exception_detected"] is True
    assert result["exception_type"] == "invalid_state"
    assert "exception_id" in result
    assert "exception_details" in result
    assert "error" not in result


def test_detect_exception_timeout():
    """Test exception detection for timeout (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    start_time = datetime.utcnow() - timedelta(seconds=2)
    current_time = datetime.utcnow()
    execution_state = {
        "start_time": start_time.isoformat(),
        "current_time": current_time.isoformat(),
        "timeout_duration": 1000,  # 1 second timeout
    }
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify exception detected
    assert "exception_detected" in result
    assert result["exception_detected"] is True
    assert result["exception_type"] == "timeout"
    assert "exception_id" in result
    assert "exception_details" in result
    assert "error" not in result


def test_detect_exception_failure_budget_violation():
    """Test exception detection for failure budget violation (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    execution_state = {
        "failure_count": 15,
        "failure_budget": 10,
    }
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify exception detected
    assert "exception_detected" in result
    assert result["exception_detected"] is True
    assert result["exception_type"] == "failure_budget_violation"
    assert "exception_id" in result
    assert "exception_details" in result
    assert "error" not in result


def test_detect_exception_failure():
    """Test exception detection failure path (C-SAFE-3)."""
    # Test failure path by passing invalid component_id
    component_id = None
    operation_type = "test_operation"
    execution_state = {}
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "exception_detected" not in result


def test_detect_exception_empty_component_id():
    """Test exception detection with empty component_id (C-SAFE-3)."""
    component_id = ""
    operation_type = "test_operation"
    execution_state = {}
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "exception_detected" not in result


def test_detect_exception_invalid_execution_state():
    """Test exception detection with invalid execution_state (C-SAFE-3)."""
    component_id = "test_component_1"
    operation_type = "test_operation"
    execution_state = None  # Not a dict
    
    result = detect_exception(component_id, operation_type, execution_state)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "exception_detected" not in result

