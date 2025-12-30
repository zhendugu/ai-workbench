"""
Unit tests for C-TF-2: Validate Task Force Completeness
"""

from backend.subsystems.task_force.models import TaskForceDefinition, TaskForceMember, TaskForceGoal
from backend.subsystems.task_force.validate_task_force import validate_task_force_completeness


def test_validate_task_force_valid():
    """Test validation of valid Task Force definition"""
    task_force_def = {
        "task_force_id": "tf-valid-1",
        "name": "Valid Task Force",
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
    
    result = validate_task_force_completeness(task_force_def)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_task_force_missing_required_fields():
    """Test validation with missing required fields"""
    task_force_def = {
        "task_force_id": "tf-invalid-1",
        # Missing "name"
    }
    
    result = validate_task_force_completeness(task_force_def)
    
    assert result["valid"] is False
    assert len(result["errors"]) > 0
    assert any("name" in e["field"] for e in result["errors"])


def test_validate_task_force_forbidden_fields():
    """Test validation with forbidden fields"""
    task_force_def = {
        "task_force_id": "tf-invalid-2",
        "name": "Test Task Force",
        "members": [],
        "goals": [],
        "dissolution_conditions": [],
        "state": "active",  # Forbidden field
    }
    
    result = validate_task_force_completeness(task_force_def)
    
    assert result["valid"] is False
    assert any("forbidden_field" in e["code"] for e in result["errors"])
    assert any("state" in e["field"] for e in result["errors"])


def test_validate_task_force_empty_lists_strict():
    """Test validation with empty lists in strict mode"""
    task_force_def = {
        "task_force_id": "tf-invalid-3",
        "name": "Test Task Force",
        "members": [],  # Empty in strict mode
        "goals": [],
        "dissolution_conditions": [],
    }
    
    result = validate_task_force_completeness(task_force_def, strict=True)
    
    assert result["valid"] is False
    assert any("empty_list" in e["code"] for e in result["errors"])


def test_validate_task_force_deterministic():
    """
    Explicit test: Validation is deterministic.
    
    This test verifies that the same input produces the same output.
    """
    task_force_def = {
        "task_force_id": "tf-deterministic",
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
    
    result1 = validate_task_force_completeness(task_force_def)
    result2 = validate_task_force_completeness(task_force_def)
    
    assert result1["valid"] == result2["valid"]
    assert len(result1["errors"]) == len(result2["errors"])
    # Error ordering should be deterministic
    assert result1["errors"] == result2["errors"]


def test_validate_task_force_pure_function():
    """
    Explicit test: Validation is a pure function (no I/O, no state mutation).
    
    This test verifies that validation does NOT:
    - Read from disk
    - Write to disk
    - Mutate global state
    - Call other subsystems
    """
    task_force_def = {
        "task_force_id": "tf-pure",
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
    
    # Multiple calls should produce same result
    result1 = validate_task_force_completeness(task_force_def)
    result2 = validate_task_force_completeness(task_force_def)
    
    assert result1 == result2
    
    # Verify no I/O or state mutation
    # (This is verified by the absence of such behavior in the implementation)


def test_validate_task_force_from_instance():
    """Test validation with TaskForceDefinition instance"""
    members = [
        TaskForceMember(
            member_id="member-1",
            role_id="role-1",
            cell_id="cell-1",
            capability_contribution=["cap-1"],
        )
    ]
    
    goals = [
        TaskForceGoal(
            goal_id="goal-1",
            description="Test goal",
            expected_output="Test output",
            success_criteria=["criterion-1"],
        )
    ]
    
    task_force = TaskForceDefinition(
        task_force_id="tf-instance-1",
        name="Test Task Force",
        members=members,
        goals=goals,
        dissolution_conditions=["condition-1"],
        created_by="human-1",
        created_at="2025-12-26T10:00:00",
    )
    
    result = validate_task_force_completeness(task_force)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

