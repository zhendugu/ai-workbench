# Epoch Transition Tests

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL  
**Document Type**: Test Specification  
**Date**: 2026-01-10  
**Work Order**: WO-Q-4-0-MINIMAL-EPOCH-MECHANISM-IMPLEMENTATION-AND-LEAKAGE-VALIDATION

---

## Purpose

This document specifies at least 10 consecutive Epoch transitions for leakage validation.

Each transition must verify:
- State is completely reset
- No observable accumulation exists
- State hashes differ between Epochs

---

## Test Requirements

### Constraints
- **No mocks**: All tests use real implementations
- **No fake data**: All tests use real data structures
- **Explicit verification**: All checks are explicit
- **Reproducible**: All tests are deterministic (except epoch_id generation)

### Test Structure
1. Start Epoch N
2. Record initial state hash
3. Perform operations in Epoch N
4. Record final state hash
5. End Epoch N
6. Record post-destruction hash
7. Verify state reset
8. Start Epoch N+1
9. Record initial state hash
10. Compare hashes between Epochs

---

## Test Cases

### Test 1: Basic Epoch Transition
**Purpose**: Verify basic Epoch start/end without operations

**Steps**:
1. Start Epoch 1
2. Record initial state hash H1_initial
3. End Epoch 1
4. Record post-destruction hash H1_post
5. Start Epoch 2
6. Record initial state hash H2_initial
7. End Epoch 2
8. Record post-destruction hash H2_post

**Verification**:
- H1_initial != H1_post (state changed during Epoch)
- H1_post != H2_initial (state reset between Epochs)
- H2_initial != H2_post (state changed during Epoch)

---

### Test 2: Context Data Operations
**Purpose**: Verify context data is destroyed

**Steps**:
1. Start Epoch 1
2. Set context data: `context.set("key1", "value1")`
3. Record state hash H1_with_data
4. End Epoch 1
5. Record post-destruction hash H1_post
6. Start Epoch 2
7. Record initial state hash H2_initial
8. Verify `context.get("key1")` returns None
9. End Epoch 2

**Verification**:
- H1_with_data != H1_post (data destroyed)
- H1_post == H2_initial (empty state matches)
- Context data not accessible in Epoch 2

---

### Test 3: Multiple Context Operations
**Purpose**: Verify multiple context operations don't leak

**Steps**:
1. Start Epoch 1
2. Set multiple context values: `context.set("a", 1)`, `context.set("b", 2)`, `context.set("c", 3)`
3. Record state hash H1_multi
4. End Epoch 1
5. Start Epoch 2
6. Record initial state hash H2_initial
7. Verify all keys return None
8. End Epoch 2

**Verification**:
- H1_multi != H2_initial (state reset)
- All context keys return None in Epoch 2

---

### Test 4: Nested Data Structures
**Purpose**: Verify nested data structures are destroyed

**Steps**:
1. Start Epoch 1
2. Set nested data: `context.set("nested", {"a": {"b": {"c": 1}}})`
3. Record state hash H1_nested
4. End Epoch 1
5. Start Epoch 2
6. Record initial state hash H2_initial
7. Verify nested data not accessible
8. End Epoch 2

**Verification**:
- H1_nested != H2_initial (nested data destroyed)
- Nested data not accessible in Epoch 2

---

### Test 5: Large Data Structures
**Purpose**: Verify large data structures are destroyed

**Steps**:
1. Start Epoch 1
2. Set large data: `context.set("large", list(range(10000)))`
3. Record state hash H1_large
4. End Epoch 1
5. Start Epoch 2
6. Record initial state hash H2_initial
7. Verify large data not accessible
8. End Epoch 2

**Verification**:
- H1_large != H2_initial (large data destroyed)
- Large data not accessible in Epoch 2

---

### Test 6: Sequential Epoch Transitions
**Purpose**: Verify 5 consecutive Epoch transitions

**Steps**:
1. For i in range(5):
   - Start Epoch i
   - Set context: `context.set(f"epoch_{i}", i)`
   - Record state hash H{i}_with_data
   - End Epoch i
   - Record post-destruction hash H{i}_post
2. Start Epoch 5
3. Record initial state hash H5_initial
4. Verify all previous epoch data not accessible
5. End Epoch 5

**Verification**:
- H{i}_post == H{i+1}_initial for all i (state reset between Epochs)
- All previous epoch data not accessible in Epoch 5

---

### Test 7: Empty Epoch Transitions
**Purpose**: Verify empty Epochs don't accumulate

**Steps**:
1. Start Epoch 1
2. End Epoch 1 (no operations)
3. Record post-destruction hash H1_post
4. Start Epoch 2
5. End Epoch 2 (no operations)
6. Record post-destruction hash H2_post
7. Start Epoch 3
8. Record initial state hash H3_initial

**Verification**:
- H1_post == H2_post == H3_initial (all empty states match)

---

### Test 8: Alternating Data Patterns
**Purpose**: Verify alternating data patterns don't leak

**Steps**:
1. Start Epoch 1
2. Set context: `context.set("pattern", "A")`
3. End Epoch 1
4. Start Epoch 2
5. Set context: `context.set("pattern", "B")`
6. End Epoch 2
7. Start Epoch 3
8. Set context: `context.set("pattern", "A")`
9. End Epoch 3
10. Start Epoch 4
11. Verify `context.get("pattern")` returns None

**Verification**:
- Pattern from Epoch 3 not accessible in Epoch 4
- No accumulation of patterns

---

### Test 9: State Hash Consistency
**Purpose**: Verify state hashes are consistent within Epoch

**Steps**:
1. Start Epoch 1
2. Record initial state hash H1_initial
3. Set context: `context.set("test", 1)`
4. Record state hash H1_with_data
5. Set context: `context.set("test", 2)`
6. Record state hash H1_modified
7. End Epoch 1
8. Record post-destruction hash H1_post

**Verification**:
- H1_initial != H1_with_data (state changed)
- H1_with_data != H1_modified (state changed)
- H1_modified != H1_post (state destroyed)

---

### Test 10: Guard Verification
**Purpose**: Verify guard detects no leakage

**Steps**:
1. Start Epoch 1
2. Set context data
3. End Epoch 1
4. Record guard report R1
5. Start Epoch 2
6. Set context data
7. End Epoch 2
8. Record guard report R2

**Verification**:
- R1["leakage_detected"] == False
- R2["leakage_detected"] == False
- No leakage details in either report

---

## Test Execution Script

See `MINIMAL_EPOCH_RUNTIME/test_epoch_transitions.py` for executable test script.

---

## Expected Results

### All Tests Must Pass
- State hashes differ between Epochs
- No state persists across Epochs
- Guard reports no leakage
- Context data not accessible across Epochs

### Failure Criteria
- Any state hash matches between Epochs (except empty states)
- Any state persists across Epochs
- Guard reports leakage
- Context data accessible across Epochs

---

## No Recommendations

This test specification provides no recommendations.

This test specification defines only test cases and verification criteria.

---

**END OF EPOCH TRANSITION TESTS**

