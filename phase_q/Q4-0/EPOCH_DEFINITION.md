# Epoch Definition

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL  
**Document Type**: Structural Definition  
**Date**: 2026-01-10  
**Work Order**: WO-Q-4-0-MINIMAL-EPOCH-MECHANISM-IMPLEMENTATION-AND-LEAKAGE-VALIDATION  
**Parent Baselines**: Phase Q-2 (Longitudinal Simulation Results), Phase Q-3 (Epoch Path Selection)

---

## Purpose

This document provides a precise, structural definition of the Epoch mechanism for time-fracture governance.

This definition is minimal, unoptimized, and designed solely for leakage validation.

---

## What is an Epoch?

**Epoch**: A discrete, bounded time period during which a system operates with a complete, isolated state container.

**Key Properties**:
- Epoch has explicit start and end boundaries
- Epoch has a unique identifier (epoch_id)
- Epoch contains all state required for operation within its boundary
- Epoch state is completely destroyed at Epoch end
- No state may persist across Epoch boundaries

---

## Epoch Start Conditions

An Epoch starts when:

1. **Explicit Human Trigger**: A human operator explicitly invokes `start_epoch()`
2. **Epoch ID Generation**: A new, unique `epoch_id` is generated (non-deterministic, non-sequential)
3. **State Container Creation**: A new `EpochContext` object is instantiated
4. **Guard Activation**: `EpochGuard` begins monitoring for cross-epoch access

**Start Invariant**: No state from any previous Epoch may exist at start.

---

## Epoch End Conditions

An Epoch ends when:

1. **Explicit Human Trigger**: A human operator explicitly invokes `end_epoch()`
2. **State Destruction**: All objects in `EpochContext` are explicitly destroyed
3. **Guard Deactivation**: `EpochGuard` verifies no cross-epoch references remain
4. **State Hash Verification**: Final state hash is computed and recorded

**End Invariant**: No state from this Epoch may persist after end.

---

## State Types Allowed Within Epoch

### Ephemeral State (Epoch-Local)

**Definition**: State that exists only within a single Epoch boundary.

**Allowed Types**:
- Runtime variables (function-local, method-local)
- EpochContext container contents
- Temporary computation results
- In-memory data structures (lists, dicts, objects)

**Lifecycle**:
- Created: During Epoch operation
- Destroyed: At Epoch end (explicit destruction)
- Access: Only within same Epoch

### Forbidden State (Must Not Exist)

**Definition**: State that would persist across Epoch boundaries.

**Forbidden Types**:
- Global variables
- Module-level variables
- Static/class variables (unless explicitly reset per Epoch)
- Cached values
- Singleton instances (unless explicitly destroyed per Epoch)
- File handles (unless explicitly closed per Epoch)
- Database connections (unless explicitly closed per Epoch)
- Log aggregators
- Metric accumulators
- Environment variable modifications
- System-level state

**Detection**: Any state that exists after `end_epoch()` and before next `start_epoch()` is forbidden.

---

## Epoch Context Container

**Name**: `EpochContext`

**Purpose**: Sole container for all Epoch-local state.

**Properties**:
- Created at Epoch start
- Destroyed at Epoch end
- No global access (must be passed explicitly)
- No implicit access (no module-level references)

**Contents**:
- Runtime data structures
- Computation state
- Temporary results

**Access Pattern**:
```python
# Allowed
def operation(epoch_context: EpochContext):
    epoch_context.data = value

# Forbidden
global_epoch_context = None  # FORBIDDEN
```

---

## Epoch Destruction Checklist

At Epoch end, the following must be explicitly destroyed:

1. **EpochContext object**: All references set to None
2. **All contained objects**: Recursively destroyed
3. **All file handles**: Explicitly closed
4. **All network connections**: Explicitly closed
5. **All temporary files**: Explicitly deleted
6. **All in-memory caches**: Explicitly cleared
7. **All static/class variables**: Explicitly reset (if any)

**Verification**: State hash before destruction must differ from state hash after destruction.

---

## Explicitly Forbidden Cross-Epoch Structures

### 1. State Inheritance
- **Forbidden**: Any object that exists in Epoch N and persists into Epoch N+1
- **Detection**: Object identity comparison across Epochs

### 2. Implicit Time Continuity
- **Forbidden**: Any mechanism that assumes "previous Epoch" exists
- **Detection**: References to previous epoch_id or previous state

### 3. Accumulation Mechanisms
- **Forbidden**: Any counter, aggregator, or accumulator that spans Epochs
- **Detection**: Value comparison across Epochs

### 4. Caching Mechanisms
- **Forbidden**: Any cache that persists across Epochs
- **Detection**: Cache hit/miss comparison across Epochs

### 5. Optimization State
- **Forbidden**: Any optimization metadata (e.g., "learned" patterns) that persists
- **Detection**: Optimization state comparison across Epochs

### 6. Log Aggregation
- **Forbidden**: Any log aggregator that accumulates across Epochs
- **Detection**: Log file size/line count comparison across Epochs

### 7. Metric Aggregation
- **Forbidden**: Any metric accumulator that spans Epochs
- **Detection**: Metric value comparison across Epochs

### 8. File System State
- **Forbidden**: Any file created in Epoch N that is read in Epoch N+1
- **Detection**: File existence/timestamp comparison across Epochs

### 9. Environment State
- **Forbidden**: Any environment variable modification that persists
- **Detection**: Environment variable comparison across Epochs

### 10. Process State
- **Forbidden**: Any process-level state (e.g., signal handlers) that persists
- **Detection**: Process state comparison across Epochs

---

## Epoch ID Generation Rules

**Rule 1**: Epoch ID must be unique per Epoch
- **Method**: UUID v4 (non-deterministic)
- **Forbidden**: Sequential IDs, timestamps, deterministic IDs

**Rule 2**: Epoch ID must not encode time information
- **Forbidden**: Timestamp-based IDs, time-ordered IDs

**Rule 3**: Epoch ID must not be predictable
- **Forbidden**: Hash-based IDs from previous state, deterministic generation

**Rule 4**: Epoch ID must be generated at Epoch start
- **Forbidden**: Pre-generation, lazy generation, cached generation

---

## Epoch Transition Rules

### Transition: End Epoch N → Start Epoch N+1

**Required Steps**:
1. Destroy all state in Epoch N
2. Compute final state hash for Epoch N
3. Verify no state remains (guard check)
4. Generate new epoch_id for Epoch N+1
5. Create new EpochContext for Epoch N+1
6. Compute initial state hash for Epoch N+1
7. Verify initial state hash differs from final state hash of Epoch N

**Forbidden**:
- Skipping any step
- Reusing any object from Epoch N
- Assuming any state from Epoch N

---

## No Recommendations

This definition provides no recommendations.

This definition defines only structural requirements.

---

**END OF EPOCH DEFINITION**

