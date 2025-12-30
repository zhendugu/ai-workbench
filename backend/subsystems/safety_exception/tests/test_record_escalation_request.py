"""
Unit tests for C-SAFE-5: Record Escalation Request

Minimal unit tests: success case and failure case.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from backend.subsystems.safety_exception.escalation import record_escalation_request


def test_record_escalation_request_success():
    """Test successful escalation request recording (C-SAFE-5)."""
    escalation_type = "high_risk"
    escalation_reason = "Operation requires human approval"
    component_id = "test_component_1"
    
    result = record_escalation_request(escalation_type, escalation_reason, component_id)
    
    # Verify success response structure
    assert "escalation_id" in result
    assert "escalation_type" in result
    assert "escalation_reason" in result
    assert "component_id" in result
    assert "created_at" in result
    assert "status" in result
    assert result["escalation_type"] == escalation_type
    assert result["escalation_reason"] == escalation_reason
    assert result["component_id"] == component_id
    assert result["status"] == "pending"
    assert "error" not in result
    
    # Verify escalation_id is a valid UUID format
    assert len(result["escalation_id"]) == 36  # UUID format length
    assert result["escalation_id"].count("-") == 4


def test_record_escalation_request_different_types():
    """Test escalation request recording with different escalation types (C-SAFE-5)."""
    test_cases = [
        ("high_risk", "High risk operation detected"),
        ("multiple_failures", "Multiple failures occurred"),
        ("knowledge_conflict", "Knowledge conflict detected"),
        ("unauthorized_behavior", "Unauthorized behavior detected"),
    ]
    
    for escalation_type, escalation_reason in test_cases:
        component_id = f"test_component_{escalation_type}"
        
        result = record_escalation_request(escalation_type, escalation_reason, component_id)
        
        assert "escalation_id" in result
        assert result["escalation_type"] == escalation_type
        assert result["escalation_reason"] == escalation_reason
        assert result["component_id"] == component_id
        assert result["status"] == "pending"
        assert "error" not in result


def test_record_escalation_request_failure():
    """Test escalation request recording failure path (C-SAFE-5)."""
    # Test failure path by passing invalid escalation_type
    escalation_type = None
    escalation_reason = "Test escalation reason"
    component_id = "test_component_1"
    
    result = record_escalation_request(escalation_type, escalation_reason, component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert "error_details" in result
    assert result["error_type"] == "ValueError"
    assert "escalation_id" not in result


def test_record_escalation_request_empty_escalation_type():
    """Test escalation request recording with empty escalation_type (C-SAFE-5)."""
    escalation_type = ""
    escalation_reason = "Test escalation reason"
    component_id = "test_component_1"
    
    result = record_escalation_request(escalation_type, escalation_reason, component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "escalation_id" not in result


def test_record_escalation_request_empty_escalation_reason():
    """Test escalation request recording with empty escalation_reason (C-SAFE-5)."""
    escalation_type = "high_risk"
    escalation_reason = ""
    component_id = "test_component_1"
    
    result = record_escalation_request(escalation_type, escalation_reason, component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "escalation_id" not in result


def test_record_escalation_request_empty_component_id():
    """Test escalation request recording with empty component_id (C-SAFE-5)."""
    escalation_type = "high_risk"
    escalation_reason = "Test escalation reason"
    component_id = ""
    
    result = record_escalation_request(escalation_type, escalation_reason, component_id)
    
    # Verify failure response structure
    assert "error" in result
    assert "error_type" in result
    assert result["error_type"] == "ValueError"
    assert "escalation_id" not in result

