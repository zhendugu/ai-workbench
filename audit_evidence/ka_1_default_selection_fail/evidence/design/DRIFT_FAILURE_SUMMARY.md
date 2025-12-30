# Drift Failure Summary - KA-1 DEFAULT_SELECTION Experiment (FAIL)

**Document Status**: AUDIT-EVIDENCE / NON-CANONICAL  
**Document Type**: Drift Failure Summary  
**Date**: 2026-01-10  
**Work Order**: WO-KA-1-SINGLE-VARIABLE-INJECTION-DEFAULT-SELECTION

---

## Purpose

This document summarizes drift failures observed in adversarial DEFAULT_SELECTION patterns.

All analysis is factual. No recommendations.

---

## Failure Patterns

### Single Variable Principle Failures

**Pattern**: Multiple variables injected simultaneously

**Examples**:
- DEFAULT_SELECTION + PREFILL
- DEFAULT_SELECTION + VISUAL_SALIENCE
- DEFAULT_SELECTION + ORDERING_BIAS
- DEFAULT_SELECTION + STATEFUL_MEMORY

**Failure Signal**: Cannot isolate DEFAULT_SELECTION effects from other variables.

---

### Hard Constraint Failures

**Pattern**: DEFAULT_SELECTION combined with prohibited mechanisms

**Examples**:
- Visual emphasis beyond minimal indication
- Text labels suggesting recommendation
- Automatic execution
- Context-based default changes

**Failure Signal**: DEFAULT_SELECTION effects contaminated by other mechanisms.

---

### Scope Violation Failures

**Pattern**: DEFAULT_SELECTION injected outside allowed scope

**Examples**:
- Multiple pages modified
- Backend API modified
- Out-of-scope pages modified

**Failure Signal**: Experiment scope exceeded, baseline contamination risk.

---

## Failure Impact

**Single Variable Isolation**: FAILED - Cannot isolate DEFAULT_SELECTION effects

**Agency Measurement**: FAILED - Cannot measure DEFAULT_SELECTION agency independently

**Baseline Comparison**: FAILED - Cannot compare to baseline (multiple changes)

**Experiment Validity**: FAILED - Experiment does not test single variable

---

## Conclusion

Adversarial patterns demonstrate that DEFAULT_SELECTION must be injected in strict isolation. Any additional mechanisms invalidate the experiment.

**Status**: ❌ FAIL

---

**END OF DRIFT FAILURE SUMMARY**

