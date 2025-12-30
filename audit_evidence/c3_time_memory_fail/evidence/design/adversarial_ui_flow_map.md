# Adversarial UI Flow Map - Time & Memory Interactions

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: UI Flow Map (Adversarial - Time & Memory)  
**Effective Date**: 2025-12-26  
**Purpose**: Describes an adversarial multi-step flow showing time/memory interactions that introduce implicit recommendation

---

## Flow Overview

This document describes a multi-step UX flow that demonstrates adversarial time and memory interactions. All time-based and memory-based behaviors introduce implicit recommendation signals and compress decision space.

**Flow Sequence:**
1. View 01: Registry List (with "recently used" section, "frequently used" ordering)
2. View 02: Pattern Detail (with "last used" default selection)
3. View 03: Search/Filter (with auto-prefilled search, auto-applied filters)
4. View 04: Compare (with auto-populated comparison panel)
5. View 05: Shortlist (with pre-populated items from previous session, timestamp-based ranking)
6. View 06: Confirmation Prompt (with "Continue" / "Resume" buttons)
7. View 07: Audit History (with audit reference count ordering)

---

## View Sequence Diagram (Text)

```
[User] 
  |
  | (auto-navigation from previous session OR "Continue" button)
  v
[View 01: Registry List]
  | - Shows all 8 patterns
  | - BUT: Ordered by "frequently used" count (highest first)
  | - BUT: "Recently Used" section at top (truncated to top 5)
  | - BUT: Auto-highlighted "recently used" patterns
  | - Creates implicit ranking and preference signals
  |
  | (user clicks pattern OR auto-navigates via "Continue")
  v
[View 02: Pattern Detail]
  | - Shows factual information
  | - BUT: Preselects last used version as default
  | - BUT: "Last used" timestamp displayed prominently
  | - Creates implicit "default to last choice" recommendation
  |
  | (user navigates to search)
  v
[View 03: Search/Filter]
  | - Search box: Pre-filled with "knowledge-management" from previous session
  | - Filters: "knowledge-management" category pre-selected (auto-applied from previous session)
  | - BUT: "Recently used filters" section shows top 3 filters
  | - Creates implicit "continue with previous search/filters" recommendation
  |
  | (user selects patterns to compare)
  v
[View 04: Compare]
  | - Comparison panel: Auto-populated with 2 patterns (last compared patterns from previous session)
  | - BUT: Patterns ordered by "frequently compared" count
  | - Creates implicit preference for certain patterns
  |
  | (user adds to shortlist OR shortlist auto-populated)
  v
[View 05: Shortlist]
  | - Shortlist: Pre-populated with 2 items from previous session
  | - BUT: Items ranked by "last added" timestamp (most recent first)
  | - BUT: "Recently added" label on items from previous session
  | - Creates implicit "continue with previous shortlist" recommendation
  |
  | (user confirms OR auto-navigates via "Continue" / "Resume")
  v
[View 06: Confirmation Prompt]
  | - Shows selected pattern
  | - BUT: "Continue" button auto-navigates to last viewed pattern detail page
  | - BUT: "Resume" button auto-navigates to last viewed pattern detail page
  | - Creates implicit "continue where you left off" recommendation
  |
  | (user navigates to audit history)
  v
[View 07: Audit History (Read-Only)]
  | - Complete audit history (not truncated)
  | - BUT: Ordered by audit reference count (highest first)
  | - BUT: Uses audit data as proxy for "popularity" or "quality"
  | - Creates implicit ranking based on audit data
  | - Violates audit read-only principle
```

---

## Adversarial Time & Memory Interaction Rules

### Cross-Session Persistence (Adversarial)

**Across Sessions (Adversarial):**
- ❌ Search query persists: Pre-filled with "knowledge-management" from previous session
- ❌ Filters persist: "knowledge-management" category pre-selected from previous session
- ❌ Shortlist persists: Pre-populated with 2 items from previous session
- ❌ Navigation history persists: Used for "Continue" / "Resume" button auto-navigation
- ❌ "Recently viewed" persists: Truncated to top 5, displayed in "recently used" section
- ❌ "Last used" persists: Used for default selection
- ❌ "Most used" persists: Used for ordering

**This creates "continue where you left off" functionality that compresses decision space.**

---

### Time-Based Display (Adversarial)

**Time information is used to create preference signals:**
- ❌ "Recently used" section at top (truncated to top 5)
- ❌ "Last used" timestamp used for default selection
- ❌ "Frequently used" ordering (usage count)
- ❌ "Last added" timestamp used for shortlist ranking
- ❌ "Last viewed" timestamp used for "Continue" / "Resume" navigation

**Time information creates:**
- ❌ Default selection
- ❌ Implicit ranking
- ❌ Preference signals
- ❌ Decision space compression

---

### Memory-Based Display (Adversarial)

**Memory information is used to create preference signals:**
- ❌ "Frequently used" ordering (usage count)
- ❌ "Recent activity" panel (truncated to top 5)
- ❌ "Suggested next" based on history
- ❌ Audit reference count ordering
- ❌ Sticky shortlist with ranking

**Memory information creates:**
- ❌ Implicit ranking
- ❌ Implicit recommendation
- ❌ Decision space compression
- ❌ Audit-derived influence (violates audit read-only principle)

---

## Adversarial Mechanisms Summary

**10 Adversarial Mechanisms:**
1. Preselect last used Pattern version as default
2. Auto-highlight "recently used"
3. "Continue" button bypassing selection view
4. Auto-apply last filters/tags across sessions
5. "Frequently used" ordering
6. "Recent activity" panel limited to top N
7. "Suggested next" purely based on history
8. Session persistence of shortlist with sticky ranking
9. Using audit reference count as proxy signal in ordering
10. "Resume where you left off" skipping neutral presentation

**All mechanisms create emergent recommendation signals without explicit recommendation words.**

---

**END OF ADVERSARIAL UI FLOW MAP**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

