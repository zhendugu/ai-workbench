#!/usr/bin/env python3
"""
ENGINE Bootstrap Check
Based on ENGINE_CI_BOOTSTRAP.md Mandatory CI Bootstrap Checks
"""
import sys
import re
from pathlib import Path

def check_file_exists(file_path, error_message):
    """Check if file exists and is readable. Exit with error if not."""
    path = Path(file_path)
    if not path.exists():
        print(error_message)
        sys.exit(1)
    if not path.is_file():
        print(error_message)
        sys.exit(1)
    try:
        path.read_text()
    except (IOError, OSError, PermissionError):
        print(error_message)
        sys.exit(1)

def parse_stage_number():
    """Parse current stage number from docs/stage_status.md"""
    stage_file = Path("docs/stage_status.md")
    if not stage_file.exists():
        print("ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable")
        sys.exit(1)
    
    try:
        content = stage_file.read_text()
    except (IOError, OSError, PermissionError):
        print("ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable")
        sys.exit(1)
    
    # Match "Current Stage: Stage N" or "Current Stage: Stage N.X"
    match = re.search(r"Current Stage:\s*Stage\s+(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    print("ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable")
    sys.exit(1)

def main():
    """Execute all bootstrap checks"""
    
    # CHECK A: File existence (4 base files)
    check_file_exists(
        "CURRENT_STATE_SNAPSHOT.md",
        "ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root"
    )
    
    check_file_exists(
        "docs/ENGINE_HANDOFF_PROMPT.md",
        "ENGINE bootstrap failure: docs/ENGINE_HANDOFF_PROMPT.md missing"
    )
    
    check_file_exists(
        "docs/BLUEPRINT_INTERFACE.md",
        "ENGINE bootstrap failure: docs/BLUEPRINT_INTERFACE.md missing"
    )
    
    check_file_exists(
        "docs/stage_status.md",
        "ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable"
    )
    
    # CHECK B: Stage parsing
    stage_number = parse_stage_number()
    
    # CHECK C: Stage-dependent files
    stage_rule_file = f"docs/STAGE_{stage_number}_CONTROLLED_IMPLEMENTATION.md"
    check_file_exists(
        stage_rule_file,
        f"ENGINE bootstrap failure: docs/STAGE_{stage_number}_CONTROLLED_IMPLEMENTATION.md missing for current stage {stage_number}"
    )
    
    registry_file = f"docs/registry/stage_{stage_number}_endpoints.yaml"
    check_file_exists(
        registry_file,
        f"ENGINE bootstrap failure: docs/registry/stage_{stage_number}_endpoints.yaml missing or unreadable for current stage {stage_number}"
    )
    
    # All checks passed
    print("ENGINE bootstrap checks passed")
    sys.exit(0)

if __name__ == "__main__":
    main()

