"""
Unit tests for C-CELL-3: Validate Cell Completeness

Test Requirements:
- valid cell_definition passes
- missing required field fails (strict=true)
- empty strings fail (strict=true)
- strict=false allows empty lists but still requires keys present
- rejects non-list role_ids
- rejects non-dict input_contract/output_format
- forbidden fields detection
- duplicate role_id detection
- deterministic output ordering for errors (stable sort by field then code)
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.cell_composition.validate_cell import validate_cell_definition
from backend.subsystems.cell_composition.models import CellDefinition


def test_validate_cell_definition_valid():
    """Test valid cell_definition passes."""
    cell_def = {
        "cell_id": "test-cell-1",
        "role_ids": ["role-1", "role-2"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "dict"},
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0
    assert result["normalized"] is None


def test_validate_cell_definition_valid_cell_definition_instance():
    """Test valid CellDefinition instance passes."""
    cell = CellDefinition(
        cell_id="test-cell-2",
        role_ids=["role-1"],
        input_contract={"input_type": "string"},
        output_format={"output_type": "string"},
    )
    
    result = validate_cell_definition(cell)
    
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_cell_definition_missing_required_field():
    """Test missing required field fails (strict=true)."""
    cell_def = {
        "cell_id": "test-cell-3",
        # Missing role_ids, input_contract, output_format
    }
    
    result = validate_cell_definition(cell_def, strict=True)
    
    assert result["valid"] is False
    assert len(result["errors"]) > 0
    assert any(e["code"] == "MISSING_FIELD" for e in result["errors"])


def test_validate_cell_definition_empty_strings_strict():
    """Test empty strings fail (strict=true)."""
    cell_def = {
        "cell_id": "",  # Empty
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def, strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "cell_id" and e["code"] == "EMPTY_VALUE" for e in result["errors"])


def test_validate_cell_definition_empty_lists_strict():
    """Test empty lists fail (strict=true)."""
    cell_def = {
        "cell_id": "test-cell-4",
        "role_ids": [],  # Empty
        "input_contract": {},
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def, strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "role_ids" and e["code"] == "EMPTY_LIST" for e in result["errors"])


def test_validate_cell_definition_empty_dicts_strict():
    """Test empty dicts fail (strict=true)."""
    cell_def = {
        "cell_id": "test-cell-5",
        "role_ids": ["role-1"],
        "input_contract": {},  # Empty
        "output_format": {},  # Empty
    }
    
    result = validate_cell_definition(cell_def, strict=True)
    
    assert result["valid"] is False
    assert any(e["field"] == "input_contract" and e["code"] == "EMPTY_DICT" for e in result["errors"])
    assert any(e["field"] == "output_format" and e["code"] == "EMPTY_DICT" for e in result["errors"])


def test_validate_cell_definition_strict_false():
    """Test strict=false allows empty lists but still requires keys present."""
    cell_def = {
        "cell_id": "test-cell-6",
        "role_ids": [],  # Empty allowed in non-strict
        "input_contract": {"key": "value"},  # Non-empty to avoid empty dict error
        "output_format": {"key": "value"},  # Non-empty to avoid empty dict error
    }
    
    result = validate_cell_definition(cell_def, strict=False)
    
    # Should pass (empty lists allowed in non-strict mode)
    assert result["valid"] is True
    assert not any(e["field"] == "role_ids" and e["code"] == "EMPTY_LIST" for e in result["errors"])


def test_validate_cell_definition_invalid_type_role_ids():
    """Test rejects non-list role_ids."""
    cell_def = {
        "cell_id": "test-cell-7",
        "role_ids": "not-a-list",  # Should be list
        "input_contract": {},
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "role_ids" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_cell_definition_invalid_type_role_id_items():
    """Test rejects non-string items in role_ids."""
    cell_def = {
        "cell_id": "test-cell-8",
        "role_ids": [123, 456],  # Should be strings
        "input_contract": {},
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["code"] == "INVALID_TYPE" and "role_ids[" in e["field"] for e in result["errors"])


def test_validate_cell_definition_invalid_type_input_contract():
    """Test rejects non-dict input_contract."""
    cell_def = {
        "cell_id": "test-cell-9",
        "role_ids": ["role-1"],
        "input_contract": "not-a-dict",  # Should be dict
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "input_contract" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_cell_definition_invalid_type_output_format():
    """Test rejects non-dict output_format."""
    cell_def = {
        "cell_id": "test-cell-10",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": "not-a-dict",  # Should be dict
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "output_format" and e["code"] == "INVALID_TYPE" for e in result["errors"])


def test_validate_cell_definition_forbidden_fields():
    """Test forbidden fields detection (Phase-2 constraint)."""
    cell_def = {
        "cell_id": "test-cell-11",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "state": "active",  # FORBIDDEN
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "state" and e["code"] == "FORBIDDEN_FIELD" for e in result["errors"])
    
    # Test multiple forbidden fields
    cell_def = {
        "cell_id": "test-cell-12",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
        "status": "idle",  # FORBIDDEN
        "lifecycle": "active",  # FORBIDDEN
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["field"] == "status" and e["code"] == "FORBIDDEN_FIELD" for e in result["errors"])
    assert any(e["field"] == "lifecycle" and e["code"] == "FORBIDDEN_FIELD" for e in result["errors"])


def test_validate_cell_definition_duplicate_role_ids():
    """Test duplicate role_id detection."""
    cell_def = {
        "cell_id": "test-cell-13",
        "role_ids": ["role-1", "role-2", "role-1"],  # Duplicate
        "input_contract": {},
        "output_format": {},
    }
    
    result = validate_cell_definition(cell_def)
    
    assert result["valid"] is False
    assert any(e["code"] == "DUPLICATE_ENTRY" and "role-1" in e["message"] for e in result["errors"])


def test_validate_cell_definition_deterministic_error_ordering():
    """Test deterministic output ordering for errors (stable sort by field then code)."""
    cell_def = {
        "cell_id": "",  # Empty
        "role_ids": "not-a-list",  # Invalid type
        # Missing input_contract, output_format
    }
    
    result1 = validate_cell_definition(cell_def)
    result2 = validate_cell_definition(cell_def)
    
    # Errors should be in same order
    assert result1["errors"] == result2["errors"]
    
    # Errors should be sorted by field then code
    if len(result1["errors"]) > 1:
        for i in range(len(result1["errors"]) - 1):
            e1 = result1["errors"][i]
            e2 = result1["errors"][i + 1]
            assert (e1["field"], e1["code"]) <= (e2["field"], e2["code"])


def test_validate_cell_definition_invalid_input_type():
    """Test invalid input type."""
    result = validate_cell_definition("not-a-dict-or-cell")
    
    assert result["valid"] is False
    assert any(e["field"] == "cell_definition" and e["code"] == "INVALID_TYPE" for e in result["errors"])

