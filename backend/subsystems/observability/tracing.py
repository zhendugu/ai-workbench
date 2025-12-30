"""
Execution tracing for Observability Subsystem.

C-OBS-2: Record Trace Entry implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import TraceEntryRecord


# Simple in-memory storage for trace entries
_trace_entries: Dict[str, TraceEntryRecord] = {}


def record_trace_entry(
    task_id: str,
    decision_point: str,
    tool_call: Dict[str, Any],
    handoff_document: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-OBS-2: Record Trace Entry
    
    Accepts trace identifier, decision point, tool call, handoff document,
    stores trace entry, links trace entry to task identifier, and records trace timestamp.
    
    Args:
        task_id: Task identifier (reference to task)
        decision_point: Decision point description
        tool_call: Tool call information (dict)
        handoff_document: Handoff document reference (optional)
    
    Returns:
        Success: {
            "trace_id": str,
            "task_id": str,
            "timestamp": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Only uses DS-OBS-2. Does NOT use DS-OBS-1, DS-OBS-3, or DS-OBS-4.
    """
    try:
        # Validate inputs
        if not task_id or not isinstance(task_id, str):
            raise ValueError("task_id must be a non-empty string")
        if not decision_point or not isinstance(decision_point, str):
            raise ValueError("decision_point must be a non-empty string")
        if not isinstance(tool_call, dict):
            raise ValueError("tool_call must be a dictionary")
        if handoff_document is not None and not isinstance(handoff_document, str):
            raise ValueError("handoff_document must be a string or None")
        
        # Generate trace identifier
        trace_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        # Create trace entry record (DS-OBS-2)
        trace_entry = TraceEntryRecord(
            trace_id=trace_id,
            task_id=task_id,
            decision_point=decision_point,
            tool_call=tool_call,
            handoff_document=handoff_document,
            timestamp=now,
        )
        
        # Store trace entry record (in-memory for MVP)
        _trace_entries[trace_id] = trace_entry
        
        # Persist to disk (make traces actually stored)
        trace_dir = Path("backend/subsystems/observability/traces")
        trace_dir.mkdir(parents=True, exist_ok=True)
        
        trace_file = trace_dir / f"{trace_id}.json"
        trace_dict = {
            "trace_id": trace_entry.trace_id,
            "task_id": trace_entry.task_id,
            "decision_point": trace_entry.decision_point,
            "tool_call": trace_entry.tool_call,
            "handoff_document": trace_entry.handoff_document,
            "timestamp": trace_entry.timestamp.isoformat(),
        }
        
        with open(trace_file, "w") as f:
            json.dump(trace_dict, f, indent=2)
        
        # Record in Observability (using C-OBS-1)
        from .logging import record_task_log
        record_task_log(
            task_id=f"trace_{trace_id}",
            goal="Record Trace Entry (C-OBS-2)",
            input_data={
                "task_id": task_id,
                "decision_point": decision_point,
                "tool_call_keys": list(tool_call.keys()),
            },
            output_data={
                "trace_id": trace_id,
            },
            status="success",
            duration=0,  # Trace recording is immediate
            cost_estimate=0,
        )
        
        # Return success response
        return {
            "trace_id": trace_id,
            "task_id": task_id,
            "timestamp": now.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error
        # Record failure in Observability (using C-OBS-1)
        try:
            from .logging import record_task_log
            record_task_log(
                task_id=f"trace_error_{uuid.uuid4()}",
                goal="Record Trace Entry (C-OBS-2)",
                input_data={
                    "task_id": task_id if isinstance(task_id, str) else None,
                    "decision_point": decision_point if isinstance(decision_point, str) else None,
                },
                output_data={
                    "error": str(e),
                },
                status="failure",
                duration=0,
                cost_estimate=0,
            )
        except Exception:
            # If Observability recording fails, continue with error response
            pass
        
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "task_id": task_id if isinstance(task_id, str) else None,
                "decision_point": decision_point if isinstance(decision_point, str) else None,
            },
        }

