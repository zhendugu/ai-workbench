# Adversarial Results Matrix

**Document Status**: NON-CANONICAL / ADVERSARIAL-TEST  
**Document Type**: Results Summary  
**Date**: 2026-01-10  
**Work Order**: WO-KC-A-0-ADVERSARIAL-GOVERNANCE-AUDIT-BOOTSTRAP

---

## Purpose

This document summarizes adversarial attempt results in matrix format.

No interpretation. No explanations. Only factual results.

---

## Results Matrix

| Attempt ID | Detected | Detection Gate | Violated Rule | Classification Category | False Negative Risk |
|------------|----------|----------------|---------------|------------------------|---------------------|
| ATTEMPT-ROLE-A-001 | YES | GATE-PRE-MERGE | G-RULE-003 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-002 | YES | GATE-POST-CHANGE-AUDIT | G-RULE-003 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-003 | YES | GATE-PRE-MERGE | G-RULE-004 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-004 | YES | GATE-PRE-MERGE | G-RULE-005 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-005 | YES | GATE-PRE-MERGE | G-RULE-004 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-006 | YES | GATE-PRE-MERGE | G-RULE-007 | Prohibited Agency | NO |
| ATTEMPT-ROLE-A-007 | YES | GATE-PRE-MERGE | G-RULE-007 | Prohibited Agency | NO |
| ATTEMPT-ROLE-B-001 | YES | GATE-PRE-MERGE | G-RULE-008 | Prohibited Agency | NO |
| ATTEMPT-ROLE-B-002 | YES | GATE-PRE-MERGE | G-RULE-009 | Prohibited Agency | NO |
| ATTEMPT-ROLE-B-003 | YES | GATE-PRE-MERGE | G-RULE-010 | Prohibited Agency | NO |
| ATTEMPT-ROLE-B-004 | YES | GATE-PRE-MERGE | G-RULE-006 | Prohibited Agency | NO |
| ATTEMPT-ROLE-B-005 | YES | GATE-PRE-MERGE | G-RULE-011 | Prohibited Agency | NO |
| ATTEMPT-ROLE-C-001 | YES | GATE-PRE-MERGE | G-RULE-012 | Prohibited Agency | NO |
| ATTEMPT-ROLE-C-002 | YES | GATE-PRE-MERGE | G-RULE-003 | Prohibited Agency | NO |
| ATTEMPT-ROLE-C-003 | YES (PARTIAL) | GATE-PRE-MERGE | G-RULE-006 | Prohibited Agency | YES |

---

## Summary Statistics

**Total Attempts**: 15

**Detected**: 15/15 (100%)

**Not Detected**: 0/15 (0%)

**Detection at GATE-PRE-MERGE**: 14/15 (93%)

**Detection at GATE-POST-CHANGE-AUDIT**: 1/15 (7%)

**False Negative Risk**: 1/15 (7%) - ATTEMPT-ROLE-C-003 (recommendation language "Popular" may not be caught by exact keyword scan)

**Classification as Prohibited Agency**: 15/15 (100%)

---

## Detection Gate Distribution

| Gate | Detection Count | Percentage |
|------|-----------------|------------|
| GATE-PRE-MERGE | 14 | 93% |
| GATE-POST-CHANGE-AUDIT | 1 | 7% |
| GATE-PRE-RELEASE | 0 | 0% |

---

## Violated Rule Distribution

| Rule ID | Violation Count |
|---------|-----------------|
| G-RULE-003 | 3 |
| G-RULE-004 | 2 |
| G-RULE-005 | 1 |
| G-RULE-006 | 2 |
| G-RULE-007 | 2 |
| G-RULE-008 | 1 |
| G-RULE-009 | 1 |
| G-RULE-010 | 1 |
| G-RULE-011 | 1 |
| G-RULE-012 | 1 |

**Total Violations**: 15 (each attempt violates exactly one rule)

---

## No Recommendations

This matrix provides no recommendations.

This matrix provides no explanations.

This matrix states only factual results.

---

**END OF ADVERSARIAL RESULTS MATRIX**

