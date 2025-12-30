#!/usr/bin/env python3
"""
Collect hashes for R-2E execution archive.

Read-only collection. No modification, no inference.
"""

import json
import hashlib
import sys
from pathlib import Path


def hash_file(file_path: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def collect_hashes(archive_dir: str, output_file: str):
    """
    Collect hashes for all runs in archive.
    
    Args:
        archive_dir: Directory containing run archives
        output_file: Output file for hash manifest
    """
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Error: Archive directory not found: {archive_dir}")
        sys.exit(1)
    
    manifest = {
        "manifest_date": None,
        "total_runs": 0,
        "runs": []
    }
    
    # Scan all run directories
    run_dirs = sorted([d for d in archive_path.iterdir() if d.is_dir() and d.name.startswith("r2_min_")])
    
    for run_dir in run_dirs:
        run_id = run_dir.name
        
        run_hashes = {
            "run_id": run_id,
            "files": {}
        }
        
        # Hash key files
        key_files = ["inputs.json", "outputs.json", "metrics.json", "hashes.json"]
        for key_file in key_files:
            file_path = run_dir / key_file
            if file_path.exists():
                run_hashes["files"][key_file] = hash_file(file_path)
        
        # Hash state snapshots directory
        snapshots_dir = run_dir / "state_snapshots"
        if snapshots_dir.exists():
            snapshot_hashes = {}
            for snapshot_file in sorted(snapshots_dir.glob("*.json")):
                snapshot_hashes[snapshot_file.name] = hash_file(snapshot_file)
            run_hashes["files"]["state_snapshots"] = snapshot_hashes
        
        manifest["runs"].append(run_hashes)
        manifest["total_runs"] += 1
    
    # Write manifest
    with open(output_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Collected hashes for {manifest['total_runs']} runs")
    print(f"Manifest written: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 collect_hashes_r2e.py <archive_dir> <output_file>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    collect_hashes(archive_dir, output_file)

