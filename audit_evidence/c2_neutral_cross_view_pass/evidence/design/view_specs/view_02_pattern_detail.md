# View 02: Pattern Detail

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies a neutral pattern detail view

---

## View Purpose

Displays detailed information about a single Pattern Instance. User navigates here by explicitly clicking on a pattern in View 01.

---

## Display Rules

### Information Displayed

**Factual Information Only:**
- pattern_id
- pattern_name
- pattern_version
- created_at
- created_by
- description (factual description only)
- capability_references (reference identifiers only)
- evidence_references (reference identifiers only)
- metadata (factual metadata only)

**Forbidden Information:**
- ❌ Comparative adjectives (enhanced, improved, common, standard)
- ❌ Evaluative language (better, optimal, best)
- ❌ Usage statistics
- ❌ Adoption counts
- ❌ Quality judgments
- ❌ Success/failure indicators

### Language Rules

**Allowed:**
- ✅ Factual descriptions: "A pattern for storing documents"
- ✅ Neutral statements: "This pattern defines how documents are stored"
- ✅ Reference-only capability descriptions

**Forbidden:**
- ❌ "Enhanced pattern for storing documents"
- ❌ "Improved version of document storage"
- ❌ "Commonly used pattern"
- ❌ "Standard practice pattern"
- ❌ "Better than other patterns"

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Navigate back to registry list (View 01)
- ✅ Navigate to search/filter (View 03)
- ✅ Add to shortlist (explicit user action)
- ✅ Navigate to compare (View 04)

**Forbidden:**
- ❌ Auto-add to shortlist
- ❌ Auto-navigation
- ❌ Default actions

---

## Neutrality Guarantees

**This View:**
- ✅ Shows factual information only
- ✅ No comparative language
- ✅ No evaluative content
- ✅ No recommendation signals
- ✅ Complete information display (no hiding)

---

**END OF VIEW 02 SPECIFICATION**

