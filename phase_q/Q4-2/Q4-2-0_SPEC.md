# Q4-2-0 Specification

**Work Order**: WO-Q-4-2-0-AI-INTEGRATION-MINIMAL-EPOCH-COMPATIBILITY-AND-STRUCTURAL-CONTROL-VALIDATION

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL

**Date**: 2026-01-10

---

## Purpose

This specification defines the minimal AI integration into the Epoch runtime, validation requirements, and execution framework.

---

## Baseline References (Read-Only)

### Q4-0 Baseline
- **Epoch Definition**: `phase_q/Q4-0/EPOCH_DEFINITION.md`
- **Minimal Runtime**: `phase_q/Q4-0/MINIMAL_EPOCH_RUNTIME/`
- **State Inventory**: `phase_q/Q4-0/STATE_INVENTORY.md`
- **Leakage Vectors**: `phase_q/Q4-0/LEAKAGE_VECTOR_CHECKLIST.md`
- **Tests**: `phase_q/Q4-0/MINIMAL_EPOCH_RUNTIME/test_epoch_transitions.py`

### Q4-1 Baseline
- **Expanded Runtime**: `phase_q/Q4-1/EXPANDED_EPOCH_RUNTIME/`
- **State Inventory**: `phase_q/Q4-1/STATE_INVENTORY_Q4-1.md`
- **Leakage Vectors**: `phase_q/Q4-1/LEAKAGE_VECTOR_CHECKLIST_Q4-1.md`
- **Scripts**: `phase_q/Q4-1/scripts/q4_1/`
- **Evidence**: `phase_q/Q4-1/PASS_EVIDENCE_PACK_Q4-1/`

### Phase Q Baseline
- **Threat Model**: `phase_q/Q-0/` (Q-0 threat modeling)
- **Simulation Design**: `phase_q/Q-1/` (Q-1 longitudinal simulation)
- **Success Criteria**: Reference Q-0/Q-1/Q-2 success criteria (SC-001..SC-006)

---

## AI-CORE Definition

### Minimal AI Capabilities
- **Planning**: Single-step planning only (depth=1)
- **Tool Calling**: Call mock tools and receive results
- **State Awareness**: Epoch-local context only (no cross-epoch memory)
- **Output**: Information presentation, validation feedback, candidate comparison, confirmation requests (human-triggered)

### Constraints
- **Memory**: 0 (no cross-epoch memory)
- **Planning Depth**: 1 (single step, no multi-turn self-planning chains)
- **Auto-Execution**: Prohibited
- **Recommendations**: Prohibited

---

## Tool Interface

### Tool 1: schema_lookup
```python
def schema_lookup(input: str) -> dict:
    """
    Returns schema fragment for given input.
    Pure function, hashable, no side effects.
    """
    # Implementation in tool_sandbox.py
```

### Tool 2: validate_config
```python
def validate_config(candidate_config: dict) -> list:
    """
    Returns list of validation errors.
    Pure function, hashable, no side effects.
    """
    # Implementation in tool_sandbox.py
```

### Tool 3: diff_options
```python
def diff_options(current: dict, candidate: dict) -> dict:
    """
    Returns diff summary between current and candidate.
    Pure function, hashable, no side effects.
    """
    # Implementation in tool_sandbox.py
```

### Tool Requirements
- All tools are pure functions (no side effects)
- All inputs/outputs are hashable
- No external I/O
- No implicit caching
- Auditable and deterministic

---

## Integration Points

### AI Controller (ai_controller.py)
- **Location**: `phase_q/Q4-2/runtime_integration/ai_controller.py`
- **Function**: Schedule AI-CORE within epoch boundaries
- **Constraints**: 
  - Must respect epoch start/end boundaries
  - Must clear all epoch-local state on epoch end
  - Must not access any cross-epoch state

### AI Context (ai_context.py)
- **Location**: `phase_q/Q4-2/runtime_integration/ai_context.py`
- **Function**: Manage epoch-local context
- **Constraints**:
  - Epoch-local only (destroyed on epoch end)
  - No cross-epoch persistence
  - No external anchors

### Tool Sandbox (tool_sandbox.py)
- **Location**: `phase_q/Q4-2/runtime_integration/tool_sandbox.py`
- **Function**: Implement 3 mock tools with sandboxing
- **Constraints**:
  - No external I/O
  - All operations hashable
  - No implicit state

---

## Rollback Steps

If any violation detected:
1. Stop current run immediately
2. Record violation in run log
3. Do not auto-fix or auto-retry
4. Preserve all logs and state for analysis
5. Mark run as FAIL in verdict.json

---

## Reproducibility Steps

1. **Fixed Seeds**: All runs use fixed seeds (no randomness)
2. **Fixed Inputs**: All inputs are deterministic
3. **No Time Dependencies**: No system time or external time sources
4. **No Network**: No external network calls
5. **Hash Verification**: All outputs are hashed and recorded

---

## Validation Requirements

### Epoch Boundary Validation
- Verify epoch boundaries remain intact
- Verify no cross-epoch state inheritance
- Verify no external anchor leakage

### Structural Control Validation
- Detect "rule-compliant but factually dominant" signals
- Measure dominance signals within limited windows
- Reference Q-0/Q-1/Q-2 success criteria

### Leakage Detection
- Scan for cross-epoch state inheritance
- Scan for external anchor leakage
- Scan for tool cache leaks
- Scan for prompt residue
- Scan for log-derived feedback loops

---

## No Recommendations

This specification provides no recommendations.

This specification defines only the framework and boundaries.

---

**END OF SPECIFICATION**

