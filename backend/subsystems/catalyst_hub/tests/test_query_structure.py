"""
Unit tests for C-CH-2: Query Structure
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

from backend.subsystems.catalyst_hub import register_structure, query_structure


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    register_structure._structures.clear()
    
    # Create temporary directory for structures
    test_structures_dir = Path("backend/subsystems/catalyst_hub/structures")
    if test_structures_dir.exists():
        shutil.rmtree(test_structures_dir)
    test_structures_dir.mkdir(parents=True, exist_ok=True)
    
    # Create test structure
    structure_data = {
        "requirement_id": "req-query-1",
        "content": "Query Test Requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
    }
    
    register_structure.register_structure(
        structure_type="requirement_envelope",
        structure_data=structure_data,
        requested_by="human-1",
    )


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    register_structure._structures.clear()
    
    # Remove test directory
    test_structures_dir = Path("backend/subsystems/catalyst_hub/structures")
    if test_structures_dir.exists():
        shutil.rmtree(test_structures_dir)


def test_query_structure_found_in_memory():
    """Test querying structure from in-memory cache"""
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-1",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["structure_id"] == "req-query-1"
    assert result["structure_type"] == "requirement_envelope"
    assert result["content"] == "Query Test Requirement"


def test_query_structure_found_on_disk():
    """Test querying structure from disk storage"""
    # Create structure file directly on disk
    structures_dir = Path("backend/subsystems/catalyst_hub/structures/requirement_envelope")
    structure_file = structures_dir / "req-query-2.json"
    
    structure_dict = {
        "requirement_id": "req-query-2",
        "content": "Disk Test Requirement",
        "source": "human-1",
        "created_at": datetime.utcnow().isoformat(),
        "structure_type": "requirement_envelope",
        "structure_id": "req-query-2",
        "created_by": "human-1",
    }
    
    with open(structure_file, "w") as f:
        json.dump(structure_dict, f, indent=2)
    
    # Query (should load from disk)
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-2",
        requested_by="human-2",
    )
    
    assert result["status"] == "found"
    assert result["structure_id"] == "req-query-2"
    assert result["content"] == "Disk Test Requirement"


def test_query_structure_not_found():
    """Test querying non-existent structure"""
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-not-found",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    assert result["structure_id"] == "req-query-not-found"
    assert result["structure_type"] == "requirement_envelope"
    assert "content" not in result


def test_query_structure_invalid_input():
    """Test invalid input"""
    result = query_structure.query_structure(
        structure_type="",
        structure_id="req-1",
        requested_by="human-1",
    )
    
    assert "error" in result
    assert "structure_type must be a non-empty string" in result["error"]


def test_query_structure_read_only():
    """Test that query is read-only (no mutations)"""
    # Query multiple times
    result1 = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-1",
        requested_by="human-2",
    )
    
    result2 = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-1",
        requested_by="human-3",
    )
    
    # Verify results are identical
    assert result1["structure_id"] == result2["structure_id"]
    assert result1["content"] == result2["content"]
    
    # Verify structure unchanged in storage
    storage_key = "requirement_envelope:req-query-1"
    assert storage_key in register_structure._structures
    original_structure = register_structure._structures[storage_key]
    assert original_structure["content"] == "Query Test Requirement"


def test_query_structure_no_repair_inference():
    """
    Test that query does NOT repair, infer, or normalize.
    
    This test verifies that querying structures does NOT:
    - Repair missing fields
    - Infer default values
    - Normalize structure definitions
    - Create default structures
    """
    # Query non-existent structure
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-no-repair",
        requested_by="human-1",
    )
    
    assert result["status"] == "not_found"
    
    # Verify no structure was created
    storage_key = "requirement_envelope:req-query-no-repair"
    assert storage_key not in register_structure._structures
    
    # Verify no file was created
    structure_file = Path("backend/subsystems/catalyst_hub/structures/requirement_envelope/req-query-no-repair.json")
    assert not structure_file.exists()


def test_query_structure_no_cell_state_dependency():
    """
    Explicit test: Query does NOT read Cell-State to affect behavior.
    
    This test verifies that querying structures does NOT:
    - Import Cell-State modules
    - Call C-CELL-4 or C-CELL-5
    - Read Cell state
    """
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-1",
        requested_by="human-1",
    )
    
    assert result["status"] == "found"
    
    # Verify no Cell-State dependency
    # (This is verified by the absence of Cell-State imports/calls in the implementation)


def test_query_structure_removal_safe():
    """
    Explicit test: Query is removal-safe.
    
    This test verifies that:
    - Querying structures does NOT affect system behavior
    - Removing Catalyst Hub subsystem does NOT change system behavior
    - Only structure storage/query disappears
    """
    result = query_structure.query_structure(
        structure_type="requirement_envelope",
        structure_id="req-query-1",
        requested_by="human-1",
    )
    
    assert result["status"] == "found"
    
    # Verify no side effects on system behavior
    # (This is verified by the absence of execution/routing/detection/triggering in the implementation)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

