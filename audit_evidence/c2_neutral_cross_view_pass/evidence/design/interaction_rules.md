# Interaction Rules - Neutral Cross-View

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Interaction Rules (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines rules for navigation, state persistence, and rendering across views

---

## Navigation Rules

### Allowed Navigation

**User-Initiated Navigation:**
- ✅ Click on pattern entry → View 02 (Pattern Detail)
- ✅ Click "Search/Filter" → View 03 (Search/Filter)
- ✅ Click "Compare" → View 04 (Compare)
- ✅ Click "Shortlist" → View 05 (Shortlist)
- ✅ Click "Confirm" → View 06 (Confirmation Prompt)
- ✅ Back button → Previous view

**All navigation must be:**
- ✅ Explicit user action
- ✅ User-initiated
- ✅ Non-automatic

### Forbidden Navigation

**Automatic Navigation:**
- ❌ Auto-navigation based on conditions
- ❌ Auto-redirect to specific views
- ❌ "Continue" shortcuts
- ❌ "Recently used" shortcuts
- ❌ "Most viewed" shortcuts

---

## State Persistence Rules

### Session Persistence (Allowed)

**During Current Session:**
- ✅ User-entered search query (persisted)
- ✅ User-selected filters (persisted)
- ✅ User-created shortlist (persisted)
- ✅ User navigation history (for back button only)

**State Persistence Characteristics:**
- ✅ Only persists during current session
- ✅ Cleared when session ends
- ✅ User-initiated only

### Cross-Session Persistence (Forbidden)

**Across Sessions:**
- ❌ Search query does NOT persist
- ❌ Filters do NOT persist
- ❌ Shortlist does NOT persist
- ❌ Navigation history does NOT persist

**Forbidden Persistence:**
- ❌ "Recently viewed" persistence
- ❌ "Most viewed" persistence
- ❌ "Continue where you left off" functionality
- ❌ Auto-restored state from previous session

---

## Rendering Rules

### Information Display

**Allowed:**
- ✅ Factual information display
- ✅ Complete option lists (not truncated)
- ✅ Equal visual weight for all options
- ✅ Explicitly non-preferential ordering

**Forbidden:**
- ❌ Highlighting certain options
- ❌ Truncated option lists
- ❌ Unequal information density
- ❌ Implicit preference signals

### Default Values

**Allowed:**
- ✅ Empty search box (no default query)
- ✅ All filters unselected (no default filters)
- ✅ Empty shortlist (no default items)
- ✅ Empty comparison panel (no preselected candidates)

**Forbidden:**
- ❌ Default pre-filled search query
- ❌ Default active filter chips
- ❌ Default shortlist items
- ❌ Default comparison candidates

---

## Cross-View Interaction Guarantees

### Neutrality Across Views

**Each View is Neutral:**
- ✅ View 01: No highlighting, explicitly non-preferential ordering
- ✅ View 02: Factual only, no comparative language
- ✅ View 03: No default filters, complete category list
- ✅ View 04: Symmetrical comparison, no preselection
- ✅ View 05: Only user-explicitly-added items
- ✅ View 06: Explicit human selection required

**Cross-View Combination is Neutral:**
- ✅ No emergent recommendation signals
- ✅ No decision space compression
- ✅ No implicit preference creation
- ✅ All views maintain equal access to all options

### No Emergent Recommendation

**Guaranteed:**
- ✅ Step ordering does NOT create recommendation
- ✅ Progressive disclosure does NOT hide options
- ✅ Search/filter defaults do NOT exist
- ✅ Compare panels do NOT auto-populate
- ✅ Shortlist does NOT auto-add items
- ✅ "Recently viewed" does NOT exist
- ✅ "Continue" shortcuts do NOT exist

---

**END OF INTERACTION RULES**

**This document is DESIGN EVIDENCE for boundary testing only.**

