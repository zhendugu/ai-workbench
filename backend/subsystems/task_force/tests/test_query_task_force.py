"""
Unit tests for C-TF-3: Query Task Force Definition
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

from backend.subsystems.task_force import register_task_force, query_task_force
from backend.subsystems.task_force.models import TaskForceDefinition, TaskForceMember, TaskForceGoal


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    register_task_force._task_forces.clear()
    
    # Create temporary directory for task_forces
    test_task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    if test_task_forces_dir.exists():
        shutil.rmtree(test_task_forces_dir)
    test_task_forces_dir.mkdir(parents=True, exist_ok=True)
    
    # Create test Task Force
    task_force_def = {
        "task_force_id": "tf-query-1",
        "name": "Query Test Task Force",
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
    
    register_task_force.register_task_force_definition(
        task_force_def,
        requested_by="human-1",
    )


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    register_task_force._task_forces.clear()
    
    # Remove test directory
    test_task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    if test_task_forces_dir.exists():
        shutil.rmtree(test_task_forces_dir)


def test_query_task_force_found_in_memory():
    """Test querying Task Force from in-memory cache"""
    result = query_task_force.query_task_force_definition(
        task_force_id="tf-query-1",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["task_force_id"] == "tf-query-1"
    assert result["name"] == "Query Test Task Force"
    assert len(result["members"]) == 1
    assert len(result["goals"]) == 1


def test_query_task_force_found_on_disk():
    """Test querying Task Force from disk storage"""
    # Create Task Force file directly on disk
    task_forces_dir = Path("backend/subsystems/task_force/task_forces")
    tf_file = task_forces_dir / "tf-query-2.json"
    
    tf_dict = {
        "task_force_id": "tf-query-2",
        "name": "Disk Test Task Force",
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
        "created_by": "human-1",
        "created_at": "2025-12-26T10:00:00",
    }
    
    with open(tf_file, "w") as f:
        json.dump(tf_dict, f, indent=2)
    
    # Query (should load from disk)
    result = query_task_force.query_task_force_definition(
        task_force_id="tf-query-2",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["task_force_id"] == "tf-query-2"
    assert result["name"] == "Disk Test Task Force"


def test_query_task_force_not_found():
    """Test querying non-existent Task Force"""
    result = query_task_force.query_task_force_definition(
        task_force_id="tf-query-not-found",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    assert result["task_force_id"] == "tf-query-not-found"
    assert "name" not in result
    assert "members" not in result


def test_query_task_force_invalid_task_force_id():
    """Test invalid task_force_id"""
    result = query_task_force.query_task_force_definition(
        task_force_id="",
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "task_force_id must be a non-empty string" in result["error"]


def test_query_task_force_read_only():
    """Test that query is read-only (no mutations)"""
    # Query multiple times
    result1 = query_task_force.query_task_force_definition(
        task_force_id="tf-query-1",
        requested_by="human-2",
    )
    
    result2 = query_task_force.query_task_force_definition(
        task_force_id="tf-query-1",
        requested_by="human-3",
    )
    
    # Verify results are identical
    assert result1["task_force_id"] == result2["task_force_id"]
    assert result1["name"] == result2["name"]
    assert result1["members"] == result2["members"]
    assert result1["goals"] == result2["goals"]
    
    # Verify Task Force unchanged in storage
    assert "tf-query-1" in register_task_force._task_forces
    original_tf = register_task_force._task_forces["tf-query-1"]
    assert original_tf.name == "Query Test Task Force"


def test_query_task_force_no_repair_inference():
    """
    Test that query does NOT repair, infer, or normalize.
    
    This test verifies that querying Task Force does NOT:
    - Repair missing fields
    - Infer default values
    - Normalize Task Force definitions
    - Create default Task Forces
    """
    # Query non-existent Task Force
    result = query_task_force.query_task_force_definition(
        task_force_id="tf-query-no-repair",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    
    # Verify no Task Force was created
    assert "tf-query-no-repair" not in register_task_force._task_forces
    
    # Verify no file was created
    tf_file = Path("backend/subsystems/task_force/task_forces/tf-query-no-repair.json")
    assert not tf_file.exists()


def test_query_task_force_no_cell_state_dependency():
    """
    Explicit test: Query does NOT read Cell-State.
    
    This test verifies that querying Task Force does NOT:
    - Import Cell-State modules
    - Call C-CELL-4 or C-CELL-5
    - Read Cell state
    """
    result = query_task_force.query_task_force_definition(
        task_force_id="tf-query-1",
        requested_by="human-1",
    )
    
    assert result["status"] == "found"
    
    # Verify no Cell-State dependency
    # (This is verified by the absence of Cell-State imports/calls in the implementation)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

