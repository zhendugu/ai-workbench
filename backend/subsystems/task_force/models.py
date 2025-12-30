"""
Data models for Task Force Subsystem (Phase-3 Level 1).

DS-TF-1: TaskForceDefinition Structure
DS-TF-2: TaskForceMember Structure
DS-TF-3: TaskForceGoal Structure
DS-TF-4: TaskForceDissolutionRecord Structure

Phase-3 Level 1: Structural only, descriptive definitions.
Task Force is a conceptual structure, not an executable entity.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TaskForceMember:
    """
    DS-TF-2: Task Force Member Structure (Phase-3 Level 1)
    
    Represents a member of a Task Force.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT execute tasks, trigger actions, or influence behavior.
    
    Required fields:
    - member_id: Unique identifier for the member
    - role_id: Role identifier (reference to Role Management, Phase-2)
    - cell_id: Cell identifier (reference to Cell Composition, Phase-2)
    - capability_contribution: List of capability identifiers this member contributes
    
    Forbidden fields (Phase-3 Level 1):
    - execution_status, task_assignments, workload, availability
    - Any field that implies execution or behavior
    """
    member_id: str
    role_id: str  # Reference to Role Management (Phase-2)
    cell_id: str  # Reference to Cell Composition (Phase-2)
    capability_contribution: List[str]  # List of capability identifiers


@dataclass
class TaskForceGoal:
    """
    DS-TF-3: Task Force Goal Structure (Phase-3 Level 1)
    
    Represents a goal for a Task Force.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT trigger execution, track progress, or influence behavior.
    
    Required fields:
    - goal_id: Unique identifier for the goal
    - description: Human-readable goal description
    - expected_output: Description of expected output
    - success_criteria: List of success criteria (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - progress, status, completion_date, execution_plan
    - Any field that implies execution or tracking
    """
    goal_id: str
    description: str
    expected_output: str
    success_criteria: List[str]  # Descriptive only, not prescriptive


@dataclass
class TaskForceDefinition:
    """
    DS-TF-1: Task Force Definition Structure (Phase-3 Level 1)
    
    Represents a Task Force definition.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT execute tasks, orchestrate workflows, or influence behavior.
    
    Required fields:
    - task_force_id: Unique identifier for the Task Force
    - name: Human-readable name
    - members: List of TaskForceMember
    - goals: List of TaskForceGoal
    - dissolution_conditions: List of dissolution condition descriptions (descriptive only)
    - created_by: Human identifier who created the Task Force
    - created_at: ISO8601 timestamp
    
    Forbidden fields (Phase-3 Level 1):
    - state, status, lifecycle, execution_history, runtime_info
    - Any field that implies execution, orchestration, or behavior
    """
    task_force_id: str
    name: str
    members: List[TaskForceMember]
    goals: List[TaskForceGoal]
    dissolution_conditions: List[str]  # Descriptive only, not prescriptive
    created_by: str
    created_at: str  # ISO8601 timestamp


@dataclass
class TaskForceDissolutionRecord:
    """
    DS-TF-4: Task Force Dissolution Record Structure (Phase-3 Level 1)
    
    Represents a record of Task Force dissolution.
    
    This structure is DESCRIPTIVE ONLY, not prescriptive.
    It does NOT trigger dissolution, execute cleanup, or influence behavior.
    
    Required fields:
    - task_force_id: Unique identifier for the dissolved Task Force
    - dissolved_by: Human identifier who dissolved the Task Force
    - dissolved_at: ISO8601 timestamp
    - dissolution_reason: Human-readable reason for dissolution
    - methodology_summary: Optional summary of methodology used (descriptive only)
    
    Forbidden fields (Phase-3 Level 1):
    - cleanup_actions, recovery_actions, next_steps
    - Any field that implies execution or behavior
    """
    task_force_id: str
    dissolved_by: str
    dissolved_at: str  # ISO8601 timestamp
    dissolution_reason: str
    methodology_summary: Optional[str] = None  # Descriptive only
