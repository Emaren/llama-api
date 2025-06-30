# backend/routes/agent_events.py

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("")
async def list_agent_events():
    now = datetime.utcnow().isoformat() + "Z"
    return {
        "events": [
            {"agent": "GoalOptimizer", "timestamp": now, "message": "Reprioritized tasks based on engagement."},
            {"agent": "ContextEngine",   "timestamp": now, "message": "Scoped context to last 1024 tokens."},
            {"agent": "BiasTracker",     "timestamp": now, "message": "Adjusted bias vector after feedback."}
        ]
    }
