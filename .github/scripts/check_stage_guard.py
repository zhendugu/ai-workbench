#!/usr/bin/env python3
"""
Stage Guard Rule Check
基于 STAGE_3_2_CI_RULES.md 2. Stage Guard Rule
"""
import sys
import re
from pathlib import Path

def read_stage_status():
    """读取 stage_status.md 获取当前阶段"""
    stage_file = Path("docs/stage_status.md")
    if not stage_file.exists():
        print("Error: docs/stage_status.md not found")
        sys.exit(1)
    
    content = stage_file.read_text()
    match = re.search(r"Current Stage:\s*(.+)", content)
    if match:
        return match.group(1).strip()
    return None

def check_forbidden_patterns():
    """检查禁止的模式"""
    violations = []
    
    # 检查后端文件
    backend_path = Path("backend")
    if backend_path.exists():
        for py_file in backend_path.rglob("*.py"):
            content = py_file.read_text()
            
            # 检查业务逻辑模式
            if re.search(r'\bif\s+.*:\s*\n\s+[^\s#]', content, re.MULTILINE):
                violations.append(f"{py_file}: Business logic detected (if with non-empty body)")
            
            if re.search(r'\bfor\s+.*:\s*\n\s+[^\s#]', content, re.MULTILINE):
                violations.append(f"{py_file}: Workflow inferred (for with non-empty body)")
            
            if re.search(r'\bwhile\s+.*:\s*\n\s+[^\s#]', content, re.MULTILINE):
                violations.append(f"{py_file}: Semantic interpretation detected (while with non-empty body)")
    
    # 检查前端文件
    frontend_path = Path("frontend")
    if frontend_path.exists():
        for ts_file in frontend_path.rglob("*.tsx"):
            content = ts_file.read_text()
            
            # 检查 API 调用
            if re.search(r'fetch\s*\(|axios\.|\.get\s*\(|\.post\s*\(', content):
                violations.append(f"{ts_file}: API calls with real endpoints detected")
            
            # 检查状态转换逻辑
            if re.search(r'useState\s*\([^)]+\)\s*\[0\]', content):
                if re.search(r'setState|dispatch|reducer', content):
                    violations.append(f"{ts_file}: State transition logic detected")
    
    return violations

def main():
    current_stage = read_stage_status()
    
    if not current_stage:
        print("Error: Could not determine current stage")
        sys.exit(1)
    
    # 检查是否在 Stage 3/3.1/3.2
    if re.match(r"Stage\s+3(\.\d+)?", current_stage):
        violations = check_forbidden_patterns()
        
        if violations:
            print("Stage violation: unauthorized implementation detected")
            for violation in violations:
                print(f"  - {violation}")
            sys.exit(1)
    
    print("Stage guard check passed")

if __name__ == "__main__":
    main()

