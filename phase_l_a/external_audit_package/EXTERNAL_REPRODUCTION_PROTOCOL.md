# External Reproduction Protocol

**Document Status**: RESEARCH-ONLY / NON-CANONICAL  
**Document Type**: Reproduction Protocol  
**Date**: 2026-01-10  
**Work Order**: WO-LA-0-REPRODUCIBLE-EXTERNAL-AUDIT-PACKAGE  
**Purpose**: Allow third-party independent verification of Phase K conclusions

---

## Purpose

This document describes how third parties can reproduce Phase K experiments and verify conclusions without modifying the system or requiring trust in author intent.

This protocol does not provide design guidance. This protocol does not provide implementation recommendations. This protocol describes only verification procedures.

---

## Reproduction Scope

### Phase K-A Experiments (KA-1 through KA-5)

**Objective**: Verify that agency variables produce measurable effects.

**Reproduction Steps**:

1. **Locate Original Evidence**:
   - KA-1: `audit_evidence/ka_1_default_selection_pass/`
   - KA-2: `audit_evidence/ka_2_visual_highlight_pass/`
   - KA-3: `audit_evidence/ka_3_ordering_pass/`
   - KA-4: `audit_evidence/ka_4_grouping_pass/`
   - KA-5: `audit_evidence/ka_5_proximity_pass/`

2. **Verify Experiment Structure**:
   - Check experiment specification: `phase_k_a/experiments/KA-{N}-{VARIABLE}.md`
   - Check variable injection: `frontend_app/capabilities.html` (search for "KA-{N} EXPERIMENT")
   - Check evidence trace: `audit_evidence/ka_{N}_{variable}_pass/evidence/design/REAL_USE_TRACE.md`
   - Check drift analysis: `audit_evidence/ka_{N}_{variable}_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

3. **Verify Consistency**:
   - Variable injection matches experiment specification
   - Evidence trace matches experiment structure
   - Drift analysis metrics match evidence trace observations
   - Checklist results match experiment constraints

**Verification Criteria**: All files exist. All references are consistent. No contradictions between specification and evidence.

---

### Phase K-B Synthesis (KB-0, KB-1, KB-2)

**Objective**: Verify that agency boundaries are classified and governance rules are defined.

**Reproduction Steps**:

1. **Locate Original Evidence**:
   - KB-0: `phase_k_b/FINAL_KB0_DECISION.md`, `phase_k_b/AGENCY_EFFECT_MATRIX.md`, `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md`
   - KB-1: `phase_k_b/FINAL_KB1_DECISION.md`, `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md`
   - KB-2: `phase_k_b/FINAL_KB2_DECISION.md`, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md`

2. **Verify Synthesis Path**:
   - KB-0: Check that AGENCY_EFFECT_MATRIX.md references KA-1 through KA-5 evidence files
   - KB-0: Check that AGENCY_BOUNDARY_CLASSIFICATION.md maps to AGENCY_EFFECT_MATRIX.md
   - KB-1: Check that DECLARED_AGENCY_PATTERN_CATALOG.md references KA-1 and KA-2 evidence
   - KB-2: Check that AGENCY_GOVERNANCE_RULESET.md references KB-0 boundaries and KB-1 patterns

3. **Verify Traceability**:
   - Each conclusion in FINAL_KB0_DECISION.md cites specific evidence files
   - Each conclusion in FINAL_KB1_DECISION.md cites specific evidence files
   - Each conclusion in FINAL_KB2_DECISION.md cites specific evidence files
   - All cited evidence files exist and are accessible

**Verification Criteria**: All synthesis documents reference Phase K-A evidence. All conclusions are traceable. No orphan conclusions.

---

### Phase K-C-A Adversarial Audit (KC-A-0)

**Objective**: Verify that governance rules block adversarial attempts.

**Reproduction Steps**:

1. **Locate Original Evidence**:
   - Attempt definitions: `phase_k_c/kc_a/ADVERSARIAL_ATTEMPT_SET.md`
   - Gate simulation: `phase_k_c/kc_a/GATE_SIMULATION_AUDIT.md`
   - Results matrix: `phase_k_c/kc_a/ADVERSARIAL_RESULTS_MATRIX.md`
   - Evidence package: `phase_k_c/kc_a/audit_evidence/kc_a_0_adversarial_fail/attempts.json`

2. **Verify Attempt Structure**:
   - Check that all 15 attempts are defined in ADVERSARIAL_ATTEMPT_SET.md
   - Check that all 15 attempts are recorded in attempts.json
   - Check that each attempt has corresponding gate simulation in GATE_SIMULATION_AUDIT.md

3. **Verify Detection Results**:
   - Check that ADVERSARIAL_RESULTS_MATRIX.md lists detection status for all 15 attempts
   - Check that GATE_SIMULATION_AUDIT.md records first blocking point for each attempt
   - Check that detection gate matches results matrix

**Verification Criteria**: All attempts are defined. All attempts have gate simulation. All detection results are consistent. No undetected attempts.

---

### Phase K-C-B Externalization (KC-B-0)

**Objective**: Verify that governance baseline is externalized and frozen.

**Reproduction Steps**:

1. **Locate Original Evidence**:
   - Baseline declaration: `phase_k_c/kc_b/GOVERNANCE_BASELINE_DECLARATION.md`
   - Capability matrix: `phase_k_c/kc_b/GOVERNANCE_CAPABILITY_MATRIX.md`
   - Risk statement: `phase_k_c/kc_b/ACCEPTABLE_RISK_STATEMENT.md`
   - Freeze manifest: `phase_k_c/kc_b/RELEASE_FREEZE_MANIFEST.md`

2. **Verify Externalization**:
   - Check that GOVERNANCE_BASELINE_DECLARATION.md references Phase K-A, K-B, K-C-A evidence
   - Check that GOVERNANCE_CAPABILITY_MATRIX.md lists all capabilities with evidence references
   - Check that ACCEPTABLE_RISK_STATEMENT.md references KC-A-0 evidence
   - Check that RELEASE_FREEZE_MANIFEST.md lists all frozen components

3. **Verify Freeze Status**:
   - Check that RELEASE_FREEZE_MANIFEST.md declares Governance Baseline v1.0 as FROZEN
   - Check that all frozen components are listed with file paths
   - Check that future changes are prohibited without new phase

**Verification Criteria**: All externalization documents reference Phase K evidence. All frozen components are listed. Freeze status is explicit.

---

## Verification Without System Access

**Prerequisite**: Third party has read-only access to repository or evidence bundle.

**Verification Procedure**:

1. **File Existence Check**:
   - Verify all files listed in reproduction steps exist
   - Use hash verification scripts (see AUDIT_VERIFICATION_SCRIPTS/)

2. **Reference Consistency Check**:
   - Verify all file references in synthesis documents point to existing files
   - Verify all evidence citations in decision documents point to existing files
   - Verify no broken references

3. **Traceability Check**:
   - Verify each conclusion in decision documents has evidence citation
   - Verify each evidence citation points to accessible file
   - Verify no orphan conclusions

4. **Structure Integrity Check**:
   - Verify evidence pack structure matches expected format
   - Verify checklist results match expected format
   - Verify no missing required files

**Verification Criteria**: All files exist. All references are valid. All conclusions are traceable. Structure is intact.

---

## No Recommendations

This protocol provides no recommendations.

This protocol provides no design guidance.

This protocol describes only verification procedures.

---

**END OF EXTERNAL REPRODUCTION PROTOCOL**

