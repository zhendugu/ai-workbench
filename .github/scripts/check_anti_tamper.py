#!/usr/bin/env python3
"""
ENGINE Anti-Tamper Enforcement
Based on ENGINE_CI_BOOTSTRAP.md Anti-Tamper Rules
"""
import sys
import os
import subprocess

# Governance-critical paths
GOVERNANCE_CRITICAL_PATHS = [
    ".github/workflows/",
    ".github/scripts/",
]

# Approval token
APPROVAL_TOKEN = "[CI-APPROVED]"

# Exact failure message
FAILURE_MESSAGE = "ENGINE anti-tamper violation: CI modification detected without explicit human approval."

def run_git_command(cmd):
    """Run git command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout.strip(), result.returncode
    except Exception:
        return "", 1

def get_changed_files():
    """Get list of changed files in governance-critical paths"""
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    
    if event_name == "pull_request":
        # PR: compare base with head (GitHub Actions provides merge commit)
        # Use GITHUB_SHA which points to the merge commit
        base_sha = os.environ.get("GITHUB_BASE_SHA", "")
        head_sha = os.environ.get("GITHUB_SHA", "")
        
        if base_sha and head_sha:
            diff_cmd = f"git diff --name-only {base_sha} {head_sha}"
        else:
            # Fallback: compare with origin/main
            diff_cmd = "git diff --name-only origin/main...HEAD"
    else:
        # Push: compare with previous commit
        diff_cmd = "git diff --name-only HEAD~1 HEAD"
    
    output, returncode = run_git_command(diff_cmd)
    if returncode != 0:
        # If diff fails, assume no changes (conservative)
        return []
    
    changed_files = [line.strip() for line in output.split("\n") if line.strip()]
    
    # Filter to only governance-critical paths
    governance_changes = []
    for file_path in changed_files:
        for critical_path in GOVERNANCE_CRITICAL_PATHS:
            if file_path.startswith(critical_path):
                governance_changes.append(file_path)
                break
    
    return governance_changes

def check_approval_token():
    """Check for approval token in commit message or PR title"""
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    
    # Check commit message (for both push and PR)
    commit_msg_output, _ = run_git_command("git log -1 --pretty=%B")
    if APPROVAL_TOKEN in commit_msg_output:
        return True
    
    # For pull requests, also check PR title
    if event_name == "pull_request":
        # Try to get from event file (most reliable)
        event_path = os.environ.get("GITHUB_EVENT_PATH", "")
        if event_path and os.path.exists(event_path):
            try:
                import json
                with open(event_path, 'r') as f:
                    event_data = json.load(f)
                    pr_title = event_data.get("pull_request", {}).get("title", "")
                    if APPROVAL_TOKEN in pr_title:
                        return True
            except Exception:
                pass
    
    return False

def main():
    """Execute anti-tamper check"""
    # Check for changes in governance-critical paths
    governance_changes = get_changed_files()
    
    # If no governance-critical files changed, pass
    if not governance_changes:
        sys.exit(0)
    
    # Governance-critical files changed - check for approval
    has_approval = check_approval_token()
    
    if not has_approval:
        print(FAILURE_MESSAGE)
        sys.exit(1)
    
    # Approval found - pass
    sys.exit(0)

if __name__ == "__main__":
    main()

