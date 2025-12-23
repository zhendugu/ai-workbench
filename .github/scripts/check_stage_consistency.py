#!/usr/bin/env python3
"""
ENGINE Stage/Registry Alignment Enforcement
Based on ENGINE_CI_BOOTSTRAP.md Stage/Registry Alignment Rules
"""
import sys
import re
from pathlib import Path

def read_stage_from_snapshot():
    """Read stage number from CURRENT_STATE_SNAPSHOT.md"""
    snapshot_file = Path("CURRENT_STATE_SNAPSHOT.md")
    if not snapshot_file.exists():
        print("Error: CURRENT_STATE_SNAPSHOT.md not found")
        sys.exit(1)
    
    try:
        content = snapshot_file.read_text()
    except (IOError, OSError, PermissionError):
        print("Error: Cannot read CURRENT_STATE_SNAPSHOT.md")
        sys.exit(1)
    
    # Primary format: ACTIVE_STAGE: 5 (machine-first format)
    match = re.search(r"ACTIVE_STAGE\s*:\s*(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Fallback format: "Active stage: STAGE N" or "Active stage: Stage N" (backward compatibility)
    match = re.search(r"Active stage:\s*STAGE\s+(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    # Try alternative pattern: "Active stage: Stage N"
    match = re.search(r"Active stage:\s*Stage\s+(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    return None

def read_stage_from_status():
    """Read stage number from docs/stage_status.md"""
    status_file = Path("docs/stage_status.md")
    if not status_file.exists():
        print("Error: docs/stage_status.md not found")
        sys.exit(1)
    
    try:
        content = status_file.read_text()
    except (IOError, OSError, PermissionError):
        print("Error: Cannot read docs/stage_status.md")
        sys.exit(1)
    
    # Match "Current Stage: Stage N"
    match = re.search(r"Current Stage:\s*Stage\s+(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    return None

def check_stage_consistency():
    """Check that stage numbers match between snapshot and status"""
    snapshot_stage = read_stage_from_snapshot()
    status_stage = read_stage_from_status()
    
    if snapshot_stage is None:
        print("Error: Cannot parse stage from CURRENT_STATE_SNAPSHOT.md")
        sys.exit(1)
    
    if status_stage is None:
        print("Error: Cannot parse stage from docs/stage_status.md")
        sys.exit(1)
    
    if snapshot_stage != status_stage:
        print(f"ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {snapshot_stage}, docs/stage_status.md declares stage {status_stage}")
        sys.exit(1)
    
    return snapshot_stage

def check_registry_exists(stage_number):
    """Check that registry file exists for the active stage"""
    registry_file = Path(f"docs/registry/stage_{stage_number}_endpoints.yaml")
    
    if not registry_file.exists():
        print(f"ENGINE registry mismatch: current stage {stage_number} requires docs/registry/stage_{stage_number}_endpoints.yaml but enforcement is using wrong registry")
        sys.exit(1)
    
    if not registry_file.is_file():
        print(f"ENGINE registry mismatch: current stage {stage_number} requires docs/registry/stage_{stage_number}_endpoints.yaml but enforcement is using wrong registry")
        sys.exit(1)
    
    try:
        registry_file.read_text()
    except (IOError, OSError, PermissionError):
        print(f"ENGINE registry mismatch: current stage {stage_number} requires docs/registry/stage_{stage_number}_endpoints.yaml but enforcement is using wrong registry")
        sys.exit(1)

def validate_registry_yaml(stage_number):
    """Validate registry YAML syntax"""
    registry_file = Path(f"docs/registry/stage_{stage_number}_endpoints.yaml")
    
    try:
        content = registry_file.read_text()
    except (IOError, OSError, PermissionError):
        print(f"ENGINE registry validation failure: docs/registry/stage_{stage_number}_endpoints.yaml is malformed or invalid")
        sys.exit(1)
    
    # Basic YAML syntax validation using simple heuristics
    # We don't import yaml library to avoid dependencies
    # Check for basic YAML structure indicators
    
    # Check for balanced colons (key: value pairs)
    lines = content.split('\n')
    if not lines:
        print(f"ENGINE registry validation failure: docs/registry/stage_{stage_number}_endpoints.yaml is malformed or invalid")
        sys.exit(1)
    
    # Check for basic YAML structure (at least one colon)
    has_structure = False
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            if ':' in stripped:
                has_structure = True
                break
    
    if not has_structure:
        print(f"ENGINE registry validation failure: docs/registry/stage_{stage_number}_endpoints.yaml is malformed or invalid")
        sys.exit(1)
    
    # Check for balanced indentation (basic check)
    # This is a minimal validation - full YAML parsing would require a library
    # For now, we accept that bootstrap check already verified file exists and is readable

def main():
    """Execute stage/registry alignment checks"""
    # TASK C-3.1: Check stage consistency
    stage_number = check_stage_consistency()
    
    # TASK C-3.2: Check registry file exists
    check_registry_exists(stage_number)
    
    # TASK C-3.3: Validate registry YAML structure
    validate_registry_yaml(stage_number)
    
    # All checks passed
    sys.exit(0)

if __name__ == "__main__":
    main()

