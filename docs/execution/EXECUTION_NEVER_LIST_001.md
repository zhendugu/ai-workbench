# Execution Never List 001

**Document ID**: EXECUTION-NEVER-LIST-001

**Status**: FROZEN

**Date**: 2025-12-28

**Authority**: docs/execution/EXECUTION_BOUNDARY_001.md

---

## Purpose

This document explicitly lists vocabulary that is **forbidden** in this system because it implies execution semantics.

**Appearance of these terms outside explicit NOT-ALLOWED sections is a semantic violation.**

---

## Forbidden Vocabulary Categories

### Category 1: Execution Actions

The following terms imply execution of actions and are **forbidden**:

- `run`
- `execute`
- `start`
- `stop`
- `begin`
- `end`
- `launch`
- `trigger`
- `invoke`
- `call` (when referring to function execution, not data retrieval)
- `perform`
- `do`
- `act`
- `carry out`
- `proceed`
- `continue`

**Example Violations**:
- ❌ "Run Cell A"
- ❌ "Execute process X"
- ❌ "Start deployment"
- ❌ "Trigger workflow"

**Allowed Contexts**:
- ✅ "Read-only" (describing UI state)
- ✅ "NOT allowed to run" (in forbidden lists)

### Category 2: Deployment and Activation

The following terms imply deployment or activation and are **forbidden**:

- `deploy`
- `activate`
- `publish`
- `release`
- `go live`
- `go-live`
- `live` (when referring to active state)
- `activate`
- `enable` (when referring to activation)
- `launch`
- `rollout`
- `roll out`

**Example Violations**:
- ❌ "Deploy structure"
- ❌ "Activate system"
- ❌ "Publish Company"
- ❌ "Go live"

**Allowed Contexts**:
- ✅ "NOT deploy" (in forbidden lists)
- ✅ "This does NOT go live" (in disclaimers)

### Category 3: Jobs, Tasks, Processes

The following terms imply job/task/process execution and are **forbidden**:

- `job`
- `task`
- `process` (when referring to execution process)
- `workflow`
- `pipeline`
- `queue`
- `worker`
- `background`
- `async` (when referring to async execution)
- `cron`
- `schedule` (when referring to task scheduling)
- `scheduler`

**Example Violations**:
- ❌ "Background job"
- ❌ "Task queue"
- ❌ "Workflow engine"
- ❌ "Pipeline execution"
- ❌ "Scheduled task"

**Allowed Contexts**:
- ✅ "No task queues" (in forbidden lists)
- ✅ "NOT allowed: workflow engines" (in disclaimers)

### Category 4: Monitoring and Control

The following terms imply monitoring or control of execution and are **forbidden**:

- `monitor`
- `observe`
- `control`
- `manage` (when referring to managing execution)
- `supervise`
- `track` (when referring to tracking execution)
- `watch`
- `oversee`

**Example Violations**:
- ❌ "Monitor execution"
- ❌ "Control process"
- ❌ "Track running jobs"
- ❌ "Manage workflows"

**Allowed Contexts**:
- ✅ "NOT monitor" (in forbidden lists)
- ✅ "Does NOT control" (in disclaimers)

### Category 5: Temporal Execution States

The following terms imply ongoing execution or active state and are **forbidden**:

- `current` (when referring to current execution)
- `live` (when referring to live execution)
- `realtime`
- `real-time`
- `real time`
- `ongoing`
- `active` (when referring to active execution)
- `running`
- `executing`
- `processing`
- `in progress`
- `in-progress`

**Example Violations**:
- ❌ "Current execution"
- ❌ "Live system"
- ❌ "Real-time updates"
- ❌ "Ongoing process"
- ❌ "Active job"
- ❌ "Running workflow"

**Allowed Contexts**:
- ✅ "NOT current" (in forbidden lists)
- ✅ "Does NOT indicate current state" (in disclaimers)
- ✅ "Frozen at [timestamp]" (describing static timestamp)

### Category 6: Agents and Automation

The following terms imply autonomous agents or automation and are **forbidden**:

- `agent` (when referring to autonomous agents)
- `automate`
- `automation`
- `autonomous`
- `automatic`
- `auto` (when referring to automatic execution)

**Example Violations**:
- ❌ "AI agent"
- ❌ "Automation pipeline"
- ❌ "Autonomous system"
- ❌ "Auto-deploy"

**Allowed Contexts**:
- ✅ "No agents allowed" (in forbidden lists)
- ✅ "NOT automated" (in disclaimers)

### Category 7: Event-Driven Execution

The following terms imply event-driven execution and are **forbidden**:

- `event` (when referring to execution events)
- `handler` (when referring to event handlers)
- `listener` (when referring to event listeners)
- `emit` (when referring to emitting events)
- `dispatch` (when referring to dispatching events)
- `subscribe`
- `publish` (when referring to event publishing)

**Example Violations**:
- ❌ "Event handler"
- ❌ "Event listener"
- ❌ "Emit event"
- ❌ "Publish event"

**Allowed Contexts**:
- ✅ "No event handlers" (in forbidden lists)
- ✅ "NOT allowed: event-driven execution" (in disclaimers)

---

## Exception Rules

### Allowed Contexts

The following contexts **explicitly allow** forbidden vocabulary for documentation purposes:

1. **FORBIDDEN TERMS LIST sections**: Lists that document what is NOT allowed
2. **NOT ALLOWED EXAMPLES sections**: Examples showing what is forbidden
3. **Disclaimers**: Statements that explicitly deny execution (e.g., "This does NOT run")
4. **Boundary declarations**: Documents that declare what is outside scope

### Detection Pattern

When scanning for violations, the following patterns indicate **allowed usage**:

- `NOT.*run` - Denial of execution
- `forbidden.*execute` - Documentation of prohibition
- `does not.*trigger` - Explicit denial
- `no.*agents` - Prohibition statement
- `EXECUTION.*NEVER` - Section headers documenting boundaries

---

## Static Enforcement

**Static verification scripts must fail if forbidden vocabulary appears outside allowed contexts.**

The verification script (`scripts/verify-no-execution-semantics.sh`) will:

1. Scan all source files in `src/`, `packages/`, and `docs/`
2. Check for forbidden vocabulary patterns
3. Allow exceptions only in explicitly marked sections:
   - Lines containing `FORBIDDEN TERMS LIST`
   - Lines containing `NOT ALLOWED`
   - Lines containing `does not` / `does NOT` / `DOES NOT`
   - Lines containing `NOT.*allow` / `NOT.*permit`

---

## Semantic Violation Severity

**Appearance of forbidden vocabulary outside allowed contexts is a semantic violation.**

This violation indicates:

1. **Risk**: Potential introduction of execution semantics
2. **Boundary breach**: Violation of system design constraints
3. **Scope creep**: Movement toward execution layer

**All violations must be corrected before code/documentation is accepted.**

---

## Vocabulary Reference

This list is comprehensive but not exhaustive. **Any term that implies execution, action, automation, or real-time operation is implicitly forbidden** unless explicitly allowed in this document.

When in doubt: **If it implies execution, it is forbidden.**

---

**END OF EXECUTION NEVER LIST**

**Note**: This list is a living reference. If new execution-related vocabulary is introduced (even accidentally), it must be added to this list and the violation must be corrected.

