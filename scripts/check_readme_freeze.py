#!/usr/bin/env python3
"""
README Freeze CI Check

This script performs lightweight text-based checks on Subsystem README files
to enforce "Behavior Semantics Frozen" rules.

Rules:
1. Responsibilities sections MUST use only design-time verbs (Define, Specify, etc.)
2. Responsibilities sections MUST NOT contain behavioral verbs (Manage, Execute, etc.)
3. Responsibilities sections MUST NOT contain conditional logic (if/when/then)
4. Responsibilities sections MUST NOT contain execution context (runtime/execution/process/flow)
5. All README files MUST contain "What this subsystem does NOT do" section

This is a text-based rule matching script only. No semantic inference.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# Design-time verbs (allowed)
ALLOWED_VERBS = {
    "define", "specify", "declare", "describe", "represent", "constrain"
}

# Behavioral verbs (forbidden in Responsibilities)
FORBIDDEN_VERBS = {
    "manage", "execute", "implement", "trigger", "detect", "monitor",
    "handle", "route", "receive", "record", "track", "maintain",
    "validate", "provide", "recover", "terminate", "restructure",
    "analyze", "read", "write", "run", "create", "extract", "perform"
}

# Conditional logic patterns (forbidden)
CONDITIONAL_PATTERNS = [
    r"\bif\b",
    r"\bwhen\b",
    r"\bthen\b",
    r"\bimmediately\b",
    r"\bauto-\w+",
]

# Execution context patterns (forbidden in behavioral sense)
# Note: These are context-dependent, but we check for common violations
EXECUTION_CONTEXT_PATTERNS = [
    r"\bruntime\b",  # except in "No runtime rules"
    r"\bexecution\b",  # except in "No execution logic"
    r"\bprocess\b",  # except in "review process structure"
    r"\blifecycle\b",  # except in state definitions
    r"\bflow\b",  # except in "document flow" (structure)
]

# Note: We use simple pattern matching. Context-aware exceptions would require
# more sophisticated parsing, which is explicitly avoided per requirements.


def find_responsibilities_section(content: str) -> Tuple[int, int, str]:
    """
    Find the Responsibilities section in README content.
    Returns (start_line, end_line, section_content)
    """
    lines = content.split('\n')
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if re.match(r'^##\s+Responsibilities', line, re.IGNORECASE):
            start_idx = i
        elif start_idx is not None and line.startswith('##'):
            end_idx = i
            break
    
    if start_idx is None:
        return None, None, ""
    
    if end_idx is None:
        end_idx = len(lines)
    
    section_lines = lines[start_idx:end_idx]
    section_content = '\n'.join(section_lines)
    
    return start_idx + 1, end_idx, section_content


def check_forbidden_verbs(content: str, file_path: str) -> List[Tuple[int, str, str]]:
    """Check for forbidden behavioral verbs in Responsibilities section."""
    violations = []
    start_line, end_line, section = find_responsibilities_section(content)
    
    if not section:
        return violations
    
    lines = section.split('\n')
    for i, line in enumerate(lines):
        line_num = start_line + i
        line_lower = line.lower()
        
        # Only check lines that start with "-" (bullet points in Responsibilities)
        if not line.strip().startswith('-'):
            continue
        
        for verb in FORBIDDEN_VERBS:
            # Check for verb as word boundary, but only if it appears to be used as a verb
            # Pattern: verb should appear after "Define" or "Specify" or at start of bullet
            # Exclude if it's part of a compound noun (e.g., "record structure", "write structure")
            pattern = r'\b' + re.escape(verb) + r'\b'
            if re.search(pattern, line_lower):
                # Exclude if it's followed by "structure", "rules", "permissions", "conditions" (noun usage)
                noun_context = re.search(
                    r'\b' + re.escape(verb) + r'\s+(structure|rules?|permissions?|conditions?|format|specification|definition)\b',
                    line_lower
                )
                # Exclude if it's preceded by "trigger" in "trigger conditions" (compound noun)
                compound_noun = re.search(
                    r'\b(trigger|call|trace|replay|write|read)\s+' + re.escape(verb) + r'\b',
                    line_lower
                )
                if not noun_context and not compound_noun:
                    # Check if it appears to be used as a verb (after Define/Specify, before object)
                    verb_usage = re.search(
                        r'(define|specify|declare|describe)\s+.*?\b' + re.escape(verb) + r'\s+',
                        line_lower
                    )
                    if verb_usage:
                        violations.append((line_num, verb, line.strip()))
    
    return violations


def check_conditional_logic(content: str, file_path: str) -> List[Tuple[int, str, str]]:
    """Check for conditional logic patterns in Responsibilities section."""
    violations = []
    start_line, end_line, section = find_responsibilities_section(content)
    
    if not section:
        return violations
    
    lines = section.split('\n')
    for i, line in enumerate(lines):
        line_num = start_line + i
        line_lower = line.lower()
        
        # Only check lines that start with "-" (bullet points in Responsibilities)
        if not line.strip().startswith('-'):
            continue
        
        for pattern in CONDITIONAL_PATTERNS:
            if re.search(pattern, line_lower):
                # Exclude "trigger conditions" (structure definition)
                if not re.search(r'\btrigger\s+conditions?\b', line_lower):
                    violations.append((line_num, pattern, line.strip()))
    
    return violations


def check_execution_context(content: str, file_path: str) -> List[Tuple[int, str, str]]:
    """Check for execution context terms in Responsibilities section."""
    violations = []
    start_line, end_line, section = find_responsibilities_section(content)
    
    if not section:
        return violations
    
    lines = section.split('\n')
    for i, line in enumerate(lines):
        line_num = start_line + i
        line_lower = line.lower()
        
        # Simple check: if these terms appear in bullet points (starting with -)
        if line.strip().startswith('-'):
            for pattern in EXECUTION_CONTEXT_PATTERNS:
                if re.search(pattern, line_lower):
                    # Basic exception: if it's in a structure definition context
                    # We do simple heuristics: if "structure" or "rules" appear nearby
                    if not re.search(r'\b(structure|rules?|specification|definition)\b', line_lower):
                        violations.append((line_num, pattern, line.strip()))
    
    return violations


def check_non_responsibility_section(content: str, file_path: str) -> bool:
    """Check if README contains 'What this subsystem does NOT do' section."""
    pattern = r'##\s+What\s+this\s+subsystem\s+does\s+NOT\s+do'
    return bool(re.search(pattern, content, re.IGNORECASE))


def check_readme_file(file_path: Path) -> Tuple[bool, List[str]]:
    """
    Check a single README file against freeze rules.
    Returns (is_valid, error_messages)
    """
    errors = []
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    # Check forbidden verbs
    verb_violations = check_forbidden_verbs(content, str(file_path))
    if verb_violations:
        for line_num, verb, line in verb_violations:
            errors.append(
                f"  Line {line_num}: Forbidden verb '{verb}' found: {line}"
            )
    
    # Check conditional logic
    conditional_violations = check_conditional_logic(content, str(file_path))
    if conditional_violations:
        for line_num, pattern, line in conditional_violations:
            errors.append(
                f"  Line {line_num}: Conditional logic pattern '{pattern}' found: {line}"
            )
    
    # Check execution context
    context_violations = check_execution_context(content, str(file_path))
    if context_violations:
        for line_num, pattern, line in context_violations:
            errors.append(
                f"  Line {line_num}: Execution context pattern '{pattern}' found: {line}"
            )
    
    # Check non-responsibility section
    if not check_non_responsibility_section(content, str(file_path)):
        errors.append(
            "  Missing 'What this subsystem does NOT do' section"
        )
    
    return len(errors) == 0, errors


def main():
    """Main entry point for CI check."""
    repo_root = Path(__file__).parent.parent
    subsystems_dir = repo_root / "backend" / "subsystems"
    
    if not subsystems_dir.exists():
        print(f"Error: Subsystems directory not found: {subsystems_dir}")
        sys.exit(1)
    
    readme_files = list(subsystems_dir.glob("*/README.md"))
    
    if not readme_files:
        print("Warning: No README files found in subsystems directory")
        sys.exit(0)
    
    all_valid = True
    all_errors = []
    
    for readme_file in sorted(readme_files):
        is_valid, errors = check_readme_file(readme_file)
        
        if not is_valid:
            all_valid = False
            all_errors.append(f"\n{readme_file.relative_to(repo_root)}:")
            all_errors.extend(errors)
    
    if all_valid:
        print("✅ All README files comply with freeze rules")
        sys.exit(0)
    else:
        print("❌ README freeze violations found:")
        print("\n".join(all_errors))
        print("\nSee docs/STAGE_6_CONTROLLED_IMPLEMENTATION.md for freeze rules.")
        sys.exit(1)


if __name__ == "__main__":
    main()

