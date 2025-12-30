#!/usr/bin/env python3
"""
Cache Pool - Configurable Cache/Reuse Layer (Guard Constrained)

This module provides a configurable cache/pool layer for Epoch operations.
All caching is GUARD-CONSTRAINED and must be destroyed at Epoch end.
"""

from typing import Dict, Any, Optional, Callable
import threading
import hashlib


class CachePool:
    """
    Cache pool for Epoch operations (guard-constrained).
    
    Properties:
    - Configurable cache size
    - Guard-constrained: Must be destroyed at Epoch end
    - No cross-Epoch persistence
    - Thread-safe (per-pool lock)
    """
    
    def __init__(self, max_size: int = 100, epoch_id: Optional[str] = None):
        """
        Initialize cache pool.
        
        Args:
            max_size: Maximum cache size
            epoch_id: Optional Epoch ID for this pool instance
        """
        self._epoch_id = epoch_id
        self._max_size = max_size
        self._cache: Dict[str, Any] = {}
        self._lock = threading.Lock()  # Per-pool lock (not global)
        self._destroyed = False
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Optional[Any]: Cached value or None
        """
        if self._destroyed:
            raise RuntimeError("CachePool has been destroyed.")
        
        with self._lock:
            return self._cache.get(key)
    
    def set(self, key: str, value: Any):
        """
        Set value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
        """
        if self._destroyed:
            raise RuntimeError("CachePool has been destroyed.")
        
        with self._lock:
            # Evict if at max size (FIFO)
            if len(self._cache) >= self._max_size:
                # Remove oldest entry (simple FIFO)
                oldest_key = next(iter(self._cache))
                del self._cache[oldest_key]
            
            self._cache[key] = value
    
    def has(self, key: str) -> bool:
        """
        Check if key exists in cache.
        
        Args:
            key: Cache key
            
        Returns:
            bool: True if key exists
        """
        if self._destroyed:
            raise RuntimeError("CachePool has been destroyed.")
        
        with self._lock:
            return key in self._cache
    
    def clear(self):
        """
        Clear all cache entries.
        """
        if self._destroyed:
            raise RuntimeError("CachePool has been destroyed.")
        
        with self._lock:
            self._cache.clear()
    
    def get_size(self) -> int:
        """
        Get current cache size.
        
        Returns:
            int: Cache size
        """
        if self._destroyed:
            return 0
        
        with self._lock:
            return len(self._cache)
    
    def get_state_snapshot(self) -> Dict[str, Any]:
        """
        Get state snapshot for verification.
        
        Returns:
            Dict: State snapshot
        """
        if self._destroyed:
            return {"destroyed": True}
        
        with self._lock:
            return {
                "epoch_id": self._epoch_id,
                "max_size": self._max_size,
                "current_size": len(self._cache),
                "keys": list(self._cache.keys()),
                "destroyed": False
            }
    
    def destroy(self):
        """
        Explicitly destroy cache pool state.
        
        This MUST be called at Epoch end to prevent cross-Epoch leakage.
        """
        with self._lock:
            self._cache.clear()
        
        self._epoch_id = None
        self._destroyed = True
    
    def is_destroyed(self) -> bool:
        """Check if destroyed."""
        return self._destroyed


# No global state
# No singleton
# No module-level variables
# GUARD-CONSTRAINED: Must be destroyed at Epoch end

