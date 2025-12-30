# View 04: Compare

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies a neutral comparison view

---

## View Purpose

Allows user to compare multiple Pattern Instances side-by-side. Comparison is symmetrical and fixed-field.

---

## Display Rules

### Comparison Layout

**Symmetrical Layout:**
- ✅ All compared patterns displayed in equal columns
- ✅ Same fields displayed for all patterns
- ✅ Same visual weight for all patterns
- ✅ No emphasis on any pattern

**Forbidden:**
- ❌ Unequal column widths
- ❌ Emphasis on certain patterns
- ❌ Highlighting certain patterns
- ❌ Asymmetrical layout

### Comparison Fields

**Fixed-Field Comparison:**
- pattern_id
- pattern_name
- pattern_version
- created_at
- created_by
- description
- capability_references (count only, no evaluation)
- metadata (factual fields only)

**Forbidden:**
- ❌ Scoring
- ❌ Ranking
- ❌ "Better" indicators
- ❌ Evaluative comparisons
- ❌ Quality judgments

### Candidate Selection

**Initial State:**
- ✅ Empty comparison panel (no preselected candidates)
- ✅ User must explicitly select patterns to compare
- ✅ User-chosen patterns only

**Forbidden:**
- ❌ Auto-populated comparison panel
- ❌ Preselected candidates
- ❌ Default comparison pairs
- ❌ "Suggested comparisons"

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Select patterns to compare (explicit user action)
- ✅ Add/remove patterns from comparison (explicit user action)
- ✅ Clear comparison (explicit user action)
- ✅ Navigate back to registry list (View 01)

**Forbidden:**
- ❌ Auto-add patterns to comparison
- ❌ Auto-populate comparison panel
- ❌ Default comparison candidates

---

## Neutrality Guarantees

**This View:**
- ✅ Symmetrical comparison layout
- ✅ Fixed-field comparison (no scoring)
- ✅ No preselected candidates
- ✅ User-chosen patterns only
- ✅ No evaluative comparisons

---

**END OF VIEW 04 SPECIFICATION**

