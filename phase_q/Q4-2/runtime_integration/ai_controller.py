"""
AI Controller for Q4-2

Schedules AI-CORE operations within epoch boundaries.
Ensures epoch isolation and no cross-epoch state inheritance.
"""

from typing import Dict, Any, Optional
import sys
from pathlib import Path

# Handle both relative and absolute imports
try:
    from .ai_context import EpochLocalContext
    from .tool_sandbox import get_tool, list_tools
except ImportError:
    # Fallback for direct execution
    _parent_dir = Path(__file__).parent
    sys.path.insert(0, str(_parent_dir))
    import ai_context
    import tool_sandbox
    EpochLocalContext = ai_context.EpochLocalContext
    get_tool = tool_sandbox.get_tool
    list_tools = tool_sandbox.list_tools


class AIController:
    """
    AI Controller for epoch-local AI operations.
    
    Constraints:
    - All operations must be within epoch boundaries
    - No cross-epoch state persistence
    - No automatic execution or decision-making
    """
    
    def __init__(self, epoch_id: str):
        """
        Initialize AI controller for an epoch.
        
        Args:
            epoch_id: Unique epoch identifier
        """
        self.epoch_id = epoch_id
        self.context = EpochLocalContext(epoch_id)
        self._epoch_active = True
        
    def start_epoch(self) -> None:
        """Start epoch (initialize context)."""
        self._epoch_active = True
        self.context = EpochLocalContext(self.epoch_id)
        
    def end_epoch(self) -> None:
        """
        End epoch (clear all epoch-local state).
        
        This ensures no cross-epoch state inheritance.
        """
        self._epoch_active = False
        self.context.clear()
        
    def plan_step(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform single-step planning (depth=1).
        
        Args:
            input_data: Planning input
            
        Returns:
            Planning result (information only, no execution)
        """
        if not self._epoch_active:
            raise RuntimeError("Epoch not active")
            
        # Single-step planning (no multi-turn chains)
        plan_result = {
            "step": 1,
            "input": input_data,
            "candidate_actions": [],
            "information_only": True
        }
        
        self.context.record_planning_step(plan_result)
        return plan_result
        
    def call_tool(self, tool_name: str, tool_input: Any) -> Dict[str, Any]:
        """
        Call a tool (within epoch boundaries).
        
        Args:
            tool_name: Name of tool to call
            tool_input: Tool input
            
        Returns:
            Tool result
        """
        if not self._epoch_active:
            raise RuntimeError("Epoch not active")
            
        # Get tool from sandbox
        tool = get_tool(tool_name)
        
        # Handle different tool signatures
        if tool_name == "diff_options":
            # diff_options requires two arguments
            if isinstance(tool_input, dict) and "current" in tool_input and "candidate" in tool_input:
                tool_output = tool(tool_input["current"], tool_input["candidate"])
            else:
                # Default mock inputs
                tool_output = tool({"default": "current"}, {"default": "candidate"})
        else:
            # Single argument tools
            tool_output = tool(tool_input)
        
        # Record tool call for auditability
        self.context.record_tool_call(tool_name, tool_input, tool_output)
        
        return {
            "tool": tool_name,
            "input": tool_input,
            "output": tool_output,
            "epoch_id": self.epoch_id
        }
        
    def summarize_result(self, tool_results: list) -> Dict[str, Any]:
        """
        Summarize tool results (information only).
        
        Args:
            tool_results: List of tool results
            
        Returns:
            Summary (information only, no recommendations)
        """
        if not self._epoch_active:
            raise RuntimeError("Epoch not active")
            
        summary = {
            "tool_count": len(tool_results),
            "results": tool_results,
            "information_only": True,
            "no_recommendations": True
        }
        
        return summary
        
    def get_state_hash(self) -> str:
        """
        Get hash of current controller state.
        
        Returns:
            SHA256 hash of controller state
        """
        return self.context.get_state_hash()
        
    def is_epoch_active(self) -> bool:
        """Check if epoch is active."""
        return self._epoch_active

