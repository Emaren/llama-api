# backend/routes/agents_health.py

from fastapi import APIRouter
import time

router = APIRouter()

def agent_status():
    return [
        {"id": "GoalOptimizer",   "status": "active", "ts": time.time()},
        {"id": "MemoryManager",   "status": "active", "ts": time.time()},
        {"id": "SessionMonitor",  "status": "active", "ts": time.time()},
    ]

@router.get("")  # This aligns with prefix="/api/agents/health" for clean path
def get_health():
    return agent_status()

__all__ = ["router"]
