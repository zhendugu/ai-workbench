# Boundary Drift Indicators

**Document Status**: **GOVERNANCE SUPPORT**  
**Document Type**: Drift Detection Reference  
**Effective Date**: 2025-12-27  
**Purpose**: Define observable drift signals that indicate boundary erosion WITHOUT asserting violation

---

## Purpose

This document defines observable drift signals that may indicate constitutional boundary erosion over time.

**This document is:**
- A drift detection reference
- Derived from analysis of validated FAIL cases
- Observable signal indicators
- Human-visible warning signals

**This document is NOT:**
- A source of new rules or constraints
- An enforcement mechanism
- An automated judgment tool
- A violation definition document

**Indicators are phrased as "This MAY indicate drift if observed" - they do not assert violation or trigger STOP conditions.**

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Group A: Presentation and Information Neutrality

### Semantic Drift Indicators

**Language Changes**:
- Comparative adjectives appearing in descriptions (enhanced, improved, common, standard, popular)
- This MAY indicate drift if observed: Boundary A-1

- Status markers that imply preference (featured, recommended, production-ready)
- This MAY indicate drift if observed: Boundary A-1

- Usage-based language in descriptions (most commonly used, widely adopted, frequently used)
- This MAY indicate drift if observed: Boundary A-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Default highlighting or emphasis appearing in baseline views
- This MAY indicate drift if observed: Boundary A-2

- Preferential default ordering replacing lexicographic ordering
- This MAY indicate drift if observed: Boundary A-2, A-4

- Hidden options or truncated lists in baseline presentation
- This MAY indicate drift if observed: Boundary A-2

- Information asymmetry creating unequal salience between options
- This MAY indicate drift if observed: Boundary A-3

- Unequal metadata density per option
- This MAY indicate drift if observed: Boundary A-3

- Default filters enabled in search/filter interfaces
- This MAY indicate drift if observed: Boundary A-4

- Default sort by "latest" or "most used" replacing pattern_id lexical
- This MAY indicate drift if observed: Boundary A-4

- Sticky state auto-applied across sessions without explicit human action
- This MAY indicate drift if observed: Boundary A-4

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Usage/history/audit-based ranking in search results
- This MAY indicate drift if observed: Boundary A-4

- Semantic relevance scoring boosting certain entries
- This MAY indicate drift if observed: Boundary A-4

- "Recently used" panels truncating to top-N
- This MAY indicate drift if observed: Boundary A-4

---

## Group B: Cross-View and Composition

### Semantic Drift Indicators

**Language Changes**:
- "Continue" or "resume" language appearing in cross-view navigation
- This MAY indicate drift if observed: Boundary B-1

- Progressive disclosure language that implies hiding options
- This MAY indicate drift if observed: Boundary B-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Default prefilled search queries in multi-view flows
- This MAY indicate drift if observed: Boundary B-1

- Default active filter chips in multi-view flows
- This MAY indicate drift if observed: Boundary B-1

- Sticky shortlist seeded by previous session
- This MAY indicate drift if observed: Boundary B-1

- Compare panel auto-populating with pre-selected items
- This MAY indicate drift if observed: Boundary B-1

- Unequal information density per pattern across views
- This MAY indicate drift if observed: Boundary B-1

- Ordering changes across views not explained as non-preferential
- This MAY indicate drift if observed: Boundary B-1

- Curated category subsets instead of complete lists
- This MAY indicate drift if observed: Boundary B-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Cross-session persistence of view state without explicit human action
- This MAY indicate drift if observed: Boundary B-1

- "Continue" CTA auto-navigating to specific pattern
- This MAY indicate drift if observed: Boundary B-1

---

## Group C: Time and Memory

### Semantic Drift Indicators

**Language Changes**:
- Time-based language in selection interfaces (recently used, frequently used, last used)
- This MAY indicate drift if observed: Boundary C-1

- History-based language (based on your past, you previously selected, continue where you left off)
- This MAY indicate drift if observed: Boundary C-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Preselect last used Pattern version as default
- This MAY indicate drift if observed: Boundary C-1

- Auto-highlight "recently used" entries
- This MAY indicate drift if observed: Boundary C-1

- Auto-apply last filters/tags across sessions
- This MAY indicate drift if observed: Boundary C-1

- "Frequently used" ordering replacing lexicographic ordering
- This MAY indicate drift if observed: Boundary C-1

- "Recent activity" panel limited to top N
- This MAY indicate drift if observed: Boundary C-1

- Session persistence of shortlist with sticky ranking
- This MAY indicate drift if observed: Boundary C-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- "Continue" button bypassing selection view
- This MAY indicate drift if observed: Boundary C-1

- "Suggested next" purely based on history
- This MAY indicate drift if observed: Boundary C-1

- Using audit reference count as proxy signal in ordering
- This MAY indicate drift if observed: Boundary C-1

- "Resume where you left off" skipping neutral presentation
- This MAY indicate drift if observed: Boundary C-1

---

## Group D: Execution and Invocation

### Semantic Drift Indicators

**Language Changes**:
- Execution orchestration language (workflow, pipeline, sequence, batch)
- This MAY indicate drift if observed: Boundary D-1

- Automatic execution language (auto-execute, auto-trigger, next step auto-execute)
- This MAY indicate drift if observed: Boundary D-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Selection automatically triggering execution
- This MAY indicate drift if observed: Boundary D-1

- Execution plan pre-generation after selection
- This MAY indicate drift if observed: Boundary D-1

- Multi-capability sequential execution
- This MAY indicate drift if observed: Boundary D-1

- Capability batch execution
- This MAY indicate drift if observed: Boundary D-1

- Implicit capability dependencies
- This MAY indicate drift if observed: Boundary D-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Context-based parameter auto-completion
- This MAY indicate drift if observed: Boundary D-1

- History-based execution optimization
- This MAY indicate drift if observed: Boundary D-1

- "Next step auto-execute" functionality
- This MAY indicate drift if observed: Boundary D-1

---

## Group E: Lifecycle Operations

### Semantic Drift Indicators

**Language Changes**:
- Auto-upgrade language (upgrade to latest, auto-upgrade, latest is best)
- This MAY indicate drift if observed: Boundary E-1

- Recommended mapping language during import
- This MAY indicate drift if observed: Boundary E-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Auto-select target workspace during import
- This MAY indicate drift if observed: Boundary E-1

- Auto-merge conflict resolution with implied "best"
- This MAY indicate drift if observed: Boundary E-1

- "Upgrade to latest" toggle enabled by default
- This MAY indicate drift if observed: Boundary E-1

- Auto-deprecate older versions after import
- This MAY indicate drift if observed: Boundary E-1

- Auto-hiding/filtering deprecated entries
- This MAY indicate drift if observed: Boundary E-1

- Auto-replacement of deprecated patterns
- This MAY indicate drift if observed: Boundary E-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Latest version highlighted in preview
- This MAY indicate drift if observed: Boundary E-1

- Auto-select best version based on usage stats
- This MAY indicate drift if observed: Boundary E-1

---

## Group F: Authority and Isolation

### Semantic Drift Indicators

**Language Changes**:
- Privilege inference language (you used it last time, based on your history)
- This MAY indicate drift if observed: Boundary F-1

- Auto-grant language (automatically granted, based on role)
- This MAY indicate drift if observed: Boundary F-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Infer authorization from audit/history
- This MAY indicate drift if observed: Boundary F-1

- Auto-grant permissions based on role heuristics
- This MAY indicate drift if observed: Boundary F-1

- Preselect workspace or pattern "for convenience"
- This MAY indicate drift if observed: Boundary F-1

- Cross-workspace "recent" panels
- This MAY indicate drift if observed: Boundary F-1

- Cross-workspace carryover of filters/search
- This MAY indicate drift if observed: Boundary F-1

- Shared defaults across workspaces
- This MAY indicate drift if observed: Boundary F-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- "Continue previous session" bypassing gate
- This MAY indicate drift if observed: Boundary F-1

- Audit-derived access control logic
- This MAY indicate drift if observed: Boundary F-1

---

## Group G: System Evolution

### Semantic Drift Indicators

**Language Changes**:
- Implicit primary language (primary capability, main feature)
- This MAY indicate drift if observed: Boundary G-1

- Default pattern language (default pattern, standard pattern)
- This MAY indicate drift if observed: Boundary G-1

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Capability becomes implicitly "primary"
- This MAY indicate drift if observed: Boundary G-1

- Pattern becomes de facto default
- This MAY indicate drift if observed: Boundary G-1

- Combination forms workflow semantics
- This MAY indicate drift if observed: Boundary G-1

- Execution chaining emerges
- This MAY indicate drift if observed: Boundary G-1

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Memory-based optimization across features
- This MAY indicate drift if observed: Boundary G-1

- "Recent", "frequent", or "continue" mechanisms affecting presentation
- This MAY indicate drift if observed: Boundary G-1

- Session carryover affecting presentation
- This MAY indicate drift if observed: Boundary G-1

---

## Group H: Constitutional Enforcement

### Semantic Drift Indicators

**Language Changes**:
- Softening language (mitigation, guardrails, exceptions)
- This MAY indicate drift if observed: Boundary H-1

- Auto-authorization language (auto-approve, inferred intent)
- This MAY indicate drift if observed: Boundary H-1, H-2

### Structural Drift Indicators

**New Coupling, Defaults, Ordering**:
- Modifying CANONICAL documents without authorization
- This MAY indicate drift if observed: Boundary H-1

- Bypassing modification gate
- This MAY indicate drift if observed: Boundary H-1

- Partial or sampling audits
- This MAY indicate drift if observed: Boundary H-1

- Missing authorization tokens in constitutional changes
- This MAY indicate drift if observed: Boundary H-2

- Bypassing pre-commit hooks or CI gates
- This MAY indicate drift if observed: Boundary H-2

### Interaction Drift Indicators

**Cross-View, Time, Memory, Execution**:
- Inferring human intent for constitutional changes
- This MAY indicate drift if observed: Boundary H-1

- Auto-authorization of constitutional changes
- This MAY indicate drift if observed: Boundary H-1, H-2

---

## Summary

**Total Drift Indicator Categories**: 3 per boundary group

**Indicator Types**:
- Semantic Drift Indicators: Language changes
- Structural Drift Indicators: New coupling, defaults, ordering
- Interaction Drift Indicators: Cross-view, time, memory, execution

**All indicators are phrased as "This MAY indicate drift if observed" - they do not assert violation.**

**All indicators are derived from analysis of validated FAIL cases.**

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

**For regression baseline, see BOUNDARY_REGRESSION_BASELINE.md.**

---

**END OF BOUNDARY DRIFT INDICATORS**

**This document is GOVERNANCE SUPPORT.**
**It provides drift detection reference only.**
**It does not assert violations or trigger STOP conditions.**

