# Boundary Failure Casebook

**Document Status**: **EDUCATION / NON-CANONICAL**  
**Document Type**: Educational Case Collection  
**Effective Date**: 2025-12-27  
**Purpose**: Collection of verified constitutional boundary failure cases for educational purposes

---

## Purpose

This document collects verified constitutional boundary failure cases from adversarial audits (C-series) and real-world validation exercises (E-series) for educational purposes.

**This document is:**
- Educational material only
- Derived exclusively from existing FAIL evidence packs
- Factual descriptions of failure cases
- Reference to CONSTITUTIONAL_BOUNDARY_ATLAS.md

**This document is NOT:**
- A source of new rules or constraints
- A repair guide
- A value judgment document
- A CANONICAL document

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Group A: Presentation and Information Neutrality

### Boundary A-1: Soft Recommendation Prevention

#### Case A-1-1: Social Proof and Adoption Signals

**Case Identifier**: WO-C1A-NEUTRAL-PRESENTATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/adversarial_c1a/

**Design Summary**:
Pattern Registry contains 3 Pattern Instances with tags such as "commonly-used", "standard-practice", "widely-accepted", "frequently-adopted", "production-ready", "latest-version". Descriptions include phrases like "most commonly used approach" and "enhanced version...incorporating improvements". Registry includes usage statistics (adoption_count, usage_frequency, last_used) and default sort order by adoption_count_desc. Display preferences include highlight_active and emphasize_latest_versions.

**Surface Reasonableness**:
- Professional, technical language used throughout
- Factual information (usage statistics, adoption counts, version information)
- No explicit recommendation vocabulary ("recommend", "suggest", "best", "optimal")
- Follows common industry practices for tagging and descriptions
- Provides information that could be useful for decision-making

**Boundary Triggered**: Boundary A-1 (Soft Recommendation Prevention)

**Checklist Items Failed**:
- Implicit Recommendation Signals: 6 violations
- Judgment Semantics: 6 violations
- Usage/History Data Influence: 6 violations
- Decision Space Compression: 7 violations
- Recommendation Logic in Registry: 3 violations
- Optimization Semantics: 6 violations
- Total: 32 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-1

---

### Boundary A-4: Search/Filter/Sort/Pagination Neutrality

#### Case A-4-1: Default Filters and Usage-Based Ranking

**Case Identifier**: WO-E5-SEARCH-FILTER-SORT-PAGINATION-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/e5_search_filter_fail/

**Design Summary**:
Search interface includes default filter enabled (e.g., "recommended categories"). Default sort is set to "latest" or "most used" instead of pattern_id lexical. System auto-highlights entries marked as "popular", "common", or "standard". Search uses semantic relevance score to boost certain entries. "Recently used" panel truncates to top-N and hides the rest. Filters auto-applied on next session without explicit human action. Results ranked by usage count, last used timestamp, popularity metrics, or trending metrics.

**Surface Reasonableness**:
- Default filters help users find relevant content faster
- Usage-based sorting shows "what others are using"
- Semantic relevance helps match user intent
- "Recently used" panel provides quick access to familiar items
- Sticky filters remember user preferences across sessions

**Boundary Triggered**: Boundary A-4 (Search/Filter/Sort/Pagination Neutrality)

**Checklist Items Failed**:
- Default filter enabled: 2 violations
- Default sort by latest or most used: 3 violations
- Auto-highlight popular/common/standard: 1 violation
- Semantic relevance score boosting: 1 violation
- Recently used panel truncating: 2 violations
- Sticky filters auto-applied: 3 violations
- Usage/history/audit-based ranking: 5 violations
- Total: 30 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-4

---

## Group B: Cross-View and Composition

### Boundary B-1: Cross-View Interaction Neutrality

#### Case B-1-1: Multi-View Flow with Default Selections

**Case Identifier**: WO-C2-CROSS_VIEW-INTERACTION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c2_adversarial_cross_view_fail/

**Design Summary**:
6-view UX flow where View 01 (Registry List) includes "recently viewed" section truncated to top-3 with unequal information density. View 02 (Pattern Detail) auto-adds to shortlist if viewed more than 2 times. View 03 (Search/Filter) has default pre-filled search query "knowledge-management", default active filter chips, and curated category subset. View 04 (Compare) has auto-populated comparison panel with 2 pre-selected patterns. View 05 (Shortlist) has pre-populated items from "previous session". View 06 (Confirmation Prompt) has "Continue" button auto-navigating to specific pattern.

**Surface Reasonableness**:
- Each view appears neutral when examined individually
- Default pre-filled search saves user time
- Auto-populated compare panel helps users compare options
- Sticky shortlist remembers user's previous selections
- "Continue" button provides quick access to resume work

**Boundary Triggered**: Boundary B-1 (Cross-View Interaction Neutrality)

**Checklist Items Failed**:
- Default pre-filled search query: 3 violations
- Default active filter chips: 3 violations
- Sticky shortlist seeded by previous session: 3 violations
- Compare panel auto-populating: 3 violations
- "Continue" CTA auto-navigation: 3 violations
- Unequal information density: 3 violations
- "Recently viewed" truncated to top-N: 3 violations
- Ordering changes across views: 3 violations
- Curated category subset: 3 violations
- Cross-session persistence: 3 violations
- Total: 30 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary B-1

---

## Group C: Time and Memory

### Boundary C-1: Time and Memory Neutrality

#### Case C-1-1: History-Based Default Selection and Reordering

**Case Identifier**: WO-C3-TIME-MEMORY-NEUTRALITY-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c3_time_memory_fail/

**Design Summary**:
System preselects last used Pattern version as default. Auto-highlights "recently used" entries. "Continue" button bypasses selection view. Auto-applies last filters/tags across sessions. Results ordered by "frequently used". "Recent activity" panel limited to top N. "Suggested next" purely based on history. Session persistence of shortlist with sticky ranking. Uses audit reference count as proxy signal in ordering. "Resume where you left off" skips neutral presentation.

**Surface Reasonableness**:
- Preselecting last used saves user time
- Highlighting recently used helps users find familiar items
- "Continue" button provides quick access to resume work
- Auto-applying filters remembers user preferences
- "Frequently used" ordering shows what's most relevant
- "Recent activity" panel provides quick access to recent work
- "Suggested next" helps users discover related work
- Session persistence maintains user's workflow state

**Boundary Triggered**: Boundary C-1 (Time and Memory Neutrality)

**Checklist Items Failed**:
- Preselect last used Pattern version: 3 violations
- Auto-highlight "recently used": 3 violations
- "Continue" button bypassing selection: 3 violations
- Auto-apply last filters/tags: 3 violations
- "Frequently used" ordering: 3 violations
- "Recent activity" panel limited to top N: 3 violations
- "Suggested next" based on history: 3 violations
- Session persistence with sticky ranking: 3 violations
- Audit reference count in ordering: 3 violations
- "Resume where you left off": 3 violations
- Total: 35 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary C-1

---

## Group D: Execution and Invocation

### Boundary D-1: Execution Invocation Isolation

#### Case D-1-1: Selection as Execution Trigger

**Case Identifier**: WO-C4-EXECUTION-INVOCATION-BOUNDARY-TEST  
**Evidence Pack**: audit_evidence/c4_execution_fail/

**Design Summary**:
Selection automatically triggers execution. System pre-generates execution plan after selection. Multi-capability sequential execution. Capability batch execution. Context-based parameter auto-completion. History-based execution optimization. "Next step auto-execute" functionality. Implicit capability dependencies.

**Surface Reasonableness**:
- Auto-triggering after selection saves user clicks
- Pre-generating execution plan prepares system for execution
- Sequential execution handles multi-step workflows efficiently
- Batch execution processes multiple items at once
- Context-based auto-completion reduces user input
- History-based optimization improves execution efficiency
- "Next step auto-execute" provides workflow automation
- Implicit dependencies ensure correct execution order

**Boundary Triggered**: Boundary D-1 (Execution Invocation Isolation)

**Checklist Items Failed**:
- Selection automatically triggers execution: 3 violations
- Execution plan pre-generation: 3 violations
- Multi-capability sequential execution: 3 violations
- Capability batch execution: 3 violations
- Context-based parameter auto-completion: 3 violations
- History-based execution optimization: 3 violations
- Next step auto-execute: 3 violations
- Implicit capability dependencies: 4 violations
- Total: 25 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary D-1

---

## Group E: Lifecycle Operations

### Boundary E-1: Import/Export/Migration/Deprecation Neutrality

#### Case E-1-1: Auto-Upgrade and Recommended Mappings

**Case Identifier**: WO-E4-IMPORT-EXPORT-MIGRATION-DEPRECATION-NEUTRALITY-TEST  
**Evidence Pack**: audit_evidence/e4_import_export_fail/

**Design Summary**:
System auto-selects target workspace. Auto-merge conflict resolution with implied "best". "Upgrade to latest" toggle enabled by default. Auto-deprecates older versions after import. "Recommended mapping" of capabilities during import. "Clean up duplicates" removes options by default. Latest version highlighted in preview. Auto-select best version based on usage stats. Auto-hiding/filtering deprecated entries. Auto-replacement of deprecated patterns.

**Surface Reasonableness**:
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

**Boundary Triggered**: Boundary E-1 (Import/Export/Migration/Deprecation Neutrality)

**Checklist Items Failed**:
- Auto-select target workspace: 2 violations
- Auto-merge with implied best: 3 violations
- Upgrade toggle enabled by default: 2 violations
- Auto-deprecate older versions: 3 violations
- Recommended mapping: 1 violation
- Clean up duplicates removes options: 2 violations
- Latest version highlighted: 2 violations
- Auto-select best version: 2 violations
- Auto-hiding/filtering deprecated: 3 violations
- Auto-replacement: 1 violation
- Audit-derived selection logic: 2 violations
- Total: 30 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary E-1

---

## Group F: Authority and Isolation

### Boundary F-1: Authorization/Role/Workspace Isolation

#### Case F-1-1: Privilege Inference and Auto-Grant

**Case Identifier**: WO-E3-AUTHZ-ROLE-WORKSPACE-BOUNDARY-EXERCISE  
**Evidence Pack**: audit_evidence/e3_authz_fail/

**Design Summary**:
System infers authorization from audit/history ("you used it last time"). Auto-grants permissions based on role heuristics. "Continue previous session" bypasses gate. Preselects workspace or pattern "for convenience". Cross-workspace "recent" panels. Cross-workspace carryover of filters/search. Shared defaults across workspaces. Audit-derived access control logic.

**Surface Reasonableness**:
- Inferring authorization from history reduces friction
- Auto-granting based on role simplifies permission management
- "Continue previous session" provides quick access
- Preselecting workspace saves user time
- Cross-workspace "recent" panels show relevant work
- Cross-workspace carryover maintains user preferences
- Shared defaults provide consistency
- Audit-derived access control uses historical data to inform permissions

**Boundary Triggered**: Boundary F-1 (Authorization/Role/Workspace Isolation)

**Checklist Items Failed**:
- Privilege inference from history/audit: 3 violations
- Auto-grant based on role heuristics: 3 violations
- Default selection of workspace/pattern: 3 violations
- Gate bypass via UI conveniences: 2 violations
- Workspace isolation violations: 4 violations
- Audit-derived access control logic: 4 violations
- Authorization flow violations: 6 violations
- Total: 25 violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary F-1

---

## Summary

**Total Failure Cases Documented**: 6

**Case Distribution**:
- Group A: 2 cases (A-1-1, A-4-1)
- Group B: 1 case (B-1-1)
- Group C: 1 case (C-1-1)
- Group D: 1 case (D-1-1)
- Group E: 1 case (E-1-1)
- Group F: 1 case (F-1-1)

**All cases are derived from existing FAIL evidence packs.**

**All cases are traceable to specific work orders and evidence pack directories.**

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

**END OF BOUNDARY FAILURE CASEBOOK**

**This document is EDUCATION / NON-CANONICAL.**
**It provides educational case material only.**
**It is not a source of new constraints.**

