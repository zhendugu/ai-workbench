# V0 Wireframe Request Specification

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: V0 Input Specification  
**Date**: 2025-12-27  
**Work Order**: WO-J4-CONTROLLED-FRONTEND-EXPANSION-DESIGN-AND-AUDIT-HARNESS

---

## Purpose

This document defines the specification for requesting wireframes/layouts from V0.

V0 output is LIMITED to wireframe/structure only.

V0 output MUST NOT include behavior logic.

---

## V0 Output Limitations

### What V0 MAY Output

**V0 MAY output**:
- Wireframe structure
- Layout arrangement
- Component placement
- Visual hierarchy (structural only, not preference-based)
- Information architecture (factual organization only)

**V0 output is**: Static structure, no behavior.

---

### What V0 MUST NOT Output

**V0 MUST NOT output**:
- Behavior logic
- Interaction patterns
- State management
- Default selections
- Highlighting mechanisms
- Ordering algorithms
- Recommendation logic
- Process guidance
- Workflow templates
- Auto-completion
- Search ranking
- State persistence
- Any mechanism from denylist

**V0 output MUST NOT include**: Any behavior that implies agency.

---

## V0 Request Template

```
V0 WIREFRAME REQUEST

OUTPUT TYPE DECLARATION:
- V0 MUST output wireframe/structure ONLY
- V0 MUST NOT output behavior logic
- V0 MUST NOT output interaction patterns
- V0 MUST NOT output state management
- V0 output is static structure, no behavior

CONSTITUTIONAL CONSTRAINTS (MANDATORY):

1. Frontend MUST NOT have agency.
   - Frontend does not make judgments
   - Frontend does not form preferences
   - Frontend does not hold state
   - Frontend does not predict
   - Frontend does not recommend

2. Frontend performs ONLY presentation and operation mapping.
   - Frontend displays capabilities
   - Frontend displays pattern instances
   - Frontend maps human actions to system operations
   - Frontend does NOT select, recommend, default, optimize, learn, or predict

3. Process-driven UI is FORBIDDEN.
   - No wizard flows
   - No step-by-step guidance
   - No workflow templates
   - No process sequences
   - No "next step" suggestions

4. Optimization is FORBIDDEN.
   - No usage-based optimization
   - No frequency-based ordering
   - No popularity-based highlighting
   - No history-based defaults
   - No behavior-based adaptation

EXPLICIT PROHIBITIONS FOR V0 OUTPUT:

- MUST NOT include default selections
- MUST NOT include highlighting mechanisms
- MUST NOT include ordering algorithms
- MUST NOT include recommendation logic
- MUST NOT include process guidance
- MUST NOT include workflow templates
- MUST NOT include auto-completion
- MUST NOT include search ranking
- MUST NOT include state persistence
- MUST NOT include any mechanism from FRONTEND_EXPANSION_DENYLIST.md

REQUIRED WIREFRAME CHARACTERISTICS:

- All capabilities displayed equally (no emphasis)
- All pattern instances displayed equally (no emphasis)
- Registration order maintained (no reordering)
- No visual hierarchy that implies preference
- No structural organization that implies recommendation
- All options accessible equally
- No default states
- No highlighted elements
- No badges, icons, or markers
- No "featured" or "popular" sections

ALLOWLIST COMPLIANCE:

Wireframe MUST only include mechanisms from FRONTEND_EXPANSION_ALLOWLIST.md:
- Basic Partitioned Views (if applicable)
- Literal Search (if applicable)
- Pagination / Virtual Scrolling (if applicable)
- Collapse / Expand (if applicable)
- Parameter Form Field Validation (if applicable)

All allowlist mechanisms MUST comply with minimum implementation boundaries.

DENYLIST EXCLUSION:

Wireframe MUST NOT include any mechanism from FRONTEND_EXPANSION_DENYLIST.md.

WIREFRAME REQUEST:

[Insert specific wireframe request here]

CURSOR IMPLEMENTATION NOTE:

Wireframe output will be implemented by Cursor following:
- CURSOR_FRONTEND_IMPLEMENTATION_RULES.md
- FRONTEND_GENERATION_CONSTRAINT_SPEC.md
- FRONTEND_EXPANSION_ALLOWLIST.md
- FRONTEND_EXPANSION_DENYLIST.md

Cursor will NOT copy any implicit logic from wireframe.
Cursor will implement only explicit structure.
```

---

## Usage Instructions

1. Copy the entire template above
2. Fill in the "WIREFRAME REQUEST" section with specific requirements
3. Include the template in ALL V0 wireframe requests
4. Do NOT modify the CONSTITUTIONAL CONSTRAINTS section
5. Do NOT modify the EXPLICIT PROHIBITIONS section
6. Do NOT modify the REQUIRED WIREFRAME CHARACTERISTICS section

---

## V0 Output Validation

### Validation Checklist

Before accepting V0 wireframe output:

- [ ] Wireframe contains structure only (no behavior logic)
- [ ] No default selections indicated
- [ ] No highlighting mechanisms indicated
- [ ] No ordering algorithms indicated
- [ ] No recommendation logic indicated
- [ ] No process guidance indicated
- [ ] No workflow templates indicated
- [ ] No auto-completion indicated
- [ ] No search ranking indicated
- [ ] No state persistence indicated
- [ ] All capabilities displayed equally
- [ ] Registration order maintained
- [ ] No visual hierarchy that implies preference
- [ ] Only allowlist mechanisms included (if any)
- [ ] No denylist mechanisms included

---

## Cursor Implementation Rules

**After V0 wireframe is received**:

Cursor MUST implement wireframe following:
- CURSOR_FRONTEND_IMPLEMENTATION_RULES.md
- FRONTEND_GENERATION_CONSTRAINT_SPEC.md
- FRONTEND_EXPANSION_ALLOWLIST.md
- FRONTEND_EXPANSION_DENYLIST.md

**Cursor MUST NOT**:
- Copy implicit logic from wireframe
- Implement behavior not explicitly defined in rules
- Add mechanisms not in allowlist
- Add mechanisms in denylist

**Cursor MUST**:
- Implement only explicit structure
- Follow all J2 constraints
- Follow all allowlist boundaries
- Exclude all denylist mechanisms

---

## Summary

**V0 Output**: Wireframe/structure only, no behavior logic

**V0 Limitations**: No agency mechanisms, no behavior patterns, no state management

**Cursor Implementation**: Follows rules, does not copy implicit logic

**Validation**: Wireframe validated against constraints before acceptance

---

**END OF V0 WIREFRAME REQUEST SPECIFICATION**

