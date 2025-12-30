# Frontend Pre-Generation Checklist

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Pre-Generation Gate Checklist  
**Date**: 2025-12-27  
**Work Order**: WO-J2-FRONTEND-CONSTRAINT-TRANSLATION-AND-GENERATION-GATE

---

## Purpose

This checklist must be executed BEFORE:
- Calling V0 for frontend generation
- Starting frontend implementation
- Creating any frontend code

Any FAIL must block entry into frontend generation phase.

---

## Section 1: Constitutional Compliance Verification

### 1.1 Frontend Role Boundary

- [ ] **Check 1.1.1**: Frontend role is defined as "presentation layer / operation mapping layer" only
- [ ] **Check 1.1.2**: Frontend does NOT possess agency
- [ ] **Check 1.1.3**: Frontend does NOT make judgments
- [ ] **Check 1.1.4**: Frontend does NOT form preferences
- [ ] **Check 1.1.5**: Frontend does NOT hold state
- [ ] **Check 1.1.6**: Frontend does NOT predict
- [ ] **Check 1.1.7**: Frontend does NOT recommend

### 1.2 Explicit Prohibitions

- [ ] **Check 1.2.1**: No pre-selection of options
- [ ] **Check 1.2.2**: No highlighting of options
- [ ] **Check 1.2.3**: No ordering by usage, frequency, popularity, or recency
- [ ] **Check 1.2.4**: No defaults
- [ ] **Check 1.2.5**: No state memory
- [ ] **Check 1.2.6**: No optimization
- [ ] **Check 1.2.7**: No learning
- [ ] **Check 1.2.8**: No prediction
- [ ] **Check 1.2.9**: No merging
- [ ] **Check 1.2.10**: No abstraction

---

## Section 2: Generation Constraint Verification

### 2.1 Selection Constraints

- [ ] **Check 2.1.1**: No pre-selection of capabilities
- [ ] **Check 2.1.2**: No pre-selection of pattern instances
- [ ] **Check 2.1.3**: No pre-selection of registry entries
- [ ] **Check 2.1.4**: No pre-selection of form fields
- [ ] **Check 2.1.5**: No pre-selection of navigation targets
- [ ] **Check 2.1.6**: No pre-selection of tabs
- [ ] **Check 2.1.7**: No pre-selection of panels
- [ ] **Check 2.1.8**: No pre-selection of categories

### 2.2 Highlighting Constraints

- [ ] **Check 2.2.1**: No highlighting of capabilities
- [ ] **Check 2.2.2**: No highlighting of pattern instances
- [ ] **Check 2.2.3**: No badges, icons, or markers
- [ ] **Check 2.2.4**: No labels such as "popular", "frequently used", "common"
- [ ] **Check 2.2.5**: No visual emphasis that implies preference

### 2.3 Ordering Constraints

- [ ] **Check 2.3.1**: No ordering by usage frequency
- [ ] **Check 2.3.2**: No ordering by popularity
- [ ] **Check 2.3.3**: No ordering by recency
- [ ] **Check 2.3.4**: No sorting by relevance, popularity, or frequency
- [ ] **Check 2.3.5**: Display in registration order only

### 2.4 Process Guidance Constraints

- [ ] **Check 2.4.1**: No wizard flows
- [ ] **Check 2.4.2**: No step-by-step guidance
- [ ] **Check 2.4.3**: No progress indicators
- [ ] **Check 2.4.4**: No "next step" suggestions
- [ ] **Check 2.4.5**: No workflow templates

### 2.5 State Memory Constraints

- [ ] **Check 2.5.1**: No memory of previous selections
- [ ] **Check 2.5.2**: No memory of previous usage
- [ ] **Check 2.5.3**: No state persistence across sessions
- [ ] **Check 2.5.4**: No state accumulation over time

### 2.6 Usage-Based Display Constraints

- [ ] **Check 2.6.1**: No "commonly used" lists
- [ ] **Check 2.6.2**: No "recently used" lists
- [ ] **Check 2.6.3**: No usage frequency tracking
- [ ] **Check 2.6.4**: No recency tracking
- [ ] **Check 2.6.5**: No popularity tracking

### 2.7 Template/Shortcut Constraints

- [ ] **Check 2.7.1**: No template buttons
- [ ] **Check 2.7.2**: No shortcut buttons
- [ ] **Check 2.7.3**: No "quick access" panels
- [ ] **Check 2.7.4**: No pre-configured combinations

### 2.8 Auto-Complete Constraints

- [ ] **Check 2.8.1**: No auto-complete input fields
- [ ] **Check 2.8.2**: No suggestion dropdowns
- [ ] **Check 2.8.3**: No ranked suggestions
- [ ] **Check 2.8.4**: No pre-highlighted suggestions

### 2.9 Search Constraints

- [ ] **Check 2.9.1**: No ranking of search results
- [ ] **Check 2.9.2**: No ordering by relevance or popularity
- [ ] **Check 2.9.3**: No highlighting of top results

### 2.10 Organization Constraints

- [ ] **Check 2.10.1**: No category organization with defaults
- [ ] **Check 2.10.2**: No tab organization with defaults
- [ ] **Check 2.10.3**: No filter presets

### 2.11 Progressive Disclosure Constraints

- [ ] **Check 2.11.1**: No hiding options initially
- [ ] **Check 2.11.2**: No progressive revelation
- [ ] **Check 2.11.3**: No "show more" mechanisms

### 2.12 Smart Defaults Constraints

- [ ] **Check 2.12.1**: No pre-filling form fields
- [ ] **Check 2.12.2**: No smart defaults based on context
- [ ] **Check 2.12.3**: No smart defaults based on history

---

## Section 3: V0 Input Template Verification

### 3.1 Template Usage

- [ ] **Check 3.1.1**: V0 input includes CONSTITUTIONAL CONSTRAINTS section
- [ ] **Check 3.1.2**: V0 input includes EXPLICIT PROHIBITIONS section
- [ ] **Check 3.1.3**: V0 input includes REQUIRED BEHAVIOR section
- [ ] **Check 3.1.4**: V0 input includes CONSTITUTIONAL COMPLIANCE VERIFICATION

### 3.2 Template Completeness

- [ ] **Check 3.2.1**: All mandatory sections present
- [ ] **Check 3.2.2**: No modifications to constraint sections
- [ ] **Check 3.2.3**: Template copied in full

---

## Section 4: Implementation Rules Verification

### 4.1 Code Prohibitions

- [ ] **Check 4.1.1**: No selection code will be written
- [ ] **Check 4.1.2**: No recommendation code will be written
- [ ] **Check 4.1.3**: No default code will be written
- [ ] **Check 4.1.4**: No ordering code will be written
- [ ] **Check 4.1.5**: No process guidance code will be written
- [ ] **Check 4.1.6**: No state memory code will be written
- [ ] **Check 4.1.7**: No optimization code will be written
- [ ] **Check 4.1.8**: No learning code will be written
- [ ] **Check 4.1.9**: No prediction code will be written
- [ ] **Check 4.1.10**: No merging code will be written
- [ ] **Check 4.1.11**: No abstraction code will be written
- [ ] **Check 4.1.12**: No behavior inference code will be written
- [ ] **Check 4.1.13**: No decision space compression code will be written
- [ ] **Check 4.1.14**: No usage-based display code will be written
- [ ] **Check 4.1.15**: No template/shortcut code will be written
- [ ] **Check 4.1.16**: No auto-complete code will be written
- [ ] **Check 4.1.17**: No search ranking code will be written
- [ ] **Check 4.1.18**: No category organization code will be written
- [ ] **Check 4.1.19**: No tab organization code will be written
- [ ] **Check 4.1.20**: No filter preset code will be written
- [ ] **Check 4.1.21**: No state persistence code will be written
- [ ] **Check 4.1.22**: No contextual help code will be written
- [ ] **Check 4.1.23**: No progressive disclosure code will be written
- [ ] **Check 4.1.24**: No smart defaults code will be written
- [ ] **Check 4.1.25**: No multi-step form code will be written

---

## Gate Decision

### Pre-Generation Gate

**If ALL checks PASS**: ✅ Proceed to frontend generation  
**If ANY check FAILS**: ❌ BLOCK frontend generation

**Gate Authority**: This checklist is the final gate before frontend generation.

**No Exceptions**: Any FAIL blocks entry into frontend generation phase.

---

## Summary

**Total Check Items**: 65  
**Required Pass Rate**: 100%  
**Gate Function**: Block entry if ANY check fails

**Check Categories**:
- Constitutional Compliance: 17 checks
- Generation Constraints: 35 checks
- V0 Input Template: 4 checks
- Implementation Rules: 25 checks

**All checks must PASS before frontend generation can proceed.**

---

**END OF FRONTEND PRE-GENERATION CHECKLIST**

