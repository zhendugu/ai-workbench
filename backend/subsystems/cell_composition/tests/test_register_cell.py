"""
Unit tests for C-CELL-1: Register Cell Definition

Test Requirements:
- valid cell registration
- overwrite same cell_id
- missing required fields
- invalid field types
- forbidden fields detection
- no state or lifecycle logic
- C-EXEC-1 compatibility
"""

import sys
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.cell_composition.register_cell import register_cell_definition


def test_register_cell_definition_valid():
    """Test valid cell registration."""
    cell_def = {
        "cell_id": "test-cell-1",
        "role_ids": ["role-1", "role-2"],
        "input_contract": {"input_type": "string", "required": True},
        "output_format": {"output_type": "dict", "schema": {}},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    
    assert "cell_id" in result
    assert result["cell_id"] == "test-cell-1"
    assert result["status"] == "registered"
    assert "timestamp" in result
    assert "error" not in result


def test_register_cell_definition_overwrite():
    """Test overwriting same cell_id."""
    cell_def1 = {
        "cell_id": "test-cell-2",
        "role_ids": ["role-1"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "string"},
    }
    
    cell_def2 = {
        "cell_id": "test-cell-2",
        "role_ids": ["role-1", "role-2", "role-3"],  # Different role_ids
        "input_contract": {"input_type": "dict"},  # Different input_contract
        "output_format": {"output_type": "list"},  # Different output_format
    }
    
    result1 = register_cell_definition(cell_def1, "test_user")
    assert result1["status"] == "registered"
    
    result2 = register_cell_definition(cell_def2, "test_user")
    assert result2["status"] == "registered"
    assert result2["cell_id"] == "test-cell-2"
    # Should overwrite successfully


def test_register_cell_definition_missing_required_fields():
    """Test missing required fields."""
    # Missing cell_id
    cell_def = {
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Missing required field" in result["error"]
    
    # Missing role_ids
    cell_def = {
        "cell_id": "test-cell-3",
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Missing required field" in result["error"]


def test_register_cell_definition_missing_cell_id():
    """Test missing cell_id."""
    cell_def = {
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Missing required field" in result["error"]


def test_register_cell_definition_invalid_field_types():
    """Test invalid field types."""
    # Invalid cell_id (not string)
    cell_def = {
        "cell_id": 123,  # Should be string
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    
    # Invalid role_ids (not list)
    cell_def = {
        "cell_id": "test-cell-4",
        "role_ids": "not-a-list",  # Should be list
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "role_ids must be a list" in result["error"]
    
    # Invalid role_ids (list of non-strings)
    cell_def = {
        "cell_id": "test-cell-5",
        "role_ids": [123, 456],  # Should be list of strings
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "role_ids must be a list of strings" in result["error"]
    
    # Invalid input_contract (not dict)
    cell_def = {
        "cell_id": "test-cell-6",
        "role_ids": ["role-1"],
        "input_contract": "not-a-dict",  # Should be dict
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "input_contract must be a dict" in result["error"]
    
    # Invalid output_format (not dict)
    cell_def = {
        "cell_id": "test-cell-7",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": "not-a-dict",  # Should be dict
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "output_format must be a dict" in result["error"]


def test_register_cell_definition_empty_cell_id():
    """Test empty cell_id."""
    cell_def = {
        "cell_id": "",  # Empty string
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "cell_id must be a non-empty string" in result["error"]


def test_register_cell_definition_empty_role_ids():
    """Test empty role_ids."""
    cell_def = {
        "cell_id": "test-cell-8",
        "role_ids": [],  # Empty list
        "input_contract": {},
        "output_format": {},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "role_ids must contain at least one role identifier" in result["error"]


def test_register_cell_definition_forbidden_fields():
    """Test forbidden fields detection (Phase-2 constraint)."""
    # Test state field
    cell_def = {
        "cell_id": "test-cell-9",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "state": "active",  # FORBIDDEN
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Forbidden field 'state'" in result["error"]
    
    # Test status field
    cell_def = {
        "cell_id": "test-cell-10",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "status": "idle",  # FORBIDDEN
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Forbidden field 'status'" in result["error"]
    
    # Test lifecycle field
    cell_def = {
        "cell_id": "test-cell-11",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "lifecycle": "active",  # FORBIDDEN
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Forbidden field 'lifecycle'" in result["error"]
    
    # Test state_transitions field
    cell_def = {
        "cell_id": "test-cell-12",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "state_transitions": {},  # FORBIDDEN
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert "error" in result
    assert "Forbidden field 'state_transitions'" in result["error"]


def test_register_cell_definition_invalid_input():
    """Test invalid input type."""
    # Non-dict input
    result = register_cell_definition("not-a-dict", "test_user")
    assert "error" in result
    # Check that error message contains relevant information
    assert "dict" in result["error"].lower() or "error_type" in result


def test_register_cell_definition_invalid_requested_by():
    """Test invalid requested_by."""
    cell_def = {
        "cell_id": "test-cell-13",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    # Empty requested_by
    result = register_cell_definition(cell_def, "")
    assert "error" in result
    assert "requested_by must be a non-empty string" in result["error"]
    
    # Non-string requested_by
    result = register_cell_definition(cell_def, None)
    assert "error" in result


def test_register_cell_definition_persistence():
    """Test persistence to disk."""
    cell_def = {
        "cell_id": "test-cell-persist",
        "role_ids": ["role-1", "role-2"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "dict"},
    }
    
    result = register_cell_definition(cell_def, "test_user")
    assert result["status"] == "registered"
    
    # Verify file exists
    cell_file = Path("backend/subsystems/cell_composition/cells/test-cell-persist.json")
    assert cell_file.exists()
    
    # Verify file content
    import json
    with open(cell_file, "r") as f:
        stored_data = json.load(f)
    
    assert stored_data["cell_id"] == "test-cell-persist"
    assert stored_data["role_ids"] == ["role-1", "role-2"]
    assert "registered_at" in stored_data
    
    # Verify no forbidden fields in stored data
    forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                       "execution_history", "runtime_info"]
    for field in forbidden_fields:
        assert field not in stored_data, f"Forbidden field '{field}' found in stored data"


def test_register_cell_definition_deterministic():
    """Test deterministic behavior for identical input."""
    cell_def = {
        "cell_id": "test-cell-deterministic",
        "role_ids": ["role-1"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "string"},
    }
    
    result1 = register_cell_definition(cell_def, "test_user")
    result2 = register_cell_definition(cell_def, "test_user")
    
    # Both should succeed
    assert result1["status"] == "registered"
    assert result2["status"] == "registered"
    
    # Same cell_id
    assert result1["cell_id"] == result2["cell_id"]
    assert result1["cell_id"] == "test-cell-deterministic"

