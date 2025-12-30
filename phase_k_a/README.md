# Phase K-A: Controlled Agency Experimentation

**Phase Status**: ACTIVE  
**Phase Type**: Experimental  
**Baseline Reference**: J10 Baseline v1.0 (FROZEN)  
**Start Date**: 2026-01-10

---

## Purpose

Phase K-A establishes controlled agency experimentation infrastructure.

This phase enables systematic injection of agency variables for experimental purposes.

All experiments are conducted on separate branches. Baseline v1.0 remains frozen.

---

## Phase Structure

**Directories**:
- `variables/` - Agency variable taxonomy and definitions
- `experiments/` - Experiment specifications
- `harness/` - Experiment harness and tooling
- `evidence_templates/` - Evidence pack templates
- `checklists/` - Gate checklists
- `reports/` - Work order completion reports

**Key Documents**:
- `KA_INDEX.md` - Phase index and work order registry
- `variables/AGENCY_VARIABLE_TAXONOMY.md` - Variable definitions
- `experiments/EXPERIMENT_SPEC_TEMPLATE.md` - Experiment specification template
- `harness/KA_HARNESS_OVERVIEW.md` - Harness overview
- `checklists/KA0_PRECHECK.md` - Pre-check checklist

---

## Baseline Reference

**Baseline**: J10 Baseline v1.0

**Baseline Location**: `release/baseline_v1.0/`

**Baseline Status**: FROZEN

**Baseline Modification**: NOT PERMITTED

---

## Experiment Principles

**Single Variable Principle**: Each experiment changes only one agency variable (or one explicitly defined minimal combination).

**Rollback Requirement**: All experiments must be rollback-able to baseline.

**Reproducibility Requirement**: All experiments must be reproducible with deterministic steps.

**Auditability Requirement**: All experiments must generate PASS/FAIL evidence packs.

---

## No Modifications to Baseline

All experiments are conducted on separate branches.

Baseline v1.0 files are not modified directly.

All changes are isolated to experiment branches.

---

## Document Status

All Phase K-A documents are NON-CANONICAL.

No CANONICAL documents are created or modified in this phase.

---

**END OF README**

