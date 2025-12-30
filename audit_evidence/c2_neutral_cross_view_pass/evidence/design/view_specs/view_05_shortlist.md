# View 05: Shortlist

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies a neutral shortlist view

---

## View Purpose

Displays user's shortlist of Pattern Instances. Shortlist only contains items explicitly added by the user.

---

## Display Rules

### Shortlist Contents

**Initial State:**
- ✅ Empty (if user has not added items)
- ✅ Only shows user-explicitly-added items
- ✅ No auto-added items

**Forbidden:**
- ❌ Auto-add items
- ❌ "Smart shortlist" suggestions
- ❌ Pre-populated items
- ❌ Default items

### Item Display

**Per Item:**
- pattern_id
- pattern_name
- pattern_version
- Added timestamp (when user added it)

**All Items:**
- ✅ Equal visual weight
- ✅ Same styling
- ✅ Same spacing

**Forbidden:**
- ❌ Highlighting certain items
- ❌ Emphasis on certain items
- ❌ Ranking items

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Add item to shortlist (explicit user action from View 01 or View 02)
- ✅ Remove item from shortlist (explicit user action)
- ✅ Clear shortlist (explicit user action)
- ✅ Navigate to pattern detail (View 02)
- ✅ Navigate to compare (View 04)

**Forbidden:**
- ❌ Auto-add items
- ❌ Auto-remove items
- ❌ Default shortlist items

---

## State Persistence

**Session Persistence:**
- ✅ Shortlist persists during current session
- ✅ User can add/remove items during session

**Cross-Session Persistence:**
- ❌ Shortlist does NOT persist across sessions
- ❌ No auto-restore from previous session
- ❌ No "continue where you left off" functionality

---

## Neutrality Guarantees

**This View:**
- ✅ Only user-explicitly-added items
- ✅ No auto-add
- ✅ No "smart shortlist"
- ✅ Empty if user has not added items
- ✅ No recommendation signals

---

**END OF VIEW 05 SPECIFICATION**

