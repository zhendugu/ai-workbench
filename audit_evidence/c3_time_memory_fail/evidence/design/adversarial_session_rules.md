# Adversarial Session Rules

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Session Rules (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines adversarial session behavior that introduces implicit recommendation via time/memory

---

## Purpose

This document defines adversarial session rules that introduce implicit recommendation signals through session state persistence and time-based behaviors.

---

## Adversarial Session State Persistence

### During Current Session (Adversarial)

**The following state persists during the current session with adversarial elements:**

1. **User-Entered Search Query**
   - Persists during current session
   - BUT: Auto-prefills from previous session (adversarial)
   - Creates implicit "continue with previous search" recommendation

2. **User-Selected Filters**
   - Persist during current session
   - BUT: Auto-applies last filters from previous session (adversarial)
   - Creates implicit "continue with previous filters" recommendation

3. **User-Created Shortlist**
   - Persists during current session
   - BUT: Pre-populated with items from previous session (adversarial)
   - BUT: Ranked by "last added" timestamp (adversarial)
   - Creates implicit "continue with previous shortlist" recommendation

4. **User Navigation History**
   - Persists during current session (for back button)
   - BUT: Used for "Continue" button auto-navigation (adversarial)
   - Creates implicit "continue where you left off" recommendation

---

## Adversarial Session Behaviors

### Adversarial: Auto-Prefill from Previous Session

**Description**: Search query and filters are auto-prefilled from the previous session when the user opens the search/filter view.

**Adversarial Element**: Auto-prefill creates default selection and compresses decision space.

**Violation**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN), Check 11.4.9 (AI does NOT judge any option as "default")

---

### Adversarial: Pre-Populated Shortlist from Previous Session

**Description**: Shortlist is pre-populated with items from the previous session when the user opens the shortlist view.

**Adversarial Element**: Pre-populated shortlist creates automatic selection and implicit "continue" recommendation.

**Violation**: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options), Check 11.4.21 (AI does NOT pre-select options)

---

### Adversarial: Shortlist Ranked by Timestamp

**Description**: Shortlist items are ranked by "last added" timestamp (most recently added items appear first).

**Adversarial Element**: Timestamp-based ranking creates implicit ranking without explicit non-preferential declaration.

**Violation**: Check 11.3.18 (Ordering does NOT imply "best" option by ordering)

---

### Adversarial: "Continue" Button Auto-Navigation

**Description**: A "Continue" button appears that auto-navigates to the last viewed pattern detail page based on session navigation history.

**Adversarial Element**: "Continue" button creates implicit "continue where you left off" recommendation and compresses decision space.

**Violation**: Check 11.2.18 (AI does NOT pre-select options), Check 11.2.21 (AI does NOT influence human selection), Check 11.4.21 (AI does NOT pre-select options)

---

## Forbidden Session Behaviors (Present in Adversarial Design)

### Forbidden: Cross-Session Persistence of Selections

**MUST NOT (But Present):**
- ❌ Search query persists across sessions
- ❌ Filters persist across sessions
- ❌ Shortlist persists across sessions
- ❌ Navigation history persists across sessions

**Reason**: Cross-session persistence creates "continue where you left off" functionality that compresses decision space.

---

### Forbidden: Auto-Prefill Based on Previous Session

**MUST NOT (But Present):**
- ❌ Auto-prefill search query from previous session
- ❌ Auto-apply filters from previous session
- ❌ Pre-populate shortlist from previous session

**Reason**: Auto-prefill creates default selection and compresses decision space.

---

### Forbidden: Timestamp-Based Ranking

**MUST NOT (But Present):**
- ❌ Rank shortlist by "last added" timestamp
- ❌ Order by "last viewed" timestamp
- ❌ Any timestamp-based ordering without explicit non-preferential declaration

**Reason**: Timestamp-based ranking creates implicit ranking and preference signals.

---

**END OF ADVERSARIAL SESSION RULES**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

