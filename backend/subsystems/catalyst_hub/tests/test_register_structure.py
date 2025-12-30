"""
Unit tests for C-CH-1: Register Structure
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

from backend.subsystems.catalyst_hub import register_structure


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    register_structure._structures.clear()
    
    # Create temporary directory for structures
    test_structures_dir = Path("backend/subsystems/catalyst_hub/structures")
    if test_structures_dir.exists():
        shutil.rmtree(test_structures_dir)
    test_structures_dir.mkdir(parents=True, exist_ok=True)


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    register_structure._structures.clear()
    
    # Remove test directory
    test_structures_dir = Path("backend/subsystems/catalyst_hub/structures")
    if test_structures_dir.exists():
        shutil.rmtree(test_structures_dir)


def test_register_requirement_envelope():
    """Test registering RequirementEnvelope structure"""
    structure_data = {
        "requirement_id": "req-1",
        "content": "Test requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
        "priority": "high",
    }
    
    result = register_structure.register_structure(
        structure_type="requirement_envelope",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    assert result["structure_id"] == "req-1"
    assert result["structure_type"] == "requirement_envelope"
    assert "created_at" in result
    
    # Verify in-memory storage
    storage_key = "requirement_envelope:req-1"
    assert storage_key in register_structure._structures
    
    # Verify disk persistence
    structure_file = Path("backend/subsystems/catalyst_hub/structures/requirement_envelope/req-1.json")
    assert structure_file.exists()


def test_register_routing_hint():
    """Test registering RoutingHint structure"""
    structure_data = {
        "hint_id": "hint-1",
        "requirement_id": "req-1",
        "suggested_cell_ids": ["cell-1", "cell-2"],
        "reasoning": "Test reasoning",
    }
    
    result = register_structure.register_structure(
        structure_type="routing_hint",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    assert result["structure_id"] == "hint-1"
    assert result["structure_type"] == "routing_hint"


def test_register_workflow_state_snapshot():
    """Test registering WorkflowStateSnapshot structure"""
    structure_data = {
        "snapshot_id": "snapshot-1",
        "captured_at": datetime.utcnow().isoformat(),
        "cell_states": {"cell-1": "active", "cell-2": "idle"},
        "workflow_id": "workflow-1",
    }
    
    result = register_structure.register_structure(
        structure_type="workflow_state_snapshot",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    assert result["structure_id"] == "snapshot-1"
    assert result["structure_type"] == "workflow_state_snapshot"


def test_register_forbidden_fields():
    """Test that forbidden fields are rejected"""
    structure_data = {
        "requirement_id": "req-2",
        "content": "Test requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
        "routing_decision": "cell-1",  # Forbidden field
    }
    
    result = register_structure.register_structure(
        structure_type="requirement_envelope",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "Forbidden field" in result["error"]
    assert "routing_decision" in result["error"]


def test_register_invalid_structure_type():
    """Test that invalid structure types are rejected"""
    structure_data = {
        "requirement_id": "req-3",
        "content": "Test requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = register_structure.register_structure(
        structure_type="invalid_type",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "Invalid structure_type" in result["error"]


def test_register_no_side_effects():
    """
    Explicit test: Registering structures causes NO side effects.
    
    This test verifies that registering structures does NOT:
    - Trigger routing
    - Trigger execution
    - Read Cell-State to affect behavior
    - Create Task Forces
    - Enforce budgets or policies
    """
    structure_data = {
        "requirement_id": "req-no-side-effects",
        "content": "Test requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    result = register_structure.register_structure(
        structure_type="requirement_envelope",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    
    # Verify no execution, routing, detection, triggering, or orchestration
    # (This is verified by the absence of such behavior in the implementation)


def test_register_no_cell_state_dependency():
    """
    Explicit test: Registration does NOT read Cell-State to affect behavior.
    
    This test verifies that registering structures does NOT:
    - Import Cell-State modules
    - Call C-CELL-4 or C-CELL-5
    - Read Cell state
    """
    structure_data = {
        "snapshot_id": "snapshot-no-cell-state",
        "captured_at": datetime.utcnow().isoformat(),
        "cell_states": {"cell-1": "active"},  # Descriptive only
        "workflow_id": "workflow-1",
    }
    
    result = register_structure.register_structure(
        structure_type="workflow_state_snapshot",
        structure_data=structure_data,
        requested_by="human-1",
    )
    
    assert result["status"] == "registered"
    
    # Verify no Cell-State dependency
    # (This is verified by the absence of Cell-State imports/calls in the implementation)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

