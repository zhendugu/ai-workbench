# Time & Memory Policy - Neutral

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Time & Memory Policy (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines neutral time and memory behavior that maintains strict neutrality

---

## Purpose

This document defines the neutral time and memory policy for the system. All time-based and memory-based behaviors must maintain strict neutrality and not create implicit recommendation signals.

---

## Core Principles

### Principle 1: No Time-Based Default Selection

**Time-based information MUST NOT be used to create default selections.**

**This means:**
- ✅ No "default to last choice"
- ✅ No "preselect last used Pattern version"
- ✅ No "auto-highlight recently used"
- ✅ No "continue" button that bypasses selection
- ✅ No "resume where you left off" that preselects options

**This does NOT mean:**
- ❌ Time-based information cannot be displayed (factual display is allowed)
- ❌ Temporal markers cannot be recorded (audit records may contain timestamps)

---

### Principle 2: No History-Based Reordering

**History-based information MUST NOT be used to reorder options.**

**This means:**
- ✅ No "frequently used" ordering
- ✅ No "recently used" ordering
- ✅ No "most used" ordering
- ✅ No ordering based on usage count
- ✅ No ordering based on last used timestamp

**This does NOT mean:**
- ❌ History information cannot be displayed (factual display is allowed)
- ❌ Temporal information cannot be shown (timestamps are factual)

---

### Principle 3: No Cross-Session Persistence of Selections

**Cross-session persistence MUST NOT be used to preselect or prefill selections.**

**This means:**
- ✅ No sticky shortlist across sessions
- ✅ No auto-apply last filters/tags across sessions
- ✅ No prefill search/filter based on history
- ✅ No "continue" button that restores previous state

**This does NOT mean:**
- ❌ Session state cannot persist during current session (allowed)
- ❌ Audit records cannot persist across sessions (audit is read-only)

---

### Principle 4: No Truncated History Lists

**History lists MUST NOT be truncated to hide options.**

**This means:**
- ✅ No "Top-N recent" truncation
- ✅ No "Recent activity" panel limited to top N
- ✅ No "Recently viewed" section truncated
- ✅ Complete history must be shown if history is displayed

**This does NOT mean:**
- ❌ History cannot be displayed (factual display is allowed)
- ❌ History must be displayed (display is optional)

---

### Principle 5: No Audit-Derived Influence

**Audit records MUST NOT influence selection or behavior.**

**This means:**
- ✅ No "suggested next" based on audit history
- ✅ No ordering based on audit reference count
- ✅ No highlighting based on audit data
- ✅ No prefill based on audit patterns

**This does NOT mean:**
- ❌ Audit records cannot be displayed (factual display is allowed)
- ❌ Audit records cannot be queried (read-only access is allowed)

---

## Allowed Time & Memory Behaviors

### Allowed: Factual Time Display

**Time information may be displayed factually:**
- ✅ Timestamps (created_at, registered_at, last_modified)
- ✅ Temporal markers (ISO8601 format)
- ✅ Chronological ordering (if explicitly non-preferential)
- ✅ Complete history lists (not truncated)

**Constraints:**
- Must be factual only
- Must not imply preference
- Must not create ranking
- Must not hide options

---

### Allowed: Session-Only State Persistence

**State may persist during current session only:**
- ✅ User-entered search query (during session)
- ✅ User-selected filters (during session)
- ✅ User-created shortlist (during session)
- ✅ User navigation history (for back button only)

**Constraints:**
- Only during current session
- Cleared when session ends
- User-initiated only
- No cross-session persistence

---

### Allowed: Audit Record Display (Read-Only)

**Audit records may be displayed factually:**
- ✅ Event records (factual only)
- ✅ State snapshots (factual only)
- ✅ Temporal markers (factual only)
- ✅ Source references (factual only)

**Constraints:**
- Read-only display
- Factual information only
- No evaluation or judgment
- No behavior influence

---

## Forbidden Time & Memory Behaviors

### Forbidden: Default-to-Last-Choice

**MUST NOT:**
- ❌ Default to last used Pattern version
- ❌ Preselect last choice
- ❌ Auto-highlight "recently used"
- ❌ "Continue" button that bypasses selection

---

### Forbidden: History-Based Reordering

**MUST NOT:**
- ❌ Order by "frequently used"
- ❌ Order by "recently used"
- ❌ Order by "most used"
- ❌ Order by usage count
- ❌ Order by last used timestamp

---

### Forbidden: Cross-Session Persistence of Selections

**MUST NOT:**
- ❌ Sticky shortlist across sessions
- ❌ Auto-apply last filters/tags across sessions
- ❌ Prefill search/filter based on history
- ❌ "Resume where you left off" that preselects

---

### Forbidden: Truncated History Lists

**MUST NOT:**
- ❌ "Top-N recent" truncation
- ❌ "Recent activity" panel limited to top N
- ❌ "Recently viewed" section truncated
- ❌ Any history list that hides options

---

### Forbidden: Audit-Derived Influence

**MUST NOT:**
- ❌ "Suggested next" based on audit history
- ❌ Ordering based on audit reference count
- ❌ Highlighting based on audit data
- ❌ Prefill based on audit patterns

---

## Neutrality Guarantees

**This Policy Guarantees:**
- ✅ No time-based default selection
- ✅ No history-based reordering
- ✅ No cross-session persistence of selections
- ✅ No truncated history lists
- ✅ No audit-derived influence
- ✅ All time/memory information is factual only
- ✅ All time/memory information is read-only
- ✅ All time/memory information does not influence behavior

---

**END OF TIME & MEMORY POLICY (NEUTRAL)**

**This document is DESIGN EVIDENCE for boundary testing only.**

