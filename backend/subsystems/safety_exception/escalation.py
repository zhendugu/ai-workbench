"""
Escalation request recording for Safety & Exception Handling Subsystem.

C-SAFE-5: Record Escalation Request implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .models import EscalationRecord

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass


# Simple in-memory storage for escalation records
_escalations: Dict[str, EscalationRecord] = {}


def _record_observability(
    task_id: str,
    goal: str,
    status: str,
    input_data: Any,
    output_data: Any,
    duration_ms: int,
) -> None:
    """
    Minimal Observability recording point.
    Records task log with minimum required fields (DS-OBS-1).
    """
    try:
        record_task_log(
            task_id=task_id,
            goal=goal,
            input_data=input_data,
            output_data=output_data,
            status=status,
            duration=duration_ms,
            cost_estimate=0,
        )
    except Exception:
        # Silently fail if observability recording fails
        # This ensures escalation recording capability is not blocked by observability issues
        pass


def record_escalation_request(
    escalation_type: str,
    escalation_reason: str,
    component_id: str,
) -> Dict[str, Any]:
    """
    C-SAFE-5: Record Escalation Request
    
    Accepts escalation type, escalation reason, and component identifier,
    stores escalation record, assigns escalation identifier, and records escalation timestamp.
    
    Behavior:
    - Passive: Only records when explicitly called
    - No Automation: Does NOT automatically escalate
    - No Action: Does NOT notify humans or trigger escalation workflows
    - Explicit Recording: Stores escalation record, does NOT trigger automatic escalation
    - No Validation: Does NOT judge whether escalation is reasonable or appropriate
    - No External Interaction: Does NOT interact with external systems
    
    Args:
        escalation_type: Escalation type (required, non-empty string)
            Valid values: "high_risk", "multiple_failures", "knowledge_conflict", "unauthorized_behavior"
        escalation_reason: Escalation reason description (required, non-empty string)
        component_id: Component identifier (required, non-empty string)
    
    Returns:
        Success: {
            "escalation_id": str,           # UUID
            "escalation_type": str,
            "escalation_reason": str,
            "component_id": str,
            "created_at": str,              # ISO format timestamp
            "status": str                   # "pending"
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Escalation recording is passive. It does NOT escalate, only records escalation requests.
    It does NOT validate escalation reasonableness, notify humans, or trigger workflows.
    """
    start_time = datetime.utcnow()
    task_id = f"escalation_record_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not escalation_type or not isinstance(escalation_type, str):
            raise ValueError("escalation_type must be a non-empty string")
        if not escalation_reason or not isinstance(escalation_reason, str):
            raise ValueError("escalation_reason must be a non-empty string")
        if not component_id or not isinstance(component_id, str):
            raise ValueError("component_id must be a non-empty string")
        
        # Record observability before execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-5: Record Escalation Request",
            status="in_progress",
            input_data={
                "escalation_type": escalation_type,
                "escalation_reason": escalation_reason,
                "component_id": component_id,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Generate escalation record
        escalation_id = str(uuid.uuid4())
        created_at = datetime.utcnow()
        
        # Status is always "pending" for new escalation records
        # Status changes are managed externally (not by this capability)
        status = "pending"
        
        escalation_record = EscalationRecord(
            escalation_id=escalation_id,
            escalation_type=escalation_type,
            escalation_reason=escalation_reason,
            component_id=component_id,
            created_at=created_at,
            status=status,
        )
        
        # Store in memory
        _escalations[escalation_id] = escalation_record
        
        # Persist to disk (MVP: JSON files)
        _persist_escalation(escalation_record)
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability after execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-5: Record Escalation Request",
            status="success",
            input_data={
                "escalation_type": escalation_type,
                "component_id": component_id,
            },
            output_data={
                "escalation_id": escalation_id,
                "status": status,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "escalation_id": escalation_id,
            "escalation_type": escalation_type,
            "escalation_reason": escalation_reason,
            "component_id": component_id,
            "created_at": created_at.isoformat(),
            "status": status,
        }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-5: Record Escalation Request",
            status="failure",
            input_data={
                "escalation_type": escalation_type,
                "component_id": component_id,
            },
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "escalation_type": escalation_type,
                "component_id": component_id,
            },
        }


def _persist_escalation(escalation_record: EscalationRecord) -> None:
    """
    Persist escalation record to disk (MVP: JSON files).
    """
    try:
        escalations_dir = Path("backend/subsystems/safety_exception/escalations")
        escalations_dir.mkdir(parents=True, exist_ok=True)
        
        escalation_dict = {
            "escalation_id": escalation_record.escalation_id,
            "escalation_type": escalation_record.escalation_type,
            "escalation_reason": escalation_record.escalation_reason,
            "component_id": escalation_record.component_id,
            "created_at": escalation_record.created_at.isoformat(),
            "status": escalation_record.status,
        }
        
        escalation_file = escalations_dir / f"{escalation_record.escalation_id}.json"
        with open(escalation_file, "w") as f:
            json.dump(escalation_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        # This ensures escalation recording capability is not blocked by persistence issues
        pass

