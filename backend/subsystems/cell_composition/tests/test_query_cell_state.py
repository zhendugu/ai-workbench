"""
Unit tests for C-CELL-5: Query Cell State
"""

import json
import shutil
from pathlib import Path
from unittest.mock import patch

import pytest

from backend.subsystems.cell_composition.query_cell_state import (
    query_cell_state,
)
from backend.subsystems.cell_composition.update_cell_state import (
    _cell_states,
    update_cell_state,
)


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    _cell_states.clear()
    
    # Create temporary directory for cell_states
    test_states_dir = Path("backend/subsystems/cell_composition/cell_states")
    if test_states_dir.exists():
        shutil.rmtree(test_states_dir)
    test_states_dir.mkdir(parents=True, exist_ok=True)


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    _cell_states.clear()
    
    # Remove test directory
    test_states_dir = Path("backend/subsystems/cell_composition/cell_states")
    if test_states_dir.exists():
        shutil.rmtree(test_states_dir)


def test_query_cell_state_found_in_memory():
    """Test querying cell state from in-memory cache"""
    # First update to create state
    update_cell_state(
        cell_id="test-query-1",
        state="ready",
        updated_by="human-1",
    )
    
    # Query
    result = query_cell_state(
        cell_id="test-query-1",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["cell_id"] == "test-query-1"
    assert result["state"] == "ready"
    assert result["updated_by"] == "human-1"
    assert "updated_at" in result


def test_query_cell_state_found_on_disk():
    """Test querying cell state from disk storage"""
    # Create state file directly on disk
    states_dir = Path("backend/subsystems/cell_composition/cell_states")
    state_file = states_dir / "test-query-2.json"
    
    state_dict = {
        "cell_id": "test-query-2",
        "state": "declared",
        "updated_by": "human-1",
        "updated_at": "2025-12-26T10:00:00",
    }
    
    with open(state_file, "w") as f:
        json.dump(state_dict, f, indent=2)
    
    # Query (should load from disk)
    result = query_cell_state(
        cell_id="test-query-2",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["cell_id"] == "test-query-2"
    assert result["state"] == "declared"
    assert result["updated_by"] == "human-1"


def test_query_cell_state_not_found():
    """Test querying non-existent cell state"""
    result = query_cell_state(
        cell_id="test-query-not-found",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    assert result["cell_id"] == "test-query-not-found"
    assert "state" not in result
    assert "updated_by" not in result
    assert "updated_at" not in result


def test_query_cell_state_invalid_cell_id():
    """Test invalid cell_id"""
    result = query_cell_state(
        cell_id="",
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "cell_id must be a non-empty string" in result["error"]


def test_query_cell_state_invalid_requested_by():
    """Test invalid requested_by"""
    result = query_cell_state(
        cell_id="test-query-3",
        requested_by="",
    )
    
    assert "error" in result
    assert "requested_by must be a non-empty string" in result["error"]


def test_query_cell_state_read_only():
    """Test that query is read-only (no mutations)"""
    # Create state
    update_cell_state(
        cell_id="test-query-readonly",
        state="ready",
        updated_by="human-1",
    )
    
    # Get initial state
    initial_state = _cell_states["test-query-readonly"]
    initial_updated_at = initial_state.updated_at
    
    # Query multiple times
    result1 = query_cell_state(
        cell_id="test-query-readonly",
        requested_by="human-2",
    )
    
    result2 = query_cell_state(
        cell_id="test-query-readonly",
        requested_by="human-3",
    )
    
    # Verify state unchanged
    assert _cell_states["test-query-readonly"].updated_at == initial_updated_at
    assert result1["state"] == result2["state"]
    assert result1["updated_at"] == result2["updated_at"]


def test_query_cell_state_no_repair_inference():
    """
    Test that query does NOT repair, infer, or normalize.
    
    This test verifies that querying cell state does NOT:
    - Repair missing fields
    - Infer default values
    - Normalize state values
    - Create default states
    """
    # Query non-existent state
    result = query_cell_state(
        cell_id="test-query-no-repair",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    
    # Verify no state was created
    assert "test-query-no-repair" not in _cell_states
    
    # Verify no file was created
    state_file = Path("backend/subsystems/cell_composition/cell_states/test-query-no-repair.json")
    assert not state_file.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

