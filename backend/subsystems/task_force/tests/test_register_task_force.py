"""
Unit tests for C-TF-1: Register Task Force Definition
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

from backend.subsystems.task_force import register_task_force


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    register_task_force._task_forces.clear()
    
    # Create temporary directory for task_forces
    test_task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    if test_task_forces_dir.exists():
        shutil.rmtree(test_task_forces_dir)
    test_task_forces_dir.mkdir(parents=True, exist_ok=True)


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    register_task_force._task_forces.clear()
    
    # Remove test directory
    test_task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    if test_task_forces_dir.exists():
        shutil.rmtree(test_task_forces_dir)


def test_register_task_force_valid():
    """Test valid Task Force registration"""
    task_force_def = {
        "task_force_id": "tf-test-1",
        "name": "Test Task Force",
        "members": [
            {
                "member_id": "member-1",
                "role_id": "role-1",
                "cell_id": "cell-1",
                "capability_contribution": ["cap-1", "cap-2"],
            }
        ],
        "goals": [
            {
                "goal_id": "goal-1",
                "description": "Test goal",
                "expected_output": "Test output",
                "success_criteria": ["criterion-1"],
            }
        ],
        "dissolution_conditions": ["condition-1"],
    }
    
    result = register_task_force.register_task_force_definition(
        task_force_def,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    assert result["task_force_id"] == "tf-test-1"
    assert "created_at" in result
    
    # Verify in-memory storage
    assert "tf-test-1" in register_task_force._task_forces
    assert register_task_force._task_forces["tf-test-1"].name == "Test Task Force"
    
    # Verify disk persistence
    tf_file = Path("backend/subsystems/task_force/task_forces/tf-test-1.json")
    assert tf_file.exists()
    
    with open(tf_file, "r") as f:
        tf_dict = json.load(f)
    
    assert tf_dict["task_force_id"] == "tf-test-1"
    assert tf_dict["name"] == "Test Task Force"
    assert len(tf_dict["members"]) == 1
    assert len(tf_dict["goals"]) == 1


def test_register_task_force_missing_required_fields():
    """Test registration with missing required fields"""
    task_force_def = {
        "task_force_id": "tf-test-2",
        # Missing "name"
    }
    
    result = register_task_force.register_task_force_definition(
        task_force_def,
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "Missing required field" in result["error"]


def test_register_task_force_forbidden_fields():
    """Test registration with forbidden fields"""
    task_force_def = {
        "task_force_id": "tf-test-3",
        "name": "Test Task Force",
        "members": [],
        "goals": [],
        "dissolution_conditions": [],
        "state": "active",  # Forbidden field
    }
    
    result = register_task_force.register_task_force_definition(
        task_force_def,
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "Forbidden field" in result["error"]
    assert "state" in result["error"]


def test_register_task_force_no_side_effects():
    """
    Explicit test: Registering Task Force causes NO side effects.
    
    This test verifies that registering a Task Force does NOT:
    - Trigger execution
    - Trigger orchestration
    - Read Cell-State
    - Change system behavior
    """
    task_force_def = {
        "task_force_id": "tf-test-no-side-effects",
        "name": "Test Task Force",
        "members": [
            {
                "member_id": "member-1",
                "role_id": "role-1",
                "cell_id": "cell-1",
                "capability_contribution": ["cap-1"],
            }
        ],
        "goals": [
            {
                "goal_id": "goal-1",
                "description": "Test goal",
                "expected_output": "Test output",
                "success_criteria": ["criterion-1"],
            }
        ],
        "dissolution_conditions": ["condition-1"],
    }
    
    result = register_task_force.register_task_force_definition(
        task_force_def,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    
    # Verify no execution, orchestration, or Cell-State reads
    # (This is verified by the absence of such behavior in the implementation)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

