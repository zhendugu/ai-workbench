"""
Unit tests for C-SAFE-1: Execute Health Check

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.health_check import execute_health_check


def test_execute_health_check_success():
    """Test successful health check execution (C-SAFE-1)."""
    component_id = "test_component_1"
    
    result = execute_health_check(component_id)
    
    # Verify success response structure
    assert "health_check_id" in result
    assert "component_id" in result
    assert "health_status" in result
    assert "check_timestamp" in result
    assert "details" in result
    assert result["component_id"] == component_id
    assert result["health_status"] in ["healthy", "unhealthy", "unknown"]
    assert "error" not in result
    
    # Verify health_check_id is a valid UUID format
    assert len(result["health_check_id"]) == 36  # UUID format length
    assert result["health_check_id"].count("-") == 4


def test_execute_health_check_failure():
    """Test health check execution failure path (C-SAFE-1)."""
    # Test failure path by passing invalid component_id
    # This should trigger a ValueError that is caught and returned as structured error
    
    # Pass None as component_id - this should cause a ValueError
    component_id = None
    
    result = execute_health_check(component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    assert result["error_type"] == "ValueError"
    assert "health_check_id" not in result


def test_execute_health_check_empty_component_id():
    """Test health check execution with empty component_id (C-SAFE-1)."""
    # Pass empty string as component_id - this should cause a ValueError
    component_id = ""
    
    result = execute_health_check(component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "health_check_id" not in result

