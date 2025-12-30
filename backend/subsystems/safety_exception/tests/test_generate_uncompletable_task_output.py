"""
Unit tests for C-SAFE-4: Generate Standard Output for Uncompletable Task

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.task_output import generate_uncompletable_task_output


def test_generate_uncompletable_task_output_success():
    """Test successful task output generation (C-SAFE-4)."""
    task_id = "test_task_1"
    failure_reason = "Task execution timeout exceeded"
    
    result = generate_uncompletable_task_output(task_id, failure_reason)
    
    # Verify success response structure
    assert "output_id" in result
    assert "task_id" in result
    assert "reason" in result
    assert "suggestions" in result
    assert "risk_warnings" in result
    assert "generated_at" in result
    assert result["task_id"] == task_id
    assert result["reason"] == failure_reason
    assert isinstance(result["suggestions"], list)
    assert isinstance(result["risk_warnings"], list)
    assert len(result["suggestions"]) > 0
    assert len(result["risk_warnings"]) > 0
    assert "error" not in result
    
    # Verify output_id is a valid UUID format
    assert len(result["output_id"]) == 36  # UUID format length
    assert result["output_id"].count("-") == 4


def test_generate_uncompletable_task_output_descriptive_only():
    """Test that suggestions and risk_warnings are descriptive only (C-SAFE-4)."""
    task_id = "test_task_2"
    failure_reason = "Invalid state detected"
    
    result = generate_uncompletable_task_output(task_id, failure_reason)
    
    # Verify suggestions are descriptive (not action recommendations)
    suggestions = result["suggestions"]
    for suggestion in suggestions:
        # Should describe what happened, not what to do
        assert not suggestion.lower().startswith(("should", "must", "need to", "you should", "please"))
        assert not suggestion.lower().endswith(("action", "recommendation", "advice"))
    
    # Verify risk_warnings are descriptive (not action recommendations)
    risk_warnings = result["risk_warnings"]
    for warning in risk_warnings:
        # Should describe what risks exist, not what to avoid
        assert not warning.lower().startswith(("should", "must", "need to", "you should", "please"))
        assert not warning.lower().endswith(("action", "recommendation", "advice"))


def test_generate_uncompletable_task_output_different_reasons():
    """Test task output generation with different failure reasons (C-SAFE-4)."""
    test_cases = [
        ("test_task_timeout", "Operation timeout exceeded"),
        ("test_task_invalid", "Invalid state detected"),
        ("test_task_dead_loop", "Dead loop condition detected"),
        ("test_task_failure_budget", "Failure budget violation"),
        ("test_task_permission", "Permission denied"),
        ("test_task_conflict", "Knowledge conflict detected"),
        ("test_task_generic", "Generic failure reason"),
    ]
    
    for task_id, failure_reason in test_cases:
        result = generate_uncompletable_task_output(task_id, failure_reason)
        
        assert "output_id" in result
        assert result["task_id"] == task_id
        assert result["reason"] == failure_reason
        assert len(result["suggestions"]) > 0
        assert len(result["risk_warnings"]) > 0
        assert "error" not in result


def test_generate_uncompletable_task_output_failure():
    """Test task output generation failure path (C-SAFE-4)."""
    # Test failure path by passing invalid task_id
    task_id = None
    failure_reason = "Test failure reason"
    
    result = generate_uncompletable_task_output(task_id, failure_reason)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    assert result["error_type"] == "ValueError"
    assert "output_id" not in result


def test_generate_uncompletable_task_output_empty_task_id():
    """Test task output generation with empty task_id (C-SAFE-4)."""
    task_id = ""
    failure_reason = "Test failure reason"
    
    result = generate_uncompletable_task_output(task_id, failure_reason)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "output_id" not in result


def test_generate_uncompletable_task_output_empty_failure_reason():
    """Test task output generation with empty failure_reason (C-SAFE-4)."""
    task_id = "test_task_3"
    failure_reason = ""
    
    result = generate_uncompletable_task_output(task_id, failure_reason)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "output_id" not in result

