# backend/agent_innovation_api.py
# API endpoints to manage agent innovation logging and retrieval.

from fastapi import APIRouter, Query
from backend.agent_innovation_tracker import AgentInnovationTracker

router = APIRouter()
innovation_tracker = AgentInnovationTracker()

@router.post("/innovation/log/{agent_id}")
def log_innovation(agent_id: str, idea: str = Query(...), context: str = ""):
    return innovation_tracker.log_innovation(agent_id, idea, context)

@router.get("/innovation/history/{agent_id}")
def get_innovation_history(agent_id: str):
    return innovation_tracker.get_innovation_history(agent_id)
