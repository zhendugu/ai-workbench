#!/usr/bin/env python3
"""
Build Q2 attack coverage matrix update from actual runs.

This script maps actual runs to AG×AV combinations from Q-1 coverage matrix.
"""

import json
import argparse
from pathlib import Path

def load_q1_coverage_matrix():
    """Load Q-1 coverage matrix mapping."""
    # This is a simplified version - in practice, would read from Q1_ATTACK_COVERAGE_MATRIX.md
    # Mapping from Q-1: strategy -> attack vectors -> attack goals
    coverage_map = {
        "STRATEGY-SLOW-DRIFT": {
            "AV-002": ["AG-001"],
            "AV-012": ["AG-001"],
            "AV-004": ["AG-001", "AG-006"],
            "AV-007": ["AG-001", "AG-004", "AG-006"],
        },
        "STRATEGY-BURST-THEN-STABILIZE": {
            "AV-001": ["AG-001", "AG-002", "AG-003", "AG-004"],
            "AV-008": ["AG-001", "AG-003"],
            "AV-003": ["AG-001", "AG-004"],
            "AV-006": ["AG-001", "AG-004"],
        },
        "STRATEGY-ALTERNATING-NOISE": {
            "AV-005": ["AG-001", "AG-002", "AG-004", "AG-005"],
            "AV-009": ["AG-001", "AG-002", "AG-003", "AG-004"],
            "AV-010": ["AG-001", "AG-003", "AG-006"],
            "AV-011": ["AG-001", "AG-002", "AG-005", "AG-006"],
        }
    }
    return coverage_map

def load_runs(runs_dir):
    """Load all run metadata."""
    runs = []
    runs_path = Path(runs_dir)
    
    for run_dir in sorted(runs_path.iterdir()):
        if not run_dir.is_dir():
            continue
        
        run_id = run_dir.name
        metadata_file = run_dir / "run_metadata.json"
        
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
            runs.append({
                "run_id": run_id,
                "strategy": metadata.get("strategy", "UNKNOWN"),
                "human_model": metadata.get("human_model", "UNKNOWN"),
                "seed": metadata.get("seed", "UNKNOWN"),
                "horizon": metadata.get("horizon", "UNKNOWN")
            })
    
    return runs

def build_coverage_update(runs_dir, output_file):
    """Build coverage matrix update."""
    coverage_map = load_q1_coverage_matrix()
    runs = load_runs(runs_dir)
    
    # Build AG×AV matrix (6 AG × 12 AV = 72 cells)
    ag_list = [f"AG-{i:03d}" for i in range(1, 7)]
    av_list = [f"AV-{i:03d}" for i in range(1, 13)]
    
    coverage_matrix = {}
    covered_cells = 0
    total_cells = len(ag_list) * len(av_list)
    
    for ag in ag_list:
        for av in av_list:
            key = f"{ag}_{av}"
            coverage_matrix[key] = {
                "ag": ag,
                "av": av,
                "strategies": [],
                "run_ids": []
            }
            
            # Find runs that cover this AG×AV combination
            for strategy, av_map in coverage_map.items():
                if av in av_map and ag in av_map[av]:
                    # Find runs with this strategy
                    strategy_runs = [r for r in runs if r["strategy"] == strategy]
                    if strategy_runs:
                        coverage_matrix[key]["strategies"].append(strategy)
                        coverage_matrix[key]["run_ids"].extend([r["run_id"] for r in strategy_runs])
            
            if coverage_matrix[key]["run_ids"]:
                covered_cells += 1
    
    coverage_percentage = (covered_cells / total_cells) * 100
    
    # Generate markdown
    lines = [
        "# Q2 Attack Coverage Matrix Update",
        "",
        "**Document Status**: SIMULATION-EXECUTION / NON-CANONICAL",
        "**Date**: 2026-01-10",
        "",
        "## Purpose",
        "",
        "This document updates Q-1 coverage matrix with actual execution coverage from Q-2 runs.",
        "",
        "## Q-1 Design Coverage",
        "",
        "**Design Coverage**: 80.6% (58/72 cells)",
        "",
        "**Reference**: `phase_q/Q1_ATTACK_COVERAGE_MATRIX.md`",
        "",
        "## Q-2 Execution Coverage",
        "",
        f"**Execution Coverage**: {coverage_percentage:.1f}% ({covered_cells}/{total_cells} cells)",
        "",
        "**Coverage Status**:",
        f"- ≥ Q-1 Design Coverage (80.6%): {'YES' if coverage_percentage >= 80.6 else 'NO'}",
        "",
        "## Coverage Matrix (Sample - First 10 AG×AV Combinations)",
        "",
        "| Attack Goal | Attack Vector | Q-1 Strategy | Q-2 Run IDs | Coverage Status |",
        "|-------------|--------------|--------------|-------------|-----------------|"
    ]
    
    # Show first 10 covered cells
    shown = 0
    for key, data in sorted(coverage_matrix.items()):
        if data["run_ids"] and shown < 10:
            run_ids_sample = ", ".join(data["run_ids"][:3])
            if len(data["run_ids"]) > 3:
                run_ids_sample += f" ... ({len(data['run_ids'])} total)"
            strategy = data["strategies"][0] if data["strategies"] else "NONE"
            lines.append(f"| {data['ag']} | {data['av']} | {strategy} | {run_ids_sample} | COVERED |")
            shown += 1
    
    lines.extend([
        "",
        "## Coverage Summary",
        "",
        f"**Q-1 Design Coverage**: 80.6% (58/72 cells)",
        f"**Q-2 Execution Coverage**: {coverage_percentage:.1f}% ({covered_cells}/{total_cells} cells)",
        "",
        "**Coverage Status**:",
        f"- ≥ Q-1 Design Coverage: {'YES' if coverage_percentage >= 80.6 else 'NO'}",
        "",
        "**All Covered Cells Have Run ID References**: YES (100%)",
        "",
        "## No Recommendations",
        "",
        "This update provides no recommendations.",
        "",
        "**END OF Q2 ATTACK COVERAGE MATRIX UPDATE**"
    ])
    
    # Write file
    output_path = Path(output_file)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Coverage update written: {output_path}")
    print(f"Coverage: {coverage_percentage:.1f}% ({covered_cells}/{total_cells} cells)")

def main():
    parser = argparse.ArgumentParser(description='Build Q2 attack coverage matrix update')
    parser.add_argument('--runs_dir', type=str, default='phase_q/runs', help='Runs directory')
    parser.add_argument('--output', type=str, default='phase_q/Q2_ATTACK_COVERAGE_MATRIX_UPDATE.md', help='Output file')
    
    args = parser.parse_args()
    
    build_coverage_update(args.runs_dir, args.output)

if __name__ == '__main__':
    main()

