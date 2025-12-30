# Adversarial Attempt Template

**Document Status**: NON-CANONICAL / ADVERSARIAL-TEST  
**Document Type**: Template Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KC-A-0-ADVERSARIAL-GOVERNANCE-AUDIT-BOOTSTRAP

---

## Purpose

This document defines the unified record format for all adversarial attempts.

All fields are structural. No narrative explanations beyond required fields.

---

## Template Fields

### Field 1: attempt_id

**Type**: String (unique identifier)

**Format**: `ATTEMPT-{ROLE_ID}-{NUMBER}`

**Example**: `ATTEMPT-ROLE-A-001`

**Required**: YES

**Description**: Unique identifier for the adversarial attempt.

---

### Field 2: role_id

**Type**: String (role identifier)

**Format**: Role ID from ADVERSARIAL_ROLE_DEFINITIONS.md

**Example**: `ROLE-A`

**Required**: YES

**Allowed Values**: `ROLE-A`, `ROLE-B`, `ROLE-C`

---

### Field 3: target_rule_ids

**Type**: Array of strings (rule identifiers)

**Format**: Array of G-RULE-IDs that this attempt targets

**Example**: `["G-RULE-001", "G-RULE-003"]`

**Required**: YES

**Allowed Values**: `G-RULE-001` through `G-RULE-012`

---

### Field 4: structural_change_description

**Type**: String (factual description)

**Format**: Factual description of code change

**Example**: "Add selected attribute to first option in dropdown. Add declaration text in primary UI above dropdown."

**Required**: YES

**Description**: Factual description of structural code change. No intent. No justification.

---

### Field 5: rule_compliance_claim

**Type**: String (compliance statement)

**Format**: Statement claiming compliance with specific rules

**Example**: "Claims compliance with G-RULE-001 (includes declaration text) and G-RULE-003 (declaration text in primary UI)."

**Required**: YES

**Description**: Statement explaining why this attempt claims to comply with targeted rules.

---

### Field 6: hidden_agency_hypothesis

**Type**: String (hypothesis statement)

**Format**: Statement of hidden agency effect hypothesis

**Example**: "Declaration text placement may minimize visibility despite being in primary UI. User may not notice declaration text and interpret default selection as recommendation."

**Required**: YES

**Description**: Hypothesis about how agency effect may still occur despite apparent compliance.

---

### Field 7: expected_user_effect

**Type**: String (effect description)

**Format**: Description of expected user behavior effect

**Example**: "Users may accept default selection without noticing declaration text, resulting in 60% acceptance rate similar to KA-1 experiment."

**Required**: YES

**Description**: Expected user behavior effect based on KA experimental results or similar mechanisms.

---

### Field 8: observed_violation

**Type**: Boolean (YES/NO)

**Format**: `YES` or `NO`

**Example**: `YES`

**Required**: YES

**Description**: Whether this attempt violates any G-RULE-* rule.

---

### Field 9: violated_rule_id

**Type**: String or null (rule identifier)

**Format**: G-RULE-ID if violation detected, `null` if no violation

**Example**: `G-RULE-003` or `null`

**Required**: YES (can be null if no violation)

**Allowed Values**: `G-RULE-001` through `G-RULE-012`, or `null`

---

### Field 10: gate_detection_point

**Type**: String (gate identifier)

**Format**: Gate ID where violation was detected, or `NONE` if not detected

**Example**: `GATE-PRE-MERGE` or `GATE-PRE-RELEASE` or `GATE-POST-CHANGE-AUDIT` or `NONE`

**Required**: YES

**Allowed Values**: `GATE-PRE-MERGE`, `GATE-PRE-RELEASE`, `GATE-POST-CHANGE-AUDIT`, `NONE`

---

### Field 11: classification_result

**Type**: String (classification category)

**Format**: Classification category from CHANGE_CLASSIFICATION_MATRIX.md

**Example**: `Prohibited Agency`

**Required**: YES

**Allowed Values**: `Non-Agency`, `Declared Agency`, `Prohibited Agency`

---

### Field 12: evidence_reference

**Type**: String (evidence file path)

**Format**: Path to evidence file or reference to KB/KA evidence

**Example**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Required**: YES

**Description**: Reference to KB-2 rule, KB-1 pattern, or KA experiment evidence.

---

## Template JSON Example

```json
{
  "attempt_id": "ATTEMPT-ROLE-A-001",
  "role_id": "ROLE-A",
  "target_rule_ids": ["G-RULE-001", "G-RULE-003"],
  "structural_change_description": "Add selected attribute to first option in dropdown. Add declaration text in primary UI above dropdown.",
  "rule_compliance_claim": "Claims compliance with G-RULE-001 (includes declaration text) and G-RULE-003 (declaration text in primary UI).",
  "hidden_agency_hypothesis": "Declaration text placement may minimize visibility despite being in primary UI. User may not notice declaration text and interpret default selection as recommendation.",
  "expected_user_effect": "Users may accept default selection without noticing declaration text, resulting in 60% acceptance rate similar to KA-1 experiment.",
  "observed_violation": "YES",
  "violated_rule_id": "G-RULE-003",
  "gate_detection_point": "GATE-PRE-MERGE",
  "classification_result": "Prohibited Agency",
  "evidence_reference": "phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-003, audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md"
}
```

---

## No Recommendations

This template provides no recommendations.

This template provides no design advice.

This template states only template field specifications.

---

**END OF ADVERSARIAL ATTEMPT TEMPLATE**

