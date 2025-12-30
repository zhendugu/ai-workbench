# Design-Time Frontend Change Boundary 001

**Status**: FROZEN

**Date**: 2025-12-28

**Authority**: DT_FE_DECISION_RECORD_001.md (HIGHEST) + DT_FE_REQ_FROZEN.md

---

## Frozen Boundary Statement

**Design-Time semantics are frozen at DT-FE-FROZEN-1.**

This document establishes the change boundary for all future work on the Design-Time frontend. Any work that crosses this boundary requires explicit authorization through Decision Record process.

---

## Allowed Future Work Categories

### 1. Run-Time Read-Only Frontend (Separate Specification)

**Scope**: A separate frontend interface for viewing frozen Company structures.

**Allowed**:
- Read-only display of frozen structures
- Navigation of frozen topology
- Viewing frozen Cell details
- Backtracking design decisions
- Referencing Company identifiers

**Constraints**:
- Must be read-only (no editing)
- Must be separate from Design-Time interface
- Requires separate specification document
- No new semantics beyond "view frozen structure"

**Status**: NOT YET SPECIFIED

---

### 2. Backend API Wiring/Persistence for Design-Time (No New Fields/Semantics)

**Scope**: Connecting the Design-Time frontend to backend APIs for data persistence.

**Allowed**:
- API integration for save/load Company Drafts
- API integration for Cell CRUD operations
- API integration for Relation CRUD operations
- API integration for Methodology persistence
- API integration for Template retrieval
- API integration for Freeze operation

**Constraints**:
- **MUST use existing data model** (no new fields)
- **MUST use existing semantics** (no new states)
- **MUST comply with DT_FE_REQ_FROZEN.md** data format assumptions
- No new entity types
- No new relationship types
- No new validation logic beyond what exists in frontend

**Example Allowed**:
- `POST /api/design-time/companies` - Create Draft (using existing Company type)
- `GET /api/design-time/companies/:id` - Load Draft (using existing Company type)

**Example Disallowed**:
- Adding "designStage" field to Company (violates DR-03)
- Adding "templateScore" to Template (violates DR-01)
- Adding "maturity" field to Draft ID (violates DR-02)

---

### 3. Visual Polish (Non-Semantic Improvements)

**Scope**: UI/UX improvements that do not introduce new meaning.

**Allowed**:
- Spacing adjustments
- Typography improvements
- Layout refinements
- Color scheme adjustments (within existing constraints)
- Accessibility improvements (ARIA labels, keyboard navigation)
- Performance optimizations
- Responsive design improvements

**Constraints**:
- **MUST NOT introduce new semantic meaning**
- **MUST NOT change existing labels or messaging**
- **MUST NOT add new UI elements that imply new capabilities**
- **MUST NOT change interaction patterns in ways that suggest new semantics**

**Example Allowed**:
- Improving button spacing
- Adding hover states
- Improving color contrast for accessibility
- Optimizing render performance

**Example Disallowed**:
- Adding a "progress bar" (implies execution/progress semantics)
- Adding a "recommendation badge" (implies recommendation semantics)
- Changing "Draft" label to "In Progress" (implies progress semantics)

---

## Disallowed Work Categories

The following work is **explicitly disallowed** without a new Decision Record:

### ❌ Any New Entity Semantics
- New entity types (beyond Company, Cell, Role, Relation, Methodology, Template)
- New relationship types (beyond dependency, reference, input-output)
- New state types (beyond Draft, Frozen)

### ❌ Any "Stage" Concept
- Design Stage field (DR-03)
- Early/Mid/Late design
- Stage 1/2/3 indicators
- Preparation/Review/Ready states

### ❌ Any Recommendation System
- Template recommendations
- Methodology recommendations
- Structure suggestions
- "Best practices" hints

### ❌ Any Automation/AI
- AI calls
- Auto-generation
- Smart suggestions
- Intelligent completion

### ❌ Any Progress/Health Indicators
- Progress bars
- Maturity scores
- Health indicators
- KPI dashboards
- Completion percentages

### ❌ Any Execution Semantics
- Run/Execute/Start buttons
- Workflow execution
- Process simulation
- Step-by-step execution

---

## How to Request Changes

### For Semantic Changes

**Step 1: Create Decision Record**
- File: `DT-FE-DECISION-RECORD-XXX.md`
- Document the decision, rationale, and explicit rules
- Mark as FROZEN after human approval

**Step 2: Create New Specification Version**
- File: `DT_FE_REQ_FROZEN_2.md` (or next version)
- Include full content from previous version
- Add new requirements based on Decision Record
- Mark as FROZEN

**Step 3: Update Implementation**
- Implement changes according to new specification
- Update acceptance record if needed

**Step 4: Update Change Boundary**
- Update this document to reflect new allowed/disallowed categories
- Create new version if boundary changes significantly

### For Non-Semantic Changes

**Step 1: Verify Non-Semantic**
- Confirm change does not introduce new meaning
- Confirm change does not violate frozen semantics
- Document rationale

**Step 2: Implement**
- Proceed with implementation
- Ensure compliance with existing frozen documents

**Step 3: Document (Optional)**
- Update implementation notes if significant
- No Decision Record required

---

## Enforcement

### Code Review Checklist

Before merging any change to Design-Time frontend, verify:

- [ ] Does this change introduce new entity types? (If yes, requires Decision Record)
- [ ] Does this change introduce new states? (If yes, requires Decision Record)
- [ ] Does this change introduce recommendation/scoring? (If yes, BLOCKED)
- [ ] Does this change introduce execution semantics? (If yes, BLOCKED)
- [ ] Does this change introduce progress/maturity indicators? (If yes, BLOCKED)
- [ ] Does this change comply with DR-01, DR-02, DR-03? (If no, BLOCKED)
- [ ] Does this change use existing data model? (If no, requires Decision Record)

### Blocking Criteria

**BLOCK immediately if**:
- Introduces "Design Stage" concept
- Adds template recommendation/scoring
- Adds Draft ID maturity encoding
- Adds execution/run/trigger controls
- Adds AI assistance
- Adds progress indicators

**REQUIRE Decision Record if**:
- Introduces new entity types
- Introduces new relationship types
- Introduces new states
- Changes core semantics

---

## Examples

### ✅ Allowed: API Integration
```typescript
// Allowed: API call using existing Company type
async function saveCompany(company: Company): Promise<void> {
  await fetch('/api/design-time/companies', {
    method: 'POST',
    body: JSON.stringify(company), // Uses existing Company type
  })
}
```

### ❌ Disallowed: Adding New Field
```typescript
// Disallowed: Adding "designStage" violates DR-03
interface Company {
  id: string
  name: string
  designStage: 'early' | 'mid' | 'late' // ❌ BLOCKED
}
```

### ✅ Allowed: Visual Polish
```css
/* Allowed: Spacing improvement, no semantic change */
.cell-card {
  padding: 1.5rem; /* Was 1rem, improved spacing */
}
```

### ❌ Disallowed: Adding Progress Indicator
```tsx
// Disallowed: Progress bar implies execution/progress semantics
<ProgressBar value={completionPercentage} /> // ❌ BLOCKED
```

---

## Version History

- **DT_FE_CHANGE_BOUNDARY_001.md** (2025-12-28): Initial freeze boundary

---

**END OF CHANGE BOUNDARY DOCUMENT**

