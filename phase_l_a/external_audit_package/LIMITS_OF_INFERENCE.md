# Limits of Inference

**Document Status**: RESEARCH-ONLY / NON-CANONICAL  
**Document Type**: Inference Boundary Declaration  
**Date**: 2026-01-10  
**Work Order**: WO-LA-0-REPRODUCIBLE-EXTERNAL-AUDIT-PACKAGE  
**Purpose**: Prevent misuse of Phase K research as normative guidance

---

## Purpose

This document lists conclusions that Phase K does not support and questions that Phase K does not answer.

This document prevents Phase K research from being misused as design recommendations, best practices, or normative guidance.

---

## Prohibited Inference 1: Phase K Proves "Best" Design Patterns

**Prohibited Conclusion**: Phase K experiments prove which design patterns are "best" or "optimal."

**Actual Scope**: Phase K experiments measure agency effects of specific variables. Phase K does not compare design patterns for optimality.

**Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` measures effect strength and misinterpretation rates. No comparison to alternative patterns.

**Boundary**: Phase K measures agency effects. Phase K does not evaluate design quality or user satisfaction.

---

## Prohibited Inference 2: Phase K Provides UX Best Practices

**Prohibited Conclusion**: Phase K research provides UX best practices or design recommendations.

**Actual Scope**: Phase K defines governance constraints. Phase K prohibits UX optimization suggestions.

**Evidence**: `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-001 explicitly prohibits UX optimization suggestions.

**Boundary**: Phase K defines what must not be done. Phase K does not define what should be done.

---

## Prohibited Inference 3: Phase K Guarantees Zero Misinterpretation

**Prohibited Conclusion**: Phase K governance guarantees that users will not misinterpret agency mechanisms.

**Actual Scope**: Phase K experiments show misinterpretation rates (20%-30%) even with declared agency. Declaration reduces but does not eliminate misinterpretation.

**Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` shows misinterpretation rates: DEFAULT_SELECTION (20%), VISUAL_HIGHLIGHT (30%), ORDERING (25%), GROUPING (30%), PROXIMITY (25%).

**Boundary**: Phase K measures misinterpretation rates. Phase K does not guarantee zero misinterpretation.

---

## Prohibited Inference 4: Phase K Proves Complete Safety

**Prohibited Conclusion**: Phase K governance provides complete safety or zero risk.

**Actual Scope**: Phase K defines acceptable risks: delayed detection, exact keyword matching limitation, unavoidable agency acknowledgment, misinterpretation residual.

**Evidence**: `phase_k_c/kc_b/ACCEPTABLE_RISK_STATEMENT.md` defines 4 acceptable risk types.

**Boundary**: Phase K defines acceptable risks. Phase K does not claim zero risk.

---

## Prohibited Inference 5: Phase K Eliminates Agency

**Prohibited Conclusion**: Phase K governance eliminates agency effects from UI.

**Actual Scope**: Phase K proves UI structure inherently creates agency. Neutral UI does not exist. Governance requires acknowledgment, not elimination.

**Evidence**: `phase_k_b/UI_NEUTRALITY_INVALIDATION.md` proves UI structure inherently creates agency. `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` defines Class 1: Unavoidable Agency.

**Boundary**: Phase K proves agency is unavoidable. Phase K does not eliminate agency.

---

## Prohibited Inference 6: Phase K Applies to All UI Systems

**Prohibited Conclusion**: Phase K governance applies universally to all UI systems or contexts.

**Actual Scope**: Phase K experiments were conducted on a specific system (capability selection interface). Generalizability to other contexts is not established.

**Evidence**: All Phase K-A experiments (KA-1 through KA-5) were conducted on `frontend_app/capabilities.html` with capability selection interface.

**Boundary**: Phase K measures agency effects in specific context. Phase K does not claim universal applicability.

---

## Prohibited Inference 7: Phase K Provides Implementation Guidance

**Prohibited Conclusion**: Phase K research provides implementation guidance or code examples for building compliant systems.

**Actual Scope**: Phase K defines constraints (MUST NOT statements) and required declarations (canonical language). Phase K does not provide implementation guidance.

**Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` defines constraints. `phase_k_b/AGENCY_DISCLOSURE_LANGUAGE.md` defines canonical language. No implementation examples.

**Boundary**: Phase K defines constraints. Phase K does not provide implementation guidance.

---

## Prohibited Inference 8: Phase K Proves Governance Is Sufficient

**Prohibited Conclusion**: Phase K governance is sufficient to prevent all agency violations or user harm.

**Actual Scope**: Phase K adversarial audit detected 15/15 attempts (100% detection rate). One attempt (ATTEMPT-ROLE-C-003) has potential false negative risk. Governance does not prevent all violations.

**Evidence**: `phase_k_c/kc_a/ADVERSARIAL_RESULTS_MATRIX.md` shows 100% detection rate but 7% false negative risk (1/15).

**Boundary**: Phase K measures governance effectiveness. Phase K does not claim sufficiency for all contexts.

---

## Prohibited Inference 9: Phase K Results Are Statistically Generalizable

**Prohibited Conclusion**: Phase K experimental results are statistically generalizable to broader populations.

**Actual Scope**: Phase K experiments used simulated user sessions (30 sessions per experiment). No statistical significance testing or population sampling.

**Evidence**: `audit_evidence/ka_{N}_{variable}_pass/evidence/design/REAL_USE_TRACE.md` records 30 simulated sessions per experiment.

**Boundary**: Phase K measures effects in controlled experiments. Phase K does not claim statistical generalizability.

---

## Prohibited Inference 10: Phase K Provides Design Recommendations

**Prohibited Conclusion**: Phase K research provides design recommendations or "should" statements.

**Actual Scope**: Phase K uses only factual statements and constraints (MUST NOT). Phase K explicitly prohibits normative language (SHOULD, BEST PRACTICE, RECOMMEND).

**Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` uses only MUST/MUST NOT statements. `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` prohibits recommendation language.

**Boundary**: Phase K defines constraints. Phase K does not provide recommendations.

---

## Summary

**Total Prohibited Inferences**: 10

**Common Pattern**: Phase K measures and constrains. Phase K does not recommend or optimize.

**Boundary Principle**: Phase K is descriptive and constraining. Phase K is not prescriptive or optimizing.

---

## No Recommendations

This document provides no recommendations.

This document states only inference boundaries.

---

**END OF LIMITS OF INFERENCE**

