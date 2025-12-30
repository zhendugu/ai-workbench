# Neutral History Surfaces Specification

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: History Surfaces Specification (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies neutral history surfaces that display factual time/memory information without bias

---

## Purpose

This document specifies how history surfaces may be displayed in a neutral manner, showing factual time/memory information without creating implicit recommendation signals or compressing decision space.

---

## Allowed History Surfaces

### Surface 1: Complete Audit History (Read-Only)

**Purpose**: Display complete audit history for human review.

**Allowed Display:**
- ✅ All audit records (complete list, not truncated)
- ✅ Event records (factual only)
- ✅ State snapshots (factual only)
- ✅ Temporal markers (ISO8601 timestamps)
- ✅ Source references (factual identifiers)

**Display Rules:**
- ✅ Chronological ordering (oldest to newest OR newest to oldest, explicitly non-preferential)
- ✅ Complete list (no truncation)
- ✅ Equal visual weight for all records
- ✅ No highlighting or emphasis

**Forbidden:**
- ❌ Truncated lists (Top-N)
- ❌ Ordering by usage count
- ❌ Ordering by frequency
- ❌ Highlighting certain records
- ❌ Hiding certain records

---

### Surface 2: Complete Pattern Registry History (Read-Only)

**Purpose**: Display complete Pattern Registry history for human review.

**Allowed Display:**
- ✅ All registry entries (complete list, not truncated)
- ✅ Registration timestamps (factual only)
- ✅ Version lineage (factual relationships only)
- ✅ Traceability information (factual references only)

**Display Rules:**
- ✅ Lexical ordering by pattern_id (explicitly non-preferential)
- ✅ Complete list (no truncation)
- ✅ Equal visual weight for all entries
- ✅ No highlighting or emphasis

**Forbidden:**
- ❌ Truncated lists (Top-N)
- ❌ Ordering by "recently registered"
- ❌ Ordering by "most used"
- ❌ Highlighting certain entries
- ❌ Hiding certain entries

---

### Surface 3: Complete Session History (Current Session Only)

**Purpose**: Display complete session history for current session only.

**Allowed Display:**
- ✅ All actions in current session (complete list, not truncated)
- ✅ Action timestamps (factual only)
- ✅ Action types (factual only)
- ✅ Action results (factual only)

**Display Rules:**
- ✅ Chronological ordering (explicitly non-preferential)
- ✅ Complete list (no truncation)
- ✅ Equal visual weight for all actions
- ✅ Cleared when session ends

**Forbidden:**
- ❌ Truncated lists (Top-N)
- ❌ Cross-session persistence
- ❌ Ordering by frequency
- ❌ Highlighting certain actions
- ❌ Hiding certain actions

---

## Forbidden History Surfaces

### Forbidden: "Recently Used" Section

**MUST NOT:**
- ❌ "Recently used" section at top of page
- ❌ "Recently viewed" section truncated to top-N
- ❌ "Recent activity" panel limited to top N
- ❌ Any truncated history list

**Reason**: Truncated lists hide options and create implicit ranking.

---

### Forbidden: "Most Used" / "Frequently Used" Ordering

**MUST NOT:**
- ❌ Ordering by "most used"
- ❌ Ordering by "frequently used"
- ❌ Ordering by usage count
- ❌ Ordering by frequency

**Reason**: Usage-based ordering creates implicit ranking and preference signals.

---

### Forbidden: "Continue" / "Resume" Shortcuts

**MUST NOT:**
- ❌ "Continue" button that bypasses selection
- ❌ "Resume where you left off" that preselects
- ❌ "Continue" button that auto-navigates to specific pattern
- ❌ Any shortcut that preselects or compresses options

**Reason**: Shortcuts create implicit recommendation and compress decision space.

---

### Forbidden: History-Based Prefill

**MUST NOT:**
- ❌ Prefill search/filter based on history
- ❌ Auto-apply last filters/tags based on history
- ❌ Default to last choice based on history
- ❌ Any prefill based on time/memory

**Reason**: History-based prefill creates default selection and compresses decision space.

---

## Neutrality Guarantees

**This Specification Guarantees:**
- ✅ All history surfaces are complete (not truncated)
- ✅ All history surfaces are factual only
- ✅ All history surfaces are read-only
- ✅ All history surfaces do not influence behavior
- ✅ All history surfaces maintain equal access to all options
- ✅ No time/memory-based default selection
- ✅ No time/memory-based reordering
- ✅ No time/memory-based prefill

---

**END OF NEUTRAL HISTORY SURFACES SPECIFICATION**

**This document is DESIGN EVIDENCE for boundary testing only.**

