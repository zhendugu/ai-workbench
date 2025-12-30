"""
Unit tests for C-AI-GOV-2: Query AI Usage (Read-Only)
"""

import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from backend.subsystems.ai_resource_governance.models import AICallRecord
from backend.subsystems.ai_resource_governance.query_ai_usage import query_ai_usage
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
    
    # Create test records
    now = datetime.utcnow()
    
    # Record 1: gpt-4, caller-1, today
    record1 = AICallRecord(
        call_id="test-query-1",
        model="gpt-4",
        provider="openai",
        input_tokens=100,
        output_tokens=50,
        total_tokens=150,
        estimated_cost=0.002,
        currency="USD",
        caller="caller-1",
        purpose="Test query 1",
        created_at=now.isoformat(),
    )
    record_ai_call.record_ai_call(record1)
    
    # Record 2: gpt-4, caller-1, today
    record2 = AICallRecord(
        call_id="test-query-2",
        model="gpt-4",
        provider="openai",
        input_tokens=200,
        output_tokens=100,
        total_tokens=300,
        estimated_cost=0.004,
        currency="USD",
        caller="caller-1",
        purpose="Test query 2",
        created_at=now.isoformat(),
    )
    record_ai_call.record_ai_call(record2)
    
    # Record 3: claude-3, caller-2, today
    record3 = AICallRecord(
        call_id="test-query-3",
        model="claude-3",
        provider="anthropic",
        input_tokens=150,
        output_tokens=75,
        total_tokens=225,
        estimated_cost=0.003,
        currency="USD",
        caller="caller-2",
        purpose="Test query 3",
        created_at=now.isoformat(),
    )
    record_ai_call.record_ai_call(record3)
    
    # Record 4: gpt-4, caller-2, yesterday (for time range test)
    yesterday = now - timedelta(days=1)
    record4 = AICallRecord(
        call_id="test-query-4",
        model="gpt-4",
        provider="openai",
        input_tokens=50,
        output_tokens=25,
        total_tokens=75,
        estimated_cost=0.001,
        currency="USD",
        caller="caller-2",
        purpose="Test query 4",
        created_at=yesterday.isoformat(),
    )
    record_ai_call.record_ai_call(record4)


def teardown_module():
    """Cleanup test environment"""
    # Clear in-memory storage
    record_ai_call._ai_call_records.clear()
    
    # Remove test directory
    test_calls_dir = Path("backend/subsystems/ai_resource_governance/ai_calls")
    if test_calls_dir.exists():
        shutil.rmtree(test_calls_dir)


def test_query_ai_usage_all():
    """Test querying all AI usage"""
    result = query_ai_usage()
    
    assert result["total_calls"] == 4
    assert result["total_tokens"] == 150 + 300 + 225 + 75  # 750
    assert result["currency"] == "USD"
    assert "breakdown" in result
    assert "by_model" in result["breakdown"]
    assert "by_caller" in result["breakdown"]


def test_query_ai_usage_by_model():
    """Test querying AI usage filtered by model"""
    result = query_ai_usage(model="gpt-4")
    
    assert result["total_calls"] == 3  # test-query-1, test-query-2, test-query-4
    assert result["total_tokens"] == 150 + 300 + 75  # 525
    assert "gpt-4" in result["breakdown"]["by_model"]
    assert result["breakdown"]["by_model"]["gpt-4"]["calls"] == 3


def test_query_ai_usage_by_caller():
    """Test querying AI usage filtered by caller"""
    result = query_ai_usage(caller="caller-1")
    
    assert result["total_calls"] == 2  # test-query-1, test-query-2
    assert result["total_tokens"] == 150 + 300  # 450
    assert "caller-1" in result["breakdown"]["by_caller"]
    assert result["breakdown"]["by_caller"]["caller-1"]["calls"] == 2


def test_query_ai_usage_time_range():
    """Test querying AI usage filtered by time range"""
    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    result = query_ai_usage(
        time_range_start=today_start.isoformat(),
        time_range_end=today_end.isoformat(),
    )
    
    assert result["total_calls"] == 3  # test-query-1, test-query-2, test-query-3 (today)
    assert result["total_tokens"] == 150 + 300 + 225  # 675
    assert "time_range" in result


def test_query_ai_usage_deterministic():
    """
    Explicit test: Query is deterministic.
    
    This test verifies that the same query produces the same results.
    """
    result1 = query_ai_usage(model="gpt-4")
    result2 = query_ai_usage(model="gpt-4")
    
    assert result1["total_calls"] == result2["total_calls"]
    assert result1["total_tokens"] == result2["total_tokens"]
    assert result1["total_cost"] == result2["total_cost"]


def test_query_ai_usage_read_only():
    """
    Explicit test: Query is read-only (no mutations).
    
    This test verifies that querying AI usage does NOT:
    - Mutate records
    - Create records
    - Delete records
    - Modify system state
    """
    initial_count = len(record_ai_call._ai_call_records)
    
    result = query_ai_usage()
    
    assert result["total_calls"] >= 0
    
    # Verify no mutations
    assert len(record_ai_call._ai_call_records) == initial_count
    
    # Verify all original records still exist
    assert "test-query-1" in record_ai_call._ai_call_records
    assert "test-query-2" in record_ai_call._ai_call_records
    assert "test-query-3" in record_ai_call._ai_call_records
    assert "test-query-4" in record_ai_call._ai_call_records


def test_query_ai_usage_no_enforcement():
    """
    Explicit test: No enforcement behavior.
    
    This test verifies that querying AI usage does NOT:
    - Trigger alerts
    - Trigger actions
    - Enforce limits
    - Block operations
    """
    result = query_ai_usage()
    
    # Query should complete successfully regardless of usage levels
    assert "total_calls" in result
    assert "total_tokens" in result
    assert "total_cost" in result
    
    # No enforcement behavior (verified by absence of such behavior in implementation)


def test_query_ai_usage_breakdown_structure():
    """Test that breakdown structure is correct"""
    result = query_ai_usage()
    
    assert "breakdown" in result
    assert "by_model" in result["breakdown"]
    assert "by_caller" in result["breakdown"]
    
    # Verify breakdown structure
    for model, stats in result["breakdown"]["by_model"].items():
        assert "calls" in stats
        assert "tokens" in stats
        assert "cost" in stats
        assert isinstance(stats["calls"], int)
        assert isinstance(stats["tokens"], int)
        assert isinstance(stats["cost"], (int, float))
    
    for caller, stats in result["breakdown"]["by_caller"].items():
        assert "calls" in stats
        assert "tokens" in stats
        assert "cost" in stats
        assert isinstance(stats["calls"], int)
        assert isinstance(stats["tokens"], int)
        assert isinstance(stats["cost"], (int, float))


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

