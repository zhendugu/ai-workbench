#!/usr/bin/env python3
"""
SSOT Lock Check
基于 STAGE_3_2_CI_RULES.md 4. SSOT (Single Source of Truth) Lock
"""
import sys
import subprocess
from pathlib import Path

def get_changed_files():
    """获取变更的文件列表"""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "origin/main"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        # 如果无法获取 diff，检查所有冻结文档
        return []

def check_frozen_documents():
    """检查冻结文档是否被修改"""
    frozen_docs = [
        "docs/GCD.md",
        "docs/S1_frontend_definition.md",
        "docs/S2_backend_definition.md",
    ]
    
    # 也检查可能的 GCD 文件名变体
    gcd_variants = [
        "docs/AI_Virtual_Company_Organizational_GCD_v2.md",
        "docs/GCD.md",
    ]
    
    violations = []
    changed_files = get_changed_files()
    
    for file_path in changed_files:
        file_path = file_path.strip()
        if not file_path:
            continue
        
        # 检查是否是冻结文档
        if file_path in frozen_docs:
            violations.append(file_path)
        
        # 检查 GCD 变体
        for gcd_variant in gcd_variants:
            if file_path == gcd_variant or file_path.endswith(gcd_variant):
                violations.append(file_path)
    
    return violations

def main():
    violations = check_frozen_documents()
    
    if violations:
        print("SSOT violation: frozen document modified — human approval required")
        for violation in violations:
            print(f"  - {violation}")
        sys.exit(1)
    
    print("SSOT lock check passed")

if __name__ == "__main__":
    main()

