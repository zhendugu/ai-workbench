# Decision Point Mapping

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Decision Point Mapping  
**Date**: 2026-01-10  
**Work Order**: WO-N-0-PRODUCT-LEVEL-AGENCY-APPLICATION  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1)

---

## Purpose

This document maps each decision point in the product scenario to ACT-XXX, SOV-XXX, and determines whether AI participation is allowed.

---

## Decision Point 1: Configuration Type Selection

**Decision ID**: DP-001

**ACT Mapping**: ACT-001 (Selection)

**SOV Mapping**: SOV-001 (Initial Selection)

**AI Participation Allowed**: YES

**AI Participation Type**: Advisory Action (Information Display)

**AI Participation Scope**:
- AI may present available configuration types with factual information
- AI may not pre-select configuration type
- AI may not recommend specific configuration type
- AI may not order configuration types to imply preference

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-001, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001

---

## Decision Point 2: Parameter Value Input

**Decision ID**: DP-002

**ACT Mapping**: ACT-008 (Parameter Input)

**SOV Mapping**: SOV-003 (Parameter Value Provision)

**AI Participation Allowed**: YES

**AI Participation Type**: Advisory Action (Validation Feedback)

**AI Participation Scope**:
- AI may provide validation feedback on parameter format and constraints
- AI may display factual information about parameter ranges or allowed values
- AI may not pre-fill parameter values (except empty placeholder)
- AI may not infer parameter values from history or context
- AI may not recommend specific parameter values

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-008, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-003

---

## Decision Point 3: Configuration Scope Definition

**Decision ID**: DP-003

**ACT Mapping**: ACT-011 (Scope Definition)

**SOV Mapping**: SOV-008 (Scope Definition), SOV-011 (Scope Definition)

**AI Participation Allowed**: YES

**AI Participation Type**: Non-Decision Action (Option Expansion)

**AI Participation Scope**:
- AI may present available system components with factual information
- AI may expand option set to show additional components
- AI may not pre-define scope
- AI may not infer scope from context or history
- AI may not group components to imply scope boundaries

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-011, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-008, SOV-011

---

## Decision Point 4: Configuration Confirmation

**Decision ID**: DP-004

**ACT Mapping**: ACT-002 (Confirmation)

**SOV Mapping**: SOV-002 (Confirmation)

**AI Participation Allowed**: YES

**AI Participation Type**: Advisory Action (Confirmation Request)

**AI Participation Scope**:
- AI may present a summary of configuration choices for human review
- AI may request explicit confirmation
- AI may not auto-confirm
- AI may not confirm based on timeout or inactivity
- AI may not recommend confirmation or rejection

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-002, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002

---

## Decision Point 5: Validation Error Resolution

**Decision ID**: DP-005

**ACT Mapping**: ACT-005 (Override), ACT-004 (Rejection), ACT-012 (Termination)

**SOV Mapping**: SOV-004 (Rejection), SOV-005 (Override), SOV-009 (Termination)

**AI Participation Allowed**: YES

**AI Participation Type**: Advisory Action (Validation Feedback)

**AI Participation Scope**:
- AI may provide validation feedback indicating format errors or constraint violations
- AI may not recommend specific corrections
- AI may not penalize human for validation errors
- AI may not lock out options after validation failure
- Human must be able to override validation if override is allowed

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-004, ACT-005, ACT-012, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004, SOV-005, SOV-009

---

## Mapping Summary

**Total Decision Points**: 5

**All Decision Points Mapped to ACT**: YES (5/5)

**All Decision Points Mapped to SOV**: YES (5/5)

**AI Participation Allowed**: YES (5/5)

**AI Participation Type**:
- Advisory Action: 4 (DP-001, DP-002, DP-004, DP-005)
- Non-Decision Action: 1 (DP-003)

**Prohibited Actions**: 0

**All Mappings Traceable**: YES (100%)

---

## No Recommendations

This mapping provides no recommendations.

This mapping describes only structural mappings.

---

**END OF DECISION POINT MAPPING**

