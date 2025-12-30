"""
Unit tests for C-ROLE-3: Validate Role Definition Completeness

Test Requirements:
- valid role_definition passes
- missing required field fails (strict=true)
- empty strings fail (strict=true)
- strict=false allows empty lists but still requires keys present
- rejects non-list inputs/outputs/boundaries
- deterministic output ordering for errors (stable sort by field then code)
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.role_management.validate_role import validate_role_definition
from backend.subsystems.role_management.models import RoleDefinition


def test_validate_role_definition_valid():
    """Test valid role_definition passes."""
    role_def = {
        "role_id": "test-role-1",
        "purpose": "Test purpose",
        "inputs": ["input1", "input2"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0
    assert result["normalized"] is None


def test_validate_role_definition_valid_with_notes():
    """Test valid role_definition with notes passes."""
    role_def = {
        "role_id": "test-role-2",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        "notes": "Test notes",
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_role_definition_valid_role_definition_instance():
    """Test valid RoleDefinition instance passes."""
    role = RoleDefinition(
        role_id="test-role-3",
        purpose="Test purpose",
        inputs=["input1"],
        outputs=["output1"],
        boundaries=["boundary1"],
    )
    
    result = validate_role_definition(role)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_role_definition_missing_required_field():
    """Test missing required field fails (strict=true)."""
    role_def = {
        "role_id": "test-role-4",
        "purpose": "Test purpose",
        # Missing inputs, outputs, boundaries
    }
    
    result = validate_role_definition(role_def, strict=True)
    
    assert result["valid"] is False
    assert len(result["errors"]) > 0
    assert any(e["code"] == "MISSING_FIELD" for e in result["errors"])


def test_validate_role_definition_empty_strings_strict():
    """Test empty strings fail (strict=true)."""
    role_def = {
        "role_id": "",  # Empty
        "purpose": "",  # Empty
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def, strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "role_id" and e["code"] == "EMPTY_VALUE" for e in result["errors"])
    assert any(e["field"] == "purpose" and e["code"] == "EMPTY_VALUE" for e in result["errors"])


def test_validate_role_definition_strict_false_allows_empty_lists():
    """Test strict=false allows empty lists but still requires keys present."""
    role_def = {
        "role_id": "test-role-5",
        "purpose": "Test purpose",
        "inputs": [],  # Empty list
        "outputs": [],  # Empty list
        "boundaries": [],  # Empty list
    }
    
    result = validate_role_definition(role_def, strict=False)
    
    # Should be valid (empty lists allowed in non-strict mode)
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_role_definition_strict_true_rejects_empty_lists():
    """Test strict=true rejects empty lists."""
    role_def = {
        "role_id": "test-role-6",
        "purpose": "Test purpose",
        "inputs": [],  # Empty list
        "outputs": [],  # Empty list
        "boundaries": [],  # Empty list
    }
    
    result = validate_role_definition(role_def, strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "inputs" and e["code"] == "EMPTY_LIST" for e in result["errors"])
    assert any(e["field"] == "outputs" and e["code"] == "EMPTY_LIST" for e in result["errors"])
    assert any(e["field"] == "boundaries" and e["code"] == "EMPTY_LIST" for e in result["errors"])


def test_validate_role_definition_rejects_non_list_inputs():
    """Test rejects non-list inputs."""
    role_def = {
        "role_id": "test-role-7",
        "purpose": "Test purpose",
        "inputs": "not-a-list",  # Invalid
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "inputs" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_rejects_non_list_outputs():
    """Test rejects non-list outputs."""
    role_def = {
        "role_id": "test-role-8",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": "not-a-list",  # Invalid
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "outputs" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_rejects_non_list_boundaries():
    """Test rejects non-list boundaries."""
    role_def = {
        "role_id": "test-role-9",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": "not-a-list",  # Invalid
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "boundaries" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_rejects_non_string_list_items():
    """Test rejects non-string items in lists."""
    role_def = {
        "role_id": "test-role-10",
        "purpose": "Test purpose",
        "inputs": ["input1", 123],  # Invalid (number)
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any("inputs[1]" in e["field"] and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_deterministic_error_ordering():
    """Test deterministic output ordering for errors (stable sort by field then code)."""
    role_def = {
        "role_id": "",  # Empty
        "purpose": "",  # Empty
        # Missing inputs, outputs, boundaries
    }
    
    result1 = validate_role_definition(role_def, strict=True)
    result2 = validate_role_definition(role_def, strict=True)
    
    # Errors should be in same order
    assert result1["errors"] == result2["errors"]
    
    # Errors should be sorted by field then code
    errors = result1["errors"]
    for i in range(len(errors) - 1):
        field1, code1 = errors[i]["field"], errors[i]["code"]
        field2, code2 = errors[i + 1]["field"], errors[i + 1]["code"]
        assert (field1 < field2) or (field1 == field2 and code1 <= code2)


def test_validate_role_definition_duplicate_entries():
    """Test duplicate entries in lists are detected."""
    role_def = {
        "role_id": "test-role-11",
        "purpose": "Test purpose",
        "inputs": ["input1", "input2", "input1"],  # Duplicate
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any(e["code"] == "DUPLICATE_ENTRY" and "input1" in e["message"] for e in result["errors"])


def test_validate_role_definition_invalid_notes_type():
    """Test invalid notes type."""
    role_def = {
        "role_id": "test-role-12",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        "notes": 123,  # Invalid (should be string or None)
    }
    
    result = validate_role_definition(role_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "notes" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_invalid_input_type():
    """Test invalid input type (not dict or RoleDefinition)."""
    result = validate_role_definition("not-a-dict-or-role", strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "role_definition" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_role_definition_pure_function_no_side_effects():
    """Test that function is pure (no side effects)."""
    role_def = {
        "role_id": "test-role-13",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    
    # Call multiple times with same input
    result1 = validate_role_definition(role_def)
    result2 = validate_role_definition(role_def)
    result3 = validate_role_definition(role_def)
    
    # Results should be identical
    assert result1 == result2 == result3
    
    # Input should not be modified
    assert role_def == {
        "role_id": "test-role-13",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }

