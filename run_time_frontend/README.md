# Run-Time Frontend

**Authority**: RT_FE_REQ_FROZEN.md

**Status**: Implementation in progress

**Mode**: RUN-TIME (FROZEN) ONLY - Read-only viewing interface

---

## Purpose

This frontend provides a strictly read-only interface for viewing frozen AI Virtual Company structures.

**Core Design Premise**:
- Run-Time is NOT "the system running"
- Run-Time is "a frozen structure being read by humans"

**Interface Feel**:
- Like reading a legal entity registry
- Like inspecting a frozen architecture blueprint
- Like auditing a declared structure

**NOT**:
- Dashboard
- Control panel
- Monitoring tool
- Workflow engine

---

## Technology Stack

- React 18.2.0
- TypeScript 5.2.2
- Vite 5.0.8
- React Router DOM 6.20.0

---

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## Implementation Status

### ✅ PHASE 1: Structural Scaffold
- [x] Run-Time frontend entry point
- [x] Global frozen banner with explicit non-running disclaimer
- [x] Application mode explicitly set to RUN-TIME (read-only)

### ✅ PHASE 2: View Implementation
- [x] Company Identity View
- [x] Structure View (Cells and Roles)
- [x] Topology View (static graph, no drag, no edit)
- [x] Methodology Context View
- [x] Freeze Record View

### ✅ PHASE 3: Navigation
- [x] View-based navigation
- [x] No default order
- [x] No highlighted "primary" path
- [x] No "next" or "previous" semantics

### ✅ PHASE 4: Visual Guardbands
- [x] Prominent frozen indicators
- [x] Clear separation from Design-Time look and feel
- [x] No dashboard metaphors
- [x] No control-panel metaphors

### ⏳ PHASE 5: Self-Audit
- [ ] Zero editable affordances verification
- [ ] Zero executable affordances verification
- [ ] Zero ambiguous verbs verification
- [ ] Zero implied activity verification
- [ ] All constraints in RT_FE_CHANGE_BOUNDARY_001.md satisfied

---

## Key Constraints

### Strictly Forbidden
- Any editable field
- Any state mutation
- Any live data indicator
- Any refresh, polling, auto-update, or "current" language
- Any progress indicator, status badge, or activity signal
- Any recommendation, score, ranking, or evaluation
- Any workflow, step, wizard, or guided sequence
- Any button whose verb implies action beyond reading

### Required Language
- Use: read, inspect, examine, audit
- Do NOT use: run, execute, start, stop, monitor, update, latest
- Timestamps MUST be labeled exactly as: "Frozen at"
- Navigation is view switching only, not task flow
- All data is treated as a frozen snapshot

---

## File Structure

```
run_time_frontend/
├── src/
│   ├── components/
│   │   ├── company/
│   │   │   └── CompanyIdentityView.tsx
│   │   ├── cell/
│   │   │   └── StructureView.tsx
│   │   ├── topology/
│   │   │   └── TopologyView.tsx
│   │   ├── methodology/
│   │   │   └── MethodologyContextView.tsx
│   │   └── freeze/
│   │       └── FreezeRecordView.tsx
│   ├── types/
│   │   └── index.ts
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

---

## References

- RT_FE_REQ_FROZEN.md - Frozen specification
- RT_FE_IMPLEMENTATION_ACCEPTANCE_001.md - Acceptance criteria
- RT_FE_CHANGE_BOUNDARY_001.md - Change boundary
- RT_FE_COGNITIVE_AUDIT_002.md - Cognitive illusion audit

---

**END OF README**

