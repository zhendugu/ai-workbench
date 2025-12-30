"""
Metrics tracking for Observability Subsystem.

C-OBS-5: Calculate Basic Metrics implementation
"""

import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import MetricsSummary, TaskLogRecord


def calculate_basic_metrics(
    time_window: Optional[int] = None,  # Number of recent records (default 100)
    task_id: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    C-OBS-5: Calculate Basic Metrics
    
    Accepts time window, task_id filter, status filter.
    Reads task logs (DS-OBS-1) and optionally failure classifications (DS-OBS-3),
    calculates basic descriptive metrics, and returns MetricsSummary (DS-OBS-4).
    
    Args:
        time_window: Number of recent records to include (default 100)
        task_id: Task identifier filter (optional)
        status: Task status filter (optional, "success", "failure", "in_progress", "cancelled")
    
    Returns:
        Success: {
            "time_range_start": str (ISO format),
            "time_range_end": str (ISO format),
            "total_count": int,
            "success_count": int,
            "failure_count": int,
            "success_rate": float,
            "avg_duration_ms": float,
            "time_window_desc": str,
            "generated_at": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Only uses DS-OBS-4 for output. Reads DS-OBS-1 (and optionally DS-OBS-3).
    Does NOT perform analysis, diagnosis, interpretation, threshold judgment, alerting,
    strategy, action, learning, historical comparison, state machine, or caching.
    Returns descriptive metrics snapshot only.
    """
    start_time = datetime.utcnow()
    metrics_task_id = f"calculate_metrics_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if time_window is not None and (not isinstance(time_window, int) or time_window < 1):
            raise ValueError("time_window must be a positive integer or None")
        if task_id is not None and (not isinstance(task_id, str) or not task_id):
            raise ValueError("task_id must be a non-empty string or None")
        if status is not None and status not in ["success", "failure", "in_progress", "cancelled"]:
            raise ValueError(f"status must be one of: success, failure, in_progress, cancelled, or None, got '{status}'")
        
        # Default time window: last 100 records
        if time_window is None:
            time_window = 100
        
        # Read task logs (DS-OBS-1) - read-only
        from .logging import _task_logs
        
        # Collect matching logs
        matching_logs: List[TaskLogRecord] = []
        
        # Query from in-memory storage
        for log_record in _task_logs.values():
            # Apply filters
            if task_id is not None and log_record.task_id != task_id:
                continue
            if status is not None and log_record.status != status:
                continue
            
            matching_logs.append(log_record)
        
        # Also query from disk (if files exist)
        log_dir = Path("backend/subsystems/observability/logs")
        if log_dir.exists():
            for log_file in log_dir.glob("*.json"):
                try:
                    with open(log_file, "r") as f:
                        disk_log = json.load(f)
                    
                    # Apply filters
                    if task_id is not None and disk_log.get("task_id") != task_id:
                        continue
                    if status is not None and disk_log.get("status") != status:
                        continue
                    
                    # Check if already in memory results (avoid duplicates)
                    if not any(log.log_id == disk_log.get("log_id") for log in matching_logs):
                        # Create TaskLogRecord from disk data
                        disk_record = TaskLogRecord(
                            log_id=disk_log.get("log_id", ""),
                            task_id=disk_log.get("task_id", ""),
                            goal=disk_log.get("goal", ""),
                            input=disk_log.get("input", ""),
                            output=disk_log.get("output", ""),
                            status=disk_log.get("status", ""),
                            duration=disk_log.get("duration", 0),
                            cost_estimate=disk_log.get("cost_estimate", 0),
                            created_at=datetime.fromisoformat(disk_log.get("created_at", datetime.utcnow().isoformat())),
                            completed_at=datetime.fromisoformat(disk_log.get("completed_at", datetime.utcnow().isoformat())),
                        )
                        matching_logs.append(disk_record)
                        
                except Exception:
                    # Skip invalid files
                    continue
        
        # Sort by created_at (most recent first) and apply time window
        matching_logs.sort(key=lambda x: x.created_at, reverse=True)
        matching_logs = matching_logs[:time_window]
        
        # Calculate basic metrics (descriptive only, no analysis)
        total_count = len(matching_logs)
        success_count = sum(1 for log in matching_logs if log.status == "success")
        failure_count = sum(1 for log in matching_logs if log.status == "failure")
        
        # Calculate success rate (descriptive metric)
        success_rate = (success_count / total_count) if total_count > 0 else 0.0
        
        # Calculate average duration (descriptive metric)
        durations = [log.duration for log in matching_logs if log.duration > 0]
        avg_duration_ms = (sum(durations) / len(durations)) if durations else 0.0
        
        # Determine time range
        if matching_logs:
            time_range_start = min(log.created_at for log in matching_logs)
            time_range_end = max(log.created_at for log in matching_logs)
        else:
            time_range_start = datetime.utcnow()
            time_range_end = datetime.utcnow()
        
        # Create time window description
        time_window_desc = f"Last {total_count} records"
        if task_id:
            time_window_desc += f" (task_id: {task_id})"
        if status:
            time_window_desc += f" (status: {status})"
        
        # Create MetricsSummary (DS-OBS-4)
        metrics_summary = MetricsSummary(
            time_range_start=time_range_start,
            time_range_end=time_range_end,
            success_count=success_count,
            failure_count=failure_count,
            average_duration=avg_duration_ms,
            total_cost_estimate=sum(log.cost_estimate for log in matching_logs),
        )
        
        # Record in Observability (using C-OBS-1)
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        from .logging import record_task_log
        record_task_log(
            task_id=metrics_task_id,
            goal="Calculate Basic Metrics (C-OBS-5)",
            input_data={
                "time_window": time_window,
                "task_id": task_id,
                "status": status,
            },
            output_data={
                "total_count": total_count,
                "success_count": success_count,
                "failure_count": failure_count,
            },
            status="success",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        # Return descriptive metrics (DS-OBS-4 format with additional fields)
        return {
            "time_range_start": time_range_start.isoformat(),
            "time_range_end": time_range_end.isoformat(),
            "total_count": total_count,
            "success_count": success_count,
            "failure_count": failure_count,
            "success_rate": round(success_rate, 4),
            "avg_duration_ms": round(avg_duration_ms, 2),
            "time_window_desc": time_window_desc,
            "generated_at": datetime.utcnow().isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record failure in Observability (using C-OBS-1)
        try:
            from .logging import record_task_log
            record_task_log(
                task_id=metrics_task_id,
                goal="Calculate Basic Metrics (C-OBS-5)",
                input_data={
                    "time_window": time_window,
                    "task_id": task_id,
                    "status": status,
                },
                output_data={
                    "error": str(e),
                },
                status="failure",
                duration=duration_ms,
                cost_estimate=0,
            )
        except Exception:
            # If Observability recording fails, continue with error response
            pass
        
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "time_window": time_window,
                "task_id": task_id,
                "status": status,
            },
        }

