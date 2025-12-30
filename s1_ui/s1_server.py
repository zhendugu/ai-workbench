#!/usr/bin/env python3
"""
S1 Operator Read-Only Control Surface Server

Flask server providing read-only API endpoints for system navigation.

READ-ONLY OPERATIONS ONLY.
No file writes, no execution, no modifications.
"""

import os
import sys
import json
from pathlib import Path

# Add s1_ui directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from flask import Flask, jsonify, send_from_directory, abort, render_template
    from flask_cors import CORS
    import markdown
    from s1_data_indexer import DataIndexer
except ImportError as e:
    print(f"Error: Missing required dependencies. Please install: pip install flask flask-cors markdown")
    print(f"Details: {e}")
    sys.exit(1)

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()

app = Flask(__name__, 
            static_folder=str(SCRIPT_DIR / 'static'),
            template_folder=str(SCRIPT_DIR / 'templates'))
CORS(app)  # Allow localhost CORS

# Global indexer (built on startup)
indexer = None
repo_root = None


def init_indexer(root_path: str):
    """Initialize data indexer"""
    global indexer, repo_root
    repo_root = Path(root_path).resolve()
    indexer = DataIndexer(str(repo_root))
    indexer.index_all()
    print(f"Indexed {len(indexer.phases)} phases, {len(indexer.work_orders)} work orders")


@app.route('/')
def index():
    """Serve main UI"""
    return render_template('index.html')


@app.route('/api/phases', methods=['GET'])
def get_phases():
    """Get list of all phases"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    phases_list = []
    for phase_id, phase in indexer.phases.items():
        phases_list.append({
            "id": phase.id,
            "status": phase.status,
            "description": phase.description,
            "closure_summary_path": phase.closure_summary_path,
            "status_file_path": phase.status_file_path,
            "work_order_count": len(phase.work_orders)
        })
    
    return jsonify({"phases": phases_list})


@app.route('/api/phases/<phase_id>', methods=['GET'])
def get_phase(phase_id):
    """Get phase details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    phase_id_upper = phase_id.upper()
    if phase_id_upper not in indexer.phases:
        abort(404, f"Phase {phase_id} not found")
    
    phase = indexer.phases[phase_id_upper]
    
    # Read status file if exists
    status_content = None
    if phase.status_file_path:
        status_file = repo_root / phase.status_file_path
        if status_file.exists():
            try:
                status_content = status_file.read_text(encoding='utf-8')
            except (UnicodeDecodeError, PermissionError):
                pass
    
    # Read closure summary if exists
    closure_content = None
    if phase.closure_summary_path:
        closure_file = repo_root / phase.closure_summary_path
        if closure_file.exists():
            try:
                closure_content = closure_file.read_text(encoding='utf-8')
            except (UnicodeDecodeError, PermissionError):
                pass
    
    # Get related work orders
    related_work_orders = [
        wo_id for wo_id, wo in indexer.work_orders.items()
        if wo.phase == phase_id_upper
    ]
    
    return jsonify({
        "id": phase.id,
        "status": phase.status,
        "description": phase.description,
        "status_file_path": phase.status_file_path,
        "status_content": status_content,
        "closure_summary_path": phase.closure_summary_path,
        "closure_content": closure_content,
        "work_orders": related_work_orders
    })


@app.route('/api/work-orders', methods=['GET'])
def get_work_orders():
    """Get list of all work orders"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    work_orders_list = []
    for wo_id, wo in indexer.work_orders.items():
        work_orders_list.append({
            "id": wo.id,
            "phase": wo.phase,
            "title": wo.title,
            "status": wo.status,
            "decision_file_path": wo.decision_file_path
        })
    
    return jsonify({"work_orders": work_orders_list})


@app.route('/api/work-orders/<wo_id>', methods=['GET'])
def get_work_order(wo_id):
    """Get work order details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    wo_id_upper = wo_id.upper()
    if wo_id_upper not in indexer.work_orders:
        abort(404, f"Work order {wo_id} not found")
    
    wo = indexer.work_orders[wo_id_upper]
    
    # Read decision file if exists
    decision_content = None
    if wo.decision_file_path:
        decision_file = repo_root / wo.decision_file_path
        if decision_file.exists():
            try:
                decision_content = decision_file.read_text(encoding='utf-8')
            except (UnicodeDecodeError, PermissionError):
                pass
    
    return jsonify({
        "id": wo.id,
        "phase": wo.phase,
        "title": wo.title,
        "status": wo.status,
        "decision_file_path": wo.decision_file_path,
        "decision_content": decision_content,
        "evidence_pack_paths": wo.evidence_pack_paths,
        "execution_paths": wo.execution_paths
    })


@app.route('/api/executions', methods=['GET'])
def get_executions():
    """Get list of all executions"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    executions_list = []
    for exec_id, execution in indexer.executions.items():
        executions_list.append({
            "id": execution.id,
            "phase": execution.phase,
            "work_order": execution.work_order,
            "status": execution.status,
            "expected_runs": execution.expected_runs,
            "completed_runs": execution.completed_runs
        })
    
    return jsonify({"executions": executions_list})


@app.route('/api/executions/<execution_id>', methods=['GET'])
def get_execution(execution_id):
    """Get execution details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    if execution_id not in indexer.executions:
        abort(404, f"Execution {execution_id} not found")
    
    execution = indexer.executions[execution_id]
    
    # Read status file if exists
    status_content = None
    if execution.status_file_path:
        status_file = repo_root / execution.status_file_path
        if status_file.exists():
            try:
                status_content = status_file.read_text(encoding='utf-8')
            except (UnicodeDecodeError, PermissionError):
                pass
    
    return jsonify({
        "id": execution.id,
        "phase": execution.phase,
        "work_order": execution.work_order,
        "status": execution.status,
        "expected_runs": execution.expected_runs,
        "completed_runs": execution.completed_runs,
        "status_file_path": execution.status_file_path,
        "status_content": status_content,
        "archive_path": execution.archive_path
    })


@app.route('/api/evidence', methods=['GET'])
def get_evidence_packs():
    """Get list of all evidence packs"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    evidence_list = []
    for pack_id, pack in indexer.evidence_packs.items():
        evidence_list.append({
            "id": pack.id,
            "type": pack.type,
            "phase": pack.phase,
            "work_order": pack.work_order,
            "directory_path": pack.directory_path,
            "file_count": len(pack.files)
        })
    
    return jsonify({"evidence_packs": evidence_list})


@app.route('/api/evidence/<pack_id>', methods=['GET'])
def get_evidence_pack(pack_id):
    """Get evidence pack details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    if pack_id not in indexer.evidence_packs:
        abort(404, f"Evidence pack {pack_id} not found")
    
    pack = indexer.evidence_packs[pack_id]
    
    return jsonify({
        "id": pack.id,
        "type": pack.type,
        "phase": pack.phase,
        "work_order": pack.work_order,
        "directory_path": pack.directory_path,
        "files": pack.files
    })


@app.route('/api/evidence/<pack_id>/file/<path:file_path>', methods=['GET'])
def get_evidence_file(pack_id, file_path):
    """Get evidence file content"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    if pack_id not in indexer.evidence_packs:
        abort(404, f"Evidence pack {pack_id} not found")
    
    pack = indexer.evidence_packs[pack_id]
    pack_dir = repo_root / pack.directory_path
    
    # Security: prevent path traversal
    requested_file = pack_dir / file_path
    try:
        requested_file.resolve().relative_to(pack_dir.resolve())
    except ValueError:
        abort(403, "Path traversal not allowed")
    
    if not requested_file.exists() or not requested_file.is_file():
        abort(404, f"File not found: {file_path}")
    
    try:
        content = requested_file.read_text(encoding='utf-8')
        
        # Render markdown if .md file
        if file_path.endswith('.md'):
            html_content = markdown.markdown(content, extensions=['fenced_code', 'tables'])
            return jsonify({
                "file_path": file_path,
                "content": html_content,
                "raw_content": content,
                "type": "markdown"
            })
        elif file_path.endswith('.json'):
            try:
                json_data = json.loads(content)
                return jsonify({
                    "file_path": file_path,
                    "content": json_data,
                    "raw_content": content,
                    "type": "json"
                })
            except json.JSONDecodeError:
                return jsonify({
                    "file_path": file_path,
                    "content": content,
                    "raw_content": content,
                    "type": "text"
                })
        else:
            return jsonify({
                "file_path": file_path,
                "content": content,
                "raw_content": content,
                "type": "text"
            })
    except (UnicodeDecodeError, PermissionError) as e:
        abort(500, f"Error reading file: {str(e)}")


@app.route('/api/decisions', methods=['GET'])
def get_decisions():
    """Get list of all decisions"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    decisions_list = []
    for decision_id, decision in indexer.decisions.items():
        decisions_list.append({
            "id": decision.id,
            "phase": decision.phase,
            "work_order": decision.work_order,
            "human_signed": decision.human_signed,
            "file_path": decision.file_path
        })
    
    return jsonify({"decisions": decisions_list})


@app.route('/api/decisions/<decision_id>', methods=['GET'])
def get_decision(decision_id):
    """Get decision details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    # Try exact match first
    if decision_id not in indexer.decisions:
        # Try case-insensitive match
        decision_id_upper = decision_id.upper()
        matching = [d for d in indexer.decisions.keys() if d.upper() == decision_id_upper]
        if not matching:
            abort(404, f"Decision {decision_id} not found")
        decision_id = matching[0]
    
    decision = indexer.decisions[decision_id]
    
    # Read decision file
    decision_file = repo_root / decision.file_path
    if not decision_file.exists():
        abort(404, f"Decision file not found: {decision.file_path}")
    
    try:
        content = decision_file.read_text(encoding='utf-8')
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables'])
    except (UnicodeDecodeError, PermissionError) as e:
        abort(500, f"Error reading decision file: {str(e)}")
    
    return jsonify({
        "id": decision.id,
        "phase": decision.phase,
        "work_order": decision.work_order,
        "file_path": decision.file_path,
        "questions": decision.questions,
        "answers": decision.answers,
        "human_signed": decision.human_signed,
        "content": html_content,
        "raw_content": content
    })


@app.route('/api/traceability', methods=['GET'])
def get_traceability_indexes():
    """Get list of all traceability indexes"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    traceability_list = []
    for trace_id, trace in indexer.traceability_indexes.items():
        traceability_list.append({
            "id": trace.id,
            "phase": trace.phase,
            "file_path": trace.file_path,
            "claim_count": trace.claim_count
        })
    
    return jsonify({"traceability_indexes": traceability_list})


@app.route('/api/traceability/<index_id>', methods=['GET'])
def get_traceability(index_id):
    """Get traceability index details"""
    if not indexer:
        abort(500, "Indexer not initialized")
    
    if index_id not in indexer.traceability_indexes:
        abort(404, f"Traceability index {index_id} not found")
    
    trace = indexer.traceability_indexes[index_id]
    trace_file = repo_root / trace.file_path
    
    if not trace_file.exists():
        abort(404, f"Traceability file not found: {trace.file_path}")
    
    try:
        content = trace_file.read_text(encoding='utf-8')
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables'])
    except (UnicodeDecodeError, PermissionError) as e:
        abort(500, f"Error reading traceability file: {str(e)}")
    
    return jsonify({
        "id": trace.id,
        "phase": trace.phase,
        "file_path": trace.file_path,
        "claim_count": trace.claim_count,
        "content": html_content,
        "raw_content": content
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": str(error)}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": str(error)}), 500


if __name__ == '__main__':
    import sys
    
    # Get repository root (default to parent directory)
    if len(sys.argv) > 1:
        repo_root_arg = sys.argv[1]
    else:
        # Default to parent of s1_ui directory
        repo_root_arg = str(Path(__file__).parent.parent.resolve())
    
    print(f"Initializing indexer for repository: {repo_root_arg}")
    init_indexer(repo_root_arg)
    
    # Try port 5000 first, fallback to 5001 if occupied
    import socket
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 5000))
    sock.close()
    if result == 0:
        port = 5001
        print(f"Port 5000 is in use, using port {port} instead")
    
    print(f"Starting S1 Operator UI server on http://127.0.0.1:{port}")
    print("Press Ctrl+C to stop")
    
    # Run server (local only, no external access)
    app.run(host='127.0.0.1', port=port, debug=False)

