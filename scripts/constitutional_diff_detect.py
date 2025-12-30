#!/usr/bin/env python3
"""
Constitutional Diff Detector

Detects if any constitutional files have been modified in a git diff range.
Requires explicit human authorization via environment variables if constitutional files are changed.

Exit codes:
- 0: No constitutional files changed, or authorized change detected
- 1: Constitutional files changed without authorization
- 2: Error in script execution
"""

import os
import sys
import subprocess
from pathlib import Path

# Constitutional fileset (from CONSTITUTIONAL_FILESET.md)
CONSTITUTIONAL_FILES = [
    "docs/IMMUTABLE_DESIGN_CONSTRAINTS.md",
    "docs/PATTERN_METHODOLOGY_ONTOLOGY.md",
    "docs/CAPABILITY_ONTOLOGY.md",
    "docs/AUDIT_EVIDENCE_ONTOLOGY.md",
    "docs/AUTHORIZATION_GOVERNANCE_ONTOLOGY.md",
    "docs/PATTERN_INSTANCE_SCHEMA.md",
    "docs/PATTERN_REGISTRY_ONTOLOGY.md",
    "docs/PATTERN_REGISTRY_LIFECYCLE_RULES.md",
    "docs/PATTERN_CAPABILITY_USAGE_CONSTRAINTS.md",
    "docs/PATTERN_REGISTRY_AUDIT_TRACEABILITY.md",
    "docs/HUMAN_DECISION_SELECTION_BOUNDARY.md",
    "docs/CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md",
    "docs/CONSTITUTIONAL_AUDIT_RUNBOOK.md",
    "docs/CONSTITUTIONAL_FREEZE_POLICY.md",
    "docs/CONSTITUTIONAL_MODIFICATION_GATE.md",
    "docs/CONSTITUTIONAL_FULL_AUDIT_REQUIREMENT.md",
    "docs/CONSTITUTIONAL_TAMPER_DETECTION.md",
    "docs/CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md",
    "docs/CANONICAL_INDEX.md",
    "docs/CONSTITUTIONAL_FILESET.md",
    "docs/CONSTITUTIONAL_ENFORCEMENT_POLICY.md",
    "docs/COMPLIANCE_AUDIT_REPORT_TEMPLATE.md",
    "docs/COMPLIANCE_EVIDENCE_PACK_GUIDE.md",
]

# Required environment variables for authorization
REQUIRED_AUTH_VARS = [
    "CONSTITUTIONAL_CHANGE_AUTH",
    "CONSTITUTIONAL_CHANGE_SCOPE",
    "CONSTITUTIONAL_CHANGE_RATIONALE",
]


def get_git_diff_files(diff_range=None):
    """
    Get list of changed files from git diff.
    
    Args:
        diff_range: Git diff range (e.g., "HEAD~1..HEAD" or None for staged changes)
    
    Returns:
        List of changed file paths, or None on error
    """
    try:
        if diff_range:
            cmd = ["git", "diff", "--name-only", diff_range]
        else:
            cmd = ["git", "diff", "--name-only", "--cached"]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            cwd=Path(__file__).parent.parent
        )
        
        files = [f.strip() for f in result.stdout.split("\n") if f.strip()]
        return files
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def check_authorization():
    """
    Check if required authorization environment variables are set.
    
    Returns:
        Tuple (is_authorized: bool, missing_vars: list)
    """
    missing_vars = []
    
    for var in REQUIRED_AUTH_VARS:
        value = os.environ.get(var)
        if not value or not value.strip():
            missing_vars.append(var)
    
    if missing_vars:
        return False, missing_vars
    
    # Verify AUTH is explicitly "YES"
    auth_value = os.environ.get("CONSTITUTIONAL_CHANGE_AUTH", "").strip()
    if auth_value != "YES":
        missing_vars.append("CONSTITUTIONAL_CHANGE_AUTH (must be 'YES')")
        return False, missing_vars
    
    return True, []


def main():
    """
    Main detection logic.
    """
    # Get diff range from environment or command line
    diff_range = os.environ.get("GIT_DIFF_RANGE")
    if not diff_range and len(sys.argv) > 1:
        diff_range = sys.argv[1]
    
    # Get changed files
    changed_files = get_git_diff_files(diff_range)
    if changed_files is None:
        sys.exit(2)
    
    # Check if any constitutional files are changed
    constitutional_changes = []
    for file_path in changed_files:
        if file_path in CONSTITUTIONAL_FILES:
            constitutional_changes.append(file_path)
    
    # If no constitutional files changed, exit successfully
    if not constitutional_changes:
        sys.exit(0)
    
    # Constitutional files changed - check authorization
    is_authorized, missing_vars = check_authorization()
    
    if is_authorized:
        # Authorized change - log and exit successfully
        print("Constitutional files changed with explicit authorization:", file=sys.stderr)
        for file_path in constitutional_changes:
            print(f"  - {file_path}", file=sys.stderr)
        print(f"\nScope: {os.environ.get('CONSTITUTIONAL_CHANGE_SCOPE')}", file=sys.stderr)
        print(f"Rationale: {os.environ.get('CONSTITUTIONAL_CHANGE_RATIONALE')}", file=sys.stderr)
        sys.exit(0)
    
    # Unauthorized change - fail
    print("ERROR: Constitutional files changed without explicit authorization!", file=sys.stderr)
    print("\nChanged constitutional files:", file=sys.stderr)
    for file_path in constitutional_changes:
        print(f"  - {file_path}", file=sys.stderr)
    
    print("\nRequired environment variables:", file=sys.stderr)
    print("  CONSTITUTIONAL_CHANGE_AUTH=YES", file=sys.stderr)
    print("  CONSTITUTIONAL_CHANGE_SCOPE=<free text>", file=sys.stderr)
    print("  CONSTITUTIONAL_CHANGE_RATIONALE=<free text>", file=sys.stderr)
    
    if missing_vars:
        print("\nMissing or invalid variables:", file=sys.stderr)
        for var in missing_vars:
            print(f"  - {var}", file=sys.stderr)
    
    print("\nSee docs/CONSTITUTIONAL_ENFORCEMENT_POLICY.md for details.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()


