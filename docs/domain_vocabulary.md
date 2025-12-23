# Domain Vocabulary

This document defines the core domain concepts used in the system. These are semantic definitions only, not implementation specifications.

## Core Concepts

### Agent (主体)

**What it is:**
- The smallest identifiable unit that can carry state changes and bear responsibility in the system.

**What it is not:**
- Not a user interface
- Not a device
- Not a role collection itself

**System commitment:**
- The system only makes semantic judgments about agents
- Does not directly judge "group entities" unless the group is explicitly defined as an agent

---

### Goal (目标)

**What it is:**
- An explicitly declared, result-oriented direction that can be judged as achieved or not achieved.

**What it is not:**
- Not an infinite goal or vague wish
- Must have a termination condition

**System commitment:**
- The system only judges goal state
- Does not judge whether a goal is "worthwhile", "reasonable", or "moral"

---

### Action Record (行为记录)

**What it is:**
- A discrete event that an agent claims or the system confirms has occurred, related to a goal.

**What it is not:**
- Not an intention
- Not a plan
- Not a speculation

**System commitment:**
- Whether an action "actually occurred" is not the system's concern
- The system only judges: **whether this action can be semantically accepted as a record**

---

### State (状态)

**What it is:**
- An enumerable semantic description of an agent at a specific point in time.

**What it is not:**
- Not a continuous process
- Not a prediction of future state

**System commitment:**
- The system only describes states that can be enumerated
- States are point-in-time snapshots, not continuous flows

---

### Rule (规则)

**What it is:**
- A constraint or condition that determines whether a state change or action is acceptable.

**What it is not:**
- Not a workflow or process
- Not an implementation instruction

**System commitment:**
- The system only judges whether rules are satisfied
- Does not execute or enforce rules directly

---

## Organizational Concepts

### Organization (组织)

**What it is:**
- The structural framework that defines how agents, roles, and cells relate to each other.

**What it is not:**
- Not a fixed hierarchy
- Not a department-based structure

**System commitment:**
- Organization is defined by role boundaries and responsibilities, not by hierarchy

---

### Cell (细胞 / 执行单元)

**What it is:**
- The smallest independently deliverable execution unit, composed of multiple roles.

**What it is not:**
- Not a fixed department
- Not a permanent structure

**System commitment:**
- Cells are cross-functional and end-to-end responsible
- Cells can be dynamically formed and dissolved

---

### Task Force (临时工作小组)

**What it is:**
- A temporary, one-time execution structure formed for a specific goal.

**What it is not:**
- Not a permanent department
- Not a fixed team

**System commitment:**
- Task Forces must have explicit goals, outputs, and dissolution conditions
- Task Forces are temporary by design

---

## Notes

- All definitions are semantic only
- No implementation details are specified here
- These concepts form the vocabulary for system design and communication
- Actual implementation must conform to these semantic definitions

