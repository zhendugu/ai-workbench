#!/usr/bin/env python3
"""
Concurrency Adapter - Concurrent Epoch Operations

This module provides concurrent/async wrappers for Epoch operations.
No automatic behavior. No optimization. Explicit concurrency only.
"""

import threading
import asyncio
import queue
from typing import List, Callable, Any, Optional
from concurrent.futures import ThreadPoolExecutor, Future
import random

# Import Q-4-0 baseline (do not modify)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../Q4-0/MINIMAL_EPOCH_RUNTIME'))
from epoch_controller import EpochController


class ConcurrencyAdapter:
    """
    Adapter for concurrent Epoch operations.
    
    Properties:
    - Wraps Q-4-0 EpochController
    - Provides thread-safe operations
    - Supports async/await
    - No state persistence across Epochs
    """
    
    def __init__(self, num_threads: int = 1, num_coroutines: int = 1):
        """
        Initialize adapter.
        
        Args:
            num_threads: Number of threads for thread pool
            num_coroutines: Number of concurrent coroutines
        """
        self._num_threads = num_threads
        self._num_coroutines = num_coroutines
        self._executor = ThreadPoolExecutor(max_workers=num_threads)
        self._lock = threading.Lock()  # Per-adapter lock (not global)
        
        # Per-adapter state (not global, destroyed with adapter)
        self._active_epochs = {}  # epoch_id -> controller
        self._destroyed = False
    
    def start_epoch_async(self, seed: Optional[int] = None) -> Future:
        """
        Start Epoch asynchronously.
        
        Args:
            seed: Optional seed for reproducibility
            
        Returns:
            Future: Future containing epoch_id
        """
        if self._destroyed:
            raise RuntimeError("ConcurrencyAdapter has been destroyed.")
        
        def _start():
            with self._lock:
                controller = EpochController()
                epoch_id = controller.start_epoch()
                self._active_epochs[epoch_id] = controller
                return epoch_id
        
        return self._executor.submit(_start)
    
    def end_epoch_async(self, epoch_id: str) -> Future:
        """
        End Epoch asynchronously.
        
        Args:
            epoch_id: Epoch ID to end
            
        Returns:
            Future: Future containing end report
        """
        if self._destroyed:
            raise RuntimeError("ConcurrencyAdapter has been destroyed.")
        
        def _end():
            with self._lock:
                if epoch_id not in self._active_epochs:
                    raise RuntimeError(f"Epoch {epoch_id} not found.")
                
                controller = self._active_epochs[epoch_id]
                report = controller.end_epoch()
                del self._active_epochs[epoch_id]
                return report
        
        return self._executor.submit(_end)
    
    async def start_epoch_coro(self, seed: Optional[int] = None) -> str:
        """
        Start Epoch as coroutine.
        
        Args:
            seed: Optional seed for reproducibility
            
        Returns:
            epoch_id: Epoch ID
        """
        if self._destroyed:
            raise RuntimeError("ConcurrencyAdapter has been destroyed.")
        
        loop = asyncio.get_event_loop()
        
        def _start():
            with self._lock:
                controller = EpochController()
                epoch_id = controller.start_epoch()
                self._active_epochs[epoch_id] = controller
                return epoch_id
        
        epoch_id = await loop.run_in_executor(self._executor, _start)
        return epoch_id
    
    async def end_epoch_coro(self, epoch_id: str) -> dict:
        """
        End Epoch as coroutine.
        
        Args:
            epoch_id: Epoch ID to end
            
        Returns:
            dict: End report
        """
        if self._destroyed:
            raise RuntimeError("ConcurrencyAdapter has been destroyed.")
        
        loop = asyncio.get_event_loop()
        
        def _end():
            with self._lock:
                if epoch_id not in self._active_epochs:
                    raise RuntimeError(f"Epoch {epoch_id} not found.")
                
                controller = self._active_epochs[epoch_id]
                report = controller.end_epoch()
                del self._active_epochs[epoch_id]
                return report
        
        report = await loop.run_in_executor(self._executor, _end)
        return report
    
    def run_concurrent_epochs(self, num_epochs: int, seed: Optional[int] = None) -> List[dict]:
        """
        Run multiple Epochs concurrently.
        
        Args:
            num_epochs: Number of concurrent Epochs
            seed: Optional seed for reproducibility
            
        Returns:
            List[dict]: List of end reports
        """
        if self._destroyed:
            raise RuntimeError("ConcurrencyAdapter has been destroyed.")
        
        futures = []
        
        # Start all Epochs
        for i in range(num_epochs):
            future = self.start_epoch_async(seed=seed + i if seed else None)
            futures.append((future, i))
        
        # Wait for all to start
        epoch_ids = []
        for future, _ in futures:
            epoch_id = future.result()
            epoch_ids.append(epoch_id)
        
        # End all Epochs
        end_futures = []
        for epoch_id in epoch_ids:
            end_future = self.end_epoch_async(epoch_id)
            end_futures.append(end_future)
        
        # Wait for all to end
        reports = []
        for end_future in end_futures:
            report = end_future.result()
            reports.append(report)
        
        return reports
    
    def destroy(self):
        """
        Explicitly destroy adapter state.
        """
        # End all active Epochs
        with self._lock:
            for epoch_id, controller in list(self._active_epochs.items()):
                try:
                    controller.end_epoch()
                except:
                    pass
            self._active_epochs.clear()
        
        # Shutdown executor
        self._executor.shutdown(wait=True)
        
        # Mark as destroyed
        self._destroyed = True
    
    def is_destroyed(self) -> bool:
        """Check if destroyed."""
        return self._destroyed


# No global state
# No singleton
# No module-level variables

