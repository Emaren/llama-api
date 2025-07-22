"""
memory_decay.py – Defines rules for pruning memory traces based on time decay or priority.
"""

from backend.shared.memory_types import MemoryTrace
import datetime

def should_prune(trace: MemoryTrace) -> bool:
    """Simple rule: prune if trace is older than 24 hours."""
    if not hasattr(trace, "timestamp") or not isinstance(trace.timestamp, datetime.datetime):
        return False
    return (datetime.datetime.utcnow() - trace.timestamp).total_seconds() > 86400
