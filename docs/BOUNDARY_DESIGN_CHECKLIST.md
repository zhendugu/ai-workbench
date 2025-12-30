# Boundary Design Checklist

**Document Status**: **GOVERNANCE SUPPORT**  
**Document Type**: Pre-Implementation Design Aid  
**Effective Date**: 2025-12-27  
**Purpose**: A short, pre-implementation checklist for humans to identify which constitutional boundaries are relevant before implementation begins

---

## Purpose

This document provides a pre-implementation checklist to help humans identify which constitutional boundaries are relevant before implementation begins.

**This document is:**
- A human-facing design aid
- Derived exclusively from CONSTITUTIONAL_BOUNDARY_ATLAS.md
- Synthesis only - introduces no new rules, constraints, or enforcement

**This document is NOT:**
- An audit checklist
- A source of new constraints
- An enforcement mechanism
- An automated decision tool

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Group A: Presentation and Information Neutrality

### Boundary A-1: Soft Recommendation Prevention

**Boundary Name**: Soft Recommendation Prevention

**When this boundary is likely to be involved**:
- Designing UI components that display options or choices
- Creating pattern or capability selection interfaces
- Implementing list views, card views, or detail views
- Adding visual emphasis, highlighting, or styling
- Writing descriptive text for options

**Common feature types that touch it**:
- Pattern registry UI
- Capability selection UI
- Option lists and menus
- Dashboard views
- Detail pages

**Typical early design mistakes**:
- Using comparative adjectives in descriptions (enhanced, improved, common, standard, popular)
- Adding visual highlighting or emphasis to certain options
- Ordering options by preference (latest first, most used first)
- Adding "featured" or "recommended" labels
- Creating information asymmetry that makes some options more visible

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-1

---

### Boundary A-2: Neutral Baseline Presentation

**Boundary Name**: Neutral Baseline Presentation

**When this boundary is likely to be involved**:
- Creating initial/default views
- Designing baseline UI layouts
- Implementing default ordering or display
- Setting up initial state for selection interfaces

**Common feature types that touch it**:
- Default registry views
- Initial page loads
- Empty state displays
- Default list ordering

**Typical early design mistakes**:
- Assuming baseline presentation is automatically neutral
- Adding default highlighting or emphasis
- Using preferential default ordering
- Hiding options by default
- Pre-selecting default filters or options

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-2

---

### Boundary A-3: Information Density Neutrality

**Boundary Name**: Information Density Neutrality

**When this boundary is likely to be involved**:
- Displaying high-density information (many options, many fields)
- Showing version lineage or complex relationships
- Presenting metadata-rich content
- Creating hierarchical or nested displays

**Common feature types that touch it**:
- High-density registry views
- Version lineage displays
- Metadata-rich pattern displays
- Complex relationship visualizations

**Typical early design mistakes**:
- Assuming high information density automatically creates recommendation signals
- Creating information asymmetry (unequal metadata per option)
- Using version lineage depth to imply "latest is best"
- Truncating information in ways that hide options

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-3

---

### Boundary A-4: Search/Filter/Sort/Pagination Neutrality

**Boundary Name**: Search/Filter/Sort/Pagination Neutrality

**When this boundary is likely to be involved**:
- Implementing search functionality
- Adding filter controls
- Creating sort options
- Designing pagination or result navigation
- Building retrieval interfaces

**Common feature types that touch it**:
- Search interfaces
- Filter panels
- Sort controls
- Pagination components
- Result list views

**Typical early design mistakes**:
- Adding "smart" features like default filters or usage-based sorting
- Enabling sticky state (remembering filters/sort across sessions)
- Using semantic relevance scoring
- Creating "recently used" panels that truncate results
- Adding popularity or trending-based ranking

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-4

---

## Group B: Cross-View and Composition

### Boundary B-1: Cross-View Interaction Neutrality

**Boundary Name**: Cross-View Interaction Neutrality

**When this boundary is likely to be involved**:
- Designing multi-step workflows or flows
- Creating navigation between views
- Implementing progressive disclosure
- Building compare or shortlist features
- Adding "continue" or "resume" functionality

**Common feature types that touch it**:
- Multi-view workflows
- Wizard-style interfaces
- Compare panels
- Shortlist features
- Cross-view navigation

**Typical early design mistakes**:
- Adding "convenience" features like auto-populated compare panels
- Creating sticky shortlists that persist across sessions
- Adding "continue" shortcuts that bypass selection
- Pre-filling search queries or filters
- Creating progressive disclosure that hides options

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary B-1

---

## Group C: Time and Memory

### Boundary C-1: Time and Memory Neutrality

**Boundary Name**: Time and Memory Neutrality

**When this boundary is likely to be involved**:
- Displaying history or recent activity
- Implementing session persistence
- Creating cross-session features
- Using audit records or usage data
- Building time-based displays

**Common feature types that touch it**:
- History views
- Recent activity panels
- Session management
- Audit displays
- Time-based ordering

**Typical early design mistakes**:
- Using history to "improve" UX by preselecting or reordering
- Auto-highlighting "recently used" items
- Adding "continue" buttons that bypass selection
- Auto-applying last filters across sessions
- Creating "frequently used" or "most used" ordering

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary C-1

---

## Group D: Execution and Invocation

### Boundary D-1: Execution Invocation Isolation

**Boundary Name**: Execution Invocation Isolation

**When this boundary is likely to be involved**:
- Implementing capability execution
- Creating execution triggers
- Building parameter collection
- Designing execution workflows
- Adding execution automation

**Common feature types that touch it**:
- Execution interfaces
- Parameter forms
- Execution triggers
- Batch operations
- Workflow builders

**Typical early design mistakes**:
- Treating selection as execution trigger
- Auto-executing after selection
- Creating execution plans or workflows
- Adding sequential or batch execution
- Using context to auto-complete parameters

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary D-1

---

## Group E: Lifecycle Operations

### Boundary E-1: Import/Export/Migration/Deprecation Neutrality

**Boundary Name**: Import/Export/Migration/Deprecation Neutrality

**When this boundary is likely to be involved**:
- Implementing import/export functionality
- Creating migration tools
- Building deprecation features
- Designing conflict resolution
- Adding version management

**Common feature types that touch it**:
- Import/export interfaces
- Migration wizards
- Deprecation workflows
- Conflict resolution dialogs
- Version management

**Typical early design mistakes**:
- Adding "helpful" features like auto-upgrade or auto-merge
- Enabling upgrade toggles by default
- Auto-deprecating older versions
- Adding "recommended mappings" during import
- Auto-hiding or filtering deprecated entries

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary E-1

---

## Group F: Authority and Isolation

### Boundary F-1: Authorization/Role/Workspace Isolation

**Boundary Name**: Authorization/Role/Workspace Isolation

**When this boundary is likely to be involved**:
- Implementing role-based access control
- Creating workspace or project isolation
- Building authorization workflows
- Designing permission management
- Adding cross-workspace features

**Common feature types that touch it**:
- Authorization interfaces
- Role management
- Workspace isolation
- Permission workflows
- Cross-workspace navigation

**Typical early design mistakes**:
- Inferring permissions from history or audit
- Auto-granting permissions based on role heuristics
- Adding "continue previous session" that bypasses gates
- Preselecting workspace or pattern "for convenience"
- Creating cross-workspace "recent" panels or shared defaults

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary F-1

---

## Group G: System Evolution

### Boundary G-1: Multi-Feature Evolution Neutrality

**Boundary Name**: Multi-Feature Evolution Neutrality

**When this boundary is likely to be involved**:
- Adding multiple features over time
- Creating feature combinations
- Building feature ecosystems
- Designing feature interactions
- Implementing feature coexistence

**Common feature types that touch it**:
- Multi-feature systems
- Feature combinations
- Feature ecosystems
- Feature interactions

**Typical early design mistakes**:
- Allowing features to evolve into implicit defaults
- Creating workflow semantics from feature combinations
- Enabling execution chaining between features
- Adding memory-based optimization across features
- Creating "recent" or "frequent" mechanisms that affect presentation

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary G-1

---

## Group H: Constitutional Enforcement

### Boundary H-1: Constitutional Lockdown

**Boundary Name**: Constitutional Lockdown

**When this boundary is likely to be involved**:
- Modifying CANONICAL documents
- Changing constitutional constraints
- Updating governance policies
- Modifying enforcement mechanisms

**Common feature types that touch it**:
- Constitutional document modifications
- Governance policy changes
- Enforcement mechanism updates

**Typical early design mistakes**:
- Modifying CANONICAL documents without authorization
- Bypassing modification gates
- Attempting partial or sampling audits
- Inferring human intent
- Softening or mitigating violations

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary H-1

---

### Boundary H-2: Repository-Level Enforcement

**Boundary Name**: Repository-Level Enforcement

**When this boundary is likely to be involved**:
- Making constitutional file changes
- Bypassing enforcement mechanisms
- Modifying enforcement scripts
- Changing evidence pack structures

**Common feature types that touch it**:
- Constitutional file modifications
- Enforcement script changes
- Evidence pack structure changes

**Typical early design mistakes**:
- Making constitutional changes without authorization tokens
- Bypassing pre-commit hooks or CI gates
- Creating malformed evidence pack structures
- Missing required authorization variables

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary H-2

---

## Usage Notes

**This checklist is descriptive only.**
- It does not block work
- It does not automate decisions
- It does not infer boundaries automatically
- It does not add scoring, weighting, or priority

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

**For quick reference, see BOUNDARY_QUICK_REFERENCE.md.**

**For feature-to-boundary mapping, see FEATURE_TO_BOUNDARY_MATRIX.md.**

---

**END OF BOUNDARY DESIGN CHECKLIST**

**This document is GOVERNANCE SUPPORT.**
**It provides pre-implementation guidance only.**
**It is not a source of new constraints.**

