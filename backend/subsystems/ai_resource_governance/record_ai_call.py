"""
AI call recording for AI Resource Governance Subsystem.

C-AI-GOV-1: Record AI Call implementation

Phase-3 Level 1: Descriptive (non-enforcing) AI resource governance.
Records AI calls for observability and querying purposes only.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from backend.subsystems.observability.logging import record_task_log
from .models import AICallRecord


# Simple in-memory storage for AI call records
_ai_call_records: Dict[str, AICallRecord] = {}


def _persist_ai_call_record(call_record: AICallRecord) -> None:
    """
    Persist AI call record to disk as JSON.
    
    File naming: ai_calls/{call_id}.json
    For observability and querying purposes only.
    """
    calls_dir = Path("backend/subsystems/ai_resource_governance/ai_calls")
    calls_dir.mkdir(parents=True, exist_ok=True)
    
    call_file = calls_dir / f"{call_record.call_id}.json"
    
    call_dict = {
        "call_id": call_record.call_id,
        "model": call_record.model,
        "provider": call_record.provider,
        "input_tokens": call_record.input_tokens,
        "output_tokens": call_record.output_tokens,
        "total_tokens": call_record.total_tokens,
        "estimated_cost": call_record.estimated_cost,
        "currency": call_record.currency,
        "caller": call_record.caller,
        "purpose": call_record.purpose,
        "created_at": call_record.created_at,
    }
    
    with open(call_file, "w") as f:
        json.dump(call_dict, f, indent=2)


def record_ai_call(
    call_record: AICallRecord,
) -> Dict[str, Any]:
    """
    C-AI-GOV-1: Record AI Call
    
    Records an AI call for observability and querying purposes only.
    
    Phase-3 Level 1 Constraints:
    - Pure function or service
    - Accepts AICallRecord
    - Writes to Observability
    - No validation beyond type safety
    - No rejection
    - No branching logic
    - No enforcement
    
    Args:
        call_record: AICallRecord instance containing AI call information
    
    Returns:
        Dict with:
        - call_id: str
        - status: "recorded"
        - recorded_at: ISO8601 timestamp
        
        Or error dict with:
        - error: str
        - error_type: str
    
    Raises:
        No exceptions raised. All errors returned as structured dict.
    """
    try:
        # Type safety validation only
        if not isinstance(call_record, AICallRecord):
            raise ValueError(f"call_record must be an AICallRecord instance, got {type(call_record).__name__}")
        
        # Store in memory
        _ai_call_records[call_record.call_id] = call_record
        
        # Persist to disk
        _persist_ai_call_record(call_record)
        
        # Record to Observability (C-OBS-1)
        record_task_log(
            task_id=call_record.call_id,
            goal=f"Record AI Call (C-AI-GOV-1): {call_record.purpose}",
            input_data={
                "model": call_record.model,
                "provider": call_record.provider,
                "caller": call_record.caller,
                "total_tokens": call_record.total_tokens,
                "estimated_cost": call_record.estimated_cost,
                "currency": call_record.currency,
            },
            output_data={
                "call_id": call_record.call_id,
                "status": "recorded",
            },
            status="success",
            duration=0,  # Recording is instantaneous
            cost_estimate=call_record.total_tokens,
        )
        
        recorded_at = datetime.utcnow().isoformat()
        
        return {
            "call_id": call_record.call_id,
            "status": "recorded",
            "recorded_at": recorded_at,
        }
        
    except Exception as e:
        error_response = {
            "error": str(e),
            "error_type": type(e).__name__,
        }
        
        return error_response

