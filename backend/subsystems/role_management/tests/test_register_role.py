"""
Unit tests for C-ROLE-1: Register Role Definition

Test Requirements:
- valid role registration
- overwrite same role_id
- missing required fields
- invalid field types
- no side effects
- C-EXEC-1 compatibility
"""

import sys
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.role_management.register_role import register_role_definition


def test_register_role_definition_valid():
    """Test valid role registration."""
    role_def = {
        "role_id": "test-role-1",
        "purpose": "Test purpose",
        "inputs": ["input1", "input2"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        "notes": "Test notes",
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "role_id" in result
    assert result["role_id"] == "test-role-1"
    assert result["status"] == "registered"
    assert "timestamp" in result
    assert "error" not in result


def test_register_role_definition_overwrite():
    """Test overwriting same role_id."""
    role_def1 = {
        "role_id": "test-role-2",
        "purpose": "Original purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    role_def2 = {
        "role_id": "test-role-2",
        "purpose": "Updated purpose",
        "inputs": ["input2"],
        "outputs": ["output2"],
        "boundaries": ["boundary2"],
    }
    
    result1 = register_role_definition(role_def1, "test_user")
    result2 = register_role_definition(role_def2, "test_user")
    
    assert result1["status"] == "registered"
    assert result2["status"] == "registered"
    assert result1["role_id"] == result2["role_id"]
    # Second registration should overwrite first
    assert result2["timestamp"] > result1["timestamp"]


def test_register_role_definition_missing_required_fields():
    """Test missing required fields."""
    role_def = {
        "role_id": "test-role-3",
        # Missing purpose, inputs, outputs, boundaries
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" in result
    assert "error_type" in result
    assert "Missing required field" in result["error"]


def test_register_role_definition_missing_role_id():
    """Test missing role_id."""
    role_def = {
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" in result
    assert "role_id" in result["error"].lower()


def test_register_role_definition_invalid_field_types():
    """Test invalid field types."""
    # Test invalid inputs type
    role_def1 = {
        "role_id": "test-role-4",
        "purpose": "Test purpose",
        "inputs": "not-a-list",  # Invalid
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result1 = register_role_definition(role_def1, "test_user")
    assert "error" in result1
    assert "inputs" in result1["error"].lower()
    
    # Test invalid outputs type
    role_def2 = {
        "role_id": "test-role-5",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": "not-a-list",  # Invalid
        "boundaries": ["boundary1"],
    }
    
    result2 = register_role_definition(role_def2, "test_user")
    assert "error" in result2
    assert "outputs" in result2["error"].lower()
    
    # Test invalid boundaries type
    role_def3 = {
        "role_id": "test-role-6",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": "not-a-list",  # Invalid
    }
    
    result3 = register_role_definition(role_def3, "test_user")
    assert "error" in result3
    assert "boundaries" in result3["error"].lower()


def test_register_role_definition_empty_role_id():
    """Test empty role_id."""
    role_def = {
        "role_id": "",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" in result
    assert "role_id" in result["error"].lower()


def test_register_role_definition_empty_purpose():
    """Test empty purpose."""
    role_def = {
        "role_id": "test-role-7",
        "purpose": "",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" in result
    assert "purpose" in result["error"].lower()


def test_register_role_definition_invalid_input():
    """Test invalid input type (not dict)."""
    result = register_role_definition("not-a-dict", "test_user")
    
    assert "error" in result
    # Error should mention dict, role_definition, or AttributeError
    error_msg = result["error"].lower()
    assert ("dict" in error_msg or 
            "role_definition" in error_msg or 
            "attribute" in error_msg or
            result.get("error_type") == "AttributeError")


def test_register_role_definition_notes_optional():
    """Test that notes field is optional."""
    role_def = {
        "role_id": "test-role-8",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        # notes is optional
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" not in result
    assert result["status"] == "registered"


def test_register_role_definition_invalid_notes_type():
    """Test invalid notes type."""
    role_def = {
        "role_id": "test-role-9",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        "notes": 123,  # Invalid (should be string or None)
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert "error" in result
    assert "notes" in result["error"].lower()


def test_register_role_definition_invalid_requested_by():
    """Test invalid requested_by."""
    role_def = {
        "role_id": "test-role-10",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = register_role_definition(role_def, "")  # Empty requested_by
    
    assert "error" in result
    assert "requested_by" in result["error"].lower()


def test_register_role_definition_persistence():
    """Test that role is persisted to disk."""
    role_def = {
        "role_id": "test-role-persist",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = register_role_definition(role_def, "test_user")
    
    assert result["status"] == "registered"
    
    # Check that file was created
    role_file = Path("backend/subsystems/role_management/roles/test-role-persist.json")
    assert role_file.exists()
    
    # Verify file content
    import json
    with open(role_file, "r") as f:
        saved_role = json.load(f)
    
    assert saved_role["role_id"] == "test-role-persist"
    assert saved_role["purpose"] == "Test purpose"
    assert saved_role["inputs"] == ["input1"]
    assert saved_role["outputs"] == ["output1"]
    assert saved_role["boundaries"] == ["boundary1"]

