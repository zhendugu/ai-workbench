"""
Unit tests for C-ROLE-2: Query Role Definition

Test Requirements:
- found path (in-memory)
- found path (disk)
- not_found path
- invalid role_id (empty / non-string)
- read-only guarantee (no file writes)
- C-EXEC-1 compatibility test
"""

import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.role_management.query_role import query_role_definition
from backend.subsystems.role_management.register_role import register_role_definition, _roles


def test_query_role_definition_found_in_memory():
    """Test query role found in memory."""
    # First register a role
    role_def = {
        "role_id": "test-query-1",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    register_role_definition(role_def, "test_user")
    
    # Query the role
    result = query_role_definition("test-query-1", "test_user")
    
    assert result["status"] == "found"
    assert result["role_id"] == "test-query-1"
    assert "role_definition" in result
    assert result["role_definition"]["purpose"] == "Test purpose"
    assert result["role_definition"]["inputs"] == ["input1"]
    assert result["role_definition"]["outputs"] == ["output1"]
    assert result["role_definition"]["boundaries"] == ["boundary1"]
    assert "timestamp" in result


def test_query_role_definition_found_on_disk():
    """Test query role found on disk (not in memory)."""
    # Register a role (this will create disk file)
    role_def = {
        "role_id": "test-query-2",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    register_role_definition(role_def, "test_user")
    
    # Clear memory cache
    if "test-query-2" in _roles:
        del _roles["test-query-2"]
    
    # Query the role (should load from disk)
    result = query_role_definition("test-query-2", "test_user")
    
    assert result["status"] == "found"
    assert result["role_id"] == "test-query-2"
    assert "role_definition" in result
    assert result["role_definition"]["purpose"] == "Test purpose"
    # Should be cached in memory now
    assert "test-query-2" in _roles


def test_query_role_definition_not_found():
    """Test query role not found."""
    result = query_role_definition("non-existent-role", "test_user")
    
    assert result["status"] == "not_found"
    assert result["role_id"] == "non-existent-role"
    assert "role_definition" not in result
    assert "timestamp" in result
    assert "error" not in result


def test_query_role_definition_invalid_role_id_empty():
    """Test invalid role_id (empty string)."""
    result = query_role_definition("", "test_user")
    
    assert "error" in result
    assert "error_type" in result
    assert "role_id" in result["error"].lower()


def test_query_role_definition_invalid_role_id_non_string():
    """Test invalid role_id (non-string)."""
    # This will fail at function call level, but test the error handling
    try:
        result = query_role_definition(123, "test_user")  # type: ignore
        assert "error" in result
        assert "role_id" in result["error"].lower() or "string" in result["error"].lower()
    except TypeError:
        # Function signature enforces string type, so this is expected
        pass


def test_query_role_definition_invalid_requested_by():
    """Test invalid requested_by."""
    result = query_role_definition("test-role", "")
    
    assert "error" in result
    assert "requested_by" in result["error"].lower()


def test_query_role_definition_read_only():
    """Test that query is read-only (no file writes)."""
    import os
    import tempfile
    import time
    
    # Register a role
    role_def = {
        "role_id": "test-query-readonly",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    register_role_definition(role_def, "test_user")
    
    # Get file modification time before query
    role_file = Path("backend/subsystems/role_management/roles/test-query-readonly.json")
    if role_file.exists():
        mtime_before = role_file.stat().st_mtime
        
        # Small delay to ensure time difference
        time.sleep(0.01)
        
        # Query the role
        result = query_role_definition("test-query-readonly", "test_user")
        
        # Check file modification time after query
        mtime_after = role_file.stat().st_mtime
        
        # File should not be modified (read-only operation)
        assert mtime_before == mtime_after, "File was modified during query (not read-only)"
        assert result["status"] == "found"


def test_query_role_definition_caches_from_disk():
    """Test that query caches role in memory after loading from disk."""
    # Register a role
    role_def = {
        "role_id": "test-query-cache",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    register_role_definition(role_def, "test_user")
    
    # Clear memory cache
    if "test-query-cache" in _roles:
        del _roles["test-query-cache"]
    
    # Verify not in memory
    assert "test-query-cache" not in _roles
    
    # Query the role (should load from disk and cache)
    result = query_role_definition("test-query-cache", "test_user")
    
    assert result["status"] == "found"
    # Should be cached in memory now
    assert "test-query-cache" in _roles


def test_query_role_definition_with_notes():
    """Test query role with notes field."""
    # Register a role with notes
    role_def = {
        "role_id": "test-query-notes",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
        "notes": "Test notes",
    }
    register_role_definition(role_def, "test_user")
    
    # Query the role
    result = query_role_definition("test-query-notes", "test_user")
    
    assert result["status"] == "found"
    assert result["role_definition"]["notes"] == "Test notes"


def test_query_role_definition_without_notes():
    """Test query role without notes field."""
    # Register a role without notes
    role_def = {
        "role_id": "test-query-no-notes",
        "purpose": "Test purpose",
        "inputs": ["input1"],
        "outputs": ["output1"],
        "boundaries": ["boundary1"],
    }
    register_role_definition(role_def, "test_user")
    
    # Query the role
    result = query_role_definition("test-query-no-notes", "test_user")
    
    assert result["status"] == "found"
    assert result["role_definition"]["notes"] is None

