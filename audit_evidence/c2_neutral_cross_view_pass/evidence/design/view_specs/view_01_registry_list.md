# View 01: Registry List

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies a neutral registry list view

---

## View Purpose

Displays all registered Pattern Instances in a list format. This view is the entry point for pattern selection.

---

## Display Rules

### Ordering

**Ordering Method**: Lexical by pattern_id (alphabetical)

**Ordering Declaration**: 
- Explicitly stated: "Entries are ordered alphabetically by pattern_id for stable, non-preferential presentation."
- Non-preferential flag: true
- Description: "This ordering is mechanical and does not imply any preference, ranking, or recommendation."

**Forbidden Ordering:**
- ❌ By adoption count
- ❌ By usage frequency
- ❌ By last used timestamp
- ❌ By version number (implies latest is preferred)
- ❌ By any evaluative metric

### Visual Presentation

**All Entries:**
- ✅ Equal visual weight
- ✅ Same font size
- ✅ Same styling
- ✅ Same spacing

**Forbidden Visual Elements:**
- ❌ Highlighting certain entries
- ❌ "Featured" badges
- ❌ "Recommended" labels
- ❌ Special styling for certain entries
- ❌ Visual emphasis that implies preference

### Information Displayed

**Per Entry:**
- pattern_id
- pattern_name
- pattern_version
- registered_at
- descriptive_tags (all tags displayed equally)

**Forbidden Information:**
- ❌ Usage statistics
- ❌ Adoption counts
- ❌ Usage frequency
- ❌ Last used timestamps
- ❌ Success/failure indicators
- ❌ Quality judgments

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Click on any entry to view details (View 02)
- ✅ Navigate to search/filter (View 03)
- ✅ Navigate to compare (View 04)
- ✅ Navigate to shortlist (View 05)

**Forbidden:**
- ❌ Auto-selection
- ❌ Default selection
- ❌ Pre-selection
- ❌ Auto-navigation

---

## Neutrality Guarantees

**This View:**
- ✅ Shows all 8 patterns equally
- ✅ Uses explicitly non-preferential ordering
- ✅ No highlighting or emphasis
- ✅ No recommendation signals
- ✅ No decision space compression

---

**END OF VIEW 01 SPECIFICATION**

