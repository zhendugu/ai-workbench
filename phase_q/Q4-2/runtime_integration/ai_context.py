"""
AI Context for Q4-2

Manages epoch-local context for AI operations.
Strictly epoch-local: destroyed on epoch end, no cross-epoch persistence.
"""

from typing import Dict, Any, Optional
import hashlib
import json


class EpochLocalContext:
    """
    Epoch-local context container.
    
    All state is destroyed on epoch end.
    No cross-epoch persistence allowed.
    """
    
    def __init__(self, epoch_id: str):
        """
        Initialize epoch-local context.
        
        Args:
            epoch_id: Unique epoch identifier
        """
        self.epoch_id = epoch_id
        self._context: Dict[str, Any] = {}
        self._tool_calls: list = []
        self._planning_steps: list = []
        
    def set(self, key: str, value: Any) -> None:
        """
        Set context value (epoch-local only).
        
        Args:
            key: Context key
            value: Context value (must be hashable)
        """
        self._context[key] = value
        
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get context value.
        
        Args:
            key: Context key
            default: Default value if key not found
            
        Returns:
            Context value or default
        """
        return self._context.get(key, default)
        
    def record_tool_call(self, tool_name: str, input_data: Any, output_data: Any) -> None:
        """
        Record tool call (for auditability).
        
        Args:
            tool_name: Name of tool called
            input_data: Tool input
            output_data: Tool output
        """
        self._tool_calls.append({
            "tool": tool_name,
            "input": input_data,
            "output": output_data,
            "hash": self._hash_interaction(tool_name, input_data, output_data)
        })
        
    def record_planning_step(self, step_data: Dict[str, Any]) -> None:
        """
        Record planning step (for auditability).
        
        Args:
            step_data: Planning step data
        """
        self._planning_steps.append(step_data)
        
    def get_tool_calls(self) -> list:
        """Get all tool calls (read-only)."""
        return self._tool_calls.copy()
        
    def get_planning_steps(self) -> list:
        """Get all planning steps (read-only)."""
        return self._planning_steps.copy()
        
    def get_state_hash(self) -> str:
        """
        Get hash of current context state.
        
        Returns:
            SHA256 hash of context state
        """
        state_data = {
            "epoch_id": self.epoch_id,
            "context": self._context,
            "tool_calls": self._tool_calls,
            "planning_steps": self._planning_steps
        }
        return hashlib.sha256(
            json.dumps(state_data, sort_keys=True).encode()
        ).hexdigest()
        
    def _hash_interaction(self, tool_name: str, input_data: Any, output_data: Any) -> str:
        """Hash tool interaction for auditability."""
        interaction = {
            "tool": tool_name,
            "input": input_data,
            "output": output_data
        }
        return hashlib.sha256(
            json.dumps(interaction, sort_keys=True).encode()
        ).hexdigest()
        
    def clear(self) -> None:
        """
        Clear all context (called on epoch end).
        
        This ensures no cross-epoch state inheritance.
        """
        self._context.clear()
        self._tool_calls.clear()
        self._planning_steps.clear()
        
    def is_empty(self) -> bool:
        """Check if context is empty."""
        return (
            len(self._context) == 0 and
            len(self._tool_calls) == 0 and
            len(self._planning_steps) == 0
        )

