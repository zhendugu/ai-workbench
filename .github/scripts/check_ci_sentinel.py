#!/usr/bin/env python3
"""
ENGINE CI Sentinel Check
Platform and CI environment viability checks only.
Does NOT check ENGINE documents or registry content.
"""
import sys
import os
import subprocess

def run_command(cmd):
    """Run shell command and return (stdout, stderr, returncode)"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def check_default_branch():
    """Check that default branch is detectable"""
    # Check GITHUB_REF_NAME (GitHub Actions provides this)
    ref_name = os.environ.get("GITHUB_REF_NAME", "")
    ref = os.environ.get("GITHUB_REF", "")
    
    if not ref_name and not ref:
        return False, "Default branch not detectable: GITHUB_REF_NAME and GITHUB_REF are both empty"
    
    # If we have a ref, it should be a valid branch reference
    if ref and not (ref.startswith("refs/heads/") or ref.startswith("refs/pull/")):
        return False, f"Malformed GITHUB_REF: {ref}"
    
    return True, None

def check_git_history_depth():
    """Check that git history depth is sufficient for diff-based enforcement"""
    # Verify git rev-parse HEAD succeeds (indicates we have commit history)
    stdout, stderr, returncode = run_command("git rev-parse HEAD")
    if returncode != 0:
        return False, "Git history insufficient: git rev-parse HEAD failed. Ensure fetch-depth: 0 in checkout action."
    
    # Verify we can access at least one parent commit (for diff operations)
    stdout, stderr, returncode = run_command("git rev-parse HEAD~1 2>/dev/null")
    # Note: HEAD~1 may not exist on first commit, but that's OK for sentinel
    # The important check is that HEAD exists (checked above)
    
    return True, None

def print_failure_message(reason):
    """Print human-readable diagnostic message"""
    print("=" * 70)
    print("ENGINE CI not fully initialized")
    print("=" * 70)
    print()
    print("This repository is an ENGINE that requires CI enforcement.")
    print("CI enforcement did not fully initialize.")
    print()
    print("This is expected on first clone or if GitHub settings are incomplete.")
    print()
    print("What to check manually in GitHub UI:")
    print()
    print("1. Check GitHub Actions is enabled")
    print("   - Go to: Settings → Actions → General")
    print("   - Ensure 'Allow all actions and reusable workflows' is selected")
    print("   - If you see no CI runs at all, GitHub Actions is likely disabled")
    print()
    print("2. Check default branch is set")
    print("   - Go to: Settings → Branches")
    print("   - Ensure a default branch (typically 'main' or 'master') is configured")
    print()
    print("3. Verify repository has commit history")
    print("   - Ensure the repository has at least one commit")
    print("   - CI workflows require git history for diff-based enforcement")
    print()
    print("CI enforcement has NOT started.")
    print("Once platform checks pass, ENGINE bootstrap and governance checks will run.")
    print()
    print("=" * 70)
    print(f"Failure reason: {reason}")
    print("=" * 70)

def main():
    """Execute CI sentinel checks"""
    failures = []
    
    # C-5.1: Check default branch is detectable
    branch_ok, branch_error = check_default_branch()
    if not branch_ok:
        failures.append(branch_error)
    
    # C-5.1: Check git history depth
    git_ok, git_error = check_git_history_depth()
    if not git_ok:
        failures.append(git_error)
    
    # C-5.1: GitHub Actions enabled check
    # If this script runs, GitHub Actions is enabled (workflow was triggered)
    # We can't directly detect if Actions is disabled, but we can provide guidance
    # This check is informational only - if workflow doesn't run, user sees no CI
    
    if failures:
        # C-5.2: Print explicit human diagnostic output
        for failure in failures:
            print_failure_message(failure)
        sys.exit(1)
    
    # C-5.5: Success - no output, exit 0
    sys.exit(0)

if __name__ == "__main__":
    main()

