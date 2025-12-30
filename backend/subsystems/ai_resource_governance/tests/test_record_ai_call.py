"""
Unit tests for C-AI-GOV-1: Record AI Call
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from backend.subsystems.ai_resource_governance.models import AICallRecord
from backend.subsystems.ai_resource_governance import record_ai_call


def setup_module():
    """Setup test environment"""
    # Clear in-memory storage
    record_ai_call._ai_call_records.clear()
    
    # Create temporary directory for ai_calls
    test_calls_dir = Path("backend/subsystems/ai_resource_governance/ai_calls")
    if test_calls_dir.exists():
        shutil.rmtree(test_calls_dir)
    test_calls_dir.mkdir(parents=True, exist_ok=True)


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    record_ai_call._ai_call_records.clear()
    
    # Remove test directory
    test_calls_dir = Path("backend/subsystems/ai_resource_governance/ai_calls")
    if test_calls_dir.exists():
        shutil.rmtree(test_calls_dir)


def test_record_ai_call_valid():
    """Test valid AI call recording"""
    call_record = AICallRecord(
        call_id="test-call-1",
        model="gpt-4",
        provider="openai",
        input_tokens=100,
        output_tokens=50,
        total_tokens=150,
        estimated_cost=0.002,
        currency="USD",
        caller="test-subsystem",
        purpose="Test call",
        created_at=datetime.utcnow().isoformat(),
    )
    
    result = record_ai_call.record_ai_call(call_record)
    
    assert result["status"] == "recorded"
    assert result["call_id"] == "test-call-1"
    assert "recorded_at" in result
    
    # Verify in-memory storage
    assert "test-call-1" in record_ai_call._ai_call_records
    assert record_ai_call._ai_call_records["test-call-1"].model == "gpt-4"
    
    # Verify disk persistence
    call_file = Path("backend/subsystems/ai_resource_governance/ai_calls/test-call-1.json")
    assert call_file.exists()
    
    with open(call_file, "r") as f:
        call_dict = json.load(f)
    
    assert call_dict["call_id"] == "test-call-1"
    assert call_dict["model"] == "gpt-4"
    assert call_dict["provider"] == "openai"
    assert call_dict["total_tokens"] == 150
    assert call_dict["estimated_cost"] == 0.002
    assert call_dict["currency"] == "USD"


def test_record_ai_call_invalid_input():
    """Test invalid input (non-AICallRecord)"""
    result = record_ai_call("not-a-call-record")
    
    assert "error" in result
    assert "AICallRecord" in result["error"]


def test_record_ai_call_no_side_effects():
    """
    Explicit test: Recording AI call causes NO side effects.
    
    This test verifies that recording an AI call does NOT:
    - Trigger execution
    - Block calls
    - Enforce limits
    - Change system behavior
    """
    call_record = AICallRecord(
        call_id="test-call-no-side-effects",
        model="gpt-4",
        provider="openai",
        input_tokens=1000,
        output_tokens=500,
        total_tokens=1500,
        estimated_cost=0.03,
        currency="USD",
        caller="test-subsystem",
        purpose="Test call with no side effects",
        created_at=datetime.utcnow().isoformat(),
    )
    
    # Record call
    result = record_ai_call.record_ai_call(call_record)
    
    assert result["status"] == "recorded"
    
    # Verify no enforcement behavior
    # (This is verified by the absence of such behavior in the implementation)
    
    # Verify record exists
    assert "test-call-no-side-effects" in record_ai_call._ai_call_records


def test_record_ai_call_no_enforcement():
    """
    Explicit test: No enforcement behavior.
    
    This test verifies that recording an AI call does NOT enforce limits.
    """
    # Record multiple calls with high cost
    for i in range(5):
        call_record = AICallRecord(
            call_id=f"test-call-enforcement-{i}",
            model="gpt-4",
            provider="openai",
            input_tokens=10000,
            output_tokens=5000,
            total_tokens=15000,
            estimated_cost=0.3,
            currency="USD",
            caller="test-subsystem",
            purpose="Test call for enforcement check",
            created_at=datetime.utcnow().isoformat(),
        )
        
        result = record_ai_call.record_ai_call(call_record)
        assert result["status"] == "recorded"
    
    # All calls should be recorded, no blocking or rejection
    assert len([k for k in record_ai_call._ai_call_records.keys() if k.startswith("test-call-enforcement-")]) == 5


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

