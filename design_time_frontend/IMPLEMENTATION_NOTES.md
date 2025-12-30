# Design-Time Frontend Implementation Notes

**Status**: MVP Implementation

**Authority**:
- `docs/frontend/DT_FE_DECISION_RECORD_001.md` (FROZEN - Highest Authority)
- `docs/frontend/DT_FE_REQ_DRAFT.md` (DRAFT - Descriptive Specification)

---

## Implementation Compliance

### DR-01: Template Semantic Boundary ✅
- Templates are structural copy sources only
- No recommendations, scoring, or matching implemented
- "Use Template" creates new independent Draft

### DR-02: Draft ID Semantic Boundary ✅
- Draft ID is technical identifier only (COMP-{UUID}, CELL-{UUID})
- No progress, maturity, or stage encoding
- No UI language implying advancement

### DR-03: Design Stage Concept ✅
- Only Draft / Frozen states implemented
- No intermediate states, phases, or stages
- No "Design Stage" field in Company

---

## Core Features Implemented

### L1: Company Context ✅
- Company name and description editing
- Company ID (auto-generated, technical only)
- Status display (Draft / Frozen)
- Freeze button (when Draft)

### L2: Structure Layer ✅
- Cell creation, editing, deletion
- Responsibility What / What NOT fields (required)
- Role constraints (attached to Cell)
- Role creation, editing, deletion

### L3: Topology Layer ✅
- Relation list view (方式 B)
- Relation creation (source, target, type, description)
- Relation deletion
- Canvas placeholder (方式 A not yet implemented)

### L4: Methodology View ✅
- Built-in methodology selection (None, Waterfall, Agile, Hybrid)
- Custom methodology description
- Perspective-only semantics enforced

### L5: Template Library ✅
- Template browsing
- Template use (creates new Draft)
- No recommendations or scoring

### L6: Freeze Confirmation ✅
- Summary information display
- Fact statements (not errors)
- Secondary confirmation (name input + checkbox)
- State transition to Frozen

---

## Prohibited Elements (Not Implemented)

- ❌ Design Stage field
- ❌ Progress indicators
- ❌ Maturity scores
- ❌ Recommendations
- ❌ AI assistance
- ❌ Execution semantics
- ❌ Run/Start/Execute buttons
- ❌ Current step indicators
- ❌ Template scoring or matching

---

## Technical Stack

- React 18
- TypeScript
- Vite
- No UI framework (vanilla CSS for strict control)

---

## Next Steps

1. Implement Topology Canvas (方式 A) - graph visualization
2. Backend API integration (currently using local state)
3. Data persistence
4. Run-Time read-only view enhancement

---

## Compliance Checklist Status

See `docs/frontend/DT_FE_REQ_DRAFT.md` Section 9 for complete checklist.

**Current Status**: MVP covers core functionality, pending full checklist verification.

