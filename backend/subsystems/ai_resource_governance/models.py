"""
Data models for AI Resource Governance Subsystem (Phase-3 Level 1).

DS-AI-CALL-1: AICallRecord Structure
DS-AI-BUDGET-1: AIBudgetPolicy Structure

Phase-3 Level 1: Descriptive (non-enforcing) AI resource governance.
Structures describe resource usage and limits, but do NOT enforce them.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AICallRecord:
    """
    DS-AI-CALL-1: AI Call Record Structure (Phase-3 Level 1)
    
    Represents a single AI call for recording and querying purposes.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT enforce limits, trigger actions, or influence behavior.
    
    Required fields:
    - call_id: Unique identifier for the AI call
    - model: AI model identifier (e.g., "gpt-4", "claude-3")
    - provider: AI provider identifier (e.g., "openai", "anthropic")
    - input_tokens: Number of input tokens
    - output_tokens: Number of output tokens
    - total_tokens: Total tokens (input + output)
    - estimated_cost: Estimated cost in the specified currency
    - currency: Currency code (e.g., "USD", "CNY")
    - caller: Subsystem / component name that made the call
    - purpose: Human-readable purpose of the call
    - created_at: ISO8601 timestamp of the call
    
    Forbidden fields (Phase-3 Level 1):
    - execution_flags, retry_info, decision_outcomes, enforcement_markers
    - Any field that implies behavior or enforcement
    """
    call_id: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost: float
    currency: str
    caller: str  # subsystem / component name
    purpose: str  # human-readable
    created_at: str  # ISO8601 timestamp


@dataclass
class AIBudgetPolicy:
    """
    DS-AI-BUDGET-1: AI Budget Policy Structure (Phase-3 Level 1)
    
    Descriptive budget / quota structure for informational purposes only.
    
    This structure is INFORMATIONAL ONLY, not prescriptive.
    It does NOT enforce limits, block calls, or trigger actions.
    Violations are NOT enforced.
    Used only for reporting / review.
    
    Required fields:
    - scope: Scope identifier (e.g., "global", "subsystem:<name>", "component:<name>")
    - period: Time period (e.g., "daily", "weekly", "monthly")
    - currency: Currency code (e.g., "USD", "CNY")
    
    Optional fields:
    - model: AI model identifier (optional, None means all models)
    - max_tokens: Maximum tokens per period (optional, None means no limit)
    - max_cost: Maximum cost per period (optional, None means no limit)
    
    Semantics:
    - This structure is INFORMATIONAL ONLY
    - Violations are NOT enforced
    - Used only for reporting / review
    """
    scope: str  # global / subsystem:<name> / component:<name>
    period: str  # daily / weekly / monthly
    currency: str
    model: Optional[str] = None  # None means all models
    max_tokens: Optional[int] = None  # None means no limit
    max_cost: Optional[float] = None  # None means no limit
