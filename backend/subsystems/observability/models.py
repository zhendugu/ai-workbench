"""
Data models for Observability Subsystem.

DS-OBS-1: Task Log Record (as defined in MVP_RUNTIME_SURFACE.md)
DS-OBS-2: Trace Entry Record (as defined in MVP_RUNTIME_SURFACE.md)
DS-OBS-3: Failure Classification Record (as defined in MVP_RUNTIME_SURFACE.md)
DS-OBS-4: Metrics Summary (as defined in MVP_RUNTIME_SURFACE.md)
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class TaskLogRecord:
    """
    DS-OBS-1: Task Log Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - log_id: Unique identifier
    - task_id: Task identifier
    - goal: Task goal description
    - input: Task input data
    - output: Task output data
    - status: Task status (success, failure, in_progress, cancelled)
    - duration: Duration in milliseconds
    - cost_estimate: Cost estimate (token count, API call count)
    - created_at: Timestamp
    - completed_at: Timestamp
    """
    log_id: str
    task_id: str
    goal: str
    input: Any
    output: Any
    status: str  # "success", "failure", "in_progress", "cancelled"
    duration: int  # milliseconds
    cost_estimate: int
    created_at: datetime
    completed_at: datetime


@dataclass
class TraceEntryRecord:
    """
    DS-OBS-2: Trace Entry Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - trace_id: Unique identifier
    - task_id: Reference to task
    - decision_point: Decision point description
    - tool_call: Tool call information
    - handoff_document: Handoff document reference
    - timestamp: Timestamp
    """
    trace_id: str
    task_id: str
    decision_point: str
    tool_call: Dict[str, Any]
    handoff_document: Optional[str]
    timestamp: datetime


@dataclass
class FailureClassificationRecord:
    """
    DS-OBS-3: Failure Classification Record
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - classification_id: Unique identifier
    - task_id: Reference to task
    - failure_reason: Failure reason description
    - failure_category: Failure category (timeout, invalid_input, system_error, etc.)
    - classified_at: Timestamp
    """
    classification_id: str
    task_id: str
    failure_reason: str
    failure_category: str  # "timeout", "invalid_input", "system_error", etc.
    classified_at: datetime


@dataclass
class MetricsSummary:
    """
    DS-OBS-4: Metrics Summary
    
    As defined in MVP_RUNTIME_SURFACE.md:
    - time_range_start: Start timestamp
    - time_range_end: End timestamp
    - success_count: Number of successful tasks
    - failure_count: Number of failed tasks
    - average_duration: Average duration in milliseconds
    - total_cost_estimate: Total cost estimate
    """
    time_range_start: datetime
    time_range_end: datetime
    success_count: int
    failure_count: int
    average_duration: float
    total_cost_estimate: int

