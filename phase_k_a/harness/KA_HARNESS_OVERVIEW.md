# Phase K-A Experiment Harness Overview

**Document Status**: NON-CANONICAL  
**Document Type**: Harness Overview  
**Date**: 2026-01-10  
**Work Order**: WO-KA-0-AGENCY-VARIABLES-EXPLICITIZATION-AND-EXPERIMENT-HARNESS-BOOTSTRAP

---

## Purpose

This document describes the Phase K-A experiment harness components.

All descriptions are factual. No recommendations. No optimization suggestions.

---

## Harness Components

### Branch Strategy

**Baseline Branch**: `baseline-v1.0` (or equivalent tag/commit)

**Experiment Branches**: `ka-<number>-<variable_id>`

**Branch Isolation**: Each experiment uses separate branch. Baseline branch is never modified.

**Branch Creation**: Experiments create new branches from baseline.

**Branch Cleanup**: Experiment branches may be deleted after rollback or completion.

---

### Build and Launch Commands

**Baseline Build**:
- Command: `cd release/baseline_v1.0 && <baseline_build_command>`
- Purpose: Build baseline system
- Output: Baseline system ready for reference

**Experiment Build**:
- Command: `cd <experiment_branch> && <experiment_build_command>`
- Purpose: Build experiment system
- Output: Experiment system ready for testing

**Baseline Launch**:
- Command: `cd release/baseline_v1.0 && <baseline_launch_command>`
- Purpose: Launch baseline system
- Output: Baseline system running

**Experiment Launch**:
- Command: `cd <experiment_branch> && <experiment_launch_command>`
- Purpose: Launch experiment system
- Output: Experiment system running

---

### Evidence Pack Generation Entry

**Evidence Pack Location**: `audit_evidence/ka_<number>_<variable_id>_<pass|fail>/`

**Evidence Pack Structure**:
- `evidence/design/` - Design artifacts
- `checklist_results/` - Checklist results
- `audit_report.md` - Audit report
- `AUDIT_SUMMARY.md` - Audit summary
- `WORK_ORDER_COMPLETE.md` - Work order completion (for PASS)
- `remediation/` - Remediation log (for FAIL)

**Generation Command**: See `scripts/ka_collect_evidence_skeleton.sh` or command list below.

---

### Diff Audit Entry

**Diff Audit Purpose**: Compare experiment branch against baseline

**Diff Audit Command**: See `scripts/ka_diff_against_baseline.sh` or command list below.

**Diff Audit Output**: 
- File-by-file diff report
- Change summary
- Violation detection (if any)

---

## Scripts and Commands

### Script 1: Create Experiment Branch

**Script**: `scripts/ka_create_experiment_branch.sh`

**Purpose**: Create new experiment branch from baseline

**Actions**:
1. Verify baseline branch/tag exists
2. Create new branch from baseline
3. Switch to new branch
4. Verify branch creation

**No Intelligent Judgment**: Script only creates branch. No automatic fixes.

---

### Script 2: Run Pre-Check

**Script**: `scripts/ka_run_precheck.sh`

**Purpose**: Run pre-check checklist before experiment

**Actions**:
1. Verify baseline reference
2. Verify branch isolation
3. Verify change scope (single variable)
4. Run static scan for prohibited keywords
5. Verify rollback steps exist
6. Verify evidence pack paths exist

**No Intelligent Judgment**: Script only runs checks. No automatic fixes.

---

### Script 3: Collect Evidence Skeleton

**Script**: `scripts/ka_collect_evidence_skeleton.sh`

**Purpose**: Generate empty evidence pack structure

**Actions**:
1. Create evidence pack directory structure
2. Copy evidence templates
3. Create empty checklist results file
4. Create empty audit report file

**No Intelligent Judgment**: Script only creates structure. No content generation.

---

### Script 4: Diff Against Baseline

**Script**: `scripts/ka_diff_against_baseline.sh`

**Purpose**: Generate diff report comparing experiment to baseline

**Actions**:
1. Compare experiment branch to baseline branch
2. Generate file-by-file diff
3. Generate change summary
4. Scan for prohibited keywords in changes

**No Intelligent Judgment**: Script only generates diff. No automatic fixes.

---

### Script 5: Rollback to Baseline

**Script**: `scripts/ka_rollback_to_baseline.sh`

**Purpose**: Rollback experiment branch to baseline state

**Actions**:
1. Switch to baseline branch
2. Verify baseline state
3. Delete experiment branch (optional)
4. Confirm rollback complete

**No Intelligent Judgment**: Script only performs rollback. No state preservation.

---

## Command List (If Scripts Not Allowed)

If repository does not allow scripts, use these commands directly:

### Create Experiment Branch

```bash
# Verify baseline exists
git tag -l | grep baseline-v1.0

# Create and switch to experiment branch
git checkout -b ka-<number>-<variable_id> baseline-v1.0

# Verify branch creation
git branch --show-current
```

### Run Pre-Check

```bash
# Verify baseline reference
git show baseline-v1.0:release/baseline_v1.0/README.md

# Verify branch isolation
git branch --show-current

# Verify change scope (manual review of changes)
git diff baseline-v1.0..HEAD --name-only

# Run static scan for prohibited keywords
grep -r "should\|recommend\|best practice" <experiment_files>

# Verify rollback steps exist (manual check)
# Verify evidence pack paths exist (manual check)
```

### Collect Evidence Skeleton

```bash
# Create evidence pack directory
mkdir -p audit_evidence/ka_<number>_<variable_id>_pass/{evidence/design,checklist_results}
mkdir -p audit_evidence/ka_<number>_<variable_id>_fail/{evidence/design,checklist_results,remediation}

# Copy templates
cp phase_k_a/evidence_templates/pass/* audit_evidence/ka_<number>_<variable_id>_pass/
cp phase_k_a/evidence_templates/fail/* audit_evidence/ka_<number>_<variable_id>_fail/
```

### Diff Against Baseline

```bash
# Generate diff report
git diff baseline-v1.0..HEAD > diff_report.txt

# Generate file-by-file diff
git diff baseline-v1.0..HEAD --name-status > files_changed.txt

# Scan for prohibited keywords
git diff baseline-v1.0..HEAD | grep -i "should\|recommend\|best practice"
```

### Rollback to Baseline

```bash
# Switch to baseline
git checkout baseline-v1.0

# Verify baseline state
git status

# Delete experiment branch (optional)
git branch -D ka-<number>-<variable_id>
```

---

## No Intelligent Judgment

All scripts and commands perform only factual operations:

- Create branches
- Run tests
- Collect logs
- Generate reports
- Generate diffs
- Perform rollback

No scripts perform:
- Intelligent judgment
- Automatic fixes
- Content generation
- Recommendation generation

---

## No Recommendations

This overview provides no recommendations.

This overview provides no optimization suggestions.

This overview states only harness components.

---

**END OF HARNESS OVERVIEW**

