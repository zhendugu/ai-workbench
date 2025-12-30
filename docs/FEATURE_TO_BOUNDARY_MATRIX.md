# Feature to Boundary Matrix

**Document Status**: **GOVERNANCE SUPPORT**  
**Document Type**: Feature-to-Boundary Mapping Aid  
**Effective Date**: 2025-12-27  
**Purpose**: Help humans quickly map feature ideas to risk surfaces

---

## Purpose

This document helps humans quickly map feature ideas to constitutional boundary risk surfaces.

**This document is:**
- A human-facing design aid
- Derived exclusively from CONSTITUTIONAL_BOUNDARY_ATLAS.md
- Synthesis only - introduces no new rules, constraints, or enforcement

**This document is NOT:**
- An automated mapping tool
- A source of new constraints
- An enforcement mechanism
- A decision automation system

**For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md.**

---

## Feature Categories

### UI / Presentation Features

**Feature Examples**:
- Pattern registry UI
- Capability selection UI
- List views, card views, detail views
- Dashboard displays
- Option menus

**Potential Boundary Groups Involved**:
- Group A (Presentation and Information Neutrality): A-1, A-2, A-3
- Group B (Cross-View and Composition): B-1

**Notes**:
- Presentation features often touch multiple Group A boundaries
- Multi-view features may also involve Group B
- High-density displays may involve Boundary A-3

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Group A, Group B

---

### Search / Filter / Sort / Pagination Features

**Feature Examples**:
- Search interfaces
- Filter panels
- Sort controls
- Pagination components
- Result list views

**Potential Boundary Groups Involved**:
- Group A (Presentation and Information Neutrality): A-4

**Notes**:
- Search/filter/sort/pagination features specifically involve Boundary A-4
- These features may also touch Group C if they use history/audit data

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary A-4

---

### Execution / Invocation Features

**Feature Examples**:
- Execution interfaces
- Parameter forms
- Execution triggers
- Batch operations
- Workflow builders

**Potential Boundary Groups Involved**:
- Group D (Execution and Invocation): D-1

**Notes**:
- Execution features specifically involve Boundary D-1
- Boundary D-1 requires strict separation between Selection and Execution

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary D-1

---

### Memory / History / Time Features

**Feature Examples**:
- History views
- Recent activity panels
- Session management
- Audit displays
- Time-based ordering

**Potential Boundary Groups Involved**:
- Group C (Time and Memory): C-1
- Group A (Presentation and Information Neutrality): A-4 (if used in search/filter/sort)

**Notes**:
- Memory/history features specifically involve Boundary C-1
- Boundary C-1 prohibits using history/audit to influence behavior or selection

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary C-1

---

### Import / Export / Migration Features

**Feature Examples**:
- Import/export interfaces
- Migration wizards
- Conflict resolution dialogs
- Version management
- Deprecation workflows

**Potential Boundary Groups Involved**:
- Group E (Lifecycle Operations): E-1

**Notes**:
- Import/export/migration features specifically involve Boundary E-1
- Boundary E-1 prohibits introducing recommendation signals or default selections

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary E-1

---

### Authorization / Role / Workspace Features

**Feature Examples**:
- Authorization interfaces
- Role management
- Workspace isolation
- Permission workflows
- Cross-workspace navigation

**Potential Boundary Groups Involved**:
- Group F (Authority and Isolation): F-1

**Notes**:
- Authorization/role/workspace features specifically involve Boundary F-1
- Boundary F-1 prohibits inferring permissions or creating cross-workspace influence

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary F-1

---

### Multi-Feature / Evolution Features

**Feature Examples**:
- Multi-feature systems
- Feature combinations
- Feature ecosystems
- Feature interactions

**Potential Boundary Groups Involved**:
- Group G (System Evolution): G-1
- May also involve other groups depending on specific features

**Notes**:
- Multi-feature evolution specifically involves Boundary G-1
- Individual features may also touch their respective boundary groups

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary G-1

---

### Cross-View / Multi-Step Features

**Feature Examples**:
- Multi-view workflows
- Wizard-style interfaces
- Compare panels
- Shortlist features
- Cross-view navigation

**Potential Boundary Groups Involved**:
- Group B (Cross-View and Composition): B-1
- May also involve Group A if presentation is involved

**Notes**:
- Cross-view features specifically involve Boundary B-1
- Boundary B-1 requires that neutral-by-components flows remain neutral when combined

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Boundary B-1

---

### Constitutional / Governance Features

**Feature Examples**:
- Constitutional document modifications
- Governance policy changes
- Enforcement mechanism updates
- Evidence pack structure changes

**Potential Boundary Groups Involved**:
- Group H (Constitutional Enforcement): H-1, H-2

**Notes**:
- Constitutional/governance features specifically involve Group H boundaries
- These are enforcement mechanisms, not feature boundaries

**Reference**: CONSTITUTIONAL_BOUNDARY_ATLAS.md - Group H

---

## Matrix Summary

| Feature Category | Primary Boundary Group | Specific Boundaries |
|-----------------|------------------------|---------------------|
| UI / Presentation | Group A | A-1, A-2, A-3 |
| Search / Filter / Sort / Pagination | Group A | A-4 |
| Execution / Invocation | Group D | D-1 |
| Memory / History / Time | Group C | C-1 |
| Import / Export / Migration | Group E | E-1 |
| Authorization / Role / Workspace | Group F | F-1 |
| Multi-Feature / Evolution | Group G | G-1 |
| Cross-View / Multi-Step | Group B | B-1 |
| Constitutional / Governance | Group H | H-1, H-2 |

**Notes**:
- Feature categories may involve multiple boundary groups
- This matrix is descriptive only - it does not automate mapping
- For complete boundary definitions, see CONSTITUTIONAL_BOUNDARY_ATLAS.md

---

**END OF FEATURE TO BOUNDARY MATRIX**

**This document is GOVERNANCE SUPPORT.**
**It provides feature-to-boundary mapping guidance only.**
**It is not a source of new constraints.**

