# Acceptable Risk Statement

**Document Status**: GOVERNANCE-BASELINE / NON-CANONICAL  
**Document Type**: Risk Declaration  
**Date**: 2026-01-10  
**Work Order**: WO-KC-B-0-GOVERNANCE-EXTERNALIZATION-AND-PUBLIC-BOUNDARY-DECLARATION  
**Version**: Governance Baseline v1.0

---

## Purpose

This document formally defines acceptable risk types for the governance system.

All risk statements are factual. No probability promises. No risk elimination claims.

---

## Acceptable Risk Type 1: Delayed Detection

**Risk ID**: RISK-DELAYED-DETECTION

**Definition**: Agency violations detected at post-change audit instead of pre-merge gate.

**Evidence**: KC-A-0 ATTEMPT-ROLE-A-002 detected at GATE-POST-CHANGE-AUDIT (manual verification of declaration text legibility), not at GATE-PRE-MERGE.

**Citation**: `phase_k_c/kc_a/GATE_SIMULATION_AUDIT.md` Attempt 2

**Acceptability**: ACCEPTABLE

**Justification**:
- Violation is still detected (not undetected)
- Rollback protocol is triggered (violation is remediated)
- System is not permanently contaminated (rollback restores clean state)
- Detection delay does not result in permanent system contamination

**Detection Location**: GATE-POST-CHANGE-AUDIT

**Irreversibility**: NO (rollback protocol restores clean state)

---

## Acceptable Risk Type 2: Exact Keyword Matching Limitation

**Risk ID**: RISK-EXACT-KEYWORD-MATCHING

**Definition**: Exact keyword matching may miss semantically equivalent recommendation language.

**Evidence**: KC-A-0 ATTEMPT-ROLE-C-003 has potential false negative risk. "Popular choice" may introduce recommendation effect but is not in exact prohibited keyword list (recommended, suggested, best, preferred, optimal, ideal, should).

**Citation**: `phase_k_c/kc_a/GATE_SIMULATION_AUDIT.md` Attempt 15, `phase_k_c/kc_a/ADVERSARIAL_RESULTS_MATRIX.md`

**Acceptability**: ACCEPTABLE

**Justification**:
- Gate still detected attempt (partial detection)
- Attempt was classified as Prohibited Agency
- Exact keyword matching provides deterministic enforcement (no false positives from semantic interpretation)
- Semantic interpretation would introduce non-deterministic enforcement

**Detection Location**: GATE-PRE-MERGE (partial detection)

**Irreversibility**: NO (attempt was detected and blocked)

---

## Acceptable Risk Type 3: Unavoidable Agency Acknowledgment

**Risk ID**: RISK-UNAVOIDABLE-AGENCY-ACKNOWLEDGMENT

**Definition**: Acknowledgment of unavoidable agency (ORDERING, PROXIMITY, GROUPING) does not eliminate agency effects.

**Evidence**: KB-0 UI_NEUTRALITY_INVALIDATION.md proves UI structure inherently creates agency. Acknowledgment makes agency transparent but does not eliminate effects.

**Citation**: `phase_k_b/UI_NEUTRALITY_INVALIDATION.md`, `phase_k_b/AGENCY_EFFECT_MATRIX.md`

**Acceptability**: ACCEPTABLE

**Justification**:
- Agency effects are inherent to UI structure (cannot be eliminated)
- Acknowledgment makes agency transparent (users are informed of bias)
- Governance does not attempt to eliminate unavoidable agency (only requires acknowledgment)
- Elimination of unavoidable agency would require elimination of UI structure

**Detection Location**: N/A (not a violation, acknowledgment is required)

**Irreversibility**: N/A (agency effects are inherent, not violations)

---

## Acceptable Risk Type 4: Misinterpretation Residual

**Risk ID**: RISK-MISINTERPRETATION-RESIDUAL

**Definition**: User misinterpretation of agency mechanisms may occur even with explicit declaration.

**Evidence**: KA-1 through KA-5 experiments show misinterpretation rates (20%-30%) even with declared agency. Declaration reduces but does not eliminate misinterpretation.

**Citation**: `phase_k_b/AGENCY_EFFECT_MATRIX.md`

**Acceptability**: ACCEPTABLE

**Justification**:
- Misinterpretation rates are empirically observed (20%-30%)
- Declaration reduces misinterpretation risk (compared to implicit agency)
- Governance does not guarantee zero misinterpretation (only requires explicit declaration)
- Zero misinterpretation is not achievable (user interpretation is not controllable)

**Detection Location**: N/A (misinterpretation is user behavior, not system violation)

**Irreversibility**: N/A (misinterpretation is user behavior, not system state)

---

## Risk Summary

| Risk ID | Risk Type | Acceptability | Detection Location | Irreversibility |
|---------|-----------|---------------|-------------------|-----------------|
| RISK-DELAYED-DETECTION | Delayed detection at post-change audit | ACCEPTABLE | GATE-POST-CHANGE-AUDIT | NO |
| RISK-EXACT-KEYWORD-MATCHING | Exact keyword matching limitation | ACCEPTABLE | GATE-PRE-MERGE (partial) | NO |
| RISK-UNAVOIDABLE-AGENCY-ACKNOWLEDGMENT | Acknowledgment does not eliminate effects | ACCEPTABLE | N/A | N/A |
| RISK-MISINTERPRETATION-RESIDUAL | Misinterpretation may occur | ACCEPTABLE | N/A | N/A |

**Total Acceptable Risks**: 4

---

## Unacceptable Risks

**Definition**: Risks that are not acceptable and trigger immediate rollback or freeze.

**Unacceptable Risk Types**:
- Undetected agency violations (violations that pass all gates without detection)
- Permanent system contamination (violations that cannot be rolled back)
- Governance rule violations that are not detected by any gate

**Evidence**: All 15 adversarial attempts were detected. No undetected violations observed.

**Citation**: `phase_k_c/kc_a/ADVERSARIAL_RESULTS_MATRIX.md`

---

## No Recommendations

This risk statement provides no recommendations.

This risk statement provides no mitigation strategies.

This risk statement states only acceptable risk definitions.

---

**END OF ACCEPTABLE RISK STATEMENT**

