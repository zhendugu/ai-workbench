#!/usr/bin/env python3
"""
Hash Collector for Q4-2

Collects SHA256 hashes of all run artifacts.
Read-only operation.
"""

import os
import json
import hashlib
from pathlib import Path


def hash_file(filepath):
    """Hash a file."""
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def collect_hashes(archive_dir):
    """
    Collect hashes for all runs in archive directory.
    
    Args:
        archive_dir: Archive directory path
    """
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Archive directory not found: {archive_dir}")
        return
    
    runs = sorted([d for d in os.listdir(archive_path) if d.startswith('run_') and (archive_path / d).is_dir()])
    
    manifest = {
        "total_runs": len(runs),
        "runs": {}
    }
    
    for run_id in runs:
        run_dir = archive_path / run_id
        
        run_hashes = {}
        
        # Hash key files
        for filename in ['inputs.json', 'config.json', 'events.log', 'metrics.json', 'verdict.json']:
            filepath = run_dir / filename
            if filepath.exists():
                run_hashes[filename.replace('.json', '').replace('.log', '')] = hash_file(filepath)
        
        manifest["runs"][run_id] = run_hashes
    
    # Write manifest
    manifest_file = archive_path / "hashes_manifest.md"
    with open(manifest_file, 'w') as f:
        f.write("# Hashes Manifest Q4-2\n\n")
        f.write("**Work Order**: WO-Q-4-2-0\n\n")
        f.write("## Run Hashes\n\n")
        
        for run_id, hashes in manifest["runs"].items():
            f.write(f"### {run_id}\n\n")
            for key, hash_val in hashes.items():
                f.write(f"- **{key}**: `{hash_val}`\n")
            f.write("\n")
    
    print(f"Collected hashes for {len(runs)} runs")
    print(f"Manifest written: {manifest_file}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 collect_hashes_q4_2.py <archive_dir>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    collect_hashes(archive_dir)

