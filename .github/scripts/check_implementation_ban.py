#!/usr/bin/env python3
"""
Implementation Ban Check
基于 STAGE_3_2_CI_RULES.md 5. Implementation Ban (Pre-Stage-4)
"""
import sys
import re
from pathlib import Path

def read_current_stage_number():
    """Read current stage number as integer from docs/stage_status.md"""
    stage_file = Path("docs/stage_status.md")
    if not stage_file.exists():
        return None
    
    try:
        content = stage_file.read_text()
    except (IOError, OSError, PermissionError):
        return None
    
    # Match "Current Stage: Stage N"
    match = re.search(r"Current Stage:\s*Stage\s+(\d+)", content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    
    return None

def read_stage_endpoint_registry(stage_number):
    """Read endpoint registry for the specified stage"""
    if stage_number is None:
        return set()
    
    registry_file = Path(f"docs/registry/stage_{stage_number}_endpoints.yaml")
    if not registry_file.exists():
        return set()
    
    try:
        content = registry_file.read_text()
    except (IOError, OSError, PermissionError):
        return set()
    
    authorized = set()
    
    # Simple string parsing to extract method and path
    # Format: method: GET, path: /health
    lines = content.split('\n')
    current_method = None
    current_path = None
    
    for line in lines:
        # Extract method
        method_match = re.search(r'method:\s*(\w+)', line, re.IGNORECASE)
        if method_match:
            current_method = method_match.group(1).upper()
        
        # Extract path
        path_match = re.search(r'path:\s*(["\']?)([^"\'\s]+)\1', line)
        if path_match:
            current_path = path_match.group(2)
        
        # If both method and path are found, add to authorized set
        if current_method and current_path:
            authorized.add(f"{current_method} {current_path}")
            # Reset for next endpoint
            current_method = None
            current_path = None
    
    return authorized

def extract_fastapi_endpoints(content):
    """从 Python 代码中提取 FastAPI endpoint 装饰器"""
    endpoints = set()  # 使用 set 避免重复
    
    # 提取 router prefix（如果有，且不在注释中）
    prefix_match = re.search(r'^[^#]*prefix\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    router_prefix = prefix_match.group(1) if prefix_match else ""
    
    # 按行处理，忽略注释行
    lines = content.split('\n')
    for line_num, line in enumerate(lines):
        # 跳过注释行（以 # 开头，或包含 # 且 # 前只有空白）
        stripped = line.lstrip()
        if stripped.startswith('#'):
            continue
        
        # 匹配 @app.get("/path"), @app.post("/path") 等
        # 也匹配 @router.get("/path") 等
        # 支持单引号和双引号
        pattern = r'@(?:app|router)\.(get|post|put|delete|patch|head|options)\s*\(\s*["\']([^"\']+)["\']'
        
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            method = match.group(1).upper()
            path = match.group(2)
            
            # 如果是 router，组合 prefix 和 path
            if router_prefix and path:
                # 确保路径正确组合（避免双斜杠）
                full_path = router_prefix.rstrip('/') + '/' + path.lstrip('/')
                full_path = full_path.replace('//', '/')
            else:
                full_path = path
            
            endpoints.add(f"{method} {full_path}")
    
    return list(endpoints)

def check_backend_implementation():
    """检查后端禁止的实现模式"""
    violations = []
    backend_path = Path("backend")
    
    if not backend_path.exists():
        return violations
    
    # TASK C-4.1: Determine current stage dynamically
    current_stage_number = read_current_stage_number()
    
    # TASK C-4.1: Load registry for active stage (not hardcoded)
    authorized_endpoints = set()
    if current_stage_number is not None:
        authorized_endpoints = read_stage_endpoint_registry(current_stage_number)
    
    # 仓库级扫描：检查所有 Python 文件
    for py_file in backend_path.rglob("*.py"):
        # 排除虚拟环境
        if ".venv" in str(py_file) or "venv" in str(py_file):
            continue
            
        content = py_file.read_text()
        
        # TASK C-4.2: Enforce registry for active stage
        # Check all FastAPI endpoints against registry for current stage
        if current_stage_number is not None:
            declared_endpoints = extract_fastapi_endpoints(content)
            for endpoint in declared_endpoints:
                if endpoint not in authorized_endpoints:
                    violations.append(f"{py_file}: Unauthorized endpoint detected: {endpoint} (must be registered in docs/registry/stage_{current_stage_number}_endpoints.yaml)")
        
        # TASK C-4.3: Preserve existing hard bans (database operations)
        db_patterns = [
            (r'\b(sqlite3|psycopg2|mysql|pymongo|sqlalchemy)\b', "Database operations"),
            (r'\.execute\s*\(', "Database execute calls"),
            (r'\.commit\s*\(|\.rollback\s*\(', "Database transaction operations"),
        ]
        
        for pattern, description in db_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                violations.append(f"{py_file}: {description} detected")
        
        # TASK C-4.3: Preserve existing hard bans (persistence)
        storage_patterns = [
            (r'open\s*\([^)]+["\']w', "File write operations"),
            (r'\.save\s*\(|\.write\s*\(', "Save/write operations"),
            (r'pickle\.dump|json\.dump', "Serialization operations"),
        ]
        
        for pattern, description in storage_patterns:
            if re.search(pattern, content):
                violations.append(f"{py_file}: {description} detected")
        
        # TASK C-4.3: Preserve existing hard bans (AI API calls)
        ai_patterns = [
            (r'openai\.|anthropic\.|cohere\.', "AI API calls"),
            (r'\.chat\.completions\.|\.embeddings\.', "AI API methods"),
            (r'requests\.(get|post).*api.*key', "AI API requests"),
        ]
        
        for pattern, description in ai_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                violations.append(f"{py_file}: {description} detected")
        
        # TASK C-4.3: Preserve existing hard bans (control flow)
        # If file contains authorized endpoint, skip control flow check
        # Exclude common entry point pattern (if __name__ == "__main__")
        has_authorized_endpoint = False
        if current_stage_number is not None:
            declared_endpoints = extract_fastapi_endpoints(content)
            has_authorized_endpoint = any(ep in authorized_endpoints for ep in declared_endpoints)
        
        if not (current_stage_number is not None and has_authorized_endpoint):
            if re.search(r'\bif\s+[^:]+:\s*\n\s+(?!pass|raise|return\s*$|#)', content, re.MULTILINE):
                # Exclude entry point pattern
                if re.search(r'if\s+__name__\s*==\s*["\']__main__["\']', content):
                    continue
                if not re.search(r'\bpass\b|\braise\s+NotImplementedError\b', content):
                    violations.append(f"{py_file}: Meaningful control flow detected (if with non-empty body)")
    
    return violations

def check_frontend_implementation():
    """检查前端禁止的实现模式"""
    violations = []
    frontend_path = Path("frontend")
    
    if not frontend_path.exists():
        return violations
    
    for ts_file in frontend_path.rglob("*.tsx"):
        content = ts_file.read_text()
        
        # 检查真实 API 调用
        if re.search(r'fetch\s*\(["\']https?://', content):
            violations.append(f"{ts_file}: API calls with real endpoints detected")
        
        # 检查状态转换逻辑
        if re.search(r'useState\s*\([^)]+\)', content):
            if re.search(r'set[A-Z]\w*\s*\([^)]+\)', content):
                # 检查是否有非空的状态更新
                if not re.search(r'set[A-Z]\w*\s*\([^)]*\)\s*;?\s*$', content, re.MULTILINE):
                    violations.append(f"{ts_file}: State transition logic detected")
        
        # 检查验证逻辑
        validation_patterns = [
            (r'\.validate\s*\(|\.test\s*\(', "Validation logic"),
            (r'if\s*\(.*\.length|if\s*\(.*===.*null', "Validation conditions"),
        ]
        
        for pattern, description in validation_patterns:
            if re.search(pattern, content):
                violations.append(f"{ts_file}: {description} detected")
        
        # 检查有副作用的 useEffect
        if re.search(r'useEffect\s*\([^)]*\)', content):
            # 检查是否有非空的 effect body
            if re.search(r'useEffect\s*\([^)]*\)\s*\{[^}]+[^\s}]', content):
                violations.append(f"{ts_file}: Side-effect-driven useEffect detected")
    
    return violations

def main():
    if len(sys.argv) < 2:
        print("Usage: check_implementation_ban.py <backend|frontend>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if target == "backend":
        violations = check_backend_implementation()
    elif target == "frontend":
        violations = check_frontend_implementation()
    else:
        print(f"Error: Unknown target '{target}'")
        sys.exit(1)
    
    if violations:
        # TASK C-4.5: Print only violation message on failure (no extra prefixes)
        print("Implementation violation: executable logic detected before authorization")
        for violation in violations:
            print(f"  - {violation}")
        sys.exit(1)
    
    # TASK C-4.5: Print nothing on success (deterministic self-test mode)
    sys.exit(0)

if __name__ == "__main__":
    main()

