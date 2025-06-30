# backend/agent_alignment_tracker_api.py
# API for tracking agent alignment to goals, values, and instructions.

from fastapi import APIRouter, Query
from backend.agent_alignment_tracker import AgentAlignmentTracker

router = APIRouter()
tracker = AgentAlignmentTracker()

@router.post("/alignment/log/{agent_id}")
def log_alignment(agent_id: str, score: float = Query(...), reason: str = ""):
    tracker.log_alignment(agent_id, score, reason)
    return {"status": "logged", "score": score, "reason": reason}

@router.get("/alignment/history/{agent_id}")
def get_alignment_history(agent_id: str):
    return tracker.get_alignment_history(agent_id)

@router.get("/alignment/average/{agent_id}")
def get_average_alignment(agent_id: str):
    return {"average_score": tracker.average_alignment(agent_id)}
