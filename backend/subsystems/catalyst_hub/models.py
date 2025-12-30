"""
Data models for Catalyst Hub Subsystem (Phase-3 Level 1).

Phase-3 Level 1: Structural only, descriptive definitions.
Catalyst Hub structures are descriptive, not prescriptive or execution-oriented.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class ExceptionType(Enum):
    """
    Exception Type Enum (Phase-3 Level 1)
    
    Represents types of exceptions that may occur in workflows.
    
    This enum is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT trigger detection, handling, or execution.
    
    Values:
    - DEAD_LOOP: Indicates potential infinite loop or repetitive execution
    - INVALID_STATE: Indicates invalid or inconsistent state
    - TIMEOUT: Indicates operation exceeded time limit
    - FAILURE_BUDGET_VIOLATION: Indicates failure budget threshold exceeded
    
    Phase-3 Level 1 Constraints:
    - Enum values only (no detection logic)
    - No behavior implications
    - No execution triggers
    """
    DEAD_LOOP = "dead_loop"
    INVALID_STATE = "invalid_state"
    TIMEOUT = "timeout"
    FAILURE_BUDGET_VIOLATION = "failure_budget_violation"


@dataclass
class RequirementEnvelope:
    """
    Requirement Envelope Structure (Phase-3 Level 1)
    
    Represents an external requirement that may be routed to Cells.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT route, execute, or trigger behavior.
    
    Required fields:
    - requirement_id: Unique identifier for the requirement
    - content: Human-readable requirement content
    - source: Source identifier (human/system/external)
    - created_at: ISO8601 timestamp
    
    Optional fields:
    - priority: Priority level (descriptive only, not prescriptive)
    - metadata: Additional metadata (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - routing_decision, target_cell_id, execution_status
    - Any field that implies routing or execution
    """
    requirement_id: str
    content: str
    source: str
    created_at: str  # ISO8601 timestamp
    priority: Optional[str] = None  # Descriptive only
    metadata: Optional[Dict[str, str]] = None  # Descriptive only


@dataclass
class RoutingHint:
    """
    Routing Hint Structure (Phase-3 Level 1)
    
    Represents a hint about where a requirement might be routed.
    
    This structure is NON-DECISIONAL and DESCRIPTIVE ONLY.
    It does NOT route, execute, or make decisions.
    
    Required fields:
    - hint_id: Unique identifier for the hint
    - requirement_id: Reference to RequirementEnvelope
    - suggested_cell_ids: List of suggested Cell IDs (descriptive only)
    - reasoning: Human-readable reasoning (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - routing_decision, selected_cell_id, execution_status
    - Any field that implies decision-making or routing
    """
    hint_id: str
    requirement_id: str
    suggested_cell_ids: List[str]  # Descriptive only, not prescriptive
    reasoning: str  # Descriptive only


@dataclass
class WorkflowStateSnapshot:
    """
    Workflow State Snapshot Structure (Phase-3 Level 1)
    
    Represents a snapshot of workflow state at a point in time.
    
    This structure is READ-ONLY and DESCRIPTIVE ONLY.
    It does NOT trigger actions, detect exceptions, or influence behavior.
    
    Required fields:
    - snapshot_id: Unique identifier for the snapshot
    - captured_at: ISO8601 timestamp
    - cell_states: Dict mapping cell_id to state (descriptive only)
    - workflow_id: Identifier for the workflow
    
    Forbidden fields (Phase-3 Level 1):
    - analysis, detection_results, trigger_conditions
    - Any field that implies analysis or action triggering
    """
    snapshot_id: str
    captured_at: str  # ISO8601 timestamp
    cell_states: Dict[str, str]  # Descriptive only, read-only
    workflow_id: str


@dataclass
class TriggerCondition:
    """
    Trigger Condition Structure (Phase-3 Level 1)
    
    Represents a condition that might trigger an action (e.g., Task Force creation).
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT trigger actions, create Task Forces, or influence behavior.
    
    Required fields:
    - condition_id: Unique identifier for the condition
    - condition_type: Type of condition (descriptive only)
    - description: Human-readable description (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - trigger_action, task_force_creation, execution_status
    - Any field that implies execution or action triggering
    """
    condition_id: str
    condition_type: str  # Descriptive only
    description: str  # Descriptive only


@dataclass
class HealthCheckRecord:
    """
    Health Check Record Structure (Phase-3 Level 1)
    
    Represents a health check record for the Catalyst Hub.
    
    This structure is RECORD-ONLY and DESCRIPTIVE ONLY.
    It does NOT perform health checks, trigger actions, or influence behavior.
    
    Required fields:
    - check_id: Unique identifier for the health check
    - checked_at: ISO8601 timestamp
    - status: Health status (descriptive only)
    - component: Component identifier being checked
    
    Optional fields:
    - details: Additional details (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - actions_taken, recovery_actions, alert_triggers
    - Any field that implies execution or action triggering
    """
    check_id: str
    checked_at: str  # ISO8601 timestamp
    status: str  # Descriptive only
    component: str
    details: Optional[Dict[str, str]] = None  # Descriptive only


@dataclass
class CostBudgetSnapshot:
    """
    Cost Budget Snapshot Structure (Phase-3 Level 1)
    
    Represents a snapshot of cost/budget information.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT enforce budgets, block operations, or influence behavior.
    
    Required fields:
    - snapshot_id: Unique identifier for the snapshot
    - captured_at: ISO8601 timestamp
    - budget_scope: Scope identifier (descriptive only)
    - currency: Currency code
    
    Optional fields:
    - current_usage: Current usage amount (descriptive only)
    - budget_limit: Budget limit (descriptive only, not enforced)
    - period: Time period for the budget (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - enforcement_status, blocking_status, alert_triggers
    - Any field that implies enforcement or behavior influence
    """
    snapshot_id: str
    captured_at: str  # ISO8601 timestamp
    budget_scope: str  # Descriptive only
    currency: str
    current_usage: Optional[float] = None  # Descriptive only
    budget_limit: Optional[float] = None  # Descriptive only, not enforced
    period: Optional[str] = None  # Descriptive only
