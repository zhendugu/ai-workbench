# Constitutional Detector Test Examples

**Document Status**: **EXAMPLE** (Non-Canonical)  
**Purpose**: Demonstrates how to test the constitutional diff detector

---

## Test Scenario 1: Unauthorized Constitutional Change (Should Fail)

### Setup

Create a test commit that modifies a constitutional file without authorization:

```bash
# Create a test branch
git checkout -b test-unauthorized-change

# Make a small change to a constitutional file (example: add a comment)
echo "# Test comment" >> docs/CANONICAL_INDEX.md

# Stage the change
git add docs/CANONICAL_INDEX.md

# Attempt commit without authorization (should fail)
git commit -m "Test: unauthorized constitutional change"
```

### Expected Result

The pre-commit hook (if enabled) or the detector script should:
- Exit with non-zero code
- Print error message about missing authorization
- Block the commit

### Verification

```bash
# Run detector manually on staged changes
scripts/constitutional_diff_detect.py

# Expected exit code: 1
# Expected output: ERROR message about missing authorization
```

---

## Test Scenario 2: Authorized Constitutional Change (Should Pass)

### Setup

Create a test commit that modifies a constitutional file WITH authorization:

```bash
# Create a test branch
git checkout -b test-authorized-change

# Make a small change to a constitutional file
echo "# Test comment" >> docs/CANONICAL_INDEX.md

# Stage the change
git add docs/CANONICAL_INDEX.md

# Set required environment variables
export CONSTITUTIONAL_CHANGE_AUTH=YES
export CONSTITUTIONAL_CHANGE_SCOPE="Test: Adding example comment to CANONICAL_INDEX.md"
export CONSTITUTIONAL_CHANGE_RATIONALE="Testing authorized constitutional change detection"

# Attempt commit with authorization (should pass)
git commit -m "Test: authorized constitutional change"
```

### Expected Result

The pre-commit hook (if enabled) or the detector script should:
- Exit with zero code
- Print authorization confirmation
- Allow the commit

### Verification

```bash
# Run detector manually on staged changes with auth vars set
CONSTITUTIONAL_CHANGE_AUTH=YES \
CONSTITUTIONAL_CHANGE_SCOPE="Test scope" \
CONSTITUTIONAL_CHANGE_RATIONALE="Test rationale" \
scripts/constitutional_diff_detect.py

# Expected exit code: 0
# Expected output: Authorization confirmation message
```

---

## Test Scenario 3: Non-Constitutional Change (Should Pass)

### Setup

Create a test commit that modifies a non-constitutional file:

```bash
# Create a test branch
git checkout -b test-non-constitutional-change

# Make a change to a non-constitutional file
echo "# Test comment" >> README.md

# Stage the change
git add README.md

# Attempt commit (should pass, no authorization needed)
git commit -m "Test: non-constitutional change"
```

### Expected Result

The pre-commit hook (if enabled) or the detector script should:
- Exit with zero code
- Not require authorization
- Allow the commit

### Verification

```bash
# Run detector manually on staged changes
scripts/constitutional_diff_detect.py

# Expected exit code: 0
# Expected output: No constitutional files changed
```

---

## Notes

- These are test examples only (non-canonical)
- Do NOT commit test changes to main/master branches
- Clean up test branches after verification
- These examples demonstrate detector behavior only

---

**END OF TEST EXAMPLES**


