"""
Execution capability for Safety & Exception Handling Subsystem.

C-EXEC-1: Execute Single Action (Real Execution implementation)
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Callable

from .models import ExecutionRequest, ExecutionResult

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
    from backend.subsystems.observability.tracing import record_trace_entry
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass
    def record_trace_entry(*args, **kwargs):
        return {"error": "Observability not available"}

# Import subsystem capabilities for execution
try:
    from backend.subsystems.knowledge_management.storage import (
        store_document,
        retrieve_document,
        check_access_permission,
        detect_knowledge_conflict,
        record_document_version,
    )
except ImportError:
    store_document = None
    retrieve_document = None
    check_access_permission = None
    detect_knowledge_conflict = None
    record_document_version = None

try:
    from backend.subsystems.observability.failure_classification import record_failure_classification
    from backend.subsystems.observability.logging import query_task_log
    from backend.subsystems.observability.metrics import calculate_basic_metrics
except ImportError:
    record_failure_classification = None
    query_task_log = None
    calculate_basic_metrics = None

try:
    from backend.subsystems.safety_exception.health_check import execute_health_check
    from backend.subsystems.safety_exception.circuit_breaker import check_circuit_breaker_state
    from backend.subsystems.safety_exception.exception_detection import detect_exception
    from backend.subsystems.safety_exception.task_output import generate_uncompletable_task_output
    from backend.subsystems.safety_exception.escalation import record_escalation_request
except ImportError:
    execute_health_check = None
    check_circuit_breaker_state = None
    detect_exception = None
    generate_uncompletable_task_output = None
    record_escalation_request = None

try:
    from backend.subsystems.handoff_protocol.validation import validate_handoff_document
    from backend.subsystems.handoff_protocol.formatter import format_handoff_document
except ImportError:
    validate_handoff_document = None
    format_handoff_document = None

try:
    from backend.subsystems.role_management.register_role import register_role_definition
    from backend.subsystems.role_management.query_role import query_role_definition
    from backend.subsystems.role_management.validate_role import validate_role_definition
except ImportError:
    register_role_definition = None
    query_role_definition = None
    validate_role_definition = None


# Simple in-memory storage for execution requests and results (dry-run only)
_execution_requests: Dict[str, ExecutionRequest] = {}
_execution_results: Dict[str, ExecutionResult] = {}


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
        # This ensures execution capability is not blocked by observability issues
        pass


def _validate_action_descriptor(
    action_identifier: str,
    target_subsystem: str,
    action_parameters: Dict[str, Any],
) -> None:
    """
    Validate action descriptor structure.
    Raises ValueError if validation fails.
    """
    if not action_identifier or not isinstance(action_identifier, str):
        raise ValueError("action_identifier must be a non-empty string")
    
    if not target_subsystem or not isinstance(target_subsystem, str):
        raise ValueError("target_subsystem must be a non-empty string")
    
    if not isinstance(action_parameters, dict):
        raise ValueError("action_parameters must be a dictionary")
    
    # Validate target_subsystem is a known subsystem
    valid_subsystems = [
        "knowledge_management",
        "observability",
        "safety_exception",
        "handoff_protocol",
        "role_management",
    ]
    
    if target_subsystem not in valid_subsystems:
        raise ValueError(
            f"target_subsystem must be one of: {', '.join(valid_subsystems)}, "
            f"got '{target_subsystem}'"
        )


def _persist_execution_request(execution_request: ExecutionRequest) -> None:
    """
    Persist execution request to disk (MVP: JSON files).
    """
    try:
        executions_dir = Path("backend/subsystems/safety_exception/executions")
        executions_dir.mkdir(parents=True, exist_ok=True)
        
        request_dict = {
            "execution_id": execution_request.execution_id,
            "action_identifier": execution_request.action_identifier,
            "target_subsystem": execution_request.target_subsystem,
            "action_parameters": execution_request.action_parameters,
            "requested_at": execution_request.requested_at.isoformat(),
            "requested_by": execution_request.requested_by,
        }
        
        request_file = executions_dir / f"{execution_request.execution_id}_request.json"
        with open(request_file, "w") as f:
            json.dump(request_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        pass


def _persist_execution_result(execution_result: ExecutionResult) -> None:
    """
    Persist execution result to disk (MVP: JSON files).
    """
    try:
        executions_dir = Path("backend/subsystems/safety_exception/executions")
        executions_dir.mkdir(parents=True, exist_ok=True)
        
        result_dict = {
            "execution_id": execution_result.execution_id,
            "status": execution_result.status,
            "result_data": execution_result.result_data,
            "error_data": execution_result.error_data,
            "completed_at": execution_result.completed_at.isoformat(),
            "duration_ms": execution_result.duration_ms,
        }
        
        result_file = executions_dir / f"{execution_result.execution_id}_result.json"
        with open(result_file, "w") as f:
            json.dump(result_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        pass


def execute_single_action_dry_run(
    action_identifier: str,
    target_subsystem: str,
    action_parameters: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-EXEC-1: Execute Single Action (DRY-RUN / NO-OP)
    
    Accepts an action descriptor, validates it structurally, logs what WOULD HAVE been executed,
    and returns a structured "execution_preview" object. Performs ZERO real execution.
    
    Behavior:
    - DRY-RUN ONLY: Performs ZERO real execution, ZERO side effects
    - NO REAL ACTION: No filesystem writes (except logs), no state mutation, no external calls
    - NO AUTOMATION: No background jobs, no triggers, no chaining, no scheduling
    - NO DECISION-MAKING: Only accepts explicit human-provided action descriptor
    - OBSERVABILITY REQUIRED: Records entry + exit via Observability (C-OBS-1)
    - FAILURE PATH REQUIRED: Invalid action descriptor, missing parameters, unsupported action type
    
    Args:
        action_identifier: What to execute (e.g., "store_document", "record_task_log")
        target_subsystem: Where to execute (e.g., "knowledge_management", "observability")
        action_parameters: Explicit parameters for the action
        requested_by: Human identifier who requested the execution
    
    Returns:
        Success: {
            "execution_mode": "dry_run",
            "execution_id": str,
            "action_identifier": str,
            "target_subsystem": str,
            "would_execute": str (description of what would have been executed),
            "blocked_reason": "dry_run_mode",
            "execution_preview": Dict[str, Any],
            "timestamp": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: This is a DRY-RUN / NO-OP implementation. It does NOT authorize real execution.
    This does NOT change Phase-2 gate status. This is a rehearsal-only capability.
    """
    start_time = datetime.utcnow()
    task_id = f"execute_action_dry_run_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        _validate_action_descriptor(action_identifier, target_subsystem, action_parameters)
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Record observability BEFORE execution (dry-run entry)
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (DRY-RUN)",
            status="in_progress",
            input_data={
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "action_parameters": action_parameters,
                "requested_by": requested_by,
                "execution_mode": "dry_run",
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Generate execution identifier
        execution_id = str(uuid.uuid4())
        requested_at = datetime.utcnow()
        
        # Create execution request (DS-EXEC-1)
        execution_request = ExecutionRequest(
            execution_id=execution_id,
            action_identifier=action_identifier,
            target_subsystem=target_subsystem,
            action_parameters=action_parameters,
            requested_at=requested_at,
            requested_by=requested_by,
        )
        
        # Store in memory (dry-run only, no real execution)
        _execution_requests[execution_id] = execution_request
        
        # Persist to disk (dry-run record only)
        _persist_execution_request(execution_request)
        
        # Generate execution preview (what WOULD HAVE been executed)
        would_execute_description = (
            f"Would execute action '{action_identifier}' "
            f"on subsystem '{target_subsystem}' "
            f"with parameters: {action_parameters}"
        )
        
        execution_preview = {
            "action_identifier": action_identifier,
            "target_subsystem": target_subsystem,
            "action_parameters": action_parameters,
            "would_execute": would_execute_description,
            "execution_blocked": True,
            "blocked_reason": "dry_run_mode",
            "note": "This is a DRY-RUN. No real execution was performed.",
        }
        
        # Calculate duration
        completed_at = datetime.utcnow()
        duration_ms = int((completed_at - start_time).total_seconds() * 1000)
        
        # Create execution result (DS-EXEC-2) - DRY-RUN result
        execution_result = ExecutionResult(
            execution_id=execution_id,
            status="success",
            result_data={
                "execution_mode": "dry_run",
                "execution_preview": execution_preview,
            },
            error_data=None,
            completed_at=completed_at,
            duration_ms=duration_ms,
        )
        
        # Store in memory (dry-run result only)
        _execution_results[execution_id] = execution_result
        
        # Persist to disk (dry-run result only)
        _persist_execution_result(execution_result)
        
        # Record observability AFTER execution (dry-run exit)
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (DRY-RUN)",
            status="success",
            input_data={
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "dry_run",
            },
            output_data={
                "execution_id": execution_id,
                "execution_mode": "dry_run",
                "blocked_reason": "dry_run_mode",
            },
            duration_ms=duration_ms,
        )
        
        # Return success response (dry-run preview)
        return {
            "execution_mode": "dry_run",
            "execution_id": execution_id,
            "action_identifier": action_identifier,
            "target_subsystem": target_subsystem,
            "would_execute": would_execute_description,
            "blocked_reason": "dry_run_mode",
            "execution_preview": execution_preview,
            "timestamp": completed_at.isoformat(),
        }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (DRY-RUN)",
            status="failure",
            input_data={
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "dry_run",
            },
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "dry_run",
            },
        }


# Action execution mapping: maps (target_subsystem, action_identifier) to execution function
_ACTION_EXECUTION_MAP: Dict[tuple, Callable] = {}

def _initialize_action_map():
    """Initialize action execution mapping."""
    global _ACTION_EXECUTION_MAP
    
    # Knowledge Management actions
    if store_document:
        _ACTION_EXECUTION_MAP[("knowledge_management", "store_document")] = store_document
    if retrieve_document:
        _ACTION_EXECUTION_MAP[("knowledge_management", "retrieve_document")] = retrieve_document
    if check_access_permission:
        _ACTION_EXECUTION_MAP[("knowledge_management", "check_access_permission")] = check_access_permission
    if detect_knowledge_conflict:
        _ACTION_EXECUTION_MAP[("knowledge_management", "detect_knowledge_conflict")] = detect_knowledge_conflict
    if record_document_version:
        _ACTION_EXECUTION_MAP[("knowledge_management", "record_document_version")] = record_document_version
    
    # Observability actions
    if record_task_log:
        _ACTION_EXECUTION_MAP[("observability", "record_task_log")] = record_task_log
    if record_trace_entry:
        _ACTION_EXECUTION_MAP[("observability", "record_trace_entry")] = record_trace_entry
    if record_failure_classification:
        _ACTION_EXECUTION_MAP[("observability", "record_failure_classification")] = record_failure_classification
    if query_task_log:
        _ACTION_EXECUTION_MAP[("observability", "query_task_log")] = query_task_log
    if calculate_basic_metrics:
        _ACTION_EXECUTION_MAP[("observability", "calculate_basic_metrics")] = calculate_basic_metrics
    
    # Safety & Exception Handling actions
    if execute_health_check:
        _ACTION_EXECUTION_MAP[("safety_exception", "execute_health_check")] = execute_health_check
    if check_circuit_breaker_state:
        _ACTION_EXECUTION_MAP[("safety_exception", "check_circuit_breaker_state")] = check_circuit_breaker_state
    if detect_exception:
        _ACTION_EXECUTION_MAP[("safety_exception", "detect_exception")] = detect_exception
    if generate_uncompletable_task_output:
        _ACTION_EXECUTION_MAP[("safety_exception", "generate_uncompletable_task_output")] = generate_uncompletable_task_output
    if record_escalation_request:
        _ACTION_EXECUTION_MAP[("safety_exception", "record_escalation_request")] = record_escalation_request
    
    # Handoff Protocol actions
    if validate_handoff_document:
        _ACTION_EXECUTION_MAP[("handoff_protocol", "validate_handoff_document")] = validate_handoff_document
    if format_handoff_document:
        _ACTION_EXECUTION_MAP[("handoff_protocol", "format_handoff_document")] = format_handoff_document
    
    # Role Management actions
    if register_role_definition:
        _ACTION_EXECUTION_MAP[("role_management", "register_role_definition")] = register_role_definition
    if query_role_definition:
        _ACTION_EXECUTION_MAP[("role_management", "query_role_definition")] = query_role_definition
    if validate_role_definition:
        _ACTION_EXECUTION_MAP[("role_management", "validate_role_definition")] = validate_role_definition

# Initialize action map on module load
_initialize_action_map()


def _execute_action(
    action_identifier: str,
    target_subsystem: str,
    action_parameters: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Execute a single action on a single subsystem.
    
    This function performs the actual execution of the action.
    It does NOT handle observability, validation, or error recovery.
    Those are handled by the caller.
    
    Args:
        action_identifier: What to execute
        target_subsystem: Where to execute
        action_parameters: Parameters for the action
    
    Returns:
        Action execution result (success or failure dict)
    
    Raises:
        ValueError: If action is not supported or parameters are invalid
    """
    # Get execution function from map
    action_key = (target_subsystem, action_identifier)
    execution_func = _ACTION_EXECUTION_MAP.get(action_key)
    
    if not execution_func:
        raise ValueError(
            f"Action '{action_identifier}' on subsystem '{target_subsystem}' is not supported. "
            f"Supported actions: {[k[1] for k in _ACTION_EXECUTION_MAP.keys() if k[0] == target_subsystem]}"
        )
    
    # Execute action with parameters
    # Parameters are passed as keyword arguments
    try:
        result = execution_func(**action_parameters)
        return result
    except TypeError as e:
        # Parameter mismatch - return structured error
        return {
            "error": f"Parameter mismatch for action '{action_identifier}': {str(e)}",
            "error_type": "TypeError",
            "error_details": {
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "action_parameters": action_parameters,
            },
        }
    except Exception as e:
        # Other execution errors - return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
            },
        }


def execute_single_action(
    action_identifier: str,
    target_subsystem: str,
    action_parameters: Dict[str, Any],
    requested_by: str,
) -> Dict[str, Any]:
    """
    C-EXEC-1: Execute Single Action (Real Execution)
    
    Executes one explicit action on one subsystem.
    Performs real execution with full observability.
    
    Behavior:
    - Executes exactly ONE action per call
    - Touches exactly ONE subsystem per call
    - NO chaining, NO workflow, NO dispatch, NO registry
    - NO retry, NO compensation, NO scheduling
    - MUST require explicit human command
    - MUST write observability BEFORE execution
    - MUST return immediately after execution
    - ALL state changes must be manually recoverable
    
    Execution Flow:
    a) Validate input
    b) Write observability entry (C-OBS-1 / C-OBS-2)
    c) Execute single action
    d) Capture result or exception
    e) Write observability exit
    f) Return result
    
    Args:
        action_identifier: What to execute (e.g., "store_document", "record_task_log")
        target_subsystem: Where to execute (e.g., "knowledge_management", "observability")
        action_parameters: Explicit parameters for the action
        requested_by: Human identifier who requested the execution
    
    Returns:
        Success: {
            "execution_mode": "real",
            "execution_id": str,
            "action_identifier": str,
            "target_subsystem": str,
            "result": Dict[str, Any] (action execution result),
            "timestamp": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: This is a REAL execution implementation. It performs actual actions.
    All constraints from SUBSYSTEM_8_PHASE_2_CAPABILITY_BOUNDARY.md must be followed.
    """
    start_time = datetime.utcnow()
    task_id = f"execute_action_{uuid.uuid4()}"
    execution_id = str(uuid.uuid4())
    
    try:
        # Step a) Validate input
        _validate_action_descriptor(action_identifier, target_subsystem, action_parameters)
        
        if not requested_by or not isinstance(requested_by, str):
            raise ValueError("requested_by must be a non-empty string")
        
        # Step b) Write observability entry (BEFORE execution)
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (Real Execution)",
            status="in_progress",
            input_data={
                "execution_id": execution_id,
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "action_parameters": action_parameters,
                "requested_by": requested_by,
                "execution_mode": "real",
            },
            output_data=None,
            duration_ms=0,
        )
        
        # Record trace entry for execution start
        try:
            record_trace_entry(
                task_id=task_id,
                decision_point="execution_start",
                tool_call={
                    "action_identifier": action_identifier,
                    "target_subsystem": target_subsystem,
                    "execution_mode": "real",
                },
            )
        except Exception:
            # Silently fail if trace entry fails - don't block execution
            pass
        
        # Create execution request (DS-EXEC-1)
        requested_at = datetime.utcnow()
        execution_request = ExecutionRequest(
            execution_id=execution_id,
            action_identifier=action_identifier,
            target_subsystem=target_subsystem,
            action_parameters=action_parameters,
            requested_at=requested_at,
            requested_by=requested_by,
        )
        
        # Store in memory
        _execution_requests[execution_id] = execution_request
        
        # Persist to disk
        _persist_execution_request(execution_request)
        
        # Step c) Execute single action
        action_result = _execute_action(
            action_identifier=action_identifier,
            target_subsystem=target_subsystem,
            action_parameters=action_parameters,
        )
        
        # Step d) Capture result or exception
        # Check if action result indicates failure
        if isinstance(action_result, dict) and "error" in action_result:
            # Action execution failed
            execution_status = "failure"
            result_data = {"execution_mode": "real", "action_result": action_result}
            error_data = action_result
        else:
            # Action execution succeeded
            execution_status = "success"
            result_data = {"execution_mode": "real", "action_result": action_result}
            error_data = None
        
        # Calculate duration
        completed_at = datetime.utcnow()
        duration_ms = int((completed_at - start_time).total_seconds() * 1000)
        
        # Create execution result (DS-EXEC-2)
        execution_result = ExecutionResult(
            execution_id=execution_id,
            status=execution_status,
            result_data=result_data,
            error_data=error_data,
            completed_at=completed_at,
            duration_ms=duration_ms,
        )
        
        # Store in memory
        _execution_results[execution_id] = execution_result
        
        # Persist to disk
        _persist_execution_result(execution_result)
        
        # Step e) Write observability exit (AFTER execution)
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (Real Execution)",
            status=execution_status,
            input_data={
                "execution_id": execution_id,
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "real",
            },
            output_data={
                "execution_id": execution_id,
                "execution_mode": "real",
                "execution_status": execution_status,
                "action_result": action_result,
            },
            duration_ms=duration_ms,
        )
        
        # Record trace entry for execution completion
        try:
            record_trace_entry(
                task_id=task_id,
                decision_point="execution_complete",
                tool_call={
                    "execution_id": execution_id,
                    "execution_status": execution_status,
                    "duration_ms": duration_ms,
                },
            )
        except Exception:
            # Silently fail if trace entry fails - don't block execution
            pass
        
        # Step f) Return result
        if execution_status == "success":
            return {
                "execution_mode": "real",
                "execution_id": execution_id,
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "result": action_result,
                "timestamp": completed_at.isoformat(),
            }
        else:
            # Return failure response
            return {
                "execution_mode": "real",
                "execution_id": execution_id,
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "error": action_result.get("error", "Unknown error"),
                "error_type": action_result.get("error_type", "ExecutionError"),
                "error_details": action_result.get("error_details", {}),
                "timestamp": completed_at.isoformat(),
            }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-EXEC-1: Execute Single Action (Real Execution)",
            status="failure",
            input_data={
                "execution_id": execution_id if 'execution_id' in locals() else None,
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "real",
            },
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "action_identifier": action_identifier,
                "target_subsystem": target_subsystem,
                "execution_mode": "real",
            },
        }

