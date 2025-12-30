#!/usr/bin/env python3
"""
Influence Signal Computer for Q4-2

Computes "factually dominant" control signals.
Read-only operation, no fixes.
"""

import os
import json
from pathlib import Path


def compute_influence_signals(archive_dir):
    """
    Compute influence signals from run archives.
    
    Args:
        archive_dir: Archive directory path
    """
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Archive directory not found: {archive_dir}")
        return
    
    runs = sorted([d for d in os.listdir(archive_path) if d.startswith('run_') and (archive_path / d).is_dir()])
    
    signals = {
        "total_runs": len(runs),
        "runs_analyzed": 0,
        "dominance_signals": []
    }
    
    for run_id in runs:
        run_dir = archive_path / run_id
        metrics_file = run_dir / "metrics.json"
        
        if not metrics_file.exists():
            continue
        
        with open(metrics_file, 'r') as f:
            metrics = json.load(f)
        
        # Compute basic signals (placeholder - actual computation would reference Q-0/Q-1/Q-2 criteria)
        tool_calls = metrics.get("tool_calls", [])
        
        # Simple signal: tool call frequency per epoch
        tool_frequency = {}
        for call in tool_calls:
            tool_name = call.get("tool", "unknown")
            tool_frequency[tool_name] = tool_frequency.get(tool_name, 0) + 1
        
        signals["runs_analyzed"] += 1
        signals["dominance_signals"].append({
            "run_id": run_id,
            "tool_frequency": tool_frequency,
            "total_tool_calls": len(tool_calls)
        })
    
    # Write signals file
    signals_file = Path(archive_dir).parent / "INFLUENCE_SIGNALS_Q4-2.md"
    with open(signals_file, 'w') as f:
        f.write("# Influence Signals Q4-2\n\n")
        f.write("**Work Order**: WO-Q-4-2-0\n\n")
        f.write("## Signals Summary\n\n")
        f.write(f"**Total Runs Analyzed**: {signals['runs_analyzed']}\n\n")
        
        f.write("## Dominance Signals\n\n")
        for signal in signals["dominance_signals"]:
            f.write(f"### {signal['run_id']}\n\n")
            f.write(f"- **Total Tool Calls**: {signal['total_tool_calls']}\n")
            f.write(f"- **Tool Frequency**: {signal['tool_frequency']}\n")
            f.write("\n")
    
    print(f"Influence signals written: {signals_file}")
    print(f"Runs analyzed: {signals['runs_analyzed']}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 compute_influence_signals.py <archive_dir>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    compute_influence_signals(archive_dir)

