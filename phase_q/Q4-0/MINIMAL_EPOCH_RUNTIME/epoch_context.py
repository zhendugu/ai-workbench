#!/usr/bin/env python3
"""
Epoch Context - Epoch-Local State Container

This module provides the sole container for Epoch-local state.
No global access. No implicit access. No persistence.
"""

from typing import Dict, Any, Optional
import hashlib


class EpochContext:
    """
    Container for all Epoch-local state.
    
    Properties:
    - Created at Epoch start
    - Destroyed at Epoch end
    - No global access
    - No implicit access
    """
    
    def __init__(self, epoch_id: str):
        """
        Initialize Epoch context.
        
        Args:
            epoch_id: Unique identifier for this Epoch
        """
        self._epoch_id = epoch_id
        self._data: Dict[str, Any] = {}
        self._destroyed = False
    
    def get_epoch_id(self) -> str:
        """Get epoch_id."""
        if self._destroyed:
            raise RuntimeError("EpochContext has been destroyed.")
        return self._epoch_id
    
    def set(self, key: str, value: Any):
        """
        Set a value in context.
        
        Args:
            key: Key name
            value: Value (must be serializable for state snapshot)
        """
        if self._destroyed:
            raise RuntimeError("EpochContext has been destroyed.")
        self._data[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value from context.
        
        Args:
            key: Key name
            default: Default value if key not found
            
        Returns:
            Value or default
        """
        if self._destroyed:
            raise RuntimeError("EpochContext has been destroyed.")
        return self._data.get(key, default)
    
    def has(self, key: str) -> bool:
        """
        Check if key exists.
        
        Args:
            key: Key name
            
        Returns:
            bool: True if key exists
        """
        if self._destroyed:
            raise RuntimeError("EpochContext has been destroyed.")
        return key in self._data
    
    def get_all(self) -> Dict[str, Any]:
        """
        Get all data (copy).
        
        Returns:
            dict: Copy of all data
        """
        if self._destroyed:
            raise RuntimeError("EpochContext has been destroyed.")
        return self._data.copy()
    
    def get_state_snapshot(self) -> Dict[str, Any]:
        """
        Get state snapshot for hashing/verification.
        
        Returns:
            dict: State snapshot
        """
        if self._destroyed:
            return {"destroyed": True}
        
        return {
            "epoch_id": self._epoch_id,
            "data": self._data.copy(),
            "data_count": len(self._data),
            "destroyed": False
        }
    
    def destroy(self):
        """
        Explicitly destroy all state.
        
        This method must ensure complete destruction.
        """
        # Clear all data
        self._data.clear()
        
        # Mark as destroyed
        self._destroyed = True
        
        # Clear epoch_id reference
        self._epoch_id = None
    
    def is_destroyed(self) -> bool:
        """Check if destroyed."""
        return self._destroyed


# No global state
# No singleton
# No module-level variables

