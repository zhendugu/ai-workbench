"""
Task logging for Observability Subsystem.

C-OBS-1: Record Task Log implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .models import TaskLogRecord


# Simple in-memory storage for task logs
_task_logs: Dict[str, TaskLogRecord] = {}


def record_task_log(
    task_id: str,
    goal: str,
    input_data: Any,
    output_data: Any,
    status: str,
    duration: int,
    cost_estimate: int = 0,
) -> Dict[str, Any]:
    """
    C-OBS-1: Record Task Log
    
    Accepts task identifier, goal, input, output, status, duration, cost estimate,
    stores task log record, assigns log entry identifier, and records log timestamp.
    
    Args:
        task_id: Task identifier
        goal: Task goal description
        input_data: Task input data
        output_data: Task output data
        status: Task status ("success", "failure", "in_progress", "cancelled")
        duration: Duration in milliseconds
        cost_estimate: Cost estimate (token count, API call count), default 0
    
    Returns:
        Success: {
            "log_id": str,
            "task_id": str,
            "created_at": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Goal is to make logs actually stored and queryable.
    Does NOT perform analysis, alerting, threshold judgment, or policy decisions.
    """
    try:
        # Validate inputs
        if not task_id or not isinstance(task_id, str):
            raise ValueError("task_id must be a non-empty string")
        if not goal or not isinstance(goal, str):
            raise ValueError("goal must be a non-empty string")
        if status not in ["success", "failure", "in_progress", "cancelled"]:
            raise ValueError(f"status must be one of: success, failure, in_progress, cancelled, got '{status}'")
        if not isinstance(duration, int) or duration < 0:
            raise ValueError("duration must be a non-negative integer")
        if not isinstance(cost_estimate, int) or cost_estimate < 0:
            raise ValueError("cost_estimate must be a non-negative integer")
        
        # Generate log entry identifier
        log_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        # Create task log record
        task_log = TaskLogRecord(
            log_id=log_id,
            task_id=task_id,
            goal=goal,
            input=input_data,
            output=output_data,
            status=status,
            duration=duration,
            cost_estimate=cost_estimate,
            created_at=now,
            completed_at=now,
        )
        
        # Store task log record (in-memory for MVP)
        _task_logs[log_id] = task_log
        
        # Persist to disk (make logs actually stored)
        log_dir = Path("backend/subsystems/observability/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"{log_id}.json"
        log_dict = {
            "log_id": task_log.log_id,
            "task_id": task_log.task_id,
            "goal": task_log.goal,
            "input": str(task_log.input),
            "output": str(task_log.output),
            "status": task_log.status,
            "duration": task_log.duration,
            "cost_estimate": task_log.cost_estimate,
            "created_at": task_log.created_at.isoformat(),
            "completed_at": task_log.completed_at.isoformat(),
        }
        
        with open(log_file, "w") as f:
            json.dump(log_dict, f, indent=2)
        
        # Return success response
        return {
            "log_id": log_id,
            "task_id": task_id,
            "created_at": now.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "error_details": {
                "task_id": task_id,
                "goal": goal if isinstance(goal, str) else None,
            },
        }


def query_task_log(
    task_id: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 100,
) -> Dict[str, Any]:
    """
    C-OBS-4: Query Task Log
    
    Accepts task identifier or query criteria, returns task log records.
    Only queries and returns raw, unprocessed data. Does NOT perform analysis,
    aggregation, metrics calculation, or trend judgment.
    
    Args:
        task_id: Task identifier (optional, if provided, returns logs for this task)
        status: Task status filter (optional, "success", "failure", "in_progress", "cancelled")
        limit: Maximum number of records to return (default 100)
    
    Returns:
        Success: {
            "task_logs": List[Dict[str, Any]],  # Raw task log records
            "count": int
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Only uses DS-OBS-1. Does NOT use DS-OBS-2, DS-OBS-3, or DS-OBS-4.
    Query ≠ Analyze. Returns raw data only, no analysis or aggregation.
    """
    start_time = datetime.utcnow()
    query_task_id = f"query_task_log_{uuid.uuid4()}"
    
    try:
        # Validate inputs
        if task_id is not None and (not isinstance(task_id, str) or not task_id):
            raise ValueError("task_id must be a non-empty string or None")
        if status is not None and status not in ["success", "failure", "in_progress", "cancelled"]:
            raise ValueError(f"status must be one of: success, failure, in_progress, cancelled, or None, got '{status}'")
        if not isinstance(limit, int) or limit < 1 or limit > 1000:
            raise ValueError("limit must be an integer between 1 and 1000")
        
        # Query from in-memory storage
        matching_logs = []
        
        for log_id, log_record in _task_logs.items():
            # Apply filters
            if task_id is not None and log_record.task_id != task_id:
                continue
            if status is not None and log_record.status != status:
                continue
            
            # Convert to dict (raw, unprocessed data)
            log_dict = {
                "log_id": log_record.log_id,
                "task_id": log_record.task_id,
                "goal": log_record.goal,
                "input": str(log_record.input),
                "output": str(log_record.output),
                "status": log_record.status,
                "duration": log_record.duration,
                "cost_estimate": log_record.cost_estimate,
                "created_at": log_record.created_at.isoformat(),
                "completed_at": log_record.completed_at.isoformat(),
            }
            matching_logs.append(log_dict)
            
            # Apply limit
            if len(matching_logs) >= limit:
                break
        
        # Also query from disk (if files exist)
        log_dir = Path("backend/subsystems/observability/logs")
        if log_dir.exists():
            for log_file in log_dir.glob("*.json"):
                if len(matching_logs) >= limit:
                    break
                
                try:
                    with open(log_file, "r") as f:
                        disk_log = json.load(f)
                    
                    # Apply filters
                    if task_id is not None and disk_log.get("task_id") != task_id:
                        continue
                    if status is not None and disk_log.get("status") != status:
                        continue
                    
                    # Check if already in memory results (avoid duplicates)
                    if not any(log.get("log_id") == disk_log.get("log_id") for log in matching_logs):
                        matching_logs.append(disk_log)
                        
                except Exception:
                    # Skip invalid files
                    continue
        
        # Record in Observability (using C-OBS-1)
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        record_task_log(
            task_id=query_task_id,
            goal="Query Task Log (C-OBS-4)",
            input_data={
                "task_id": task_id,
                "status": status,
                "limit": limit,
            },
            output_data={
                "count": len(matching_logs),
            },
            status="success",
            duration=duration_ms,
            cost_estimate=0,
        )
        
        # Return raw, unprocessed data
        return {
            "task_logs": matching_logs,
            "count": len(matching_logs),
        }
        
    except Exception as e:
        # Failure path: return structured error
        duration_ms = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        # Record failure in Observability (using C-OBS-1)
        try:
            record_task_log(
                task_id=query_task_id,
                goal="Query Task Log (C-OBS-4)",
                input_data={
                    "task_id": task_id,
                    "status": status,
                    "limit": limit,
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
                "task_id": task_id,
                "status": status,
                "limit": limit,
            },
        }

