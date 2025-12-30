"""
Unit tests for C-EXEC-1: Execute Single Action (DRY-RUN / NO-OP)

Minimal unit tests: success case and failure cases.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.execution import execute_single_action_dry_run


def test_execute_single_action_dry_run_success():
    """Test successful dry-run execution (C-EXEC-1)."""
    action_identifier = "store_document"
    target_subsystem = "knowledge_management"
    action_parameters = {
        "content": "Test document content",
        "metadata": {"title": "Test Document"},
    }
    requested_by = "test_user_1"
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify success response structure
    assert "execution_mode" in result
    assert result["execution_mode"] == "dry_run"
    assert "execution_id" in result
    assert "action_identifier" in result
    assert "target_subsystem" in result
    assert "would_execute" in result
    assert "blocked_reason" in result
    assert result["blocked_reason"] == "dry_run_mode"
    assert "execution_preview" in result
    assert "timestamp" in result
    assert "error" not in result
    
    # Verify execution_id is a valid UUID format
    assert len(result["execution_id"]) == 36  # UUID format length
    assert result["execution_id"].count("-") == 4
    
    # Verify execution_preview structure
    preview = result["execution_preview"]
    assert preview["execution_blocked"] is True
    assert preview["blocked_reason"] == "dry_run_mode"
    assert "note" in preview


def test_execute_single_action_dry_run_different_subsystems():
    """Test dry-run execution with different target subsystems (C-EXEC-1)."""
    test_cases = [
        ("record_task_log", "observability", {"task_id": "test_task", "goal": "test"}),
        ("execute_health_check", "safety_exception", {"component_id": "test_component"}),
    ]
    
    for action_identifier, target_subsystem, action_parameters in test_cases:
        requested_by = "test_user_1"
        
        result = execute_single_action_dry_run(
            action_identifier, target_subsystem, action_parameters, requested_by
        )
        
        assert result["execution_mode"] == "dry_run"
        assert result["action_identifier"] == action_identifier
        assert result["target_subsystem"] == target_subsystem
        assert result["blocked_reason"] == "dry_run_mode"
        assert "error" not in result


def test_execute_single_action_dry_run_invalid_action_identifier():
    """Test dry-run execution with invalid action_identifier (C-EXEC-1)."""
    action_identifier = None
    target_subsystem = "knowledge_management"
    action_parameters = {}
    requested_by = "test_user_1"
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "execution_id" not in result


def test_execute_single_action_dry_run_empty_action_identifier():
    """Test dry-run execution with empty action_identifier (C-EXEC-1)."""
    action_identifier = ""
    target_subsystem = "knowledge_management"
    action_parameters = {}
    requested_by = "test_user_1"
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "execution_id" not in result


def test_execute_single_action_dry_run_invalid_target_subsystem():
    """Test dry-run execution with invalid target_subsystem (C-EXEC-1)."""
    action_identifier = "test_action"
    target_subsystem = "invalid_subsystem"
    action_parameters = {}
    requested_by = "test_user_1"
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "invalid_subsystem" in result["error"] or "target_subsystem" in result["error"]
    assert "execution_id" not in result


def test_execute_single_action_dry_run_invalid_action_parameters():
    """Test dry-run execution with invalid action_parameters (C-EXEC-1)."""
    action_identifier = "test_action"
    target_subsystem = "knowledge_management"
    action_parameters = None  # Not a dict
    requested_by = "test_user_1"
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "execution_id" not in result


def test_execute_single_action_dry_run_empty_requested_by():
    """Test dry-run execution with empty requested_by (C-EXEC-1)."""
    action_identifier = "test_action"
    target_subsystem = "knowledge_management"
    action_parameters = {}
    requested_by = ""
    
    result = execute_single_action_dry_run(
        action_identifier, target_subsystem, action_parameters, requested_by
    )
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "execution_id" not in result

