#!/usr/bin/env python3
"""
ENGINE_VERSION Presence Gate
Based on ENGINE_VERSION_DECLARATION_SPEC.md
Checks only for field existence, not value validation.
"""
import sys
import re
from pathlib import Path

def check_engine_version_presence():
    """Check that ENGINE_VERSION field exists in CURRENT_STATE_SNAPSHOT.md"""
    snapshot_file = Path("CURRENT_STATE_SNAPSHOT.md")
    
    if not snapshot_file.exists():
        print("ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md")
        sys.exit(1)
    
    try:
        content = snapshot_file.read_text()
    except (IOError, OSError, PermissionError):
        print("ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md")
        sys.exit(1)
    
    # Check for ENGINE_VERSION field (case-insensitive, flexible whitespace)
    # Match patterns like:
    # ENGINE_VERSION: v1
    # ENGINE_VERSION: v2
    # ENGINE_VERSION:v1
    # ENGINE_VERSION = v1
    pattern = r'ENGINE_VERSION\s*[:=]\s*v\d+'
    match = re.search(pattern, content, re.IGNORECASE)
    
    if not match:
        print("ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md")
        sys.exit(1)
    
    # Field exists - pass (no output)
    sys.exit(0)

if __name__ == "__main__":
    check_engine_version_presence()

