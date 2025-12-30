"""
AI usage querying for AI Resource Governance Subsystem.

C-AI-GOV-2: Query AI Usage (Read-Only) implementation

Phase-3 Level 1: Descriptive (non-enforcing) AI resource governance.
Provides read-only access to AI usage statistics.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import AICallRecord


# Access in-memory storage from record_ai_call module
# Import the module to access the storage variable
def _get_ai_call_records():
    """Get in-memory AI call records from record_ai_call module"""
    try:
        from backend.subsystems.ai_resource_governance import record_ai_call
        return record_ai_call._ai_call_records
    except (ImportError, AttributeError):
        # Fallback to empty dict if module not loaded
        return {}


def _load_ai_call_records_from_disk() -> Dict[str, AICallRecord]:
    """
    Load all AI call records from disk storage.
    
    File naming: ai_calls/{call_id}.json
    
    Returns:
        Dictionary mapping call_id to AICallRecord
    """
    calls_dir = Path("backend/subsystems/ai_resource_governance/ai_calls")
    
    if not calls_dir.exists():
        return {}
    
    records = {}
    
    for call_file in calls_dir.glob("*.json"):
        try:
            with open(call_file, "r") as f:
                call_dict = json.load(f)
            
            call_record = AICallRecord(
                call_id=call_dict["call_id"],
                model=call_dict["model"],
                provider=call_dict["provider"],
                input_tokens=call_dict["input_tokens"],
                output_tokens=call_dict["output_tokens"],
                total_tokens=call_dict["total_tokens"],
                estimated_cost=call_dict["estimated_cost"],
                currency=call_dict["currency"],
                caller=call_dict["caller"],
                purpose=call_dict["purpose"],
                created_at=call_dict["created_at"],
            )
            
            records[call_record.call_id] = call_record
            
        except Exception:
            # Skip invalid files
            continue
    
    return records


def query_ai_usage(
    time_range_start: Optional[str] = None,
    time_range_end: Optional[str] = None,
    model: Optional[str] = None,
    caller: Optional[str] = None,
    scope: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-AI-GOV-2: Query AI Usage (Read-Only)
    
    Provides read-only access to AI usage statistics through aggregation.
    
    Phase-3 Level 1 Constraints:
    - Read-only access
    - Aggregate by time range
    - Aggregate by model
    - Aggregate by caller
    - Aggregate by scope
    - NO filtering that changes behavior
    - NO alerts
    - NO triggers
    - NO enforcement
    
    Args:
        time_range_start: ISO8601 timestamp (optional, inclusive)
        time_range_end: ISO8601 timestamp (optional, inclusive)
        model: AI model identifier (optional, filter by model)
        caller: Subsystem / component name (optional, filter by caller)
        scope: Scope identifier (optional, filter by scope - not implemented in L1, reserved for future)
    
    Returns:
        Dict with:
        - total_calls: int
        - total_tokens: int
        - total_cost: float
        - currency: str (first currency found, or "unknown")
        - breakdown: {
            "by_model": { model: { "calls": int, "tokens": int, "cost": float } },
            "by_caller": { caller: { "calls": int, "tokens": int, "cost": float } },
          }
        - time_range: { "start": str, "end": str } (if provided)
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    try:
        # Load records from memory and disk
        all_records = {}
        all_records.update(_get_ai_call_records())
        all_records.update(_load_ai_call_records_from_disk())
        
        # Filter records based on optional parameters
        filtered_records: List[AICallRecord] = []
        
        for call_record in all_records.values():
            # Time range filter
            if time_range_start:
                try:
                    record_time = datetime.fromisoformat(call_record.created_at.replace('Z', '+00:00'))
                    start_time = datetime.fromisoformat(time_range_start.replace('Z', '+00:00'))
                    if record_time < start_time:
                        continue
                except Exception:
                    # Skip records with invalid timestamps
                    continue
            
            if time_range_end:
                try:
                    record_time = datetime.fromisoformat(call_record.created_at.replace('Z', '+00:00'))
                    end_time = datetime.fromisoformat(time_range_end.replace('Z', '+00:00'))
                    if record_time > end_time:
                        continue
                except Exception:
                    # Skip records with invalid timestamps
                    continue
            
            # Model filter
            if model and call_record.model != model:
                continue
            
            # Caller filter
            if caller and call_record.caller != caller:
                continue
            
            # Scope filter (reserved for future, not implemented in L1)
            # if scope:
            #     continue
            
            filtered_records.append(call_record)
        
        # Aggregate statistics
        total_calls = len(filtered_records)
        total_tokens = sum(record.total_tokens for record in filtered_records)
        total_cost = sum(record.estimated_cost for record in filtered_records)
        
        # Determine currency (use first found, or "unknown")
        currency = "unknown"
        if filtered_records:
            currency = filtered_records[0].currency
        
        # Breakdown by model
        breakdown_by_model: Dict[str, Dict[str, Any]] = {}
        for record in filtered_records:
            if record.model not in breakdown_by_model:
                breakdown_by_model[record.model] = {
                    "calls": 0,
                    "tokens": 0,
                    "cost": 0.0,
                }
            breakdown_by_model[record.model]["calls"] += 1
            breakdown_by_model[record.model]["tokens"] += record.total_tokens
            breakdown_by_model[record.model]["cost"] += record.estimated_cost
        
        # Breakdown by caller
        breakdown_by_caller: Dict[str, Dict[str, Any]] = {}
        for record in filtered_records:
            if record.caller not in breakdown_by_caller:
                breakdown_by_caller[record.caller] = {
                    "calls": 0,
                    "tokens": 0,
                    "cost": 0.0,
                }
            breakdown_by_caller[record.caller]["calls"] += 1
            breakdown_by_caller[record.caller]["tokens"] += record.total_tokens
            breakdown_by_caller[record.caller]["cost"] += record.estimated_cost
        
        result = {
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "total_cost": total_cost,
            "currency": currency,
            "breakdown": {
                "by_model": breakdown_by_model,
                "by_caller": breakdown_by_caller,
            },
        }
        
        # Include time range if provided
        if time_range_start or time_range_end:
            result["time_range"] = {
                "start": time_range_start,
                "end": time_range_end,
            }
        
        return result
        
    except Exception as e:
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        return error_response

