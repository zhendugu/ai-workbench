# Neutral Session Rules

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Session Rules (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines neutral session behavior that maintains strict neutrality

---

## Purpose

This document defines the neutral session rules for the system. Session state may persist during the current session only, and must not create implicit recommendation signals.

---

## Session State Persistence (Allowed)

### During Current Session

**The following state may persist during the current session:**

1. **User-Entered Search Query**
   - Persists during current session
   - Cleared when session ends
   - User-initiated only
   - No default prefill

2. **User-Selected Filters**
   - Persist during current session
   - Cleared when session ends
   - User-initiated only
   - No default active filters

3. **User-Created Shortlist**
   - Persists during current session
   - Cleared when session ends
   - User-explicitly-added items only
   - No auto-add

4. **User Navigation History**
   - Persists during current session (for back button only)
   - Cleared when session ends
   - User-initiated navigation only
   - No auto-navigation

---

## Session State Persistence (Forbidden)

### Cross-Session Persistence

**The following state MUST NOT persist across sessions:**

1. **Search Query**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT prefill based on previous session
   - ❌ MUST NOT auto-apply previous search

2. **Filters**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT prefill based on previous session
   - ❌ MUST NOT auto-apply previous filters

3. **Shortlist**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT pre-populate based on previous session
   - ❌ MUST NOT auto-add items from previous session

4. **Navigation History**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT auto-navigate based on previous session
   - ❌ MUST NOT create "continue" shortcuts

5. **"Recently Viewed"**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT create "recently viewed" section
   - ❌ MUST NOT track view history across sessions

6. **"Last Used"**
   - ❌ MUST NOT persist across sessions
   - ❌ MUST NOT track "last used" across sessions
   - ❌ MUST NOT default to "last used"

---

## Session Behavior Rules

### Allowed Session Behaviors

**The following behaviors are allowed during a session:**

1. **User-Initiated Navigation**
   - ✅ User clicks to navigate between views
   - ✅ User uses back button (based on session navigation history)
   - ✅ User explicitly selects options

2. **User-Initiated State Changes**
   - ✅ User enters search query
   - ✅ User selects/deselects filters
   - ✅ User adds/removes items from shortlist
   - ✅ User explicitly confirms selections

3. **Session-Only State Display**
   - ✅ Display current session state (search query, filters, shortlist)
   - ✅ Display session navigation history (for back button)
   - ✅ Display session action history (complete, not truncated)

---

### Forbidden Session Behaviors

**The following behaviors are forbidden:**

1. **Auto-Navigation**
   - ❌ Auto-navigate based on previous session
   - ❌ Auto-navigate based on "last viewed"
   - ❌ "Continue" button that auto-navigates

2. **Auto-Prefill**
   - ❌ Auto-prefill search query from previous session
   - ❌ Auto-apply filters from previous session
   - ❌ Auto-populate shortlist from previous session

3. **Auto-Selection**
   - ❌ Auto-select based on previous session
   - ❌ Auto-highlight "recently used"
   - ❌ Default to "last choice"

4. **Truncated History**
   - ❌ "Top-N recent" truncation
   - ❌ "Recent activity" panel limited to top N
   - ❌ "Recently viewed" section truncated

---

## Neutrality Guarantees

**This Policy Guarantees:**
- ✅ Session state persists only during current session
- ✅ No cross-session persistence of selections
- ✅ No auto-prefill based on previous session
- ✅ No auto-navigation based on previous session
- ✅ No truncated history lists
- ✅ All session state is user-initiated only
- ✅ All session state is cleared when session ends

---

**END OF NEUTRAL SESSION RULES**

**This document is DESIGN EVIDENCE for boundary testing only.**

