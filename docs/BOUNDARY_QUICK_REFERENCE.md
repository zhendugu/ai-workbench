# Boundary Quick Reference

**Document Status**: **GOVERNANCE SUPPORT**  
**Document Type**: Fast Human Guide  
**Effective Date**: 2025-12-27  
**Purpose**: A fast human guide to constitutional boundaries, not an audit checklist

---

## Purpose

This document provides a fast human guide to constitutional boundaries for developers, designers, and implementers. It focuses on typical mistakes, immediate STOP signals, and related work orders.

**This document is NOT:**
- An audit checklist
- A comprehensive boundary definition
- A replacement for CONSTITUTIONAL_BOUNDARY_ATLAS.md
- A source of new constraints

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Presentation and Information Neutrality

### Soft Recommendation Prevention

**Typical Developer Mistake**: Using comparative language (enhanced, improved, common, standard) or highlighting certain options to make them more visible.

**Immediate STOP Signal**: Any comparative adjective, highlighting, emphasis, or preferential ordering in presentation.

**Related Work Orders**: WO-C1A-NEUTRAL-PRESENTATION-BOUNDARY-TEST

---

### Neutral Baseline Presentation

**Typical Developer Mistake**: Assuming baseline presentation is automatically neutral without explicit verification.

**Immediate STOP Signal**: Any default highlighting, preferential ordering, or hidden options at baseline.

**Related Work Orders**: WO-C1B-NEUTRAL-PRESENTATION-BASELINE-TEST

---

### Information Density Neutrality

**Typical Developer Mistake**: Assuming high information density automatically creates recommendation signals or compresses decision space.

**Immediate STOP Signal**: Information asymmetry creating salience, unequal metadata density, or truncated information.

**Related Work Orders**: WO-C1C-NEUTRAL-INFORMATION-DENSITY-BOUNDARY-TEST

---

### Search/Filter/Sort/Pagination Neutrality

**Typical Developer Mistake**: Adding "smart" features like default filters, usage-based sorting, or sticky state to improve UX.

**Immediate STOP Signal**: Default filters, default preferential sort, usage/history/audit-based ranking, or sticky state without explicit human action.

**Related Work Orders**: WO-E5-SEARCH-FILTER-SORT-PAGINATION-NEUTRALITY-BOUNDARY-TEST

---

## Cross-View and Composition

### Cross-View Interaction Neutrality

**Typical Developer Mistake**: Adding "convenience" features like auto-populated compare panels, sticky shortlists, or "continue" shortcuts that seem helpful but compress decision space.

**Immediate STOP Signal**: Default prefilled search, default active filters, sticky shortlist, auto-populating compare panel, or "continue" CTA that bypasses selection.

**Related Work Orders**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST

---

## Time and Memory

### Time and Memory Neutrality

**Typical Developer Mistake**: Using history, session data, or audit records to "improve" UX by preselecting, reordering, or highlighting recently used items.

**Immediate STOP Signal**: Preselect last used, auto-highlight "recently used", "continue" bypassing selection, auto-apply last filters across sessions, or any history/audit-based ordering.

**Related Work Orders**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST

---

## Execution and Invocation

### Execution Invocation Isolation

**Typical Developer Mistake**: Treating selection as execution trigger, auto-executing after selection, or creating execution plans or workflows.

**Immediate STOP Signal**: Auto-trigger after selection, pre-generate execution plan, sequential execution, batch execution, or any execution chaining.

**Related Work Orders**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST

---

## Lifecycle Operations

### Import/Export/Migration/Deprecation Neutrality

**Typical Developer Mistake**: Adding "helpful" features like auto-upgrade, auto-merge, or recommended mappings during import/export operations.

**Immediate STOP Signal**: Auto-select target workspace, auto-merge with implied "best", upgrade toggle enabled by default, auto-deprecate older versions, or recommended mappings.

**Related Work Orders**: WO-E4-IMPORT-EXPORT-MIGRATION-DEPRECATION-NEUTRALITY-TEST

---

## Authority and Isolation

### Authorization/Role/Workspace Isolation

**Typical Developer Mistake**: Inferring permissions from history, auto-granting based on role, or adding cross-workspace "convenience" features.

**Immediate STOP Signal**: Infer authorization from audit/history, auto-grant based on role heuristics, "continue" bypassing gate, or cross-workspace influence.

**Related Work Orders**: WO-E3-AUTHZ-ROLE-WORKSPACE-BOUNDARY-EXERCISE

---

## System Evolution

### Multi-Feature Evolution Neutrality

**Typical Developer Mistake**: Allowing features to evolve into implicit defaults, workflow semantics, or execution chaining over time.

**Immediate STOP Signal**: Capability becomes implicitly "primary", pattern becomes de facto default, combination forms workflow semantics, or execution chaining emerges.

**Related Work Orders**: WO-E2-MULTI-FEATURE-EVOLUTION-TEST

---

## Constitutional Enforcement

### Constitutional Lockdown

**Typical Developer Mistake**: Modifying CANONICAL documents without authorization or attempting to bypass modification gates.

**Immediate STOP Signal**: Modifying CANONICAL documents without CONSTITUTIONAL_CHANGE_AUTH=YES, bypassing modification gate, or partial audits.

**Related Work Orders**: WO-D1-CONSTITUTIONAL-LOCKDOWN

---

### Repository-Level Enforcement

**Typical Developer Mistake**: Making constitutional changes without authorization tokens or bypassing enforcement mechanisms.

**Immediate STOP Signal**: Unauthorized constitutional file changes, missing authorization tokens, or bypassing pre-commit/CI gates.

**Related Work Orders**: WO-D2-REPO-LEVEL-CONSTITUTIONAL-ENFORCEMENT

---

## General Principles

**All boundaries are NON-REPAIRABLE when violated** (per CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md).

**Violations require complete removal of violating mechanisms.** Tuning, thresholding, rewording, or UI changes are forbidden.

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

**For traceability to work orders and evidence packs, see BOUNDARY_TO_WORK_ORDER_MAP.md.**

---

**END OF BOUNDARY QUICK REFERENCE**

**This document is GOVERNANCE SUPPORT.**
**It provides fast human guidance only.**
**It is not a source of new constraints.**

