# K-A Pre-Check Checklist (Gate 0)

**Document Status**: NON-CANONICAL  
**Document Type**: Pre-Check Checklist  
**Date**: 2026-01-10  
**Work Order**: WO-KA-0-AGENCY-VARIABLES-EXPLICITIZATION-AND-EXPERIMENT-HARNESS-BOOTSTRAP

---

## Purpose

This checklist verifies experiment readiness before agency variable injection.

All checks must PASS before proceeding to experiment execution.

Any FAIL blocks entry to KA-1.

---

## Section 1: Baseline Reference Correctness (20 checks)

### Baseline Existence

- [ ] **Check 1.1**: Baseline reference (baseline-v1.0 or equivalent) exists
- [ ] **Check 1.2**: Baseline reference is accessible
- [ ] **Check 1.3**: Baseline reference points to J10 Baseline v1.0
- [ ] **Check 1.4**: Baseline directory (release/baseline_v1.0/) exists
- [ ] **Check 1.5**: Baseline documentation (BASELINE_RELEASE_DECLARATION.md) exists

### Baseline Integrity

- [ ] **Check 1.6**: Baseline files are not modified
- [ ] **Check 1.7**: Baseline frontend pages (4 pages) are intact
- [ ] **Check 1.8**: Baseline allowlist items (5 items) are documented
- [ ] **Check 1.9**: Baseline denylist items (33 items) are documented
- [ ] **Check 1.10**: Baseline backend API endpoints (3 endpoints) are documented

### Baseline Reference in Experiment Spec

- [ ] **Check 1.11**: Experiment spec contains baseline_ref field
- [ ] **Check 1.12**: baseline_ref field references correct baseline
- [ ] **Check 1.13**: baseline_ref format is valid (tag/commit/path)
- [ ] **Check 1.14**: Baseline reference is accessible from experiment branch
- [ ] **Check 1.15**: Baseline reference matches J10 Baseline v1.0

### Baseline Verification

- [ ] **Check 1.16**: Baseline can be checked out
- [ ] **Check 1.17**: Baseline builds successfully
- [ ] **Check 1.18**: Baseline launches successfully
- [ ] **Check 1.19**: Baseline behavior matches J10 specification
- [ ] **Check 1.20**: Baseline constraints are documented

---

## Section 2: Branch Isolation (20 checks)

### Branch Creation

- [ ] **Check 2.1**: Experiment branch name follows format: ka-<number>-<variable_id>
- [ ] **Check 2.2**: Experiment branch is created from baseline
- [ ] **Check 2.3**: Experiment branch is separate from baseline branch
- [ ] **Check 2.4**: Experiment branch does not modify baseline branch
- [ ] **Check 2.5**: Experiment branch is checked out

### Branch Isolation Verification

- [ ] **Check 2.6**: Current branch is experiment branch (not baseline)
- [ ] **Check 2.7**: Baseline branch is not modified
- [ ] **Check 2.8**: Experiment changes are isolated to experiment branch
- [ ] **Check 2.9**: No baseline files are directly modified
- [ ] **Check 2.10**: Baseline reference remains unchanged

### Branch Naming

- [ ] **Check 2.11**: Branch name matches experiment_id
- [ ] **Check 2.12**: Branch name is unique (not conflicting)
- [ ] **Check 2.13**: Branch name contains variable_id
- [ ] **Check 2.14**: Branch name follows naming convention
- [ ] **Check 2.15**: Branch name is documented in experiment spec

### Branch State

- [ ] **Check 2.16**: Branch is clean (no uncommitted changes) or changes are intentional
- [ ] **Check 2.17**: Branch is up to date with baseline
- [ ] **Check 2.18**: Branch can be rolled back to baseline
- [ ] **Check 2.19**: Branch isolation is maintained
- [ ] **Check 2.20**: No baseline contamination in experiment branch

---

## Section 3: Change Scope Limitation (20 checks)

### Single Variable Principle

- [ ] **Check 3.1**: Experiment spec contains variable_id field
- [ ] **Check 3.2**: Only one variable_id is specified (or explicit minimal combination)
- [ ] **Check 3.3**: Variable_id matches AGENCY_VARIABLE_TAXONOMY.md definition
- [ ] **Check 3.4**: Variable_id is valid (exists in taxonomy)
- [ ] **Check 3.5**: If multiple variables, explicit justification provided

### Change Scope Verification

- [ ] **Check 3.6**: Only one variable is injected
- [ ] **Check 3.7**: Changes are limited to variable injection
- [ ] **Check 3.8**: No additional features are introduced
- [ ] **Check 3.9**: No UX optimizations are introduced
- [ ] **Check 3.10**: No unrelated changes are included

### Files Modified

- [ ] **Check 3.11**: Experiment spec lists files_modified
- [ ] **Check 3.12**: Files modified are minimal (only necessary for variable injection)
- [ ] **Check 3.13**: No baseline files are modified directly
- [ ] **Check 3.14**: Modified files are documented
- [ ] **Check 3.15**: File modifications are limited to variable injection

### Code Changes

- [ ] **Check 3.16**: code_changes_summary is factual (no recommendations)
- [ ] **Check 3.17**: Code changes are limited to variable injection
- [ ] **Check 3.18**: No prohibited mechanisms are introduced
- [ ] **Check 3.19**: Changes match variable definition
- [ ] **Check 3.20**: Change scope is verifiable

---

## Section 4: Frontend Non-Agency Constraint Inheritance (20 checks)

### J2 Constraint References

- [ ] **Check 4.1**: J2 constraints (25 constraints) are referenced (not restated)
- [ ] **Check 4.2**: J2 constraints remain in effect
- [ ] **Check 4.3**: No J2 constraints are violated
- [ ] **Check 4.4**: J2 constraint violations are checked
- [ ] **Check 4.5**: J2 constraint compliance is verified

### J4 Denylist References

- [ ] **Check 4.6**: J4 denylist (33 items) is referenced (not restated)
- [ ] **Check 4.7**: J4 denylist items remain prohibited
- [ ] **Check 4.8**: No J4 denylist items are introduced
- [ ] **Check 4.9**: J4 denylist compliance is checked
- [ ] **Check 4.10**: J4 denylist violations are detected

### J10 Freeze Declaration References

- [ ] **Check 4.11**: J10 freeze declaration is referenced (not restated)
- [ ] **Check 4.12**: J10 freeze constraints are maintained
- [ ] **Check 4.13**: No J10 freeze violations
- [ ] **Check 4.14**: J10 allowlist items (5 items) are referenced
- [ ] **Check 4.15**: J10 allowlist boundaries are respected

### Frontend Constraint Verification

- [ ] **Check 4.16**: Frontend non-agency constraints are inherited
- [ ] **Check 4.17**: Frontend constraints are not restated
- [ ] **Check 4.18**: Frontend constraint compliance is verified
- [ ] **Check 4.19**: Frontend constraint violations are checked
- [ ] **Check 4.20**: Frontend behavior remains non-agentic (except injected variable)

---

## Section 5: Backend API Neutrality Requirement Inheritance (15 checks)

### J7 Neutrality References

- [ ] **Check 5.1**: J7 neutrality requirements are referenced (not restated)
- [ ] **Check 5.2**: J7 neutrality requirements remain in effect
- [ ] **Check 5.3**: No J7 neutrality violations
- [ ] **Check 5.4**: J7 neutrality compliance is checked
- [ ] **Check 5.5**: J7 neutrality violations are detected

### J10 Backend API Freeze References

- [ ] **Check 5.6**: J10 backend API freeze is referenced (not restated)
- [ ] **Check 5.7**: J10 backend API endpoints (3 endpoints) are referenced
- [ ] **Check 5.8**: J10 backend API usage is maintained
- [ ] **Check 5.9**: No J10 backend API violations
- [ ] **Check 5.10**: J10 backend API compliance is verified

### Backend API Neutrality Verification

- [ ] **Check 5.11**: Backend API neutrality is maintained
- [ ] **Check 5.12**: Backend responses are displayed verbatim
- [ ] **Check 5.13**: No backend response interpretation
- [ ] **Check 5.14**: Backend API neutrality compliance is checked
- [ ] **Check 5.15**: Backend API neutrality violations are detected

---

## Section 6: Prohibited Mechanism Static Scan (15 checks)

### Prohibited Keyword Scan

- [ ] **Check 6.1**: Static scan for "should" keyword
- [ ] **Check 6.2**: Static scan for "recommend" keyword
- [ ] **Check 6.3**: Static scan for "best practice" keyword
- [ ] **Check 6.4**: Static scan for "default" keyword (in selection context)
- [ ] **Check 6.5**: Static scan for "pre-fill" keyword

### Prohibited Mechanism Scan

- [ ] **Check 6.6**: Static scan for automatic retry mechanisms
- [ ] **Check 6.7**: Static scan for caching mechanisms
- [ ] **Check 6.8**: Static scan for fallback mechanisms
- [ ] **Check 6.9**: Static scan for recommendation mechanisms
- [ ] **Check 6.10**: Static scan for workflow mechanisms

### Prohibited Pattern Scan

- [ ] **Check 6.11**: Static scan for state memory patterns
- [ ] **Check 6.12**: Static scan for sorting preference patterns
- [ ] **Check 6.13**: Static scan for highlighting patterns
- [ ] **Check 6.14**: Static scan for process guidance patterns
- [ ] **Check 6.15**: No prohibited mechanisms detected

---

## Section 7: Rollback and Reproduction Steps Completeness (15 checks)

### Rollback Steps

- [ ] **Check 7.1**: Experiment spec contains rollback_steps field
- [ ] **Check 7.2**: rollback_steps are deterministic
- [ ] **Check 7.3**: rollback_steps are complete
- [ ] **Check 7.4**: rollback_steps can restore baseline state
- [ ] **Check 7.5**: rollback_steps are testable

### Reproduction Steps

- [ ] **Check 7.6**: Experiment spec contains reproduction_steps field
- [ ] **Check 7.7**: reproduction_steps are deterministic
- [ ] **Check 7.8**: reproduction_steps are complete
- [ ] **Check 7.9**: reproduction_steps can reproduce experiment
- [ ] **Check 7.10**: reproduction_steps are testable

### Step Verification

- [ ] **Check 7.11**: Rollback steps are verified (tested)
- [ ] **Check 7.12**: Reproduction steps are verified (tested)
- [ ] **Check 7.13**: Steps are documented clearly
- [ ] **Check 7.14**: Steps are executable
- [ ] **Check 7.15**: Steps completeness is verified

---

## Section 8: Evidence Pack Path Existence and Naming (15 checks)

### Evidence Pack Paths

- [ ] **Check 8.1**: Experiment spec contains evidence_pack_paths field
- [ ] **Check 8.2**: PASS evidence pack path is specified
- [ ] **Check 8.3**: FAIL evidence pack path is specified
- [ ] **Check 8.4**: Evidence pack paths follow naming convention
- [ ] **Check 8.5**: Evidence pack paths are valid

### Evidence Pack Structure

- [ ] **Check 8.6**: PASS evidence pack directory structure exists
- [ ] **Check 8.7**: FAIL evidence pack directory structure exists
- [ ] **Check 8.8**: Evidence pack templates are available
- [ ] **Check 8.9**: Evidence pack structure matches template
- [ ] **Check 8.10**: Evidence pack paths are accessible

### Naming Convention

- [ ] **Check 8.11**: Evidence pack names follow format: ka_<number>_<variable_id>_<pass|fail>
- [ ] **Check 8.12**: Evidence pack names match experiment_id
- [ ] **Check 8.13**: Evidence pack names are unique
- [ ] **Check 8.14**: Evidence pack naming is consistent
- [ ] **Check 8.15**: Evidence pack naming is documented

---

## Summary

**Total Checks**: 120

**Required Pass Rate**: 100%

**Any FAIL**: Blocks entry to KA-1

---

## No Recommendations

This checklist provides no recommendations.

This checklist provides no optimization suggestions.

This checklist states only verification requirements.

---

**END OF K-A PRE-CHECK CHECKLIST**

