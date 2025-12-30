"""
Standard output generation for uncompletable tasks for Safety & Exception Handling Subsystem.

C-SAFE-4: Generate Standard Output for Uncompletable Task implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .models import StandardOutputForUncompletableTask

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass


# Simple in-memory storage for task outputs
_task_outputs: Dict[str, StandardOutputForUncompletableTask] = {}


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
        # This ensures task output generation capability is not blocked by observability issues
        pass


def _generate_descriptive_suggestions(failure_reason: str) -> List[str]:
    """
    Generate descriptive suggestions based on failure reason.
    
    Note: These are descriptive information only, not action recommendations.
    They describe "what might have happened" or "what conditions might exist",
    not "what should be done".
    """
    suggestions = []
    
    # Generate descriptive information based on failure reason
    # These are observations, not recommendations
    
    if "timeout" in failure_reason.lower():
        suggestions.append("Operation duration exceeded expected time window")
        suggestions.append("System may have been under high load during execution")
    
    if "invalid" in failure_reason.lower() or "invalid_state" in failure_reason.lower():
        suggestions.append("System state did not match expected conditions")
        suggestions.append("State transition may have occurred during operation")
    
    if "dead_loop" in failure_reason.lower():
        suggestions.append("Operation repeated identical steps multiple times")
        suggestions.append("Termination condition may not have been reached")
    
    if "failure_budget" in failure_reason.lower():
        suggestions.append("Failure count exceeded configured threshold")
        suggestions.append("Multiple previous attempts may have failed")
    
    if "permission" in failure_reason.lower() or "access" in failure_reason.lower():
        suggestions.append("Access control rules prevented operation completion")
        suggestions.append("Required permissions may not have been granted")
    
    if "conflict" in failure_reason.lower():
        suggestions.append("Conflicting information or state detected")
        suggestions.append("Multiple versions or states may exist simultaneously")
    
    # If no specific suggestions, provide generic descriptive information
    if not suggestions:
        suggestions.append("Task execution encountered conditions that prevented completion")
        suggestions.append("System state or input conditions did not allow successful completion")
    
    return suggestions


def _generate_descriptive_risk_warnings(failure_reason: str) -> List[str]:
    """
    Generate descriptive risk warnings based on failure reason.
    
    Note: These are descriptive information only, not action recommendations.
    They describe "what risks exist" or "what conditions are present",
    not "what should be avoided" or "what actions to take".
    """
    risk_warnings = []
    
    # Generate descriptive risk information based on failure reason
    # These are observations, not recommendations
    
    if "timeout" in failure_reason.lower():
        risk_warnings.append("Operation may have been interrupted or incomplete")
        risk_warnings.append("System resources may have been unavailable")
    
    if "invalid" in failure_reason.lower() or "invalid_state" in failure_reason.lower():
        risk_warnings.append("System state may be inconsistent or unexpected")
        risk_warnings.append("State transitions may have occurred unexpectedly")
    
    if "dead_loop" in failure_reason.lower():
        risk_warnings.append("Operation may continue indefinitely without progress")
        risk_warnings.append("Termination conditions may not be properly defined")
    
    if "failure_budget" in failure_reason.lower():
        risk_warnings.append("System may be experiencing repeated failures")
        risk_warnings.append("Underlying conditions may persist across attempts")
    
    if "permission" in failure_reason.lower() or "access" in failure_reason.lower():
        risk_warnings.append("Access control configuration may restrict required operations")
        risk_warnings.append("Permission requirements may not be met")
    
    if "conflict" in failure_reason.lower():
        risk_warnings.append("Conflicting information may lead to inconsistent system state")
        risk_warnings.append("Multiple versions or states may require resolution")
    
    # If no specific risk warnings, provide generic descriptive information
    if not risk_warnings:
        risk_warnings.append("Task completion failure may indicate underlying system conditions")
        risk_warnings.append("System state or configuration may require attention")
    
    return risk_warnings


def generate_uncompletable_task_output(
    task_id: str,
    failure_reason: str,
) -> Dict[str, Any]:
    """
    C-SAFE-4: Generate Standard Output for Uncompletable Task
    
    Accepts task identifier and failure reason, generates standard output structure
    with reason, suggestions, and risk warnings, and returns standard output.
    
    Behavior:
    - Passive: Only generates output when explicitly called
    - No Automation: Does NOT automatically generate outputs
    - No Action: Does NOT complete or retry tasks
    - Explicit Output: Returns structured output, does NOT trigger automatic actions
    - Descriptive Only: Suggestions and risk warnings are descriptive information only,
      not action recommendations or decision logic
    - No Escalation: Does NOT trigger C-SAFE-5 or any escalation
    
    Args:
        task_id: Task identifier
        failure_reason: Failure reason description
    
    Returns:
        Success: {
            "output_id": str,
            "task_id": str,
            "reason": str,
            "suggestions": List[str],      # Descriptive information only, not action recommendations
            "risk_warnings": List[str],    # Descriptive information only, not action recommendations
            "generated_at": str            # ISO format timestamp
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Suggestions and risk warnings are descriptive information describing
    "what happened" and "why it cannot be completed", not action recommendations.
    """
    start_time = datetime.utcnow()
    observability_task_id = f"task_output_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not task_id or not isinstance(task_id, str):
            raise ValueError("task_id must be a non-empty string")
        if not failure_reason or not isinstance(failure_reason, str):
            raise ValueError("failure_reason must be a non-empty string")
        
        # Record observability before execution
        _record_observability(
            task_id=observability_task_id,
            goal="C-SAFE-4: Generate Standard Output for Uncompletable Task",
            status="in_progress",
            input_data={
                "task_id": task_id,
                "failure_reason": failure_reason,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Generate descriptive suggestions (not action recommendations)
        suggestions = _generate_descriptive_suggestions(failure_reason)
        
        # Generate descriptive risk warnings (not action recommendations)
        risk_warnings = _generate_descriptive_risk_warnings(failure_reason)
        
        # Generate output record
        output_id = str(uuid.uuid4())
        generated_at = datetime.utcnow()
        
        standard_output = StandardOutputForUncompletableTask(
            output_id=output_id,
            task_id=task_id,
            reason=failure_reason,
            suggestions=suggestions,
            risk_warnings=risk_warnings,
            generated_at=generated_at,
        )
        
        # Store in memory
        _task_outputs[output_id] = standard_output
        
        # Persist to disk (MVP: JSON files)
        _persist_task_output(standard_output)
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability after execution
        _record_observability(
            task_id=observability_task_id,
            goal="C-SAFE-4: Generate Standard Output for Uncompletable Task",
            status="success",
            input_data={
                "task_id": task_id,
                "failure_reason": failure_reason,
            },
            output_data={
                "output_id": output_id,
                "task_id": task_id,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "output_id": output_id,
            "task_id": task_id,
            "reason": failure_reason,
            "suggestions": suggestions,
            "risk_warnings": risk_warnings,
            "generated_at": generated_at.isoformat(),
        }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=observability_task_id,
            goal="C-SAFE-4: Generate Standard Output for Uncompletable Task",
            status="failure",
            input_data={
                "task_id": task_id,
                "failure_reason": failure_reason,
            },
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "task_id": task_id,
                "failure_reason": failure_reason,
            },
        }


def _persist_task_output(standard_output: StandardOutputForUncompletableTask) -> None:
    """
    Persist standard output to disk (MVP: JSON files).
    """
    try:
        task_outputs_dir = Path("backend/subsystems/safety_exception/task_outputs")
        task_outputs_dir.mkdir(parents=True, exist_ok=True)
        
        task_output_dict = {
            "output_id": standard_output.output_id,
            "task_id": standard_output.task_id,
            "reason": standard_output.reason,
            "suggestions": standard_output.suggestions,
            "risk_warnings": standard_output.risk_warnings,
            "generated_at": standard_output.generated_at.isoformat(),
        }
        
        task_output_file = task_outputs_dir / f"{standard_output.output_id}.json"
        with open(task_output_file, "w") as f:
            json.dump(task_output_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        # This ensures task output generation capability is not blocked by persistence issues
        pass

