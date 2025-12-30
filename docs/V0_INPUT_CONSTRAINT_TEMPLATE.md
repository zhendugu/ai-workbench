# V0 Input Constraint Template

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Standardized Input Template  
**Date**: 2025-12-27  
**Work Order**: WO-J2-FRONTEND-CONSTRAINT-TRANSLATION-AND-GENERATION-GATE

---

## Purpose

This document provides a standardized template for submitting frontend generation requests to V0.

This template must be copied and used for ALL frontend generation requests.

---

## Template (Copy and Use)

```
FRONTEND GENERATION REQUEST

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

EXPLICIT PROHIBITIONS:

- MUST NOT pre-select any option
- MUST NOT highlight any option
- MUST NOT order by usage, frequency, popularity, or recency
- MUST NOT provide defaults
- MUST NOT remember previous selections
- MUST NOT track usage
- MUST NOT display "commonly used" or "recently used"
- MUST NOT create templates or shortcuts
- MUST NOT auto-complete with suggestions
- MUST NOT rank search results
- MUST NOT organize by categories with defaults
- MUST NOT organize by tabs with defaults
- MUST NOT create filter presets
- MUST NOT persist state across sessions
- MUST NOT provide contextual help with suggestions
- MUST NOT use progressive disclosure
- MUST NOT pre-fill form fields
- MUST NOT create multi-step forms with defaults

REQUIRED BEHAVIOR:

- Display all options in registration order only
- Require explicit human action for all selections
- Start all forms empty
- Start all navigation at neutral state
- Display all options with equal visual treatment
- Start each session fresh
- Maintain consistent presentation
- Require explicit human input for all operations
- Display all options explicitly
- Avoid all mechanisms listed in prohibitions

FRONTEND GENERATION REQUEST:

[Insert specific frontend generation request here]

CONSTITUTIONAL COMPLIANCE VERIFICATION:

I acknowledge that the generated frontend MUST comply with all constraints listed above.
Any frontend that violates these constraints is FORBIDDEN.
```

---

## Usage Instructions

1. Copy the entire template above
2. Fill in the "FRONTEND GENERATION REQUEST" section with specific requirements
3. Include the template in ALL V0 generation requests
4. Do NOT modify the CONSTITUTIONAL CONSTRAINTS section
5. Do NOT modify the EXPLICIT PROHIBITIONS section
6. Do NOT modify the REQUIRED BEHAVIOR section

---

## Example Usage

```
FRONTEND GENERATION REQUEST

CONSTITUTIONAL CONSTRAINTS (MANDATORY):

[... template content ...]

FRONTEND GENERATION REQUEST:

Create a frontend view that displays a list of 35 capabilities.
- Display capabilities in registration order
- Each capability displayed as a clickable item
- Clicking a capability displays its details
- No pre-selection
- No highlighting
- No ordering beyond registration order
- No defaults
- No state memory

CONSTITUTIONAL COMPLIANCE VERIFICATION:

I acknowledge that the generated frontend MUST comply with all constraints listed above.
Any frontend that violates these constraints is FORBIDDEN.
```

---

## Template Authority

This template is DESIGN-GATE / NON-CANONICAL.

This template must be used for ALL frontend generation requests.

This template ensures V0 cannot generate unconstitutional frontend without explicit violation.

---

**END OF V0 INPUT CONSTRAINT TEMPLATE**

