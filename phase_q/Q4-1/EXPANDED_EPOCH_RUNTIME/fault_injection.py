#!/usr/bin/env python3
"""
Fault Injection - Timeout, Exception, Cancellation, Interruption

This module provides fault injection for Epoch stress testing.
No automatic retry. No automatic healing. Explicit faults only.
"""

import random
import time
import threading
from typing import Callable, Any, Optional, Dict
from enum import Enum


class FaultType(Enum):
    """Fault types."""
    TIMEOUT = "timeout"
    EXCEPTION = "exception"
    CANCELLATION = "cancellation"
    INTERRUPTION = "interruption"
    PARTIAL_WRITE = "partial_write"
    NONE = "none"


class FaultInjector:
    """
    Fault injector for Epoch operations.
    
    Properties:
    - Configurable fault probabilities
    - No automatic retry
    - No automatic healing
    - Explicit fault injection only
    """
    
    def __init__(
        self,
        timeout_prob: float = 0.0,
        exception_prob: float = 0.0,
        cancellation_prob: float = 0.0,
        interruption_prob: float = 0.0,
        partial_write_prob: float = 0.0,
        seed: Optional[int] = None
    ):
        """
        Initialize fault injector.
        
        Args:
            timeout_prob: Probability of timeout (0.0-1.0)
            exception_prob: Probability of exception (0.0-1.0)
            cancellation_prob: Probability of cancellation (0.0-1.0)
            interruption_prob: Probability of interruption (0.0-1.0)
            partial_write_prob: Probability of partial write (0.0-1.0)
            seed: Random seed for reproducibility
        """
        self._timeout_prob = timeout_prob
        self._exception_prob = exception_prob
        self._cancellation_prob = cancellation_prob
        self._interruption_prob = interruption_prob
        self._partial_write_prob = partial_write_prob
        
        if seed is not None:
            random.seed(seed)
        
        # Per-injector state (not global)
        self._fault_count = 0
        self._destroyed = False
    
    def inject_fault(self, operation: Callable[[], Any]) -> tuple[Any, Optional[FaultType], Optional[Exception]]:
        """
        Inject fault into operation.
        
        Args:
            operation: Operation to execute
            
        Returns:
            tuple: (result, fault_type, exception)
        """
        if self._destroyed:
            raise RuntimeError("FaultInjector has been destroyed.")
        
        # Determine fault type
        fault_type = self._determine_fault_type()
        
        if fault_type == FaultType.TIMEOUT:
            return self._inject_timeout(operation)
        elif fault_type == FaultType.EXCEPTION:
            return self._inject_exception(operation)
        elif fault_type == FaultType.CANCELLATION:
            return self._inject_cancellation(operation)
        elif fault_type == FaultType.INTERRUPTION:
            return self._inject_interruption(operation)
        elif fault_type == FaultType.PARTIAL_WRITE:
            return self._inject_partial_write(operation)
        else:
            # No fault
            try:
                result = operation()
                return (result, None, None)
            except Exception as e:
                return (None, FaultType.EXCEPTION, e)
    
    def _determine_fault_type(self) -> FaultType:
        """Determine fault type based on probabilities."""
        r = random.random()
        cumulative = 0.0
        
        if r < (cumulative := cumulative + self._timeout_prob):
            return FaultType.TIMEOUT
        if r < (cumulative := cumulative + self._exception_prob):
            return FaultType.EXCEPTION
        if r < (cumulative := cumulative + self._cancellation_prob):
            return FaultType.CANCELLATION
        if r < (cumulative := cumulative + self._interruption_prob):
            return FaultType.INTERRUPTION
        if r < (cumulative := cumulative + self._partial_write_prob):
            return FaultType.PARTIAL_WRITE
        
        return FaultType.NONE
    
    def _inject_timeout(self, operation: Callable[[], Any]) -> tuple[Any, FaultType, Optional[Exception]]:
        """Inject timeout fault."""
        # Simulate timeout by raising TimeoutError
        self._fault_count += 1
        return (None, FaultType.TIMEOUT, TimeoutError("Injected timeout"))
    
    def _inject_exception(self, operation: Callable[[], Any]) -> tuple[Any, FaultType, Optional[Exception]]:
        """Inject exception fault."""
        self._fault_count += 1
        return (None, FaultType.EXCEPTION, RuntimeError("Injected exception"))
    
    def _inject_cancellation(self, operation: Callable[[], Any]) -> tuple[Any, FaultType, Optional[Exception]]:
        """Inject cancellation fault."""
        self._fault_count += 1
        return (None, FaultType.CANCELLATION, RuntimeError("Injected cancellation"))
    
    def _inject_interruption(self, operation: Callable[[], Any]) -> tuple[Any, FaultType, Optional[Exception]]:
        """Inject interruption fault."""
        self._fault_count += 1
        return (None, FaultType.INTERRUPTION, RuntimeError("Injected interruption"))
    
    def _inject_partial_write(self, operation: Callable[[], Any]) -> tuple[Any, FaultType, Optional[Exception]]:
        """Inject partial write fault."""
        self._fault_count += 1
        # Execute operation but indicate partial write
        try:
            result = operation()
            return (result, FaultType.PARTIAL_WRITE, RuntimeError("Injected partial write"))
        except Exception as e:
            return (None, FaultType.PARTIAL_WRITE, e)
    
    def get_fault_count(self) -> int:
        """Get total fault count."""
        return self._fault_count
    
    def destroy(self):
        """Explicitly destroy injector state."""
        self._fault_count = 0
        self._destroyed = True
    
    def is_destroyed(self) -> bool:
        """Check if destroyed."""
        return self._destroyed


# No global state
# No singleton
# No module-level variables

