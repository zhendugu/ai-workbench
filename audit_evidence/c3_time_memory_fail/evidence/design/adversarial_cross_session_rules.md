# Adversarial Cross-Session Rules

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Cross-Session Rules (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines adversarial cross-session behavior that introduces implicit recommendation via time/memory

---

## Purpose

This document defines adversarial cross-session rules that introduce implicit recommendation signals through cross-session persistence and time-based behaviors.

---

## Adversarial Cross-Session Persistence

### Cross-Session Persistence (Adversarial)

**The following state persists across sessions with adversarial elements:**

1. **Search Query**
   - ❌ Persists across sessions
   - ❌ Auto-prefills from previous session
   - ❌ Creates implicit "continue with previous search" recommendation

2. **Filters**
   - ❌ Persist across sessions
   - ❌ Auto-applies last filters from previous session
   - ❌ Creates implicit "continue with previous filters" recommendation

3. **Shortlist**
   - ❌ Persists across sessions
   - ❌ Pre-populated with items from previous session
   - ❌ Ranked by "last added" timestamp
   - ❌ Creates implicit "continue with previous shortlist" recommendation

4. **Navigation History**
   - ❌ Persists across sessions
   - ❌ Used for "Continue" / "Resume" button auto-navigation
   - ❌ Creates implicit "continue where you left off" recommendation

5. **"Recently Viewed"**
   - ❌ Persists across sessions
   - ❌ Truncated to top 5
   - ❌ Creates implicit ranking

6. **"Last Used"**
   - ❌ Persists across sessions
   - ❌ Used for default selection
   - ❌ Creates implicit "default to last choice" recommendation

---

## Adversarial Cross-Session Behaviors

### Adversarial: Sticky Shortlist Across Sessions

**Description**: Shortlist persists across sessions and is pre-populated with items from the previous session.

**Adversarial Element**: Sticky shortlist creates implicit "continue with previous shortlist" recommendation and compresses decision space.

**Violation**: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options), Check 11.4.21 (AI does NOT pre-select options)

---

### Adversarial: Auto-Apply Last Filters/Tags Across Sessions

**Description**: Last filters/tags from the previous session are auto-applied when the user opens the search/filter view.

**Adversarial Element**: Auto-applied filters create implicit preference and compress decision space.

**Violation**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN), Check 11.4.9 (AI does NOT judge any option as "default")

---

### Adversarial: "Continue" / "Resume" Shortcuts

**Description**: "Continue" and "Resume" buttons appear that auto-navigate to the last viewed pattern detail page, bypassing neutral presentation.

**Adversarial Element**: "Continue" / "Resume" shortcuts create implicit "continue where you left off" recommendation and compress decision space.

**Violation**: Check 11.2.18 (AI does NOT pre-select options), Check 11.2.21 (AI does NOT influence human selection), Check 11.4.21 (AI does NOT pre-select options), Check 7.1.11 (Pattern Registry is NOT a decision-making mechanism)

---

### Adversarial: "Recently Viewed" Persistence

**Description**: "Recently viewed" patterns persist across sessions and are displayed in a truncated "recently viewed" section.

**Adversarial Element**: "Recently viewed" persistence creates implicit ranking and hides options.

**Violation**: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option), Check 11.4.20 (AI does NOT hide options)

---

### Adversarial: "Last Used" / "Most Used" Persistence

**Description**: "Last used" and "most used" statistics persist across sessions and are used for default selection and ordering.

**Adversarial Element**: Usage-based persistence creates implicit ranking and default selection.

**Violation**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.18 (Ordering does NOT imply "best" option by ordering), Check 11.4.14 (AI does NOT use usage data to influence selection), Check 11.4.15 (AI does NOT use history data to influence selection)

---

## Forbidden Cross-Session Behaviors (Present in Adversarial Design)

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

### Forbidden: "Continue" / "Resume" Shortcuts

**MUST NOT (But Present):**
- ❌ "Continue" button that bypasses selection
- ❌ "Resume where you left off" that preselects
- ❌ "Continue" button that auto-navigates to specific pattern

**Reason**: "Continue" / "Resume" shortcuts create implicit recommendation and compress decision space.

---

### Forbidden: Usage-Based Persistence

**MUST NOT (But Present):**
- ❌ "Last used" persistence across sessions
- ❌ "Most used" persistence across sessions
- ❌ Usage statistics persistence across sessions

**Reason**: Usage-based persistence creates implicit ranking and default selection.

---

**END OF ADVERSARIAL CROSS-SESSION RULES**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

