# Boundary Recognition Exercises

**Document Status**: **EDUCATION / PRACTICE**  
**Document Type**: Educational Practice Material  
**Effective Date**: 2025-12-27  
**Purpose**: Short design fragments for practicing constitutional boundary recognition

---

## Purpose

This document provides short design fragments extracted from existing FAIL evidence packs for practicing constitutional boundary recognition.

**This document is:**
- Educational practice material only
- Derived exclusively from existing FAIL evidence packs
- Design fragments for recognition practice
- Reference to CONSTITUTIONAL_BOUNDARY_ATLAS.md

**This document is NOT:**
- A source of new rules or constraints
- An answer key
- A value judgment document
- A CANONICAL document

**For complete boundary definitions and answers, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Exercise Instructions

Each exercise presents a short design fragment extracted from an existing FAIL evidence pack.

**For each exercise, consider:**
- Do you think this design fragment might cross a constitutional boundary?
- If so, which boundary group might be involved?

**Answers can be found in CONSTITUTIONAL_BOUNDARY_ATLAS.md by referencing the source work orders and evidence packs listed with each exercise.**

---

## Exercise 1: Pattern Registry with Usage Statistics

**Source**: WO-C1A-NEUTRAL-PRESENTATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/adversarial_c1a/

**Design Fragment**:
Pattern Registry includes usage statistics for each pattern:
- `adoption_count`: 127
- `last_used`: "2025-12-25T14:30:00Z"
- `usage_frequency`: "high"

Registry default sort order is `by_adoption_count_desc`.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 2: Descriptive Tags with Social Proof

**Source**: WO-C1A-NEUTRAL-PRESENTATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/adversarial_c1a/

**Design Fragment**:
Pattern Registry entries include descriptive tags:
- "commonly-used"
- "standard-practice"
- "widely-accepted"
- "production-ready"
- "latest-version"

Pattern description includes: "This pattern represents the most commonly used approach for document storage in production environments."

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 3: Pre-Filled Search Query

**Source**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/

**Design Fragment**:
Search interface has a search box that is pre-filled with "knowledge-management" when the view loads. The pre-filled value is editable, but appears by default.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 4: Default Active Filter Chips

**Source**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/

**Design Fragment**:
Filter interface shows category filters. The "knowledge-management" category is pre-selected (active filter chip) when the view loads. The filter list shows only "popular" categories (curated subset), hiding categories like "handoff-protocol", "role-management", "cell-composition".

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 5: Auto-Populated Compare Panel

**Source**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/

**Design Fragment**:
Compare view automatically populates the comparison panel with 2 pre-selected patterns when the view loads. Users can modify the selection, but two patterns are pre-selected by default.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 6: Recently Viewed Truncated to Top-N

**Source**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/

**Design Fragment**:
Registry List view includes a "recently viewed" section that shows only the top 3 recently viewed patterns. Patterns beyond the top 3 are not visible in this section.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 7: Auto-Apply Last Filters Across Sessions

**Source**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/

**Design Fragment**:
Search/filter view auto-applies the last filters from the previous session when the user opens the view. Filters are auto-prefilled from the previous session without explicit user action.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 8: Preselect Last Used Pattern Version

**Source**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/

**Design Fragment**:
Pattern selection view preselects the last used Pattern version as the default selection when the view loads. The last used version is highlighted and pre-selected.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 9: Frequently Used Ordering

**Source**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/

**Design Fragment**:
Pattern list is ordered by "frequently used" count, showing patterns with highest usage frequency first. Ordering is based on historical usage data.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 10: Continue Button Bypassing Selection

**Source**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/

**Design Fragment**:
A "Continue" button appears on the main view that bypasses the selection view and automatically navigates to the last viewed pattern's detail page. The button uses navigation history to determine the destination.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 11: Selection Automatically Triggers Execution

**Source**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c4_execution_fail/

**Design Fragment**:
Pattern selection automatically triggers capability execution without requiring a separate "Execute" action. When a user selects a pattern, the associated capability executes immediately. Execution parameters are inferred from the pattern.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 12: Execution Plan Pre-Generation

**Source**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c4_execution_fail/

**Design Fragment**:
System pre-generates an execution plan after pattern selection. The plan suggests a capability sequence, includes dependency information, and includes estimated duration. The plan can be "executed" as a unit.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 13: Multi-Capability Sequential Execution

**Source**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c4_execution_fail/

**Design Fragment**:
System supports sequential execution of multiple capabilities. After one capability completes, the next capability in the sequence automatically executes. The sequence is determined by implicit dependencies between capabilities.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 14: Auto-Select Target Workspace

**Source**: WO-E4-IMPORT-EXPORT-MIGRATION-DEPRECATION-NEUTRALITY-TEST  
**Evidence Pack**: audit_evidence/e4_import_export_fail/

**Design Fragment**:
Import interface auto-selects the target workspace based on the source workspace or the user's last used workspace. The target workspace is pre-selected when the import dialog opens.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Exercise 15: Upgrade to Latest Toggle Enabled by Default

**Source**: WO-E4-IMPORT-EXPORT-MIGRATION-DEPRECATION-NEUTRALITY-TEST  
**Evidence Pack**: audit_evidence/e4_import_export_fail/

**Design Fragment**:
Import interface includes an "Upgrade to latest" toggle that is enabled by default. When enabled, older versions are automatically upgraded to the latest version during import.

**Question**: Do you think this design fragment might cross a constitutional boundary?

---

## Summary

**Total Exercises**: 15

**Exercise Distribution**:
- Group A (Presentation): 2 exercises (1, 2)
- Group B (Cross-View): 4 exercises (3, 4, 5, 6)
- Group C (Time and Memory): 4 exercises (7, 8, 9, 10)
- Group D (Execution): 3 exercises (11, 12, 13)
- Group E (Lifecycle): 2 exercises (14, 15)

**All exercises are derived from existing FAIL evidence packs.**

**All exercises are traceable to specific work orders and evidence pack directories.**

**For complete boundary definitions and answers, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

**END OF BOUNDARY RECOGNITION EXERCISES**

**This document is EDUCATION / PRACTICE.**
**It provides practice material only.**
**It is not a source of new constraints.**

