# CI Check Scripts

## check_readme_freeze.py

Lightweight CI check script for enforcing "Behavior Semantics Frozen" rules on Subsystem README files.

### Usage

```bash
python3 scripts/check_readme_freeze.py
```

### What It Checks

1. **Forbidden Verbs**: Scans Responsibilities sections for behavioral verbs (Manage, Execute, Implement, etc.)
2. **Conditional Logic**: Checks for conditional patterns (if/when/then/immediately/auto-*)
3. **Execution Context**: Detects execution context terms (runtime/execution/process/flow) in behavioral sense
4. **Non-Responsibility Section**: Verifies presence of "What this subsystem does NOT do" section

### Rules

- Only checks bullet points (lines starting with `-`) in Responsibilities sections
- Excludes noun usage (e.g., "record structure", "trigger conditions")
- Simple text pattern matching only (no semantic inference)

### Exit Codes

- `0`: All checks passed
- `1`: Violations found

### Integration

This script can be integrated into CI/CD pipelines to enforce freeze rules automatically.

See `docs/STAGE_6_CONTROLLED_IMPLEMENTATION.md` for complete freeze rules.

