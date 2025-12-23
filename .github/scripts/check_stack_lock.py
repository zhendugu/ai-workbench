#!/usr/bin/env python3
"""
Technology Stack Lock Check
基于 STAGE_3_2_CI_RULES.md 3. Technology Stack Lock
"""
import sys
from pathlib import Path

def check_backend():
    """检查后端技术栈"""
    violations = []
    backend_path = Path("backend")
    
    if not backend_path.exists():
        return violations
    
    # 禁止的文件类型
    forbidden_patterns = [
        ("*.ts", "TypeScript files"),
        ("*.js", "JavaScript files"),
        ("package.json", "Node.js package.json"),
    ]
    
    for pattern, description in forbidden_patterns:
        for file_path in backend_path.rglob(pattern):
            # 排除 _ci_probe 目录（CI 测试探针，非运行时代码）
            if "_ci_probe" in str(file_path):
                continue
            violations.append(f"{file_path}: {description} detected")
    
    # 检查 node_modules
    node_modules = backend_path / "node_modules"
    if node_modules.exists():
        violations.append(f"{node_modules}: node_modules directory detected")
    
    return violations

def check_frontend():
    """检查前端技术栈"""
    violations = []
    frontend_path = Path("frontend")
    
    if not frontend_path.exists():
        return violations
    
    # 禁止的文件类型
    forbidden_patterns = [
        ("*.py", "Python files"),
        ("requirements.txt", "Python requirements.txt"),
    ]
    
    for pattern, description in forbidden_patterns:
        for file_path in frontend_path.rglob(pattern):
            violations.append(f"{file_path}: {description} detected")
    
    # 检查 FastAPI/Flask 导入
    for ts_file in frontend_path.rglob("*.ts*"):
        content = ts_file.read_text()
        if "fastapi" in content.lower() or "flask" in content.lower():
            violations.append(f"{ts_file}: FastAPI/Flask imports detected")
    
    return violations

def main():
    if len(sys.argv) < 2:
        print("Usage: check_stack_lock.py <backend|frontend>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if target == "backend":
        violations = check_backend()
    elif target == "frontend":
        violations = check_frontend()
    else:
        print(f"Error: Unknown target '{target}'")
        sys.exit(1)
    
    if violations:
        print("Stack violation: unauthorized technology detected")
        for violation in violations:
            print(f"  - {violation}")
        sys.exit(1)
    
    print(f"Stack lock check passed for {target}")

if __name__ == "__main__":
    main()

