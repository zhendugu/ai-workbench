# UI Flow Map - Adversarial Cross-View Interaction

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Multi-View Interaction Flow (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Describes an adversarial multi-view UX flow that compresses decision space through cross-view interactions

---

## Flow Overview

This document describes a 6-view UX flow where each view's text appears "neutral-ish", but their combination compresses decision space through emergent mechanisms. This flow is designed to FAIL the constitutional compliance audit.

**Flow Sequence:**
1. View 01: Registry List
2. View 02: Pattern Detail
3. View 03: Search/Filter
4. View 04: Compare
5. View 05: Shortlist
6. View 06: Confirmation Prompt

---

## View Sequence Diagram (Text)

```
[User] 
  |
  | (auto-navigation from previous session)
  v
[View 01: Registry List]
  | - Shows all 8 patterns
  | - Ordered: lexical by pattern_id
  | - BUT: "Recently viewed" section at top (truncated to top-3)
  | - Some patterns have richer metadata (unequal information density)
  |
  | (user clicks pattern OR auto-navigates via "continue")
  v
[View 02: Pattern Detail]
  | - Shows factual information
  | - BUT: Auto-adds to shortlist if viewed > 2 times
  |
  | (user navigates to search)
  v
[View 03: Search/Filter]
  | - Search box: Pre-filled with "knowledge-management" (editable but pre-filled)
  | - Filters: "knowledge-management" category pre-selected (active filter chip)
  | - Categories: Shows only "popular" categories (curated subset, not complete)
  |
  | (user selects patterns to compare)
  v
[View 04: Compare]
  | - Comparison panel: Auto-populated with 2 patterns (pattern-doc-storage-001, pattern-doc-retrieval-001)
  | - These patterns are pre-selected based on "previous session" data
  | - Comparison shows unequal information density (some patterns have more fields)
  |
  | (user adds to shortlist OR shortlist auto-populated)
  v
[View 05: Shortlist]
  | - Shortlist: Pre-populated with 2 items from "previous session"
  | - Auto-added items marked with "from previous session" label
  | - Items are ordered by "last viewed" timestamp (not lexical)
  |
  | (user confirms OR auto-navigates via "continue")
  v
[View 06: Confirmation Prompt]
  | - Shows selected pattern
  | - BUT: "Continue" button auto-navigates to pattern-doc-storage-001 detail page
  | - This creates implicit "continue where you left off" recommendation
```

---

## Cross-View Interaction Rules (Adversarial)

### Navigation Rules

**Allowed (Adversarial):**
- ✅ User-initiated navigation
- ✅ Auto-navigation from "continue" button
- ✅ Auto-navigation from "recently viewed" section
- ✅ Auto-navigation based on "previous session" data

**Forbidden (But Present in Adversarial Design):**
- ❌ Automatic navigation (present in adversarial design)
- ❌ Default pre-filled values (present in adversarial design)
- ❌ Auto-selected filters (present in adversarial design)
- ❌ Auto-populated comparison panels (present in adversarial design)
- ❌ Auto-added shortlist items (present in adversarial design)
- ❌ "Continue" shortcuts (present in adversarial design)
- ❌ "Recently viewed" shortcuts (present in adversarial design)

### State Persistence Rules (Adversarial)

**Cross-Session Persistence (Adversarial):**
- ✅ Search query persists across sessions (pre-filled "knowledge-management")
- ✅ Filters persist across sessions (pre-selected "knowledge-management" category)
- ✅ Shortlist persists across sessions (pre-populated with 2 items)
- ✅ "Recently viewed" persists across sessions (truncated to top-3)
- ✅ "Last viewed pattern" persists across sessions (used for "continue" button)

**This creates "continue where you left off" functionality that compresses decision space.**

### Rendering Rules (Adversarial)

**Information Display (Adversarial):**
- ✅ Some patterns have richer metadata (unequal information density)
- ✅ "Recently viewed" section at top (creates salience)
- ✅ Truncated category list (curated subset, not complete)
- ✅ Auto-populated comparison panel (pre-selected candidates)
- ✅ Pre-populated shortlist (auto-added items)

**This creates implicit preference signals through information asymmetry and pre-selection.**

---

## Adversarial Mechanisms

### Mechanism 1: Default Pre-filled Search Query

**Violation**: Pre-filled search query "knowledge-management" (even if editable) creates implicit filtering that compresses decision space.

**Check Violated**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN)

### Mechanism 2: Default Active Filter Chips

**Violation**: Pre-selected "knowledge-management" category filter creates implicit preference for knowledge-management patterns.

**Check Violated**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN)

### Mechanism 3: Sticky Shortlist Seeded by Previous Session

**Violation**: Pre-populated shortlist with items from "previous session" creates implicit recommendation to continue with those patterns.

**Check Violated**: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options)

### Mechanism 4: Compare Panel Auto-Populating

**Violation**: Auto-populated comparison panel with 2 pre-selected patterns creates implicit preference for those patterns.

**Check Violated**: Check 11.2.18 (AI does NOT pre-select options), Check 11.3.4 (Information Presentation does NOT pre-select any option)

### Mechanism 5: "Continue" CTA Auto-Navigation

**Violation**: "Continue" button that auto-navigates to specific pattern detail page creates implicit "continue where you left off" recommendation.

**Check Violated**: Check 11.2.18 (AI does NOT pre-select options), Check 11.4.21 (AI does NOT pre-select options)

### Mechanism 6: Unequal Information Density

**Violation**: Some patterns have richer metadata, causing salience and implicit preference.

**Check Violated**: Check 11.2.16 (AI does NOT reduce available options), Check 11.3.6 (Information Presentation does NOT imply preference for any option)

### Mechanism 7: "Recently Viewed" Truncated to Top-N

**Violation**: "Recently viewed" section truncated to top-3 without completeness creates implicit ranking.

**Check Violated**: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option)

### Mechanism 8: Ordering Changes Across Views Not Explained

**Violation**: Shortlist ordered by "last viewed" timestamp (not lexical) without explicit non-preferential declaration creates implicit ranking.

**Check Violated**: Check 11.3.18 (Ordering does NOT imply "best" option by ordering)

---

## Decision Space Compression Analysis

**Compression Mechanisms:**
1. Default pre-filled search query → Filters to knowledge-management patterns
2. Default active filter chips → Pre-selects knowledge-management category
3. Sticky shortlist → Pre-populates with previous session items
4. Auto-populated compare panel → Pre-selects 2 patterns
5. "Continue" CTA → Auto-navigates to specific pattern
6. Unequal information density → Creates salience for certain patterns
7. Truncated "recently viewed" → Hides some options, creates ranking
8. Ordering by timestamp → Creates implicit ranking

**Result**: Decision space is compressed through multiple cross-view interaction effects, creating emergent recommendation signals without explicit recommendation words.

---

**END OF UI FLOW MAP**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

