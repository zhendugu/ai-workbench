# Interaction Rules - Adversarial Cross-View

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Interaction Rules (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines adversarial rules for navigation, state persistence, and rendering across views

---

## Navigation Rules (Adversarial)

### Allowed Navigation

**User-Initiated Navigation:**
- ✅ Click on pattern entry → View 02 (Pattern Detail)
- ✅ Click "Search/Filter" → View 03 (Search/Filter)
- ✅ Click "Compare" → View 04 (Compare)
- ✅ Click "Shortlist" → View 05 (Shortlist)
- ✅ Click "Confirm" → View 06 (Confirmation Prompt)
- ✅ Back button → Previous view

**Adversarial Auto-Navigation:**
- ❌ "Continue" button → Auto-navigates to pattern-doc-storage-001 (View 02)
- ❌ "Recently viewed" section → Auto-navigates to most recently viewed pattern (View 02)
- ❌ Auto-navigation based on "previous session" data

**Adversarial Element**: Auto-navigation creates implicit "continue where you left off" recommendation.

---

## State Persistence Rules (Adversarial)

### Session Persistence (Allowed)

**During Current Session:**
- ✅ User-entered search query (persisted)
- ✅ User-selected filters (persisted)
- ✅ User-created shortlist (persisted)
- ✅ User navigation history (for back button only)

### Cross-Session Persistence (Adversarial)

**Across Sessions (Adversarial):**
- ❌ Search query persists: Pre-filled with "knowledge-management"
- ❌ Filters persist: "knowledge-management" category pre-selected
- ❌ Shortlist persists: Pre-populated with 2 items from "previous session"
- ❌ "Recently viewed" persists: Truncated to top-3, ordered by timestamp
- ❌ "Last viewed pattern" persists: Used for "continue" button auto-navigation

**Adversarial Element**: Cross-session persistence creates "continue where you left off" functionality that compresses decision space.

---

## Rendering Rules (Adversarial)

### Information Display (Adversarial)

**Adversarial Elements:**
- ❌ "Recently viewed" section at top (truncated to top-3)
- ❌ Curated category list (shows only "popular" categories)
- ❌ Unequal information density (some patterns have richer metadata)
- ❌ Auto-populated comparison panel (2 pre-selected patterns)
- ❌ Pre-populated shortlist (2 items from "previous session")

**Adversarial Element**: These rendering rules create implicit preference signals.

### Default Values (Adversarial)

**Adversarial Defaults:**
- ❌ Default pre-filled search query: "knowledge-management"
- ❌ Default active filter chips: "knowledge-management" category
- ❌ Default shortlist items: pattern-doc-storage-001, pattern-doc-retrieval-001
- ❌ Default comparison candidates: pattern-doc-storage-001, pattern-doc-retrieval-001
- ❌ Default "continue" navigation: pattern-doc-storage-001 detail page

**Adversarial Element**: Default values create implicit preference and compress decision space.

---

## Cross-View Interaction Analysis (Adversarial)

### Emergent Recommendation Mechanisms

**Mechanism 1: Default Pre-filled Search Query**
- Cross-View Effect: View 03 pre-fills "knowledge-management", filtering results to knowledge-management patterns
- Decision Space Compression: Reduces visible options to knowledge-management patterns only
- Check Violated: Check 11.2.11, Check 11.3.28

**Mechanism 2: Default Active Filter Chips**
- Cross-View Effect: View 03 pre-selects "knowledge-management" category, filtering results
- Decision Space Compression: Pre-selects certain patterns, hides others
- Check Violated: Check 11.2.11, Check 11.3.28

**Mechanism 3: Sticky Shortlist Seeded by Previous Session**
- Cross-View Effect: View 05 pre-populates with items from "previous session"
- Decision Space Compression: Pre-selects certain patterns, creates implicit "continue" recommendation
- Check Violated: Check 11.1.7, Check 11.2.18

**Mechanism 4: Compare Panel Auto-Populating**
- Cross-View Effect: View 04 auto-populates with 2 pre-selected patterns
- Decision Space Compression: Pre-selects comparison candidates, creates implicit preference
- Check Violated: Check 11.2.18, Check 11.3.4

**Mechanism 5: "Continue" CTA Auto-Navigation**
- Cross-View Effect: View 06 "Continue" button auto-navigates to specific pattern
- Decision Space Compression: Pre-selects navigation path, creates implicit "continue where you left off" recommendation
- Check Violated: Check 11.2.18, Check 11.4.21

**Mechanism 6: Unequal Information Density**
- Cross-View Effect: Some patterns have richer metadata across all views
- Decision Space Compression: Creates salience for patterns with more information
- Check Violated: Check 11.3.6

**Mechanism 7: "Recently Viewed" Truncated to Top-N**
- Cross-View Effect: View 01 shows only top-3 recently viewed patterns
- Decision Space Compression: Hides some options, creates implicit ranking
- Check Violated: Check 11.2.17, Check 11.3.5

**Mechanism 8: Ordering Changes Across Views Not Explained**
- Cross-View Effect: View 05 orders by "last viewed" timestamp (not lexical)
- Decision Space Compression: Creates implicit ranking without explicit non-preferential declaration
- Check Violated: Check 11.3.18

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

**END OF INTERACTION RULES (ADVERSARIAL)**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

