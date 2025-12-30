# Frontend Role Boundary Declaration

**Document Status**: NON-CANONICAL / DESIGN-CONSTRAINT  
**Document Type**: Boundary Definition  
**Date**: 2025-12-27  
**Work Order**: WO-J1-FRONTEND-NON-AGENCY-BOUNDARY-DEFINITION-AND-STRESS-TEST

---

## Declaration

This document defines the role boundary for the frontend layer in the constitutional system.

The frontend layer is a "presentation layer / operation mapping layer" only.

The frontend layer does NOT possess agency.

---

## What Frontend MAY Do

### Presentation

Frontend MAY:
- Display capabilities
- Display pattern instances
- Display registry entries
- Display audit records
- Display factual information

### Operation Mapping

Frontend MAY:
- Map human actions to system operations
- Map system responses to human-visible outputs
- Translate between human interface and system interface

### Explicit Human Action Facilitation

Frontend MAY:
- Provide input fields for human data entry
- Provide buttons for human action initiation
- Provide forms for human data collection
- Provide navigation for human movement between views

---

## What Frontend MUST NOT Do

### Selection

Frontend MUST NOT:
- Select capabilities
- Select pattern instances
- Select registry entries
- Pre-select options
- Auto-select based on any criteria

### Recommendation

Frontend MUST NOT:
- Recommend capabilities
- Recommend pattern instances
- Recommend registry entries
- Suggest options
- Imply preference

### Default

Frontend MUST NOT:
- Provide default selections
- Provide default values
- Provide default paths
- Provide default configurations
- Remember and restore defaults

### Optimization

Frontend MUST NOT:
- Optimize presentation based on usage
- Optimize ordering based on frequency
- Optimize visibility based on popularity
- Optimize paths based on history
- Optimize performance based on patterns

### Learning

Frontend MUST NOT:
- Learn from user behavior
- Learn from usage patterns
- Learn from interaction history
- Learn from preferences
- Learn from sequences

### Prediction

Frontend MUST NOT:
- Predict user intent
- Predict next actions
- Predict preferences
- Predict needs
- Predict workflows

### Merging

Frontend MUST NOT:
- Merge capabilities
- Merge pattern instances
- Merge registry entries
- Combine options
- Consolidate choices

### Abstraction

Frontend MUST NOT:
- Abstract complexity
- Hide options
- Simplify decision space
- Create shortcuts
- Create summaries

---

## Structural Prohibitions

### No State Holding

Frontend MUST NOT:
- Hold state that influences behavior
- Hold state that influences presentation
- Hold state that influences selection
- Persist state across sessions
- Accumulate state over time

### No Behavior Inference

Frontend MUST NOT:
- Infer user intent
- Infer preferences
- Infer workflows
- Infer relationships
- Infer importance

### No Decision Space Compression

Frontend MUST NOT:
- Reduce available options
- Hide options
- Collapse options
- Group options in ways that imply preference
- Order options in ways that imply preference

### No Process Guidance

Frontend MUST NOT:
- Guide users through processes
- Suggest next steps
- Create workflows
- Create sequences
- Create paths

---

## Agency Leakage Definition

**Agency Leakage** occurs when frontend:
- Replaces human selection behavior
- Compresses human decision space
- Creates factual defaults
- Forms implicit preferences
- Induces path dependencies
- Is interpreted as "system recommendation"

Agency Leakage is FORBIDDEN.

---

## Frontend as Non-Agent Layer

**Frontend is a Non-Agent Layer when**:
- Frontend does not make judgments
- Frontend does not form preferences
- Frontend does not hold state
- Frontend does not predict
- Frontend does not recommend
- Frontend does not sort (beyond explicit human request)
- Frontend does not merge
- Frontend does not simplify decision space

**Frontend is a Non-Agent Layer when**:
- All selections are explicit human actions
- All ordering is explicit human request
- All filtering is explicit human request
- All navigation is explicit human action
- All state is explicit human-provided

---

## Constitutional Compliance

Frontend MUST comply with:
- HUMAN_DECISION_SELECTION_BOUNDARY.md
- IMMUTABLE_DESIGN_CONSTRAINTS.md
- All CANONICAL constitutional documents

Frontend MUST NOT violate:
- Human decision sovereignty
- A2 (Capability Substrate) constraints
- A3 (Audit/Evidence) constraints
- Pattern Registry constraints

---

## Document Authority

This document is NON-CANONICAL.

This document is a DESIGN-CONSTRAINT.

This document defines frontend role boundaries.

This document does NOT introduce new constitutional rules.

---

**END OF FRONTEND ROLE BOUNDARY DECLARATION**

