"""
Tool Sandbox for Q4-2

Implements 3 mock tools with strict sandboxing:
- schema_lookup: Returns schema fragment
- validate_config: Returns validation errors
- diff_options: Returns diff summary

All tools are pure functions, hashable, no side effects.
"""

import hashlib
import json
from typing import Dict, List, Any


def _hash_object(obj: Any) -> str:
    """Hash any hashable object."""
    if isinstance(obj, (dict, list)):
        return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()
    return hashlib.sha256(str(obj).encode()).hexdigest()


def schema_lookup(input_str: str) -> Dict[str, Any]:
    """
    Tool 1: Schema Lookup
    
    Returns schema fragment for given input.
    Pure function, hashable, no side effects.
    
    Args:
        input_str: Input string to look up
        
    Returns:
        Dictionary containing schema fragment
    """
    # Mock implementation: return deterministic schema fragment
    # In real execution, this would be a pure lookup function
    return {
        "input": input_str,
        "schema_fragment": {
            "type": "object",
            "properties": {
                "field": {"type": "string"}
            }
        },
        "hash": _hash_object(input_str)
    }


def validate_config(candidate_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Tool 2: Validate Config
    
    Returns list of validation errors.
    Pure function, hashable, no side effects.
    
    Args:
        candidate_config: Configuration dictionary to validate
        
    Returns:
        List of validation error dictionaries
    """
    # Mock implementation: return deterministic validation errors
    # In real execution, this would be a pure validation function
    errors = []
    
    # Simple validation: check for required fields
    if "required_field" not in candidate_config:
        errors.append({
            "field": "required_field",
            "error": "missing_required_field",
            "message": "Required field is missing"
        })
    
    return errors


def diff_options(current: Dict[str, Any], candidate: Dict[str, Any]) -> Dict[str, Any]:
    """
    Tool 3: Diff Options
    
    Returns diff summary between current and candidate.
    Pure function, hashable, no side effects.
    
    Args:
        current: Current configuration dictionary
        candidate: Candidate configuration dictionary
        
    Returns:
        Dictionary containing diff summary
    """
    # Mock implementation: return deterministic diff summary
    # In real execution, this would be a pure diff function
    diff_summary = {
        "added": [],
        "removed": [],
        "modified": []
    }
    
    current_keys = set(current.keys())
    candidate_keys = set(candidate.keys())
    
    diff_summary["added"] = list(candidate_keys - current_keys)
    diff_summary["removed"] = list(current_keys - candidate_keys)
    
    for key in current_keys & candidate_keys:
        if current[key] != candidate[key]:
            diff_summary["modified"].append(key)
    
    return {
        "diff": diff_summary,
        "current_hash": _hash_object(current),
        "candidate_hash": _hash_object(candidate)
    }


# Tool registry for auditability
TOOL_REGISTRY = {
    "schema_lookup": schema_lookup,
    "validate_config": validate_config,
    "diff_options": diff_options
}


def get_tool(tool_name: str):
    """Get tool by name (for auditability)."""
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {tool_name}")
    return TOOL_REGISTRY[tool_name]


def list_tools() -> List[str]:
    """List all available tools (for auditability)."""
    return list(TOOL_REGISTRY.keys())

