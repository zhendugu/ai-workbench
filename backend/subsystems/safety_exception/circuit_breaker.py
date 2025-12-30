"""
Circuit breaker state checking for Safety & Exception Handling Subsystem.

C-SAFE-2: Check Circuit Breaker State implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import CircuitBreakerState

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass


# Simple in-memory storage for circuit breaker states
_circuit_breakers: Dict[str, CircuitBreakerState] = {}


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
        # This ensures circuit breaker check capability is not blocked by observability issues
        pass


def _load_circuit_breaker_from_disk(circuit_breaker_id: str) -> Optional[CircuitBreakerState]:
    """
    Load circuit breaker state from disk (MVP: JSON files).
    Returns None if not found.
    """
    try:
        circuit_breakers_dir = Path("backend/subsystems/safety_exception/circuit_breakers")
        circuit_breaker_file = circuit_breakers_dir / f"{circuit_breaker_id}.json"
        
        if not circuit_breaker_file.exists():
            return None
        
        with open(circuit_breaker_file, "r") as f:
            data = json.load(f)
        
        return CircuitBreakerState(
            circuit_breaker_id=data["circuit_breaker_id"],
            state=data["state"],
            failure_count=data["failure_count"],
            failure_threshold=data["failure_threshold"],
            last_state_change=datetime.fromisoformat(data["last_state_change"]),
            timeout_duration=data["timeout_duration"],
        )
    except Exception:
        return None


def check_circuit_breaker_state(circuit_breaker_id: str) -> Dict[str, Any]:
    """
    C-SAFE-2: Check Circuit Breaker State
    
    Accepts circuit breaker identifier, retrieves circuit breaker state from storage,
    and returns circuit breaker state (closed / open / half-open) and state transition timestamp.
    
    Behavior:
    - Passive: Only checks state when explicitly called
    - No Automation: Does NOT automatically open/close circuit breaker
    - No Action: Does NOT modify circuit breaker state
    - Read-Only: Returns current state only
    
    Args:
        circuit_breaker_id: Circuit breaker identifier to check
    
    Returns:
        Success: {
            "circuit_breaker_id": str,
            "state": str ("closed", "open", "half_open"),
            "failure_count": int,
            "failure_threshold": int,
            "last_state_change": str (ISO format),
            "timeout_duration": int (milliseconds)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Circuit breaker state is managed externally (not by this capability).
    This capability only reads state.
    """
    start_time = datetime.utcnow()
    task_id = f"circuit_breaker_check_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not circuit_breaker_id or not isinstance(circuit_breaker_id, str):
            raise ValueError("circuit_breaker_id must be a non-empty string")
        
        # Record observability before execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-2: Check Circuit Breaker State",
            status="in_progress",
            input_data={"circuit_breaker_id": circuit_breaker_id},
            output_data=None,
            duration_ms=0,
        )
        
        # Retrieve circuit breaker state from storage
        # First check in-memory storage
        circuit_breaker_state = _circuit_breakers.get(circuit_breaker_id)
        
        # If not in memory, try loading from disk
        if circuit_breaker_state is None:
            circuit_breaker_state = _load_circuit_breaker_from_disk(circuit_breaker_id)
            # If found on disk, also store in memory for faster access
            if circuit_breaker_state is not None:
                _circuit_breakers[circuit_breaker_id] = circuit_breaker_state
        
        # If still not found, return error
        if circuit_breaker_state is None:
            raise ValueError(f"Circuit breaker not found: {circuit_breaker_id}")
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability after execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-2: Check Circuit Breaker State",
            status="success",
            input_data={"circuit_breaker_id": circuit_breaker_id},
            output_data={
                "circuit_breaker_id": circuit_breaker_id,
                "state": circuit_breaker_state.state,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "circuit_breaker_id": circuit_breaker_state.circuit_breaker_id,
            "state": circuit_breaker_state.state,
            "failure_count": circuit_breaker_state.failure_count,
            "failure_threshold": circuit_breaker_state.failure_threshold,
            "last_state_change": circuit_breaker_state.last_state_change.isoformat(),
            "timeout_duration": circuit_breaker_state.timeout_duration,
        }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-2: Check Circuit Breaker State",
            status="failure",
            input_data={"circuit_breaker_id": circuit_breaker_id},
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {"circuit_breaker_id": circuit_breaker_id},
        }


def _persist_circuit_breaker_state(circuit_breaker_state: CircuitBreakerState) -> None:
    """
    Persist circuit breaker state to disk (MVP: JSON files).
    This is a helper function for testing/initialization, not part of C-SAFE-2.
    """
    try:
        circuit_breakers_dir = Path("backend/subsystems/safety_exception/circuit_breakers")
        circuit_breakers_dir.mkdir(parents=True, exist_ok=True)
        
        circuit_breaker_dict = {
            "circuit_breaker_id": circuit_breaker_state.circuit_breaker_id,
            "state": circuit_breaker_state.state,
            "failure_count": circuit_breaker_state.failure_count,
            "failure_threshold": circuit_breaker_state.failure_threshold,
            "last_state_change": circuit_breaker_state.last_state_change.isoformat(),
            "timeout_duration": circuit_breaker_state.timeout_duration,
        }
        
        circuit_breaker_file = circuit_breakers_dir / f"{circuit_breaker_state.circuit_breaker_id}.json"
        with open(circuit_breaker_file, "w") as f:
            json.dump(circuit_breaker_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        pass

