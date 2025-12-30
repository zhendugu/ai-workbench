#!/usr/bin/env python3
"""
Collect Hashes for All Runs

Generates hashes.json for each run and global hashes_manifest.md
"""

import sys
import os
import json
import hashlib
from pathlib import Path


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA256 hash of file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def collect_run_hashes(run_dir: Path) -> dict:
    """Collect hashes for a single run."""
    hashes = {}
    
    files = {
        "inputs": "inputs.json",
        "config": "config.json",
        "events": "events.log",
        "metrics": "metrics.json",
        "verdict": "verdict.json"
    }
    
    for key, filename in files.items():
        file_path = run_dir / filename
        if file_path.exists():
            hashes[key] = compute_file_hash(file_path)
        else:
            hashes[key] = None
    
    return hashes


def collect_all_hashes(archive_dir: str):
    """Collect hashes for all runs."""
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Error: Archive directory not found: {archive_dir}")
        return
    
    # Collect hashes for each run
    run_hashes = {}
    
    for run_dir in sorted(archive_path.iterdir()):
        if not run_dir.is_dir():
            continue
        
        run_id = run_dir.name
        hashes = collect_run_hashes(run_dir)
        
        # Save hashes.json for this run
        hashes_file = run_dir / "hashes.json"
        with open(hashes_file, 'w') as f:
            json.dump({
                "run_id": run_id,
                "hashes": hashes
            }, f, indent=2)
        
        run_hashes[run_id] = hashes
    
    # Generate global manifest
    manifest_lines = [
        "# Hashes Manifest",
        "",
        "**Work Order**: WO-Q-4-1-EPOCH-EXPANDED-RUNTIME-STRESS-AND-LEAKAGE-REGRESSION",
        "**Date**: 2026-01-10",
        "",
        "## Purpose",
        "",
        "This document provides SHA256 hashes for all run artifacts.",
        "",
        "## Run Hashes",
        ""
    ]
    
    for run_id, hashes in sorted(run_hashes.items()):
        manifest_lines.append(f"### {run_id}")
        manifest_lines.append("")
        for key, hash_value in sorted(hashes.items()):
            if hash_value:
                manifest_lines.append(f"- **{key}**: `{hash_value}`")
            else:
                manifest_lines.append(f"- **{key}**: MISSING")
        manifest_lines.append("")
    
    manifest_lines.extend([
        "## Summary",
        "",
        f"**Total Runs**: {len(run_hashes)}",
        "",
        "## No Recommendations",
        "",
        "This manifest provides no recommendations.",
        "",
        "**END OF HASHES MANIFEST**"
    ])
    
    manifest_file = archive_path / "hashes_manifest.md"
    with open(manifest_file, 'w') as f:
        f.write('\n'.join(manifest_lines))
    
    print(f"Collected hashes for {len(run_hashes)} runs")
    print(f"Manifest written: {manifest_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: collect_hashes.py <archive_dir>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    collect_all_hashes(archive_dir)

