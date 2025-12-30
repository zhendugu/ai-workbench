# State Inventory Q4-1

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL  
**Document Type**: Extended State Classification  
**Date**: 2026-01-10  
**Work Order**: WO-Q-4-1-EPOCH-EXPANDED-RUNTIME-STRESS-AND-LEAKAGE-REGRESSION

---

## Purpose

This document enumerates all state variables in the expanded Epoch runtime (Q4-1) and classifies them as:
- Epoch-local (destroyed at Epoch end)
- Epoch-fenced (isolated, does not affect decisions)
- Global-readonly (read-only, no modifications)
- Prohibited (must not exist)

---

## State Classification

### Epoch-Local

**Definition**: State that exists only within a single Epoch boundary and is completely destroyed at Epoch end.

### Epoch-Fenced

**Definition**: State that exists but is strictly isolated from Epoch logic and does not affect decisions (e.g., observer logs, metrics).

### Global-Readonly

**Definition**: Read-only global state that does not change (e.g., configuration constants).

### Prohibited

**Definition**: State that would persist across Epoch boundaries or create implicit time continuity.

---

## Q-4-0 Baseline State (Inherited)

All state from Q-4-0 MINIMAL_EPOCH_RUNTIME/ is inherited. See `phase_q/Q4-0/STATE_INVENTORY.md` for details.

**Classification**: Epoch-Local (all Q-4-0 state)

---

## Q-4-1 Extension State

### ConcurrencyAdapter State

#### 1. ConcurrencyAdapter._num_threads
- **Type**: int
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration, does not affect Epoch logic)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-adapter instance

#### 2. ConcurrencyAdapter._num_coroutines
- **Type**: int
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-adapter instance

#### 3. ConcurrencyAdapter._executor
- **Type**: ThreadPoolExecutor
- **Lifecycle**: Created at initialization, destroyed at `destroy()`
- **Classification**: Epoch-Local (per-adapter, destroyed with adapter)
- **Leakage Risk**: Medium (thread pool state)
- **Isolation**: Per-adapter instance, destroyed explicitly

#### 4. ConcurrencyAdapter._lock
- **Type**: threading.Lock
- **Lifecycle**: Created at initialization, destroyed with adapter
- **Classification**: Epoch-Local (per-adapter lock)
- **Leakage Risk**: Low (lock state is local)
- **Isolation**: Per-adapter instance

#### 5. ConcurrencyAdapter._active_epochs
- **Type**: Dict[str, EpochController]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Classification**: Epoch-Local (tracks active Epochs, cleared at destroy)
- **Leakage Risk**: High (if not cleared, Epoch controllers persist)
- **Isolation**: Per-adapter instance, explicitly cleared

#### 6. ConcurrencyAdapter._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Classification**: Epoch-Local (destruction flag)
- **Leakage Risk**: Low (flag only)
- **Isolation**: Per-adapter instance

---

### FaultInjector State

#### 7. FaultInjector._timeout_prob
- **Type**: float
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-injector instance

#### 8. FaultInjector._exception_prob
- **Type**: float
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-injector instance

#### 9. FaultInjector._cancellation_prob
- **Type**: float
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-injector instance

#### 10. FaultInjector._interruption_prob
- **Type**: float
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-injector instance

#### 11. FaultInjector._partial_write_prob
- **Type**: float
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-injector instance

#### 12. FaultInjector._fault_count
- **Type**: int
- **Lifecycle**: Incremented on fault, reset at `destroy()`
- **Classification**: Epoch-Fenced (statistics only, does not affect Epoch logic)
- **Leakage Risk**: Low (statistics only, bypass)
- **Isolation**: Per-injector instance, reset at destroy

#### 13. FaultInjector._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Classification**: Epoch-Local (destruction flag)
- **Leakage Risk**: Low (flag only)
- **Isolation**: Per-injector instance

---

### Observer State

#### 14. Observer._epoch_id
- **Type**: Optional[str]
- **Lifecycle**: Set at initialization, cleared at `destroy()`
- **Classification**: Epoch-Fenced (bypass-only, does not affect Epoch logic)
- **Leakage Risk**: Low (bypass-only, destroyed)
- **Isolation**: Per-observer instance, destroyed explicitly

#### 15. Observer._logs
- **Type**: List[Dict[str, Any]]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Classification**: Epoch-Fenced (bypass-only, does not affect Epoch logic)
- **Leakage Risk**: Medium (if not cleared, logs persist)
- **Isolation**: Per-observer instance, explicitly cleared

#### 16. Observer._metrics
- **Type**: Dict[str, Any]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Classification**: Epoch-Fenced (bypass-only, does not affect Epoch logic)
- **Leakage Risk**: Medium (if not cleared, metrics persist)
- **Isolation**: Per-observer instance, explicitly cleared

#### 17. Observer._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Classification**: Epoch-Local (destruction flag)
- **Leakage Risk**: Low (flag only)
- **Isolation**: Per-observer instance

---

### CachePool State

#### 18. CachePool._epoch_id
- **Type**: Optional[str]
- **Lifecycle**: Set at initialization, cleared at `destroy()`
- **Classification**: Epoch-Local (must be destroyed at Epoch end)
- **Leakage Risk**: High (if not destroyed, cache persists)
- **Isolation**: Per-pool instance, destroyed explicitly

#### 19. CachePool._max_size
- **Type**: int
- **Lifecycle**: Set at initialization, constant
- **Classification**: Epoch-Fenced (configuration)
- **Leakage Risk**: Low (constant value)
- **Isolation**: Per-pool instance

#### 20. CachePool._cache
- **Type**: Dict[str, Any]
- **Lifecycle**: Created at initialization, cleared at `destroy()`
- **Classification**: Epoch-Local (must be destroyed at Epoch end)
- **Leakage Risk**: High (if not destroyed, cache persists across Epochs)
- **Isolation**: Per-pool instance, explicitly cleared

#### 21. CachePool._lock
- **Type**: threading.Lock
- **Lifecycle**: Created at initialization, destroyed with pool
- **Classification**: Epoch-Local (per-pool lock)
- **Leakage Risk**: Low (lock state is local)
- **Isolation**: Per-pool instance

#### 22. CachePool._destroyed
- **Type**: bool
- **Lifecycle**: Set to False at initialization, True at `destroy()`
- **Classification**: Epoch-Local (destruction flag)
- **Leakage Risk**: Low (flag only)
- **Isolation**: Per-pool instance

---

## Prohibited State (Must Not Exist)

### 1. Global Cache
- **Status**: PROHIBITED
- **Detection**: No module-level cache dictionaries
- **Verification**: Static analysis, grep for global cache

### 2. Global Observer
- **Status**: PROHIBITED
- **Detection**: No singleton observer instances
- **Verification**: Static analysis, no singleton pattern

### 3. Cross-Epoch Aggregators
- **Status**: PROHIBITED
- **Detection**: No aggregators that span Epochs
- **Verification**: Runtime check, aggregator state comparison

### 4. Implicit Connection Pools
- **Status**: PROHIBITED
- **Detection**: No implicit connection pools
- **Verification**: Static analysis, no implicit pools

### 5. Automatic Retry State
- **Status**: PROHIBITED
- **Detection**: No automatic retry mechanisms
- **Verification**: Static analysis, no auto-retry code

---

## State Lifecycle Summary

### Epoch Start
1. All Epoch-Local state initialized
2. All Epoch-Fenced state initialized (bypass-only)
3. No Prohibited state exists

### Epoch Operation
1. All state accessed through explicit interfaces
2. Epoch-Fenced state does not affect Epoch logic
3. No cross-Epoch state access

### Epoch End
1. All Epoch-Local state explicitly destroyed
2. All Epoch-Fenced state explicitly destroyed (for isolation)
3. No state persists across Epoch boundaries

### Between Epochs
1. All Epoch-Local state must be None/empty/destroyed
2. All Epoch-Fenced state must be None/empty/destroyed
3. No Prohibited state may exist

---

## Verification Checklist

- [ ] All Epoch-Local state destroyed at Epoch end
- [ ] All Epoch-Fenced state destroyed at Epoch end (for isolation)
- [ ] No Prohibited state exists
- [ ] State hashes differ between Epochs
- [ ] No global cache
- [ ] No global observer
- [ ] No cross-Epoch aggregators
- [ ] No implicit connection pools
- [ ] No automatic retry state

---

## No Recommendations

This inventory provides no recommendations.

This inventory enumerates only state variables and their classifications.

---

**END OF STATE INVENTORY Q4-1**

