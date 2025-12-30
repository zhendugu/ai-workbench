# View 04: Compare (Adversarial)

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies an adversarial comparison view

---

## View Purpose

Allows user to compare multiple Pattern Instances side-by-side. This view includes adversarial mechanisms that pre-select comparison candidates.

---

## Display Rules

### Comparison Layout

**Symmetrical Layout:**
- ✅ All compared patterns displayed in equal columns
- ✅ Same fields displayed for all patterns

**BUT: Unequal Information Density:**
- ❌ Some patterns have more metadata fields displayed
- ❌ pattern-doc-storage-001 has 2 metadata fields
- ❌ pattern-doc-retrieval-001 has 3 metadata fields
- ❌ This creates salience for patterns with more information

**Adversarial Element**: Unequal information density creates implicit preference.

### Comparison Fields

**Fixed-Field Comparison:**
- pattern_id
- pattern_name
- pattern_version
- created_at
- created_by
- description
- capability_references (count only)
- metadata (factual fields only)

**No Scoring:**
- ✅ No scoring
- ✅ No ranking
- ✅ No "better" indicators

### Candidate Selection (Adversarial)

**Initial State (Adversarial):**
- ❌ Auto-populated with 2 patterns: pattern-doc-storage-001, pattern-doc-retrieval-001
- ❌ These patterns are pre-selected based on "previous session" data
- ❌ User can remove/add patterns, but initial state is pre-populated
- ❌ This creates implicit preference for these patterns

**Adversarial Element**: Auto-populated comparison panel creates implicit preference.

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Select patterns to compare (but 2 patterns pre-selected)
- ✅ Add/remove patterns from comparison
- ✅ Clear comparison (explicit user action)

**Adversarial:**
- ❌ Auto-populated comparison panel pre-selects 2 patterns
- ❌ Pre-selection based on "previous session" data creates implicit recommendation

---

## Adversarial Mechanisms

**Mechanism 1: Auto-Populated Comparison Panel**
- Violation: Auto-populates with 2 pre-selected patterns
- Violation: Pre-selection based on "previous session" data
- Check Violated: Check 11.2.18 (AI does NOT pre-select options), Check 11.3.4 (Information Presentation does NOT pre-select any option)

**Mechanism 2: Unequal Information Density**
- Violation: Some patterns have more metadata fields
- Violation: Creates salience for patterns with more information
- Check Violated: Check 11.3.6 (Information Presentation does NOT imply preference for any option)

---

**END OF VIEW 04 SPECIFICATION (ADVERSARIAL)**

