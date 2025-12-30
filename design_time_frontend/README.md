# Design-Time Frontend

**Status**: MVP Implementation

**Authority**:
- DT-FE-DECISION-RECORD-001.md (HIGHEST - FROZEN)
- DT_FE_REQ_DRAFT.md (DRAFT - 描述性规范)

**Scope**: Design-Time Frontend Only

---

## Project Structure

```
design_time_frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # React components
│   │   ├── company/     # Company Context (L1)
│   │   ├── cell/        # Cell Management (L2)
│   │   ├── topology/    # Topology Canvas (L3)
│   │   ├── methodology/ # Methodology Selector (L4)
│   │   ├── template/    # Template Library (L5)
│   │   └── freeze/      # Freeze Confirmation (L6)
│   ├── hooks/           # React hooks
│   ├── utils/           # Utility functions
│   ├── types/           # TypeScript types
│   └── App.tsx          # Main application
├── package.json
└── README.md
```

---

## Implementation Notes

- **No Design Stage**: Only Draft / Frozen states allowed (DR-03)
- **Template as Copy Source Only**: No recommendations, scoring, or matching (DR-01)
- **Draft ID as Technical Identifier**: No progress or maturity encoding (DR-02)
- **No Execution Semantics**: All operations are structural declarations only
- **No AI Assistance**: No AI calls, recommendations, or auto-generation

---

## Running the Application

```bash
npm install
npm run dev
```

---

## Compliance Checklist

See DT_FE_REQ_DRAFT.md Section 9 for complete checklist.

