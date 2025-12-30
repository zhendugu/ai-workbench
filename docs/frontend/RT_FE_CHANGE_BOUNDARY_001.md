# Run-Time Frontend Change Boundary 001

**Status**: FROZEN

**Date**: 2025-12-28

**Authority**: DT_FE_DECISION_RECORD_001.md (HIGHEST) + RT_FE_REQ_FROZEN.md

---

## Frozen Boundary Statement

**Run-Time semantics are frozen at RT-FE-FROZEN-1.**

This document establishes the change boundary for all future work on the Run-Time frontend. Any work that crosses this boundary requires explicit authorization through Decision Record process.

---

## Allowed Future Work Categories

### 1. Visual Polish (Non-Semantic Improvements)

**Scope**: UI/UX improvements that do not introduce new meaning.

**Allowed**:
- Spacing adjustments
- Typography improvements
- Layout refinements (within existing constraints)
- Color scheme adjustments (within existing constraints: neutral colors, no green/red/yellow)
- Accessibility improvements (ARIA labels, keyboard navigation)
- Performance optimizations
- Responsive design improvements
- Information presentation refinements (read-only display)

**Constraints**:
- **MUST NOT introduce new semantic meaning**
- **MUST NOT change existing labels or messaging**
- **MUST NOT add new UI elements that imply new capabilities**
- **MUST NOT change interaction patterns in ways that suggest new semantics**
- **MUST NOT introduce any execution/monitor/recommendation/evaluation semantics**

**Example Allowed**:
- Improving text spacing for readability
- Adding hover states (for navigation only)
- Improving color contrast for accessibility
- Optimizing render performance
- Refining information hierarchy presentation

**Example Disallowed**:
- Adding a "progress bar" (implies execution/progress semantics)
- Adding a "recommendation badge" (implies recommendation semantics)
- Changing "Frozen at" to "Last updated" (violates time stamp semantics)
- Adding green/red status indicators (violates color principles)

---

### 2. Read-Only Information Presentation Enhancements

**Scope**: Improvements to how frozen information is displayed, without introducing new capabilities.

**Allowed**:
- Enhanced information layout for better readability
- Improved navigation structure (within existing constraints)
- Better depth linking presentation
- Export button implementation (if already specified in RT_FE_REQ_FROZEN.md)
- Information filtering/sorting (display control only, no recommendation)

**Constraints**:
- **MUST remain read-only**
- **MUST NOT imply any activity or execution**
- **MUST NOT introduce recommendation or evaluation**
- **MUST comply with all forbidden semantics in Section 7**

**Example Allowed**:
- Improving Cell list presentation for better scanning
- Adding collapsible sections for Role constraints
- Enhancing topology canvas visualization (no execution semantics)
- Improving freeze record presentation

**Example Disallowed**:
- Adding "recommended reading order" (violates PATH semantics)
- Adding "completeness score" (violates evaluation semantics)
- Adding "last viewed" indicators (violates activity semantics)

---

### 3. Backend API Integration (No New Fields/Semantics)

**Scope**: Connecting the Run-Time frontend to backend APIs for data loading.

**Allowed**:
- API integration for loading frozen Company structures
- API integration for loading Cell details
- API integration for loading Topology relations
- API integration for loading Methodology context
- API integration for loading Freeze Records

**Constraints**:
- **MUST use existing data model** (no new fields)
- **MUST use existing semantics** (no new states)
- **MUST comply with RT_FE_REQ_FROZEN.md** data format assumptions
- **MUST be read-only** (no write operations)
- **MUST be one-time load** (no polling or real-time updates)
- No new entity types
- No new relationship types
- No new validation logic beyond what exists in specification

**Example Allowed**:
- `GET /api/run-time/companies/:frozenId` - Load frozen Company (using existing Company type)
- `GET /api/run-time/companies/:frozenId/cells` - Load Cells (using existing Cell type)

**Example Disallowed**:
- Adding "lastUpdated" field to Company (violates time stamp semantics)
- Adding "healthScore" field to Company (violates evaluation semantics)
- Adding polling for updates (violates read-only and activity semantics)

---

## Disallowed Work Categories

The following work is **explicitly disallowed** without a new Decision Record:

### ❌ Any New Entity Semantics
- New entity types (beyond Company, Cell, Role, Relation, Methodology, Freeze Record)
- New relationship types (beyond dependency, reference, input-output)
- New state types (beyond Frozen)

### ❌ Any Execution Semantics
- Run/Execute/Start buttons
- Workflow execution
- Process simulation
- Step-by-step execution
- Progress indicators
- Activity logs

### ❌ Any Monitor/Dashboard Semantics
- Dashboards
- KPI cards
- Metric charts
- Real-time data visualization
- Health indicators
- Status badges (green/yellow/red)
- Alert notifications

### ❌ Any Recommendation System
- Template recommendations
- Methodology recommendations
- Structure suggestions
- "Best practices" hints
- AI assistance
- Smart suggestions

### ❌ Any Evaluation/Scoring System
- Quality scores
- Maturity indicators
- Completeness percentages
- Risk levels
- Priority labels

### ❌ Any Activity Semantics
- Auto-refresh buttons
- Real-time update indicators
- Activity logs
- "Last updated" timestamps (auto-updating)
- Online/offline status
- Connection status indicators

### ❌ Any Process/Workflow Semantics
- "Next step" buttons
- "Continue" buttons
- "Complete" buttons
- Step indicators
- Process progress bars
- Workflow visualizations

### ❌ Any Editable Capabilities
- Edit buttons
- Modify links
- Delete operations
- State switching controls
- Any write operations

---

## How to Request Changes

### For Semantic Changes

**Step 1: Create Decision Record**
- File: `DT-FE-DECISION-RECORD-XXX.md` (or new RT-specific Decision Record)
- Document the decision, rationale, and explicit rules
- Mark as FROZEN after human approval

**Step 2: Create New Specification Version**
- File: `RT_FE_REQ_FROZEN_2.md` (or next version)
- Include full content from previous version
- Add new requirements based on Decision Record
- Mark as FROZEN

**Step 3: Re-execute Cognitive Illusion Audit**
- Perform cognitive illusion audit on new specification
- Verify no new illusion risks introduced
- Document audit results

**Step 4: Update Implementation**
- Implement changes according to new specification
- Update acceptance record if needed

**Step 5: Update Change Boundary**
- Update this document to reflect new allowed/disallowed categories
- Create new version if boundary changes significantly

### For Non-Semantic Changes

**Step 1: Verify Non-Semantic**
- Confirm change does not introduce new meaning
- Confirm change does not violate frozen semantics
- Confirm change does not introduce any forbidden semantics
- Document rationale

**Step 2: Implement**
- Proceed with implementation
- Ensure compliance with existing frozen documents
- Verify against Section 7 (Forbidden Semantics)

**Step 3: Document (Optional)**
- Update implementation notes if significant
- No Decision Record required

---

## Enforcement

### Code Review Checklist

Before merging any change to Run-Time frontend, verify:

- [ ] Does this change introduce new entity types? (If yes, requires Decision Record)
- [ ] Does this change introduce new states? (If yes, requires Decision Record)
- [ ] Does this change introduce execution semantics? (If yes, BLOCKED)
- [ ] Does this change introduce monitor/dashboard semantics? (If yes, BLOCKED)
- [ ] Does this change introduce recommendation/scoring? (If yes, BLOCKED)
- [ ] Does this change introduce activity semantics? (If yes, BLOCKED)
- [ ] Does this change introduce process/workflow semantics? (If yes, BLOCKED)
- [ ] Does this change introduce editable capabilities? (If yes, BLOCKED)
- [ ] Does this change comply with RT_FE_REQ_FROZEN.md? (If no, BLOCKED)
- [ ] Does this change use existing data model? (If no, requires Decision Record)
- [ ] Does this change maintain "静止/权威/可审计" feeling? (If no, BLOCKED)

### Blocking Criteria

**BLOCK immediately if**:
- Introduces execution/run/trigger controls
- Adds monitor/dashboard elements
- Adds recommendation/scoring systems
- Adds activity indicators
- Adds process/workflow semantics
- Adds editable capabilities
- Changes "Frozen at" to "Last updated"
- Introduces green/red/yellow status indicators
- Adds AI assistance or smart suggestions

**REQUIRE Decision Record if**:
- Introduces new entity types
- Introduces new relationship types
- Introduces new states
- Changes core semantics
- Changes time stamp semantics
- Changes navigation semantics

---

## Examples

### ✅ Allowed: Visual Polish
```css
/* Allowed: Spacing improvement, no semantic change */
.frozen-company-header {
  padding: 1.5rem; /* Was 1rem, improved spacing */
  font-size: 1.1rem; /* Improved readability */
}
```

### ❌ Disallowed: Adding Progress Indicator
```tsx
// Disallowed: Progress bar implies execution/progress semantics
<ProgressBar value={completionPercentage} /> // ❌ BLOCKED
```

### ✅ Allowed: API Integration
```typescript
// Allowed: API call using existing Company type
async function loadFrozenCompany(frozenId: string): Promise<Company> {
  const response = await fetch(`/api/run-time/companies/${frozenId}`)
  return response.json() // Uses existing Company type
}
```

### ❌ Disallowed: Adding New Field
```typescript
// Disallowed: Adding "lastUpdated" violates time stamp semantics
interface Company {
  id: string
  name: string
  lastUpdated: Date // ❌ BLOCKED - violates Section 3.6
}
```

### ✅ Allowed: Information Presentation Enhancement
```tsx
// Allowed: Better information layout, no semantic change
<div className="freeze-record">
  <h3>Freeze Record</h3>
  <p>Frozen at: {freezeRecord.timestamp}</p>
  <p>Frozen by: {freezeRecord.actor}</p>
</div>
```

### ❌ Disallowed: Adding Recommendation
```tsx
// Disallowed: Recommendation implies recommendation semantics
<RecommendationBadge text="Recommended reading order" /> // ❌ BLOCKED
```

---

## Version History

- **RT_FE_CHANGE_BOUNDARY_001.md** (2025-12-28): Initial freeze boundary

---

**END OF CHANGE BOUNDARY DOCUMENT**

