"""
Data models for Safety & Exception Handling Subsystem.

DS-SAFE-1: Health Check Result (as defined in MVP_RUNTIME_SURFACE.md)
DS-SAFE-2: Circuit Breaker State (as defined in MVP_RUNTIME_SURFACE.md)
DS-SAFE-3: Exception Detection Result (as defined in MVP_RUNTIME_SURFACE.md)
DS-SAFE-4: Standard Output for Uncompletable Task (as defined in MVP_RUNTIME_SURFACE.md)
DS-SAFE-5: Escalation Record (as defined in MVP_RUNTIME_SURFACE.md)
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class HealthCheckResult:
    """
    DS-SAFE-1: Health Check Result
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - health_check_id: Unique identifier
    - component_id: Component identifier
    - health_status: Health status (healthy, unhealthy, unknown)
    - check_timestamp: Timestamp
    - details: Health check details (response time, error messages, etc.)
    """
    health_check_id: str
    component_id: str
    health_status: str  # "healthy", "unhealthy", "unknown"
    check_timestamp: datetime
    details: Dict[str, Any]


@dataclass
class CircuitBreakerState:
    """
    DS-SAFE-2: Circuit Breaker State
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - circuit_breaker_id: Unique identifier
    - state: Circuit breaker state (closed, open, half_open)
    - failure_count: Current failure count
    - failure_threshold: Failure threshold
    - last_state_change: Timestamp of last state change
    - timeout_duration: Timeout duration in milliseconds
    """
    circuit_breaker_id: str
    state: str  # "closed", "open", "half_open"
    failure_count: int
    failure_threshold: int
    last_state_change: datetime
    timeout_duration: int  # milliseconds


@dataclass
class ExceptionDetectionResult:
    """
    DS-SAFE-3: Exception Detection Result
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - exception_id: Unique identifier
    - component_id: Component identifier
    - operation_type: Operation type
    - exception_type: Exception type (dead_loop, invalid_state, timeout, failure_budget_violation)
    - exception_details: Exception details
    - detected_at: Timestamp
    """
    exception_id: str
    component_id: str
    operation_type: str
    exception_type: str  # "dead_loop", "invalid_state", "timeout", "failure_budget_violation"
    exception_details: Dict[str, Any]
    detected_at: datetime


@dataclass
class StandardOutputForUncompletableTask:
    """
    DS-SAFE-4: Standard Output for Uncompletable Task
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - output_id: Unique identifier
    - task_id: Task identifier
    - reason: Failure reason
    - suggestions: List of suggestions
    - risk_warnings: List of risk warnings
    - generated_at: Timestamp
    """
    output_id: str
    task_id: str
    reason: str
    suggestions: List[str]
    risk_warnings: List[str]
    generated_at: datetime


@dataclass
class EscalationRecord:
    """
    DS-SAFE-5: Escalation Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - escalation_id: Unique identifier
    - escalation_type: Escalation type (high_risk, multiple_failures, knowledge_conflict, unauthorized_behavior)
    - escalation_reason: Escalation reason description
    - component_id: Component identifier
    - created_at: Timestamp
    - status: Escalation status (pending, resolved, escalated_to_human)
    """
    escalation_id: str
    escalation_type: str  # "high_risk", "multiple_failures", "knowledge_conflict", "unauthorized_behavior"
    escalation_reason: str
    component_id: str
    created_at: datetime
    status: str  # "pending", "resolved", "escalated_to_human"


@dataclass
class ExecutionRequest:
    """
    DS-EXEC-1: Execution Request
    
    As defined in SUBSYSTEM_8_PHASE_2_CAPABILITY_BOUNDARY.md:
    - execution_id: Unique identifier
    - action_identifier: What to execute
    - target_subsystem: Where to execute
    - action_parameters: Explicit parameters
    - requested_at: Timestamp
    - requested_by: Human identifier
    """
    execution_id: str
    action_identifier: str
    target_subsystem: str
    action_parameters: Dict[str, Any]
    requested_at: datetime
    requested_by: str


@dataclass
class ExecutionResult:
    """
    DS-EXEC-2: Execution Result
    
    As defined in SUBSYSTEM_8_PHASE_2_CAPABILITY_BOUNDARY.md:
    - execution_id: Reference to request
    - status: success / failure
    - result_data: Execution output
    - error_data: Error information (if failure)
    - completed_at: Timestamp
    - duration_ms: Execution duration
    """
    execution_id: str
    status: str  # "success", "failure"
    result_data: Dict[str, Any]
    error_data: Optional[Dict[str, Any]]
    completed_at: datetime
    duration_ms: int

