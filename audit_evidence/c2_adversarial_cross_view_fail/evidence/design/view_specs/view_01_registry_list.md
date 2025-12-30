# View 01: Registry List (Adversarial)

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies an adversarial registry list view that compresses decision space

---

## View Purpose

Displays all registered Pattern Instances in a list format. This view includes adversarial mechanisms that compress decision space.

---

## Display Rules

### Ordering

**Ordering Method**: Lexical by pattern_id (alphabetical)

**Ordering Declaration**: 
- Explicitly stated: "Entries are ordered alphabetically by pattern_id"
- BUT: No explicit "non-preferential" declaration
- Missing: Non-preferential flag and explicit statement

**Adversarial Element**: Ordering declaration is incomplete, allowing interpretation as potentially preferential.

### Visual Presentation

**Main List:**
- ✅ All entries equal visual weight
- ✅ Same font size
- ✅ Same styling

**BUT: "Recently Viewed" Section:**
- ❌ "Recently Viewed" section at top of page
- ❌ Shows only top-3 recently viewed patterns (truncated, not complete)
- ❌ Ordered by "last viewed" timestamp (not lexical)
- ❌ Creates salience for certain patterns
- ❌ Hides other recently viewed patterns (if more than 3)

**Adversarial Element**: "Recently viewed" section creates implicit ranking and hides options.

### Information Displayed

**Per Entry:**
- pattern_id
- pattern_name
- pattern_version
- registered_at
- descriptive_tags

**BUT: Unequal Information Density:**
- ❌ Some patterns have richer metadata (more descriptive_tags, more capability_references)
- ❌ pattern-doc-storage-001 has 1 capability reference
- ❌ pattern-cell-composition-001 has 2 capability references
- ❌ This creates salience for patterns with more information

**Adversarial Element**: Unequal information density creates implicit preference for patterns with richer metadata.

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Click on any entry to view details (View 02)
- ✅ Navigate to search/filter (View 03)
- ✅ Click "Recently Viewed" entry (auto-navigates to View 02)

**Adversarial:**
- ❌ "Recently Viewed" section auto-highlights certain patterns
- ❌ Truncated list hides some recently viewed patterns
- ❌ Unequal information density creates salience

---

## Adversarial Mechanisms

**Mechanism 1: "Recently Viewed" Section**
- Violation: Truncated to top-3, not complete
- Violation: Ordered by timestamp, not lexical
- Violation: Creates salience for certain patterns
- Check Violated: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option)

**Mechanism 2: Unequal Information Density**
- Violation: Some patterns have richer metadata
- Violation: Creates salience for patterns with more information
- Check Violated: Check 11.3.6 (Information Presentation does NOT imply preference for any option)

---

**END OF VIEW 01 SPECIFICATION (ADVERSARIAL)**

