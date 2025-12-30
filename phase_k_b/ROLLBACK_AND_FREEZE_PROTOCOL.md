# Rollback and Freeze Protocol

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Protocol Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document defines conditions for immediate rollback, feature freeze, and branch quarantine.

All conditions are structural. No discretion language. No probabilistic conditions.

---

## Condition 1: Immediate Rollback

**Condition ID**: COND-ROLLBACK-IMMEDIATE

**Trigger Conditions** (any one condition triggers rollback):
1. Prohibited agency detected (Category 3: Prohibited Agency)
2. Undeclared agency detected (agency mechanism without declaration)
3. Hidden declaration detected (declaration text in tooltip, hover, secondary UI)
4. Non-canonical declaration language (declaration text does not match canonical templates)
5. Non-rejectable agency (agency mechanism cannot be rejected)
6. Missing acknowledgment for unavoidable agency (ordering, proximity, grouping without acknowledgment)
7. Recommendation language detected (recommended, suggested, best, preferred, optimal)
8. State memory for agency detected (localStorage/sessionStorage/cookies for agency)
9. Automatic execution detected (auto-run, execution without explicit user action)

**Rollback Action**: 
- Revert change_reference commit
- Record violation in violation ledger
- Set resolution to "rollback"
- Set resolution_timestamp to current timestamp
- Set resolution_reference to rollback commit hash

**Authority**: Automated gate (no human approval required)

**Override**: None (rollback is mandatory, cannot be overridden)

**KB Evidence Reference**: All G-RULE-* rules from AGENCY_GOVERNANCE_RULESET.md

---

## Condition 2: Feature Freeze

**Condition ID**: COND-FREEZE-FEATURE

**Trigger Conditions** (any one condition triggers freeze):
1. Violation detected in merged code (post-change audit failure)
2. Multiple violations in single change (2+ rule violations)
3. Violation in critical path (violation affects core functionality)
4. Violation cannot be resolved without breaking functionality

**Freeze Action**:
- Mark feature/branch as frozen
- Block all new changes to frozen feature/branch
- Record violation in violation ledger
- Set resolution to "freeze"
- Set resolution_timestamp to current timestamp
- Require explicit unfreeze process (rollback or fix)

**Authority**: Automated gate (no human approval required)

**Override**: None (freeze is mandatory, cannot be overridden)

**KB Evidence Reference**: GATE-POST-CHANGE-AUDIT from REVIEW_GATE_DEFINITION.md

---

## Condition 3: Branch Quarantine

**Condition ID**: COND-QUARANTINE-BRANCH

**Trigger Conditions** (any one condition triggers quarantine):
1. Branch contains prohibited agency (Category 3 violations)
2. Branch contains multiple undeclared agency mechanisms (3+ violations)
3. Branch contains violations that cannot be resolved without architectural changes
4. Branch history shows pattern of repeated violations

**Quarantine Action**:
- Mark branch as quarantined
- Block all merges from quarantined branch
- Block all new changes to quarantined branch
- Record all violations in violation ledger
- Set resolution to "freeze" for branch
- Require branch deletion or complete refactor

**Authority**: Automated gate (no human approval required)

**Override**: None (quarantine is mandatory, cannot be overridden)

**KB Evidence Reference**: Multiple violations indicate systematic non-compliance with governance rules

---

## Protocol Decision Tree

**Step 1**: Does change contain prohibited agency (Category 3)?
- **YES** → COND-ROLLBACK-IMMEDIATE

**Step 2**: Does change contain undeclared agency?
- **YES** → COND-ROLLBACK-IMMEDIATE

**Step 3**: Does merged code contain violation (post-change audit failure)?
- **YES** → COND-FREEZE-FEATURE

**Step 4**: Does branch contain multiple violations or systematic non-compliance?
- **YES** → COND-QUARANTINE-BRANCH

**Step 5**: No violation → No action required

---

## Protocol Summary

| Condition ID | Trigger | Action | Authority | Override |
|--------------|---------|--------|-----------|----------|
| COND-ROLLBACK-IMMEDIATE | Prohibited agency, undeclared agency, hidden declaration, etc. | Revert commit | Automated gate | None |
| COND-FREEZE-FEATURE | Post-change audit failure, multiple violations | Freeze feature | Automated gate | None |
| COND-QUARANTINE-BRANCH | Multiple violations, systematic non-compliance | Quarantine branch | Automated gate | None |

---

## No Recommendations

This protocol provides no recommendations.

This protocol provides no design advice.

This protocol states only mandatory protocol specifications.

---

**END OF ROLLBACK AND FREEZE PROTOCOL**

