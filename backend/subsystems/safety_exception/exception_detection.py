"""
Exception detection for Safety & Exception Handling Subsystem.

C-SAFE-3: Detect Exception implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import ExceptionDetectionResult

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass


# Simple in-memory storage for exception detection results
_exceptions: Dict[str, ExceptionDetectionResult] = {}


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
        # This ensures exception detection capability is not blocked by observability issues
        pass


def _check_dead_loop(execution_state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Check for dead loop condition.
    Returns exception details if detected, None otherwise.
    """
    # For MVP, check if execution_state contains repeated operation indicators
    # In production, this would check actual execution history
    
    if not execution_state:
        return None
    
    # Check for repeated operation count
    operation_count = execution_state.get("operation_count", 0)
    max_operations = execution_state.get("max_operations", 100)
    
    if operation_count > max_operations:
        return {
            "operation_count": operation_count,
            "max_operations": max_operations,
            "description": f"Operation count ({operation_count}) exceeds maximum ({max_operations})",
        }
    
    # Check for repeated identical operations
    recent_operations = execution_state.get("recent_operations", [])
    if len(recent_operations) >= 3:
        # Check if last 3 operations are identical
        if len(set(recent_operations[-3:])) == 1:
            return {
                "recent_operations": recent_operations[-3:],
                "description": "Last 3 operations are identical (potential dead loop)",
            }
    
    return None


def _check_invalid_state(execution_state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Check for invalid state condition.
    Returns exception details if detected, None otherwise.
    """
    if not execution_state:
        return None
    
    # Check for invalid state values
    state = execution_state.get("state")
    valid_states = execution_state.get("valid_states", [])
    
    if state is not None and valid_states and state not in valid_states:
        return {
            "current_state": state,
            "valid_states": valid_states,
            "description": f"Current state ({state}) is not in valid states list",
        }
    
    # Check for required state fields
    required_fields = execution_state.get("required_fields", [])
    for field in required_fields:
        if field not in execution_state:
            return {
                "missing_field": field,
                "required_fields": required_fields,
                "description": f"Required field '{field}' is missing",
            }
    
    return None


def _check_timeout(execution_state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Check for timeout condition.
    Returns exception details if detected, None otherwise.
    """
    if not execution_state:
        return None
    
    # Check for timeout
    start_time = execution_state.get("start_time")
    timeout_duration = execution_state.get("timeout_duration")
    current_time = execution_state.get("current_time")
    
    if start_time and timeout_duration and current_time:
        # Calculate elapsed time
        if isinstance(start_time, str):
            start_time = datetime.fromisoformat(start_time)
        if isinstance(current_time, str):
            current_time = datetime.fromisoformat(current_time)
        
        elapsed_ms = int((current_time - start_time).total_seconds() * 1000)
        
        if elapsed_ms > timeout_duration:
            return {
                "elapsed_ms": elapsed_ms,
                "timeout_duration": timeout_duration,
                "description": f"Operation elapsed time ({elapsed_ms}ms) exceeds timeout ({timeout_duration}ms)",
            }
    
    return None


def _check_failure_budget_violation(execution_state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Check for failure budget violation condition.
    Returns exception details if detected, None otherwise.
    """
    if not execution_state:
        return None
    
    # Check for failure budget violation
    failure_count = execution_state.get("failure_count", 0)
    failure_budget = execution_state.get("failure_budget", 10)
    
    if failure_count > failure_budget:
        return {
            "failure_count": failure_count,
            "failure_budget": failure_budget,
            "description": f"Failure count ({failure_count}) exceeds failure budget ({failure_budget})",
        }
    
    return None


def detect_exception(
    component_id: str,
    operation_type: str,
    execution_state: Dict[str, Any],
) -> Dict[str, Any]:
    """
    C-SAFE-3: Detect Exception
    
    Accepts execution context (component identifier, operation type, execution state),
    checks for exception conditions (dead loop, invalid state, timeout, failure budget violation),
    and returns exception detection result (exception detected / no exception) and exception details.
    
    Behavior:
    - Passive: Only detects when explicitly called
    - No Automation: Does NOT automatically monitor or detect
    - No Action: Does NOT resolve or handle exceptions
    - Explicit Detection: Returns detection result, does NOT trigger automatic handling
    - No Escalation: Does NOT automatically create escalation records
    - No Cross-Subsystem: Does NOT interact with circuit breaker or other capabilities
    
    Args:
        component_id: Component identifier
        operation_type: Operation type
        execution_state: Execution state dictionary containing:
            - operation_count: Number of operations performed
            - max_operations: Maximum allowed operations
            - recent_operations: List of recent operations
            - state: Current state value
            - valid_states: List of valid state values
            - required_fields: List of required field names
            - start_time: Operation start time (ISO format or datetime)
            - current_time: Current time (ISO format or datetime)
            - timeout_duration: Timeout duration in milliseconds
            - failure_count: Current failure count
            - failure_budget: Maximum allowed failures
    
    Returns:
        Success (Exception Detected): {
            "exception_detected": True,
            "exception_id": str,
            "component_id": str,
            "operation_type": str,
            "exception_type": str ("dead_loop", "invalid_state", "timeout", "failure_budget_violation"),
            "exception_details": Dict[str, Any],
            "detected_at": str (ISO format)
        }
        Success (No Exception): {
            "exception_detected": False,
            "component_id": str,
            "operation_type": str,
            "detected_at": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    """
    start_time = datetime.utcnow()
    task_id = f"exception_detection_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not component_id or not isinstance(component_id, str):
            raise ValueError("component_id must be a non-empty string")
        if not operation_type or not isinstance(operation_type, str):
            raise ValueError("operation_type must be a non-empty string")
        if not isinstance(execution_state, dict):
            raise ValueError("execution_state must be a dictionary")
        
        # Record observability before execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-3: Detect Exception",
            status="in_progress",
            input_data={
                "component_id": component_id,
                "operation_type": operation_type,
                "execution_state": execution_state,
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Check for exception conditions (in order of priority)
        exception_type = None
        exception_details = None
        
        # 1. Check for dead loop
        dead_loop_details = _check_dead_loop(execution_state)
        if dead_loop_details:
            exception_type = "dead_loop"
            exception_details = dead_loop_details
        
        # 2. Check for invalid state
        if not exception_type:
            invalid_state_details = _check_invalid_state(execution_state)
            if invalid_state_details:
                exception_type = "invalid_state"
                exception_details = invalid_state_details
        
        # 3. Check for timeout
        if not exception_type:
            timeout_details = _check_timeout(execution_state)
            if timeout_details:
                exception_type = "timeout"
                exception_details = timeout_details
        
        # 4. Check for failure budget violation
        if not exception_type:
            failure_budget_details = _check_failure_budget_violation(execution_state)
            if failure_budget_details:
                exception_type = "failure_budget_violation"
                exception_details = failure_budget_details
        
        detected_at = datetime.utcnow()
        
        # If exception detected, create exception detection result
        if exception_type:
            exception_id = str(uuid.uuid4())
            
            exception_detection_result = ExceptionDetectionResult(
                exception_id=exception_id,
                component_id=component_id,
                operation_type=operation_type,
                exception_type=exception_type,
                exception_details=exception_details,
                detected_at=detected_at,
            )
            
            # Store in memory
            _exceptions[exception_id] = exception_detection_result
            
            # Persist to disk (MVP: JSON files)
            _persist_exception(exception_detection_result)
            
            # Calculate duration
            duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            # Record observability after execution
            _record_observability(
                task_id=task_id,
                goal="C-SAFE-3: Detect Exception",
                status="success",
                input_data={
                    "component_id": component_id,
                    "operation_type": operation_type,
                },
                output_data={
                    "exception_detected": True,
                    "exception_id": exception_id,
                    "exception_type": exception_type,
                },
                duration_ms=duration_ms,
            )
            
            # Return exception detected response
            return {
                "exception_detected": True,
                "exception_id": exception_id,
                "component_id": component_id,
                "operation_type": operation_type,
                "exception_type": exception_type,
                "exception_details": exception_details,
                "detected_at": detected_at.isoformat(),
            }
        else:
            # No exception detected
            duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            # Record observability after execution
            _record_observability(
                task_id=task_id,
                goal="C-SAFE-3: Detect Exception",
                status="success",
                input_data={
                    "component_id": component_id,
                    "operation_type": operation_type,
                },
                output_data={
                    "exception_detected": False,
                },
                duration_ms=duration_ms,
            )
            
            # Return no exception response
            return {
                "exception_detected": False,
                "component_id": component_id,
                "operation_type": operation_type,
                "detected_at": detected_at.isoformat(),
            }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-3: Detect Exception",
            status="failure",
            input_data={
                "component_id": component_id,
                "operation_type": operation_type,
            },
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "component_id": component_id,
                "operation_type": operation_type,
            },
        }


def _persist_exception(exception_detection_result: ExceptionDetectionResult) -> None:
    """
    Persist exception detection result to disk (MVP: JSON files).
    """
    try:
        exceptions_dir = Path("backend/subsystems/safety_exception/exceptions")
        exceptions_dir.mkdir(parents=True, exist_ok=True)
        
        exception_dict = {
            "exception_id": exception_detection_result.exception_id,
            "component_id": exception_detection_result.component_id,
            "operation_type": exception_detection_result.operation_type,
            "exception_type": exception_detection_result.exception_type,
            "exception_details": exception_detection_result.exception_details,
            "detected_at": exception_detection_result.detected_at.isoformat(),
        }
        
        exception_file = exceptions_dir / f"{exception_detection_result.exception_id}.json"
        with open(exception_file, "w") as f:
            json.dump(exception_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        # This ensures exception detection capability is not blocked by persistence issues
        pass

