"""
Failure classification for Observability Subsystem.

C-OBS-3: Record Failure Classification implementation
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .models import FailureClassificationRecord


# Simple in-memory storage for failure classifications
_failure_classifications: Dict[str, FailureClassificationRecord] = {}


def record_failure_classification(
    task_id: str,
    failure_reason: str,
    failure_category: str,
) -> Dict[str, Any]:
    """
    C-OBS-3: Record Failure Classification
    
    Accepts task identifier, failure reason, failure category,
    stores failure classification record, links to task log, and records classification timestamp.
    
    Args:
        task_id: Task identifier (reference to task)
        failure_reason: Failure reason description
        failure_category: Failure category ("timeout", "invalid_input", "system_error", etc.)
    
    Returns:
        Success: {
            "classification_id": str,
            "task_id": str,
            "classified_at": str (ISO format)
        }
        Failure: { "error": str, "error_type": str, "error_details": Any }
    
    Note: Only uses DS-OBS-3. Does NOT use DS-OBS-1, DS-OBS-2, or DS-OBS-4.
    """
    try:
        # Validate inputs
        if not task_id or not isinstance(task_id, str):
            raise ValueError("task_id must be a non-empty string")
        if not failure_reason or not isinstance(failure_reason, str):
            raise ValueError("failure_reason must be a non-empty string")
        if not failure_category or not isinstance(failure_category, str):
            raise ValueError("failure_category must be a non-empty string")
        
        # Generate classification identifier
        classification_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        # Create failure classification record (DS-OBS-3)
        failure_classification = FailureClassificationRecord(
            classification_id=classification_id,
            task_id=task_id,
            failure_reason=failure_reason,
            failure_category=failure_category,
            classified_at=now,
        )
        
        # Store failure classification record (in-memory for MVP)
        _failure_classifications[classification_id] = failure_classification
        
        # Persist to disk (make classifications actually stored)
        classification_dir = Path("backend/subsystems/observability/classifications")
        classification_dir.mkdir(parents=True, exist_ok=True)
        
        classification_file = classification_dir / f"{classification_id}.json"
        classification_dict = {
            "classification_id": failure_classification.classification_id,
            "task_id": failure_classification.task_id,
            "failure_reason": failure_classification.failure_reason,
            "failure_category": failure_classification.failure_category,
            "classified_at": failure_classification.classified_at.isoformat(),
        }
        
        with open(classification_file, "w") as f:
            json.dump(classification_dict, f, indent=2)
        
        # Record in Observability (using C-OBS-1)
        from .logging import record_task_log
        record_task_log(
            task_id=f"classification_{classification_id}",
            goal="Record Failure Classification (C-OBS-3)",
            input_data={
                "task_id": task_id,
                "failure_category": failure_category,
            },
            output_data={
                "classification_id": classification_id,
            },
            status="success",
            duration=0,  # Classification recording is immediate
            cost_estimate=0,
        )
        
        # Return success response
        return {
            "classification_id": classification_id,
            "task_id": task_id,
            "classified_at": now.isoformat(),
        }
        
    except Exception as e:
        # Failure path: return structured error
        # Record failure in Observability (using C-OBS-1)
        try:
            from .logging import record_task_log
            record_task_log(
                task_id=f"classification_error_{uuid.uuid4()}",
                goal="Record Failure Classification (C-OBS-3)",
                input_data={
                    "task_id": task_id if isinstance(task_id, str) else None,
                    "failure_category": failure_category if isinstance(failure_category, str) else None,
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
                "failure_category": failure_category if isinstance(failure_category, str) else None,
            },
        }

