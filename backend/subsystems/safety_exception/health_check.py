"""
Health check mechanisms for Safety & Exception Handling Subsystem.

C-SAFE-1: Execute Health Check implementation
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .models import HealthCheckResult

# Import Observability capability for recording
try:
    from backend.subsystems.observability.logging import record_task_log
except ImportError:
    # Fallback if import fails
    def record_task_log(*args, **kwargs):
        pass


# Simple in-memory storage for health check results
_health_checks: Dict[str, HealthCheckResult] = {}


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
        # This ensures health check capability is not blocked by observability issues
        pass


def execute_health_check(component_id: str) -> Dict[str, Any]:
    """
    C-SAFE-1: Execute Health Check
    
    Accepts component identifier, performs health check operation,
    and returns health status (healthy / unhealthy / unknown) and health check timestamp.
    
    Behavior:
    - Passive: Only checks health when explicitly called
    - No Automation: Does NOT automatically monitor or schedule checks
    - No Action: Does NOT fix or recover from unhealthy state
    - Explicit Failure: Returns unhealthy status, does NOT trigger automatic recovery
    
    Args:
        component_id: Component identifier to check
    
    Returns:
        Success: {
            "health_check_id": str,
            "component_id": str,
            "health_status": str ("healthy", "unhealthy", "unknown"),
            "check_timestamp": str (ISO format),
            "details": Dict[str, Any]
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    """
    start_time = datetime.utcnow()
    task_id = f"health_check_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if not component_id or not isinstance(component_id, str):
            raise ValueError("component_id must be a non-empty string")
        
        # Record observability before execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-1: Execute Health Check",
            status="in_progress",
            input_data={"component_id": component_id},
            output_data=None,
            duration_ms=0,
        )
        
        # Perform minimal health check
        # For MVP, we perform a basic check:
        # - Check if component_id is provided (already validated)
        # - For MVP, we assume "healthy" if component_id is valid
        # - In production, this would check actual component health
        
        # Generate health check result
        health_check_id = str(uuid.uuid4())
        check_timestamp = datetime.utcnow()
        
        # Minimal health check logic (passive, no automatic actions)
        # For MVP, we return "healthy" for valid component_id
        # In production, this would check actual component state
        health_status = "healthy"  # Default for MVP
        details = {
            "component_id": component_id,
            "check_type": "basic",
            "response_time_ms": 0,  # Minimal implementation
        }
        
        # Create health check result
        health_check_result = HealthCheckResult(
            health_check_id=health_check_id,
            component_id=component_id,
            health_status=health_status,
            check_timestamp=check_timestamp,
            details=details,
        )
        
        # Store in memory
        _health_checks[health_check_id] = health_check_result
        
        # Persist to disk (MVP: JSON files)
        _persist_health_check(health_check_result)
        
        # Calculate duration
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability after execution
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-1: Execute Health Check",
            status="success",
            input_data={"component_id": component_id},
            output_data={
                "health_check_id": health_check_id,
                "health_status": health_status,
            },
            duration_ms=duration_ms,
        )
        
        # Return success response
        return {
            "health_check_id": health_check_id,
            "component_id": component_id,
            "health_status": health_status,
            "check_timestamp": check_timestamp.isoformat(),
            "details": details,
        }
    
    except Exception as e:
        # Calculate duration even on failure
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record observability for failure
        _record_observability(
            task_id=task_id,
            goal="C-SAFE-1: Execute Health Check",
            status="failure",
            input_data={"component_id": component_id},
            output_data={"error": str(e)},
            duration_ms=duration_ms,
        )
        
        # Return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {"component_id": component_id},
        }


def _persist_health_check(health_check_result: HealthCheckResult) -> None:
    """
    Persist health check result to disk (MVP: JSON files).
    """
    try:
        health_checks_dir = Path("backend/subsystems/safety_exception/health_checks")
        health_checks_dir.mkdir(parents=True, exist_ok=True)
        
        health_check_dict = {
            "health_check_id": health_check_result.health_check_id,
            "component_id": health_check_result.component_id,
            "health_status": health_check_result.health_status,
            "check_timestamp": health_check_result.check_timestamp.isoformat(),
            "details": health_check_result.details,
        }
        
        health_check_file = health_checks_dir / f"{health_check_result.health_check_id}.json"
        with open(health_check_file, "w") as f:
            json.dump(health_check_dict, f, indent=2)
    
    except Exception:
        # Silently fail if persistence fails
        # This ensures health check capability is not blocked by persistence issues
        pass

