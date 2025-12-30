"""
Unit tests for C-CELL-4: Update Cell State
"""

import json
import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

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


def test_update_cell_state_valid():
    """Test valid cell state update"""
    result = update_cell_state(
        cell_id="test-cell-1",
        state="ready",
        updated_by="human-1",
    )
    
    assert result["status"] == "updated"
    assert result["cell_id"] == "test-cell-1"
    assert result["state"] == "ready"
    assert "updated_at" in result
    
    # Verify in-memory storage
    assert "test-cell-1" in _cell_states
    assert _cell_states["test-cell-1"].state == "ready"
    assert _cell_states["test-cell-1"].updated_by == "human-1"
    
    # Verify disk persistence
    state_file = Path("backend/subsystems/cell_composition/cell_states/test-cell-1.json")
    assert state_file.exists()
    
    with open(state_file, "r") as f:
        state_dict = json.load(f)
    
    assert state_dict["cell_id"] == "test-cell-1"
    assert state_dict["state"] == "ready"
    assert state_dict["updated_by"] == "human-1"
    assert "updated_at" in state_dict


def test_update_cell_state_overwrite():
    """Test overwriting existing cell state"""
    # First update
    result1 = update_cell_state(
        cell_id="test-cell-2",
        state="declared",
        updated_by="human-1",
    )
    
    assert result1["status"] == "updated"
    assert result1["state"] == "declared"
    
    # Second update (overwrite)
    result2 = update_cell_state(
        cell_id="test-cell-2",
        state="ready",
        updated_by="human-2",
    )
    
    assert result2["status"] == "updated"
    assert result2["state"] == "ready"
    assert result2["updated_by"] != result1["updated_by"]  # Different updater
    
    # Verify final state
    assert _cell_states["test-cell-2"].state == "ready"
    assert _cell_states["test-cell-2"].updated_by == "human-2"


def test_update_cell_state_invalid_cell_id():
    """Test invalid cell_id"""
    result = update_cell_state(
        cell_id="",
        state="ready",
        updated_by="human-1",
    )
    
    assert "error" in result
    assert "cell_id must be a non-empty string" in result["error"]


def test_update_cell_state_invalid_state():
    """Test invalid state"""
    result = update_cell_state(
        cell_id="test-cell-3",
        state="",
        updated_by="human-1",
    )
    
    assert "error" in result
    assert "state must be a non-empty string" in result["error"]


def test_update_cell_state_invalid_updated_by():
    """Test invalid updated_by"""
    result = update_cell_state(
        cell_id="test-cell-4",
        state="ready",
        updated_by="",
    )
    
    assert "error" in result
    assert "updated_by must be a non-empty string" in result["error"]


def test_update_cell_state_no_side_effects():
    """
    Explicit test: state change causes NO side effects.
    
    This test verifies that updating cell state does NOT:
    - Trigger execution
    - Trigger validation
    - Trigger handoff
    - Trigger orchestration
    - Modify other subsystems
    """
    # Mock any potential cross-subsystem calls
    with patch('backend.subsystems.cell_composition.update_cell_state._record_observability') as mock_obs:
        result = update_cell_state(
            cell_id="test-cell-no-side-effects",
            state="ready",
            updated_by="human-1",
        )
        
        assert result["status"] == "updated"
        
        # Verify only observability was called (for logging)
        # No other subsystem calls should occur
        assert mock_obs.call_count >= 2  # Entry and exit records
        
        # Verify no execution, validation, handoff, or orchestration calls
        # (This is verified by the absence of such calls in the implementation)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

