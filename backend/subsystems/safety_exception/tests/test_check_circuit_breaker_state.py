"""
Unit tests for C-SAFE-2: Check Circuit Breaker State

Minimal unit tests: success case and failure case.
"""

import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.circuit_breaker import (
    check_circuit_breaker_state,
    _persist_circuit_breaker_state,
    _circuit_breakers,
)
from backend.subsystems.safety_exception.models import CircuitBreakerState


def test_check_circuit_breaker_state_success():
    """Test successful circuit breaker state check (C-SAFE-2)."""
    # Create a test circuit breaker state
    circuit_breaker_id = "test_circuit_breaker_1"
    test_state = CircuitBreakerState(
        circuit_breaker_id=circuit_breaker_id,
        state="closed",
        failure_count=0,
        failure_threshold=5,
        last_state_change=datetime.utcnow(),
        timeout_duration=1000,
    )
    
    # Store in memory and persist to disk for test
    _circuit_breakers[circuit_breaker_id] = test_state
    _persist_circuit_breaker_state(test_state)
    
    # Check circuit breaker state
    result = check_circuit_breaker_state(circuit_breaker_id)
    
    # Verify success response structure
    assert "circuit_breaker_id" in result
    assert "state" in result
    assert "failure_count" in result
    assert "failure_threshold" in result
    assert "last_state_change" in result
    assert "timeout_duration" in result
    assert result["circuit_breaker_id"] == circuit_breaker_id
    assert result["state"] in ["closed", "open", "half_open"]
    assert result["failure_count"] == 0
    assert result["failure_threshold"] == 5
    assert result["timeout_duration"] == 1000
    assert "error" not in result


def test_check_circuit_breaker_state_not_found():
    """Test circuit breaker state check with non-existent circuit breaker (C-SAFE-2)."""
    # Check non-existent circuit breaker
    circuit_breaker_id = "non_existent_circuit_breaker"
    
    result = check_circuit_breaker_state(circuit_breaker_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    assert "not found" in result["error"].lower() or "circuit_breaker_id" in result["error_details"]
    assert "state" not in result or result.get("state") is None


def test_check_circuit_breaker_state_invalid_id():
    """Test circuit breaker state check with invalid circuit_breaker_id (C-SAFE-2)."""
    # Pass None as circuit_breaker_id - this should cause a ValueError
    circuit_breaker_id = None
    
    result = check_circuit_breaker_state(circuit_breaker_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "state" not in result


def test_check_circuit_breaker_state_empty_id():
    """Test circuit breaker state check with empty circuit_breaker_id (C-SAFE-2)."""
    # Pass empty string as circuit_breaker_id - this should cause a ValueError
    circuit_breaker_id = ""
    
    result = check_circuit_breaker_state(circuit_breaker_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "state" not in result


def test_check_circuit_breaker_state_different_states():
    """Test circuit breaker state check with different states (C-SAFE-2)."""
    # Test "open" state
    circuit_breaker_id_open = "test_circuit_breaker_open"
    test_state_open = CircuitBreakerState(
        circuit_breaker_id=circuit_breaker_id_open,
        state="open",
        failure_count=5,
        failure_threshold=5,
        last_state_change=datetime.utcnow(),
        timeout_duration=2000,
    )
    _circuit_breakers[circuit_breaker_id_open] = test_state_open
    _persist_circuit_breaker_state(test_state_open)
    
    result_open = check_circuit_breaker_state(circuit_breaker_id_open)
    assert result_open["state"] == "open"
    assert result_open["failure_count"] == 5
    
    # Test "half_open" state
    circuit_breaker_id_half_open = "test_circuit_breaker_half_open"
    test_state_half_open = CircuitBreakerState(
        circuit_breaker_id=circuit_breaker_id_half_open,
        state="half_open",
        failure_count=3,
        failure_threshold=5,
        last_state_change=datetime.utcnow(),
        timeout_duration=1500,
    )
    _circuit_breakers[circuit_breaker_id_half_open] = test_state_half_open
    _persist_circuit_breaker_state(test_state_half_open)
    
    result_half_open = check_circuit_breaker_state(circuit_breaker_id_half_open)
    assert result_half_open["state"] == "half_open"
    assert result_half_open["failure_count"] == 3

