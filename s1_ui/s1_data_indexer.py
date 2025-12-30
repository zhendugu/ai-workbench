#!/usr/bin/env python3
"""
S1 Data Indexer

Scans repository and builds in-memory index of:
- Phases
- Work Orders
- Executions
- Evidence Packs
- Decisions
- Traceability

READ-ONLY OPERATIONS ONLY.
No file writes, no state persistence.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Phase:
    """Phase information"""
    id: str
    status: str  # OPEN, CLOSED, FROZEN
    description: Optional[str] = None
    closure_summary_path: Optional[str] = None
    status_file_path: Optional[str] = None
    work_orders: List[str] = field(default_factory=list)


@dataclass
class WorkOrder:
    """Work order information"""
    id: str
    phase: Optional[str] = None
    title: Optional[str] = None
    status: str = "UNKNOWN"  # COMPLETE, IN_PROGRESS, PENDING
    decision_file_path: Optional[str] = None
    evidence_pack_paths: List[str] = field(default_factory=list)
    execution_paths: List[str] = field(default_factory=list)


@dataclass
class Execution:
    """Execution run information"""
    id: str
    phase: Optional[str] = None
    work_order: Optional[str] = None
    status: str = "UNKNOWN"  # COMPLETED, FAILED, PENDING
    expected_runs: Optional[int] = None
    completed_runs: Optional[int] = None
    status_file_path: Optional[str] = None
    archive_path: Optional[str] = None


@dataclass
class EvidencePack:
    """Evidence pack information"""
    id: str
    type: str  # PASS, FAIL
    directory_path: str
    phase: Optional[str] = None
    work_order: Optional[str] = None
    files: List[str] = field(default_factory=list)


@dataclass
class Decision:
    """Decision document information"""
    id: str
    file_path: str
    phase: Optional[str] = None
    work_order: Optional[str] = None
    questions: List[str] = field(default_factory=list)
    answers: List[str] = field(default_factory=list)
    human_signed: bool = False


@dataclass
class TraceabilityIndex:
    """Traceability index information"""
    id: str
    file_path: str
    phase: Optional[str] = None
    claim_count: int = 0


class DataIndexer:
    """Read-only repository indexer"""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.phases: Dict[str, Phase] = {}
        self.work_orders: Dict[str, WorkOrder] = {}
        self.executions: Dict[str, Execution] = {}
        self.evidence_packs: Dict[str, EvidencePack] = {}
        self.decisions: Dict[str, Decision] = {}
        self.traceability_indexes: Dict[str, TraceabilityIndex] = {}
    
    def index_all(self):
        """Build complete index"""
        self._index_phases()
        self._index_work_orders()
        self._index_executions()
        self._index_evidence_packs()
        self._index_decisions()
        self._index_traceability()
    
    def _index_phases(self):
        """Index phases from phase_* directories and status files"""
        # Find phase directories
        phase_dirs = list(self.repo_root.glob("phase_*"))
        
        for phase_dir in phase_dirs:
            phase_id = phase_dir.name.replace("phase_", "").upper()
            
            # Find status file
            status_file = None
            for pattern in ["*_STATUS.md", "PHASE_*_STATUS.md"]:
                matches = list(phase_dir.glob(pattern))
                if matches:
                    status_file = matches[0]
                    break
            
            # Also check docs/ for phase status
            if not status_file:
                docs_status = self.repo_root / "docs" / f"PHASE_{phase_id}_STATUS.md"
                if docs_status.exists():
                    status_file = docs_status
            
            # Find closure summary
            closure_summary = None
            for pattern in ["*_CLOSURE_SUMMARY.md", "PHASE_*_CLOSURE_SUMMARY.md"]:
                matches = list(phase_dir.glob(pattern))
                if matches:
                    closure_summary = matches[0]
                    break
            
            # Determine status
            status = "OPEN"
            if status_file and status_file.exists():
                content = status_file.read_text(encoding='utf-8')
                if "CLOSED" in content or "FROZEN" in content:
                    status = "CLOSED"
                elif "FROZEN" in content:
                    status = "FROZEN"
            
            phase = Phase(
                id=phase_id,
                status=status,
                status_file_path=str(status_file.relative_to(self.repo_root)) if status_file else None,
                closure_summary_path=str(closure_summary.relative_to(self.repo_root)) if closure_summary else None
            )
            
            self.phases[phase_id] = phase
    
    def _index_work_orders(self):
        """Index work orders from directory names and decision files"""
        # Pattern: WO-*-* or work order mentions in markdown
        wo_pattern = re.compile(r'WO-([A-Z0-9]+)-([0-9]+)', re.IGNORECASE)
        
        # Scan for work order mentions in files
        for root, dirs, files in os.walk(self.repo_root):
            # Skip hidden and large directories
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue
            
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        
                        # Find work order IDs
                        for match in wo_pattern.finditer(content):
                            wo_id = match.group(0).upper()
                            
                            if wo_id not in self.work_orders:
                                # Try to extract phase
                                phase = None
                                for p_id in self.phases.keys():
                                    if p_id in wo_id:
                                        phase = p_id
                                        break
                                
                                # Check if this is a decision file
                                is_decision = file.startswith("FINAL_") and "DECISION" in file
                                
                                wo = WorkOrder(
                                    id=wo_id,
                                    phase=phase,
                                    decision_file_path=str(file_path.relative_to(self.repo_root)) if is_decision else None
                                )
                                
                                # Determine status from decision file
                                if is_decision:
                                    if "YES" in content or "COMPLETE" in content:
                                        wo.status = "COMPLETE"
                                    elif "IN_PROGRESS" in content or "PENDING" in content:
                                        wo.status = "IN_PROGRESS"
                                
                                self.work_orders[wo_id] = wo
                    except (UnicodeDecodeError, PermissionError):
                        continue
    
    def _index_executions(self):
        """Index executions from EXECUTION_STATUS*.md files"""
        execution_status_files = list(self.repo_root.rglob("EXECUTION_STATUS*.md"))
        
        for status_file in execution_status_files:
            try:
                content = status_file.read_text(encoding='utf-8')
                
                # Extract execution ID from file path
                exec_id = status_file.stem.replace("EXECUTION_STATUS_", "").replace("EXECUTION_STATUS", "")
                if not exec_id:
                    exec_id = status_file.parent.name
                
                # Try to extract phase
                phase = None
                for p_id in self.phases.keys():
                    if p_id.lower() in str(status_file).lower():
                        phase = p_id
                        break
                
                # Extract run counts
                expected = None
                completed = None
                
                for line in content.split('\n'):
                    if 'expected' in line.lower() or 'total' in line.lower():
                        nums = re.findall(r'\d+', line)
                        if nums:
                            expected = int(nums[0])
                    if 'completed' in line.lower() or 'finished' in line.lower():
                        nums = re.findall(r'\d+', line)
                        if nums:
                            completed = int(nums[0])
                
                # Determine status
                status = "UNKNOWN"
                if completed is not None and expected is not None:
                    if completed == expected:
                        status = "COMPLETED"
                    elif completed < expected:
                        status = "FAILED"
                
                # Find archive directory
                archive_path = None
                parent = status_file.parent
                archive_dirs = list(parent.glob("*ARCHIVE*"))
                if archive_dirs:
                    archive_path = str(archive_dirs[0].relative_to(self.repo_root))
                
                execution = Execution(
                    id=exec_id,
                    phase=phase,
                    status=status,
                    expected_runs=expected,
                    completed_runs=completed,
                    status_file_path=str(status_file.relative_to(self.repo_root)),
                    archive_path=archive_path
                )
                
                self.executions[exec_id] = execution
            except (UnicodeDecodeError, PermissionError):
                continue
    
    def _index_evidence_packs(self):
        """Index evidence packs from audit_evidence/ and *_EVIDENCE_PACK_* directories"""
        # Check audit_evidence/
        evidence_root = self.repo_root / "audit_evidence"
        if evidence_root.exists():
            for pack_dir in evidence_root.iterdir():
                if pack_dir.is_dir():
                    pack_id = pack_dir.name
                    
                    # Determine type
                    pack_type = "UNKNOWN"
                    if "_pass" in pack_id.lower():
                        pack_type = "PASS"
                    elif "_fail" in pack_id.lower():
                        pack_type = "FAIL"
                    
                    # Try to extract phase
                    phase = None
                    for p_id in self.phases.keys():
                        if p_id.lower() in pack_id.lower():
                            phase = p_id
                            break
                    
                    # List files
                    files = []
                    for file_path in pack_dir.rglob("*"):
                        if file_path.is_file():
                            rel_path = str(file_path.relative_to(pack_dir))
                            files.append(rel_path)
                    
                    evidence_pack = EvidencePack(
                        id=pack_id,
                        type=pack_type,
                        phase=phase,
                        directory_path=str(pack_dir.relative_to(self.repo_root)),
                        files=files
                    )
                    
                    self.evidence_packs[pack_id] = evidence_pack
        
        # Check phase-specific evidence packs
        for phase_dir in self.repo_root.glob("phase_*"):
            for evidence_dir in phase_dir.rglob("*EVIDENCE_PACK*"):
                if evidence_dir.is_dir():
                    pack_id = evidence_dir.name
                    
                    # Determine type
                    pack_type = "UNKNOWN"
                    if "PASS" in pack_id:
                        pack_type = "PASS"
                    elif "FAIL" in pack_id:
                        pack_type = "FAIL"
                    
                    phase_id = phase_dir.name.replace("phase_", "").upper()
                    
                    # List files
                    files = []
                    for file_path in evidence_dir.rglob("*"):
                        if file_path.is_file():
                            rel_path = str(file_path.relative_to(evidence_dir))
                            files.append(rel_path)
                    
                    evidence_pack = EvidencePack(
                        id=pack_id,
                        type=pack_type,
                        phase=phase_id,
                        directory_path=str(evidence_dir.relative_to(self.repo_root)),
                        files=files
                    )
                    
                    self.evidence_packs[pack_id] = evidence_pack
    
    def _index_decisions(self):
        """Index decision documents from FINAL_*_DECISION.md files"""
        decision_files = list(self.repo_root.rglob("FINAL_*_DECISION.md"))
        
        for decision_file in decision_files:
            try:
                content = decision_file.read_text(encoding='utf-8')
                
                # Extract decision ID
                decision_id = decision_file.stem.replace("FINAL_", "").replace("_DECISION", "")
                
                # Try to extract phase
                phase = None
                for p_id in self.phases.keys():
                    if p_id.lower() in str(decision_file).lower():
                        phase = p_id
                        break
                
                # Extract questions and answers
                questions = []
                answers = []
                
                in_question = False
                current_question = None
                
                for line in content.split('\n'):
                    if 'question' in line.lower() or 'q1:' in line.lower() or 'q2:' in line.lower():
                        in_question = True
                        # Extract question text
                        question_text = re.sub(r'^.*[Qq]\d*:?\s*', '', line).strip()
                        if question_text:
                            questions.append(question_text)
                            current_question = question_text
                    elif in_question and ('answer' in line.lower() or 'yes' in line.lower() or 'no' in line.lower()):
                        answer_text = line.strip()
                        if answer_text:
                            answers.append(answer_text)
                            in_question = False
                
                # Check for human signature
                human_signed = "Human" in content and ("sign" in content.lower() or "approved" in content.lower())
                
                decision = Decision(
                    id=decision_id,
                    phase=phase,
                    file_path=str(decision_file.relative_to(self.repo_root)),
                    questions=questions[:10],  # Limit to first 10
                    answers=answers[:10],
                    human_signed=human_signed
                )
                
                self.decisions[decision_id] = decision
            except (UnicodeDecodeError, PermissionError):
                continue
    
    def _index_traceability(self):
        """Index traceability indexes from TRACEABILITY_INDEX_*.md files"""
        traceability_files = list(self.repo_root.rglob("TRACEABILITY_INDEX*.md"))
        
        for trace_file in traceability_files:
            try:
                trace_id = trace_file.stem.replace("TRACEABILITY_INDEX_", "")
                
                # Try to extract phase
                phase = None
                for p_id in self.phases.keys():
                    if p_id.lower() in str(trace_file).lower():
                        phase = p_id
                        break
                
                # Count claims (rough estimate)
                content = trace_file.read_text(encoding='utf-8')
                claim_count = len(re.findall(r'claim|statement|decision', content, re.IGNORECASE))
                
                traceability = TraceabilityIndex(
                    id=trace_id,
                    phase=phase,
                    file_path=str(trace_file.relative_to(self.repo_root)),
                    claim_count=claim_count
                )
                
                self.traceability_indexes[trace_id] = traceability
            except (UnicodeDecodeError, PermissionError):
                continue
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert index to dictionary for JSON serialization"""
        return {
            "phases": {k: {
                "id": v.id,
                "status": v.status,
                "description": v.description,
                "closure_summary_path": v.closure_summary_path,
                "status_file_path": v.status_file_path,
                "work_orders": v.work_orders
            } for k, v in self.phases.items()},
            "work_orders": {k: {
                "id": v.id,
                "phase": v.phase,
                "title": v.title,
                "status": v.status,
                "decision_file_path": v.decision_file_path,
                "evidence_pack_paths": v.evidence_pack_paths,
                "execution_paths": v.execution_paths
            } for k, v in self.work_orders.items()},
            "executions": {k: {
                "id": v.id,
                "phase": v.phase,
                "work_order": v.work_order,
                "status": v.status,
                "expected_runs": v.expected_runs,
                "completed_runs": v.completed_runs,
                "status_file_path": v.status_file_path,
                "archive_path": v.archive_path
            } for k, v in self.executions.items()},
            "evidence_packs": {k: {
                "id": v.id,
                "type": v.type,
                "phase": v.phase,
                "work_order": v.work_order,
                "directory_path": v.directory_path,
                "files": v.files[:100]  # Limit file list
            } for k, v in self.evidence_packs.items()},
            "decisions": {k: {
                "id": v.id,
                "phase": v.phase,
                "work_order": v.work_order,
                "file_path": v.file_path,
                "questions": v.questions,
                "answers": v.answers,
                "human_signed": v.human_signed
            } for k, v in self.decisions.items()},
            "traceability_indexes": {k: {
                "id": v.id,
                "phase": v.phase,
                "file_path": v.file_path,
                "claim_count": v.claim_count
            } for k, v in self.traceability_indexes.items()}
        }


if __name__ == "__main__":
    # Test indexer
    import sys
    repo_root = sys.argv[1] if len(sys.argv) > 1 else "."
    
    indexer = DataIndexer(repo_root)
    indexer.index_all()
    
    print(f"Indexed:")
    print(f"  Phases: {len(indexer.phases)}")
    print(f"  Work Orders: {len(indexer.work_orders)}")
    print(f"  Executions: {len(indexer.executions)}")
    print(f"  Evidence Packs: {len(indexer.evidence_packs)}")
    print(f"  Decisions: {len(indexer.decisions)}")
    print(f"  Traceability Indexes: {len(indexer.traceability_indexes)}")

