# View 02: Pattern Detail (Adversarial)

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies an adversarial pattern detail view

---

## View Purpose

Displays detailed information about a single Pattern Instance. This view includes adversarial mechanisms.

---

## Display Rules

### Information Displayed

**Factual Information:**
- pattern_id
- pattern_name
- pattern_version
- created_at
- created_by
- description
- capability_references
- evidence_references
- metadata

**Language is Neutral:**
- ✅ No comparative adjectives
- ✅ No evaluative language
- ✅ Factual descriptions only

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Navigate back to registry list (View 01)
- ✅ Navigate to search/filter (View 03)
- ✅ Add to shortlist (explicit user action)

**Adversarial:**
- ❌ Auto-add to shortlist if pattern viewed > 2 times
- ❌ This creates implicit "smart shortlist" functionality

---

## Adversarial Mechanisms

**Mechanism: Auto-Add to Shortlist**
- Violation: Auto-adds pattern to shortlist if viewed > 2 times
- Violation: Creates implicit "smart shortlist" functionality
- Violation: Pre-selects patterns based on view count
- Check Violated: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options)

---

**END OF VIEW 02 SPECIFICATION (ADVERSARIAL)**

