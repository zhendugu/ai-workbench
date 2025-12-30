#!/usr/bin/env python3
"""
Observer - Structured Logging and Metrics (Bypass Isolation)

This module provides structured logging and metrics for Epoch operations.
All observation is BYPASS-ONLY and does not affect Epoch state or decisions.
"""

import json
import hashlib
from typing import Dict, Any, Optional, List
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    """Log levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Observer:
    """
    Observer for Epoch operations (bypass-only).
    
    Properties:
    - Structured logging
    - Metrics collection
    - BYPASS-ONLY: Does not affect Epoch state
    - Does not participate in decisions
    - Strictly isolated from Epoch logic
    """
    
    def __init__(self, epoch_id: Optional[str] = None):
        """
        Initialize observer.
        
        Args:
            epoch_id: Optional Epoch ID for this observer instance
        """
        self._epoch_id = epoch_id
        self._logs: List[Dict[str, Any]] = []
        self._metrics: Dict[str, Any] = {}
        self._destroyed = False
    
    def log(self, level: LogLevel, message: str, data: Optional[Dict[str, Any]] = None):
        """
        Log an event (bypass-only).
        
        Args:
            level: Log level
            message: Log message
            data: Optional additional data
        """
        if self._destroyed:
            return  # Silently ignore after destruction
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "epoch_id": self._epoch_id,
            "level": level.value,
            "message": message,
            "data": data or {}
        }
        
        self._logs.append(log_entry)
    
    def record_metric(self, name: str, value: Any, tags: Optional[Dict[str, str]] = None):
        """
        Record a metric (bypass-only).
        
        Args:
            name: Metric name
            value: Metric value
            tags: Optional tags
        """
        if self._destroyed:
            return  # Silently ignore after destruction
        
        if name not in self._metrics:
            self._metrics[name] = []
        
        metric_entry = {
            "timestamp": datetime.now().isoformat(),
            "epoch_id": self._epoch_id,
            "value": value,
            "tags": tags or {}
        }
        
        self._metrics[name].append(metric_entry)
    
    def get_logs(self) -> List[Dict[str, Any]]:
        """
        Get all logs (copy).
        
        Returns:
            List[Dict]: Copy of logs
        """
        if self._destroyed:
            return []
        return self._logs.copy()
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get all metrics (copy).
        
        Returns:
            Dict: Copy of metrics
        """
        if self._destroyed:
            return {}
        return {k: v.copy() for k, v in self._metrics.items()}
    
    def export_logs_json(self) -> str:
        """
        Export logs as JSON (bypass-only).
        
        Returns:
            str: JSON string
        """
        return json.dumps(self._logs, indent=2)
    
    def export_metrics_json(self) -> str:
        """
        Export metrics as JSON (bypass-only).
        
        Returns:
            str: JSON string
        """
        return json.dumps(self._metrics, indent=2)
    
    def get_state_snapshot(self) -> Dict[str, Any]:
        """
        Get state snapshot for verification (bypass-only).
        
        Returns:
            Dict: State snapshot
        """
        if self._destroyed:
            return {"destroyed": True}
        
        return {
            "epoch_id": self._epoch_id,
            "log_count": len(self._logs),
            "metric_count": len(self._metrics),
            "destroyed": False
        }
    
    def destroy(self):
        """
        Explicitly destroy observer state.
        
        Note: This is BYPASS-ONLY state, but must be destroyed for Epoch isolation.
        """
        self._logs.clear()
        self._metrics.clear()
        self._epoch_id = None
        self._destroyed = True
    
    def is_destroyed(self) -> bool:
        """Check if destroyed."""
        return self._destroyed


# No global state
# No singleton
# No module-level variables
# BYPASS-ONLY: Does not affect Epoch state or decisions

