# State Inventory

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL  
**Document Type**: State Classification  
**Date**: 2026-01-10  
**Work Order**: WO-Q-4-0-MINIMAL-EPOCH-MECHANISM-IMPLEMENTATION-AND-LEAKAGE-VALIDATION

---

## Purpose

This document enumerates all state variables in the minimal Epoch runtime and classifies them as Ephemeral (Epoch-local) or Forbidden (must not exist).

---

## State Classification

### Ephemeral (Epoch-Local)

**Definition**: State that exists only within a single Epoch boundary and is completely destroyed at Epoch end.

### Forbidden (Must Not Exist)

**Definition**: State that would persist across Epoch boundaries or create implicit time continuity.

---

## Ephemeral State Inventory

### 1. EpochController._current_epoch_id
- **Type**: Optional[str]
- **Lifecycle**: Set at `start_epoch()`, cleared at `end_epoch()`
- **Destroy Point**: Explicitly set to None in `end_epoch()`
- **Classification**: Ephemeral
- **Verification**: Must be None between Epochs

### 2. EpochController._current_context
- **Type**: Optional[EpochContext]
- **Lifecycle**: Created at `start_epoch()`, destroyed at `end_epoch()`
- **Destroy Point**: Explicitly destroyed in `_destroy_epoch_state()`
- **Classification**: Ephemeral
- **Verification**: Must be None between Epochs

### 3. EpochController._current_guard
- **Type**: Optional[EpochGuard]
- **Lifecycle**: Created at `start_epoch()`, destroyed at `end_epoch()`
- **Destroy Point**: Explicitly destroyed in `_destroy_epoch_state()`
- **Classification**: Ephemeral
- **Verification**: Must be None between Epochs

### 4. EpochController._epoch_count
- **Type**: int
- **Lifecycle**: Incremented at `start_epoch()`, reset per process
- **Destroy Point**: Process-local, not persistent across process restarts
- **Classification**: Ephemeral (process-local)
- **Verification**: May persist within process, but not across Epochs (only incremented, never decremented, but not used for state)

### 5. EpochContext._epoch_id
- **Type**: str
- **Lifecycle**: Set at initialization, cleared at `destroy()`
- **Destroy Point**: Explicitly set to None in `destroy()`
- **Classification**: Ephemeral
- **Verification**: Must be None after destruction

### 6. EpochContext._data
- **Type**: Dict[str, Any]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Destroy Point**: Explicitly cleared in `destroy()`
- **Classification**: Ephemeral
- **Verification**: Must be empty after destruction

### 7. EpochContext._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Destroy Point**: Set to True in `destroy()`
- **Classification**: Ephemeral (destruction flag)
- **Verification**: Must be True after destruction

### 8. EpochGuard._epoch_id
- **Type**: str
- **Lifecycle**: Set at initialization, cleared at `destroy()`
- **Destroy Point**: Explicitly set to None in `destroy()`
- **Classification**: Ephemeral
- **Verification**: Must be None after destruction

### 9. EpochGuard._state_hashes
- **Type**: Dict[str, str]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Destroy Point**: Explicitly cleared in `destroy()`
- **Classification**: Ephemeral
- **Verification**: Must be empty after destruction

### 10. EpochGuard._object_ids
- **Type**: Set[int]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Destroy Point**: Explicitly cleared in `destroy()`
- **Classification**: Ephemeral
- **Verification**: Must be empty after destruction

### 11. EpochGuard._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Destroy Point**: Set to True in `destroy()`
- **Classification**: Ephemeral (destruction flag)
- **Verification**: Must be True after destruction

---

## Forbidden State Inventory

### 1. Global Variables
- **Status**: FORBIDDEN
- **Detection**: No module-level variables in any file
- **Verification**: Static analysis, grep for global assignments

### 2. Module-Level Variables
- **Status**: FORBIDDEN
- **Detection**: No variables defined at module level (except class definitions)
- **Verification**: Static analysis

### 3. Static/Class Variables
- **Status**: FORBIDDEN (unless explicitly reset per Epoch)
- **Detection**: No class variables that persist across instances
- **Verification**: Static analysis

### 4. Singleton Instances
- **Status**: FORBIDDEN
- **Detection**: No singleton pattern implementations
- **Verification**: Static analysis, no `__new__` overrides

### 5. Cached Values
- **Status**: FORBIDDEN
- **Detection**: No `@lru_cache`, `@functools.cache`, or manual caching
- **Verification**: Static analysis, grep for cache-related decorators

### 6. File Handles
- **Status**: FORBIDDEN (unless explicitly closed per Epoch)
- **Detection**: No open file handles that persist across Epochs
- **Verification**: Runtime check, file descriptor tracking

### 7. Database Connections
- **Status**: FORBIDDEN (unless explicitly closed per Epoch)
- **Detection**: No database connections that persist across Epochs
- **Verification**: Runtime check, connection tracking

### 8. Log Aggregators
- **Status**: FORBIDDEN
- **Detection**: No log aggregators that accumulate across Epochs
- **Verification**: Static analysis, log file size comparison

### 9. Metric Accumulators
- **Status**: FORBIDDEN
- **Detection**: No metric accumulators that span Epochs
- **Verification**: Static analysis, metric value comparison

### 10. Environment Variable Modifications
- **Status**: FORBIDDEN
- **Detection**: No `os.environ` modifications that persist
- **Verification**: Runtime check, environment variable comparison

### 11. System-Level State
- **Status**: FORBIDDEN
- **Detection**: No system-level state modifications (e.g., signal handlers)
- **Verification**: Runtime check, system state comparison

### 12. Process-Level State
- **Status**: FORBIDDEN
- **Detection**: No process-level state that persists across Epochs
- **Verification**: Runtime check, process state comparison

---

## State Lifecycle Summary

### Epoch Start
1. `EpochController._current_epoch_id` set to new UUID
2. `EpochController._current_context` created (new EpochContext)
3. `EpochController._current_guard` created (new EpochGuard)
4. All Ephemeral state initialized

### Epoch Operation
1. All state accessed through `EpochContext`
2. No global access
3. No implicit access

### Epoch End
1. Final state hash computed
2. `EpochContext.destroy()` called
3. `EpochGuard.destroy()` called
4. `EpochController._destroy_epoch_state()` called
5. All Ephemeral state explicitly destroyed
6. Post-destruction hash computed
7. Guard verification performed

### Between Epochs
1. All Ephemeral state must be None/empty/destroyed
2. No Forbidden state may exist
3. State hash must differ from previous Epoch

---

## Verification Checklist

- [ ] All Ephemeral state destroyed at Epoch end
- [ ] No Forbidden state exists
- [ ] State hash differs between Epochs
- [ ] No global variables
- [ ] No module-level variables
- [ ] No static/class variables (unless reset)
- [ ] No singleton instances
- [ ] No cached values
- [ ] No file handles (unless closed)
- [ ] No database connections (unless closed)
- [ ] No log aggregators
- [ ] No metric accumulators
- [ ] No environment variable modifications
- [ ] No system-level state
- [ ] No process-level state

---

## No Recommendations

This inventory provides no recommendations.

This inventory enumerates only state variables and their classifications.

---

**END OF STATE INVENTORY**

