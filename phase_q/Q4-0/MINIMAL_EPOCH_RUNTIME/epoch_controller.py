#!/usr/bin/env python3
"""
Epoch Controller - Manual Epoch Triggering

This module provides explicit, manual control over Epoch lifecycle.
No automatic behavior. No optimization. No convenience.
"""

import uuid
import hashlib
from typing import Optional
from datetime import datetime

from epoch_context import EpochContext
from epoch_guard import EpochGuard


class EpochController:
    """
    Controller for explicit Epoch lifecycle management.
    
    No automatic behavior.
    No state persistence.
    No optimization.
    """
    
    def __init__(self):
        """Initialize controller. No state persistence."""
        self._current_epoch_id: Optional[str] = None
        self._current_context: Optional[EpochContext] = None
        self._current_guard: Optional[EpochGuard] = None
        self._epoch_count: int = 0  # Ephemeral counter, reset per process
        
    def start_epoch(self) -> str:
        """
        Explicitly start a new Epoch.
        
        Returns:
            epoch_id: Unique identifier for this Epoch
            
        Raises:
            RuntimeError: If previous Epoch not ended
        """
        # Verify previous Epoch ended
        if self._current_epoch_id is not None:
            raise RuntimeError(
                f"Previous Epoch {self._current_epoch_id} not ended. "
                "Must call end_epoch() before starting new Epoch."
            )
        
        # Generate non-deterministic, non-sequential epoch_id
        epoch_id = str(uuid.uuid4())
        
        # Create new context (no state inheritance)
        context = EpochContext(epoch_id)
        
        # Create guard
        guard = EpochGuard(epoch_id)
        
        # Set current state
        self._current_epoch_id = epoch_id
        self._current_context = context
        self._current_guard = guard
        
        # Increment ephemeral counter (process-local, not persistent)
        self._epoch_count += 1
        
        # Compute initial state hash
        initial_hash = self._compute_state_hash()
        guard.record_state_hash("initial", initial_hash)
        
        print(f"[EPOCH] Started: {epoch_id}")
        print(f"[EPOCH] Initial state hash: {initial_hash}")
        
        return epoch_id
    
    def end_epoch(self) -> dict:
        """
        Explicitly end current Epoch.
        
        Returns:
            dict: Epoch end report with state hashes and verification
            
        Raises:
            RuntimeError: If no Epoch is active
        """
        if self._current_epoch_id is None:
            raise RuntimeError("No active Epoch to end.")
        
        epoch_id = self._current_epoch_id
        
        # Compute final state hash before destruction
        final_hash = self._compute_state_hash()
        if self._current_guard is not None:
            self._current_guard.record_state_hash("final", final_hash)
        
        # Guard verification (before destruction)
        guard_report = {}
        if self._current_guard is not None:
            guard_report = self._current_guard.verify_no_leakage()
        
        # Explicitly destroy all state
        self._destroy_epoch_state()
        
        # Verify destruction
        post_destruction_hash = self._compute_state_hash()
        
        # Build report
        report = {
            "epoch_id": epoch_id,
            "final_state_hash": final_hash,
            "post_destruction_hash": post_destruction_hash,
            "guard_report": guard_report,
            "timestamp": datetime.now().isoformat()
        }
        
        # Clear current state (explicit)
        self._current_epoch_id = None
        self._current_context = None
        self._current_guard = None
        
        print(f"[EPOCH] Ended: {epoch_id}")
        print(f"[EPOCH] Final state hash: {final_hash}")
        print(f"[EPOCH] Post-destruction hash: {post_destruction_hash}")
        print(f"[EPOCH] Guard report: {guard_report}")
        
        return report
    
    def get_current_context(self) -> EpochContext:
        """
        Get current Epoch context.
        
        Returns:
            EpochContext: Current context
            
        Raises:
            RuntimeError: If no Epoch is active
        """
        if self._current_context is None:
            raise RuntimeError("No active Epoch. Call start_epoch() first.")
        return self._current_context
    
    def get_current_epoch_id(self) -> Optional[str]:
        """
        Get current epoch_id.
        
        Returns:
            Optional[str]: Current epoch_id or None
        """
        return self._current_epoch_id
    
    def _compute_state_hash(self) -> str:
        """
        Compute hash of current system state.
        
        This includes:
        - EpochContext contents
        - Guard state
        - Controller state (minimal)
        
        Returns:
            str: SHA256 hash of state
        """
        hasher = hashlib.sha256()
        
        # Hash context state
        if self._current_context is not None:
            context_state = self._current_context.get_state_snapshot()
            hasher.update(str(context_state).encode('utf-8'))
        
        # Hash guard state
        if self._current_guard is not None:
            guard_state = self._current_guard.get_state_snapshot()
            hasher.update(str(guard_state).encode('utf-8'))
        
        # Hash controller minimal state
        controller_state = {
            "epoch_id": self._current_epoch_id,
            "epoch_count": self._epoch_count
        }
        hasher.update(str(controller_state).encode('utf-8'))
        
        return hasher.hexdigest()
    
    def _destroy_epoch_state(self):
        """
        Explicitly destroy all Epoch state.
        
        This method must ensure complete destruction.
        """
        # Destroy context (explicit)
        if self._current_context is not None:
            self._current_context.destroy()
            self._current_context = None
        
        # Destroy guard (explicit)
        if self._current_guard is not None:
            self._current_guard.destroy()
            self._current_guard = None
        
        # Note: epoch_id and epoch_count are ephemeral controller state
        # They are reset by setting _current_epoch_id to None above
    
    def get_epoch_count(self) -> int:
        """
        Get ephemeral epoch count (process-local, not persistent).
        
        Returns:
            int: Number of Epochs started in this process
        """
        return self._epoch_count


# No global state
# No singleton
# No module-level variables

