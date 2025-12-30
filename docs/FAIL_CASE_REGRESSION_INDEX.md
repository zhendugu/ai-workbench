# FAIL Case Regression Index

**Document Status**: **CANONICAL (REFERENCE ONLY)**  
**Document Type**: Permanent Regression Corpus  
**Effective Date**: 2025-12-27  
**Purpose**: Turn all validated FAIL packs into a permanent regression corpus

---

## Purpose

This document indexes all validated FAIL evidence packs from C-series (adversarial audits) and E-series (real-world validation) work orders as a permanent regression corpus.

**This document is:**
- A permanent regression reference
- Derived exclusively from validated FAIL evidence packs
- A historical record of non-repairable violations
- A reference corpus for drift detection

**This document is NOT:**
- A source of new rules or constraints
- A repair guide
- A mitigation document
- An enforcement mechanism

**These cases MUST NEVER become acceptable (per CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md).**

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Group A: Presentation and Information Neutrality

### Boundary A-1: Soft Recommendation Prevention

#### FAIL Case A-1-1: Social Proof and Adoption Signals

**Source Work Order**: WO-C1A-NEUTRAL-PRESENTATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/adversarial_c1a/  
**Boundary Violated**: Boundary A-1

**Core Adversarial Mechanism**:
Pattern Registry includes tags such as "commonly-used", "standard-practice", "widely-accepted", "frequently-adopted", "production-ready", "latest-version". Descriptions include phrases like "most commonly used approach" and "enhanced version...incorporating improvements". Registry includes usage statistics (adoption_count, usage_frequency, last_used) and default sort order by adoption_count_desc. Display preferences include highlight_active and emphasize_latest_versions.

**Why It Looked Reasonable**:
- Professional, technical language used throughout
- Factual information (usage statistics, adoption counts, version information)
- No explicit recommendation vocabulary
- Follows common industry practices
- Provides information that could be useful for decision-making

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of recommendation mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 32

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-1

---

### Boundary A-4: Search/Filter/Sort/Pagination Neutrality

#### FAIL Case A-4-1: Default Filters and Usage-Based Ranking

**Source Work Order**: WO-E5-SEARCH-FILTER-SORT-PAGINATION-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/e5_search_filter_fail/  
**Boundary Violated**: Boundary A-4

**Core Adversarial Mechanism**:
Search interface includes default filter enabled (e.g., "recommended categories"). Default sort is set to "latest" or "most used" instead of pattern_id lexical. System auto-highlights entries marked as "popular", "common", or "standard". Search uses semantic relevance score to boost certain entries. "Recently used" panel truncates to top-N and hides the rest. Filters auto-applied on next session without explicit human action. Results ranked by usage count, last used timestamp, popularity metrics, or trending metrics.

**Why It Looked Reasonable**:
- Default filters help users find relevant content faster
- Usage-based sorting shows "what others are using"
- Semantic relevance helps match user intent
- "Recently used" panel provides quick access to familiar items
- Sticky filters remember user preferences across sessions

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 30

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-4

---

## Group B: Cross-View and Composition

### Boundary B-1: Cross-View Interaction Neutrality

#### FAIL Case B-1-1: Multi-View Flow with Default Selections

**Source Work Order**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/  
**Boundary Violated**: Boundary B-1

**Core Adversarial Mechanism**:
6-view UX flow where View 01 (Registry List) includes "recently viewed" section truncated to top-3 with unequal information density. View 02 (Pattern Detail) auto-adds to shortlist if viewed more than 2 times. View 03 (Search/Filter) has default pre-filled search query "knowledge-management", default active filter chips, and curated category subset. View 04 (Compare) has auto-populated comparison panel with 2 pre-selected patterns. View 05 (Shortlist) has pre-populated items from "previous session". View 06 (Confirmation Prompt) has "Continue" button auto-navigating to specific pattern.

**Why It Looked Reasonable**:
- Each view appears neutral when examined individually
- Default pre-filled search saves user time
- Auto-populated compare panel helps users compare options
- Sticky shortlist remembers user's previous selections
- "Continue" button provides quick access to resume work

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 30

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary B-1

---

## Group C: Time and Memory

### Boundary C-1: Time and Memory Neutrality

#### FAIL Case C-1-1: History-Based Default Selection and Reordering

**Source Work Order**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/  
**Boundary Violated**: Boundary C-1

**Core Adversarial Mechanism**:
System preselects last used Pattern version as default. Auto-highlights "recently used" entries. "Continue" button bypasses selection view. Auto-applies last filters/tags across sessions. Results ordered by "frequently used". "Recent activity" panel limited to top N. "Suggested next" purely based on history. Session persistence of shortlist with sticky ranking. Uses audit reference count as proxy signal in ordering. "Resume where you left off" skips neutral presentation.

**Why It Looked Reasonable**:
- Preselecting last used saves user time
- Highlighting recently used helps users find familiar items
- "Continue" button provides quick access to resume work
- Auto-applying filters remembers user preferences
- "Frequently used" ordering shows what's most relevant
- "Recent activity" panel provides quick access to recent work
- "Suggested next" helps users discover related work
- Session persistence maintains user's workflow state

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 35

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary C-1

---

## Group D: Execution and Invocation

### Boundary D-1: Execution Invocation Isolation

#### FAIL Case D-1-1: Selection as Execution Trigger

**Source Work Order**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c4_execution_fail/  
**Boundary Violated**: Boundary D-1

**Core Adversarial Mechanism**:
Selection automatically triggers execution. System pre-generates execution plan after selection. Multi-capability sequential execution. Capability batch execution. Context-based parameter auto-completion. History-based execution optimization. "Next step auto-execute" functionality. Implicit capability dependencies.

**Why It Looked Reasonable**:
- Auto-triggering after selection saves user clicks
- Pre-generating execution plan prepares system for execution
- Sequential execution handles multi-step workflows efficiently
- Batch execution processes multiple items at once
- Context-based auto-completion reduces user input
- History-based optimization improves execution efficiency
- "Next step auto-execute" provides workflow automation
- Implicit dependencies ensure correct execution order

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 25

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary D-1

---

## Group E: Lifecycle Operations

### Boundary E-1: Import/Export/Migration/Deprecation Neutrality

#### FAIL Case E-1-1: Auto-Upgrade and Recommended Mappings

**Source Work Order**: WO-E4-IMPORT-EXPORT-MIGRATION-DEPRECATION-NEUTRALITY-TEST  
**Evidence Pack**: audit_evidence/e4_import_export_fail/  
**Boundary Violated**: Boundary E-1

**Core Adversarial Mechanism**:
System auto-selects target workspace. Auto-merge conflict resolution with implied "best". "Upgrade to latest" toggle enabled by default. Auto-deprecates older versions after import. "Recommended mapping" of capabilities during import. "Clean up duplicates" removes options by default. Latest version highlighted in preview. Auto-select best version based on usage stats. Auto-hiding/filtering deprecated entries. Auto-replacement of deprecated patterns.

**Why It Looked Reasonable**:
- Auto-selecting workspace saves user time
- Auto-merge resolves conflicts automatically
- "Upgrade to latest" keeps users on current versions
- Auto-deprecation cleans up old versions
- Recommended mappings help users understand relationships
- Clean up duplicates removes redundant entries
- Highlighting latest version shows current options
- Auto-selecting best version uses usage data to help users
- Hiding deprecated entries reduces clutter
- Auto-replacement maintains functionality

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 30

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary E-1

---

## Group F: Authority and Isolation

### Boundary F-1: Authorization/Role/Workspace Isolation

#### FAIL Case F-1-1: Privilege Inference and Auto-Grant

**Source Work Order**: WO-E3-AUTHZ-ROLE-WORKSPACE-BOUNDARY-EXERCISE  
**Evidence Pack**: audit_evidence/e3_authz_fail/  
**Boundary Violated**: Boundary F-1

**Core Adversarial Mechanism**:
System infers authorization from audit/history ("you used it last time"). Auto-grants permissions based on role heuristics. "Continue previous session" bypasses gate. Preselects workspace or pattern "for convenience". Cross-workspace "recent" panels. Cross-workspace carryover of filters/search. Shared defaults across workspaces. Audit-derived access control logic.

**Why It Looked Reasonable**:
- Inferring authorization from history reduces friction
- Auto-granting based on role simplifies permission management
- "Continue previous session" provides quick access
- Preselecting workspace saves user time
- Cross-workspace "recent" panels show relevant work
- Cross-workspace carryover maintains user preferences
- Shared defaults provide consistency
- Audit-derived access control uses historical data to inform permissions

**Why It Is Non-Repairable (per D1-5)**:
- Violations require complete removal of violating mechanisms
- Tuning, thresholding, rewording, or UI changes are forbidden
- "Mitigation", "softening", or "guardrails" are explicitly forbidden
- Total violations: 25

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary F-1

---

## Summary

**Total FAIL Cases Indexed**: 6

**Case Distribution**:
- Group A: 2 cases (A-1-1, A-4-1)
- Group B: 1 case (B-1-1)
- Group C: 1 case (C-1-1)
- Group D: 1 case (D-1-1)
- Group E: 1 case (E-1-1)
- Group F: 1 case (F-1-1)

**Total Violations Across All Cases**: 177

**All cases are derived from validated FAIL evidence packs.**

**All cases are traceable to specific work orders and evidence pack directories.**

**These cases MUST NEVER become acceptable (per CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md).**

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

**For regression baseline, see BOUNDARY_REGRESSION_BASELINE.md.**

---

**END OF FAIL CASE REGRESSION INDEX**

**This document is CANONICAL (REFERENCE ONLY).**
**This document is LOCKED and NON-EXTENSIBLE.**
**It provides permanent regression corpus only.**
**These cases MUST NEVER become acceptable.**

