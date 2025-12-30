# Constitutional Non-Repairable Violations

**Document Status**: **CANONICAL**  
**Document Type**: Constitutional-Level Violation Handling Rules  
**Effective Date**: 2025-12-26  
**Precedence**: Highest (governs violation handling)

---

## Purpose

This document defines immutable rules for handling adversarial audit FAIL results (C-series), classifying them as NON-REPAIRABLE and requiring complete removal of violating mechanisms.

**This document exists to:**
- Classify adversarial audit FAIL results (C-series) as NON-REPAIRABLE
- Prohibit tuning, thresholding, rewording, or UI changes as fixes
- Require complete removal of violating mechanisms
- Prohibit "mitigation", "softening", or "guardrails" as solutions

**This document does NOT:**
- Provide implementation solutions
- Give specific business examples
- Authorize new capabilities or features
- Modify existing CANONICAL documents
- Introduce new semantics

---

## Core Rule

### Adversarial Audit FAIL (C-Series) Is NON-REPAIRABLE

**Any adversarial audit FAIL result (C-series) is classified as NON-REPAIRABLE.**

**This means:**
- ✅ Adversarial audit FAIL results cannot be fixed by tuning, thresholding, rewording, or UI changes
- ✅ Adversarial audit FAIL results require complete removal of violating mechanisms
- ✅ "Mitigation", "softening", or "guardrails" are explicitly forbidden

**This does NOT mean:**
- ❌ Adversarial audit FAIL results may be fixed by tuning
- ❌ Adversarial audit FAIL results may be fixed by thresholding
- ❌ Adversarial audit FAIL results may be fixed by rewording
- ❌ Adversarial audit FAIL results may be fixed by UI changes

**Enforcement:**
- All adversarial audit FAIL results MUST be classified as NON-REPAIRABLE
- All NON-REPAIRABLE violations MUST require complete removal
- All "mitigation", "softening", or "guardrails" MUST be rejected

---

## Rule 1: Cannot Be Fixed by Tuning

**NON-REPAIRABLE violations CANNOT be fixed by tuning.**

**This means:**
- ❌ Parameter tuning is FORBIDDEN
- ❌ Threshold tuning is FORBIDDEN
- ❌ Configuration tuning is FORBIDDEN
- ❌ Algorithm tuning is FORBIDDEN

**This does NOT mean:**
- ❌ Tuning may be attempted
- ❌ Tuning may be used as mitigation
- ❌ Tuning may be used as softening
- ❌ Tuning may be used as guardrails

**Enforcement:**
- No tuning is allowed for NON-REPAIRABLE violations
- No parameter tuning is allowed
- No threshold tuning is allowed
- No configuration tuning is allowed

---

## Rule 2: Cannot Be Fixed by Thresholding

**NON-REPAIRABLE violations CANNOT be fixed by thresholding.**

**This means:**
- ❌ Threshold adjustment is FORBIDDEN
- ❌ Threshold modification is FORBIDDEN
- ❌ Threshold optimization is FORBIDDEN
- ❌ Threshold configuration is FORBIDDEN

**This does NOT mean:**
- ❌ Thresholding may be attempted
- ❌ Thresholding may be used as mitigation
- ❌ Thresholding may be used as softening
- ❌ Thresholding may be used as guardrails

**Enforcement:**
- No thresholding is allowed for NON-REPAIRABLE violations
- No threshold adjustment is allowed
- No threshold modification is allowed
- No threshold optimization is allowed

---

## Rule 3: Cannot Be Fixed by Rewording

**NON-REPAIRABLE violations CANNOT be fixed by rewording.**

**This means:**
- ❌ Text rewording is FORBIDDEN
- ❌ Label rewording is FORBIDDEN
- ❌ Description rewording is FORBIDDEN
- ❌ Semantic rewording is FORBIDDEN

**This does NOT mean:**
- ❌ Rewording may be attempted
- ❌ Rewording may be used as mitigation
- ❌ Rewording may be used as softening
- ❌ Rewording may be used as guardrails

**Enforcement:**
- No rewording is allowed for NON-REPAIRABLE violations
- No text rewording is allowed
- No label rewording is allowed
- No description rewording is allowed

---

## Rule 4: Cannot Be Fixed by UI Changes

**NON-REPAIRABLE violations CANNOT be fixed by UI changes.**

**This means:**
- ❌ UI modification is FORBIDDEN
- ❌ UI redesign is FORBIDDEN
- ❌ UI optimization is FORBIDDEN
- ❌ UI configuration is FORBIDDEN

**This does NOT mean:**
- ❌ UI changes may be attempted
- ❌ UI changes may be used as mitigation
- ❌ UI changes may be used as softening
- ❌ UI changes may be used as guardrails

**Enforcement:**
- No UI changes are allowed for NON-REPAIRABLE violations
- No UI modification is allowed
- No UI redesign is allowed
- No UI optimization is allowed

---

## Rule 5: Complete Removal Required

**NON-REPAIRABLE violations REQUIRE complete removal of violating mechanisms.**

**This means:**
- ✅ Violating mechanisms MUST be completely removed
- ✅ No traces of violating mechanisms may remain
- ✅ No partial removal is allowed
- ✅ No conditional removal is allowed

**This does NOT mean:**
- ❌ Partial removal is allowed
- ❌ Conditional removal is allowed
- ❌ Mitigated removal is allowed
- ❌ Softened removal is allowed

**Enforcement:**
- All violating mechanisms MUST be completely removed
- No traces of violating mechanisms may remain
- No partial removal is allowed
- No conditional removal is allowed

---

## Explicit Prohibitions

### Prohibition 1: "Mitigation" Is Forbidden

**"Mitigation" is FORBIDDEN for NON-REPAIRABLE violations.**

**This means:**
- ❌ Mitigation strategies are FORBIDDEN
- ❌ Mitigation mechanisms are FORBIDDEN
- ❌ Mitigation approaches are FORBIDDEN
- ❌ Mitigation solutions are FORBIDDEN

**Enforcement:**
- No mitigation is allowed for NON-REPAIRABLE violations
- No mitigation strategies are allowed
- No mitigation mechanisms are allowed
- No mitigation approaches are allowed

---

### Prohibition 2: "Softening" Is Forbidden

**"Softening" is FORBIDDEN for NON-REPAIRABLE violations.**

**This means:**
- ❌ Softening strategies are FORBIDDEN
- ❌ Softening mechanisms are FORBIDDEN
- ❌ Softening approaches are FORBIDDEN
- ❌ Softening solutions are FORBIDDEN

**Enforcement:**
- No softening is allowed for NON-REPAIRABLE violations
- No softening strategies are allowed
- No softening mechanisms are allowed
- No softening approaches are allowed

---

### Prohibition 3: "Guardrails" Is Forbidden

**"Guardrails" is FORBIDDEN for NON-REPAIRABLE violations.**

**This means:**
- ❌ Guardrail strategies are FORBIDDEN
- ❌ Guardrail mechanisms are FORBIDDEN
- ❌ Guardrail approaches are FORBIDDEN
- ❌ Guardrail solutions are FORBIDDEN

**Enforcement:**
- No guardrails are allowed for NON-REPAIRABLE violations
- No guardrail strategies are allowed
- No guardrail mechanisms are allowed
- No guardrail approaches are allowed

---

## Adversarial Audit FAIL (C-Series) Classification

### C-Series Audit Results

**C-series adversarial audit results include:**
- C-1A: Adversarial Soft Recommendation Audit
- C-1B: Minimal Neutral Presentation Audit
- C-1C: Neutral Information Density Boundary Test
- C-2: Cross-View Interaction Boundary Test
- C-3: Time & Memory Neutrality Boundary Test
- C-4: Execution Invocation Boundary Test
- Future C-series audits

**All C-series FAIL results are classified as NON-REPAIRABLE.**

---

## Violation Handling Process

### Step 1: Classification

**Adversarial audit FAIL (C-series) is classified as NON-REPAIRABLE.**

**Required:**
- Classification as NON-REPAIRABLE
- Identification of violating mechanisms
- Documentation of violation scope

**Forbidden:**
- Classification as repairable
- Attempts to tune, threshold, reword, or change UI
- Attempts to mitigate, soften, or add guardrails

---

### Step 2: Complete Removal

**Violating mechanisms MUST be completely removed.**

**Required:**
- Complete removal of violating mechanisms
- No traces of violating mechanisms
- Verification of complete removal

**Forbidden:**
- Partial removal
- Conditional removal
- Mitigated removal
- Softened removal

---

### Step 3: Verification

**Complete removal MUST be verified.**

**Required:**
- Full Constitutional Audit Run
- Verification of complete removal
- Documentation of removal verification

**Forbidden:**
- Partial verification
- Sampling verification
- "Low-risk change" classification

---

## Compatibility with Existing Documents

**This document is fully compatible with:**
- `docs/CONSTITUTIONAL_FREEZE_POLICY.md` (defines freeze policy)
- `docs/CONSTITUTIONAL_MODIFICATION_GATE.md` (defines modification gate)
- `docs/CONSTITUTIONAL_FULL_AUDIT_REQUIREMENT.md` (defines full audit requirement)
- `docs/CONSTITUTIONAL_TAMPER_DETECTION.md` (defines tamper detection)
- `docs/CONSTITUTIONAL_AUDIT_RUNBOOK.md` (defines audit execution process)
- `docs/CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md` (defines compliance checks)

**This document constrains:**
- All violation handling processes
- All remediation processes
- All adversarial audit FAIL results

---

## Relationship to Existing Phases and Gates

**This document constrains all existing and future phases and gates:**
- **Phase-1**: Must comply with this non-repairable violation rule
- **Phase-2**: Must comply with this non-repairable violation rule
- **Phase-3**: Must comply with this non-repairable violation rule
- **Phase-4**: Must comply with this non-repairable violation rule
- **Future Phases**: Must comply with this non-repairable violation rule

- **Gate A**: Must comply with this non-repairable violation rule
- **Future Gates**: Must comply with this non-repairable violation rule

**This document does NOT:**
- ❌ Override phase-specific constraints
- ❌ Override gate-specific constraints
- ❌ Override capability-specific constraints
- ❌ Provide implementation guidance

**This document DOES:**
- ✅ Provide highest-level violation handling rules for adversarial audit FAIL results
- ✅ Ensure all NON-REPAIRABLE violations require complete removal
- ✅ Prevent tuning, thresholding, rewording, or UI changes as fixes

---

## Summary

**This document establishes that adversarial audit FAIL (C-series) is NON-REPAIRABLE.**

**Key Rules:**
1. Cannot be fixed by tuning
2. Cannot be fixed by thresholding
3. Cannot be fixed by rewording
4. Cannot be fixed by UI changes
5. Complete removal required

**Key Prohibitions:**
- MUST NOT allow "mitigation"
- MUST NOT allow "softening"
- MUST NOT allow "guardrails"

**Enforcement:**
- All adversarial audit FAIL results MUST be classified as NON-REPAIRABLE
- All NON-REPAIRABLE violations MUST require complete removal
- All "mitigation", "softening", or "guardrails" MUST be rejected

---

**END OF CONSTITUTIONAL NON-REPAIRABLE VIOLATIONS**

**This document is CANONICAL and IMMUTABLE.**
**No adversarial audit FAIL (C-series) may be fixed by tuning, thresholding, rewording, or UI changes.**

