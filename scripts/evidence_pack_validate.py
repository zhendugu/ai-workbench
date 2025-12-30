#!/usr/bin/env python3
"""
Evidence Pack Structure Validator

Validates the directory structure and required filenames for audit_evidence/*/
Must match COMPLIANCE_EVIDENCE_PACK_GUIDE.md structure.

This validator checks ONLY structure, NOT content, quality, or completeness.

Exit codes:
- 0: All evidence packs have valid structure
- 1: Structural violations found
- 2: Error in script execution
"""

import os
import sys
from pathlib import Path

# Required directory structure (from COMPLIANCE_EVIDENCE_PACK_GUIDE.md)
# Only top-level required directories are checked
# Subdirectories under evidence/ are optional (code, documentation, design)
REQUIRED_DIRS = [
    "evidence",
    "checklist_results",
    "remediation",
]

# Required files (at least one must exist)
REQUIRED_FILES = [
    "audit_report.md",
    "checklist_results/checklist_results.md",
    "remediation/remediation_log.md",
]

# Optional but common files
OPTIONAL_FILES = [
    "AUDIT_SUMMARY.md",
    "ADVERSARIAL_AUDIT_SUMMARY.md",
]


def validate_evidence_pack(pack_path):
    """
    Validate a single evidence pack structure.
    
    Args:
        pack_path: Path to evidence pack directory
    
    Returns:
        Tuple (is_valid: bool, violations: list)
    """
    violations = []
    pack_path = Path(pack_path)
    
    if not pack_path.is_dir():
        violations.append(f"{pack_path}: Not a directory")
        return False, violations
    
    # Check required directories
    for req_dir in REQUIRED_DIRS:
        dir_path = pack_path / req_dir
        if not dir_path.is_dir():
            violations.append(f"{pack_path}: Missing required directory '{req_dir}'")
    
    # Check required files
    for req_file in REQUIRED_FILES:
        file_path = pack_path / req_file
        if not file_path.is_file():
            violations.append(f"{pack_path}: Missing required file '{req_file}'")
    
    # Check that evidence directory exists and has at least one subdirectory or file
    evidence_path = pack_path / "evidence"
    if evidence_path.is_dir():
        items = list(evidence_path.iterdir())
        if not items:
            violations.append(f"{pack_path}: 'evidence' directory is empty (should contain at least code/, documentation/, or design/ subdirectory)")
    
    is_valid = len(violations) == 0
    return is_valid, violations


def find_evidence_packs(base_path):
    """
    Find all evidence pack directories.
    
    Args:
        base_path: Base path to search from
    
    Returns:
        List of evidence pack paths
    """
    base_path = Path(base_path)
    evidence_base = base_path / "audit_evidence"
    
    if not evidence_base.is_dir():
        return []
    
    packs = []
    for item in evidence_base.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            packs.append(item)
    
    return packs


def main():
    """
    Main validation logic.
    """
    # Get base path (repository root)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Find all evidence packs
    evidence_packs = find_evidence_packs(repo_root)
    
    if not evidence_packs:
        # No evidence packs found - this is OK
        sys.exit(0)
    
    # Validate each pack
    all_violations = []
    for pack_path in evidence_packs:
        is_valid, violations = validate_evidence_pack(pack_path)
        if not is_valid:
            all_violations.extend(violations)
    
    # Report results
    if all_violations:
        print("ERROR: Evidence pack structure violations found:", file=sys.stderr)
        for violation in all_violations:
            print(f"  - {violation}", file=sys.stderr)
        print("\nSee docs/COMPLIANCE_EVIDENCE_PACK_GUIDE.md for required structure.", file=sys.stderr)
        sys.exit(1)
    
    # All packs valid
    print(f"Validated {len(evidence_packs)} evidence pack(s): All structures valid.", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()


