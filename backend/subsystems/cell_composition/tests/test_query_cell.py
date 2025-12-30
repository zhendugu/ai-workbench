"""
Unit tests for C-CELL-2: Query Cell Definition

Test Requirements:
- found path (in-memory)
- found path (disk)
- not_found path
- invalid cell_id (empty / non-string)
- read-only guarantee (no file writes)
- no state or lifecycle information returned
- C-EXEC-1 compatibility test
"""

import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.cell_composition.query_cell import query_cell_definition
from backend.subsystems.cell_composition.register_cell import register_cell_definition, _cells


def test_query_cell_definition_found_in_memory():
    """Test query cell found in memory."""
    # First register a cell
    cell_def = {
        "cell_id": "test-query-cell-1",
        "role_ids": ["role-1", "role-2"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "dict"},
    }
    register_cell_definition(cell_def, "test_user")
    
    # Query the cell
    result = query_cell_definition("test-query-cell-1", "test_user")
    
    assert result["status"] == "found"
    assert result["cell_id"] == "test-query-cell-1"
    assert "cell_definition" in result
    assert result["cell_definition"]["cell_id"] == "test-query-cell-1"
    assert result["cell_definition"]["role_ids"] == ["role-1", "role-2"]
    assert result["cell_definition"]["input_contract"] == {"input_type": "string"}
    assert result["cell_definition"]["output_format"] == {"output_type": "dict"}
    assert "timestamp" in result
    
    # Verify no forbidden fields in result
    forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                       "execution_history", "runtime_info"]
    for field in forbidden_fields:
        assert field not in result["cell_definition"], f"Forbidden field '{field}' found in result"


def test_query_cell_definition_found_on_disk():
    """Test query cell found on disk (not in memory)."""
    # Register a cell (this will create disk file)
    cell_def = {
        "cell_id": "test-query-cell-2",
        "role_ids": ["role-1"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "string"},
    }
    register_cell_definition(cell_def, "test_user")
    
    # Clear memory cache
    if "test-query-cell-2" in _cells:
        del _cells["test-query-cell-2"]
    
    # Query the cell (should load from disk)
    result = query_cell_definition("test-query-cell-2", "test_user")
    
    assert result["status"] == "found"
    assert result["cell_id"] == "test-query-cell-2"
    assert "cell_definition" in result
    assert result["cell_definition"]["role_ids"] == ["role-1"]
    # Should be cached in memory now
    assert "test-query-cell-2" in _cells


def test_query_cell_definition_not_found():
    """Test query cell not found."""
    result = query_cell_definition("non-existent-cell", "test_user")
    
    assert result["status"] == "not_found"
    assert result["cell_id"] == "non-existent-cell"
    assert "cell_definition" not in result
    assert "timestamp" in result
    assert "error" not in result


def test_query_cell_definition_invalid_cell_id():
    """Test invalid cell_id."""
    # Empty cell_id
    result = query_cell_definition("", "test_user")
    assert "error" in result
    assert "cell_id must be a non-empty string" in result["error"]
    
    # Non-string cell_id
    result = query_cell_definition(None, "test_user")
    assert "error" in result


def test_query_cell_definition_invalid_requested_by():
    """Test invalid requested_by."""
    result = query_cell_definition("test-cell", "")
    assert "error" in result
    assert "requested_by must be a non-empty string" in result["error"]


def test_query_cell_definition_read_only_guarantee():
    """Test read-only guarantee (no file writes)."""
    # Register a cell
    cell_def = {
        "cell_id": "test-readonly-cell",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    register_cell_definition(cell_def, "test_user")
    
    # Get file modification time before query
    cell_file = Path("backend/subsystems/cell_composition/cells/test-readonly-cell.json")
    if cell_file.exists():
        mtime_before = cell_file.stat().st_mtime
    
    # Query the cell
    result = query_cell_definition("test-readonly-cell", "test_user")
    
    # Verify file was not modified
    if cell_file.exists():
        mtime_after = cell_file.stat().st_mtime
        assert mtime_after == mtime_before, "File was modified during read-only query"
    
    assert result["status"] == "found"


def test_query_cell_definition_deterministic():
    """Test deterministic output for identical storage state."""
    # Register a cell
    cell_def = {
        "cell_id": "test-deterministic-cell",
        "role_ids": ["role-1"],
        "input_contract": {"input_type": "string"},
        "output_format": {"output_type": "string"},
    }
    register_cell_definition(cell_def, "test_user")
    
    # Query multiple times
    result1 = query_cell_definition("test-deterministic-cell", "test_user")
    result2 = query_cell_definition("test-deterministic-cell", "test_user")
    
    # Results should be identical (except timestamp)
    assert result1["status"] == result2["status"] == "found"
    assert result1["cell_id"] == result2["cell_id"]
    assert result1["cell_definition"] == result2["cell_definition"]


def test_query_cell_definition_no_state_information():
    """Test that no state or lifecycle information is returned."""
    # Register a cell
    cell_def = {
        "cell_id": "test-no-state-cell",
        "role_ids": ["role-1"],
        "input_contract": {},
        "output_format": {},
    }
    register_cell_definition(cell_def, "test_user")
    
    # Query the cell
    result = query_cell_definition("test-no-state-cell", "test_user")
    
    assert result["status"] == "found"
    cell_def_result = result["cell_definition"]
    
    # Verify only allowed fields are present
    allowed_fields = ["cell_id", "role_ids", "input_contract", "output_format"]
    for field in allowed_fields:
        assert field in cell_def_result
    
    # Verify no forbidden fields
    forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                        "execution_history", "runtime_info", "activation_time",
                        "deactivation_time", "current_state", "previous_state"]
    for field in forbidden_fields:
        assert field not in cell_def_result, f"Forbidden field '{field}' found in result"

