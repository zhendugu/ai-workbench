#!/usr/bin/env python3
"""
ENGINE_VERSION Value Allowlist Gate
Based on ENGINE_VERSION_DECLARATION_SPEC.md
Validates ENGINE_VERSION value against hardcoded allowlist.
Does NOT interpret version semantics or trigger upgrades.
"""
import sys
import re
from pathlib import Path

# Hardcoded allowlist of valid ENGINE_VERSION values
ALLOWED_VERSIONS = ["v1"]

def check_engine_version_value():
    """Check that ENGINE_VERSION value is in the allowlist"""
    snapshot_file = Path("CURRENT_STATE_SNAPSHOT.md")
    
    if not snapshot_file.exists():
        # Presence check is handled by B-B gate, not this gate
        # If file doesn't exist, we can't check value - exit silently
        # (presence gate will catch this)
        sys.exit(0)
    
    try:
        content = snapshot_file.read_text()
    except (IOError, OSError, PermissionError):
        # Presence check is handled by B-B gate, not this gate
        # If file can't be read, we can't check value - exit silently
        # (presence gate will catch this)
        sys.exit(0)
    
    # Extract ENGINE_VERSION value
    # Match patterns like:
    # ENGINE_VERSION: v1
    # ENGINE_VERSION: v2
    # ENGINE_VERSION:v1
    # ENGINE_VERSION = v1
    pattern = r'ENGINE_VERSION\s*[:=]\s*(v\d+)'
    match = re.search(pattern, content, re.IGNORECASE)
    
    if not match:
        # Presence check is handled by B-B gate, not this gate
        # If field doesn't exist, we can't check value - exit silently
        # (presence gate will catch this)
        sys.exit(0)
    
    version_value = match.group(1).lower()  # Normalize to lowercase
    
    # Check if value is in allowlist
    if version_value not in ALLOWED_VERSIONS:
        print(f"ENGINE_VERSION value is invalid or unsupported: {version_value}")
        sys.exit(1)
    
    # Value is valid - pass (no output)
    sys.exit(0)

if __name__ == "__main__":
    check_engine_version_value()

