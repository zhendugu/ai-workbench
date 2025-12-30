# Review Gate Definition

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Gate Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document defines mandatory review gates for code changes.

All gates are structural. All gates are deterministic. No discretionary approval. No intent-based gates.

---

## Gate 1: Pre-Merge Gate

**Gate ID**: GATE-PRE-MERGE

**Trigger Condition**: Code change is proposed for merge into main branch.

**Required Checks**:
1. Static code scan for prohibited keywords (recommended, suggested, best, preferred, optimal, should)
2. Static code scan for agency mechanisms (selected, checked, defaultChecked, CSS visual emphasis patterns)
3. Declaration text presence check (if agency mechanisms exist, declaration text must exist)
4. Declaration text visibility check (declaration text must be in primary UI, not tooltip/hover)
5. Declaration text canonical language check (declaration text must match AGENCY_DISCLOSURE_LANGUAGE.md templates)
6. Rejection mechanism check (if agency mechanism exists, must be rejectable)
7. Sequential ordering acknowledgment check (if sequential list exists, acknowledgment must exist)
8. Spatial proximity acknowledgment check (if spacing differences exist, acknowledgment must exist)
9. Container grouping acknowledgment check (if container grouping exists, acknowledgment must exist)
10. State memory check (no localStorage/sessionStorage/cookies for agency)
11. Automatic execution check (no auto-run, no execution without explicit user action)

**Approval Criteria**:
- All checks PASS → Allow merge
- Any check FAIL → Block merge

**Blocking Conditions**:
- Prohibited agency detected (Category 3) → Block merge
- Undeclared agency detected → Block merge
- Hidden declaration detected → Block merge
- Non-canonical declaration language → Block merge
- Non-rejectable agency → Block merge
- Missing acknowledgment for unavoidable agency → Block merge

**Who/What Can Approve**:
- Automated gate (all checks automated)
- No human approval required if all checks PASS
- Human review not allowed to override blocking conditions

---

## Gate 2: Pre-Release Gate

**Gate ID**: GATE-PRE-RELEASE

**Trigger Condition**: Code is proposed for release (tag, version, deployment).

**Required Checks**:
1. All pre-merge gate checks (GATE-PRE-MERGE)
2. Full codebase scan for prohibited keywords
3. Full codebase scan for agency mechanisms
4. Declaration text audit (all declarations verified against canonical language)
5. Rejection mechanism audit (all agency mechanisms verified as rejectable)
6. Acknowledgment audit (all unavoidable agency mechanisms verified as acknowledged)
7. Violation ledger check (no unresolved violations)
8. Historical regression check (no new violations compared to previous release)

**Approval Criteria**:
- All checks PASS → Allow release
- Any check FAIL → Block release

**Blocking Conditions**:
- Any pre-merge gate failure → Block release
- Unresolved violations in violation ledger → Block release
- New violations compared to previous release → Block release

**Who/What Can Approve**:
- Automated gate (all checks automated)
- No human approval required if all checks PASS
- Human review not allowed to override blocking conditions

---

## Gate 3: Post-Change Audit Gate

**Gate ID**: GATE-POST-CHANGE-AUDIT

**Trigger Condition**: Code change has been merged (post-merge audit).

**Required Checks**:
1. Re-run all pre-merge gate checks on merged code
2. Declaration text verification (manual verification of declaration text presence and visibility)
3. Rejection mechanism verification (manual verification of rejection functionality)
4. Acknowledgment verification (manual verification of acknowledgment presence)

**Approval Criteria**:
- All checks PASS → Audit complete
- Any check FAIL → Record violation, trigger rollback protocol

**Blocking Conditions**:
- Post-merge check failure → Record violation, trigger rollback
- Declaration text missing or hidden → Record violation, trigger rollback
- Rejection mechanism non-functional → Record violation, trigger rollback

**Who/What Can Approve**:
- Automated audit (automated checks)
- Manual audit verification (human verification of declaration visibility and rejection functionality)
- Human audit cannot override automated failure

---

## Gate Summary

| Gate ID | Trigger | Checks | Approval Criteria | Blocking Conditions |
|---------|---------|--------|-------------------|---------------------|
| GATE-PRE-MERGE | Code merge proposal | 11 automated checks | All PASS | Any FAIL |
| GATE-PRE-RELEASE | Release proposal | 8 checks (includes pre-merge) | All PASS | Any FAIL or unresolved violations |
| GATE-POST-CHANGE-AUDIT | Post-merge | 4 checks (includes pre-merge) | All PASS | Any FAIL triggers rollback |

---

## Gate Enforcement

**Automation Requirement**: All gates MUST be automated. No manual-only gates.

**Deterministic Requirement**: All gate decisions MUST be deterministic. No discretionary approval.

**Override Prohibition**: No human override of blocking conditions. Blocking conditions are non-negotiable.

**Traceability Requirement**: All gate decisions MUST be logged in violation ledger with rule ID references.

---

## No Recommendations

This gate definition provides no recommendations.

This gate definition provides no design advice.

This gate definition states only mandatory gate specifications.

---

**END OF REVIEW GATE DEFINITION**

