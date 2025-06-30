# backend/agent_emergence_api.py
# API to observe and surface emergent behaviors in agents.

from fastapi import APIRouter, Query
from backend.agent_emergence_tracker import AgentEmergenceTracker

router = APIRouter()
tracker = AgentEmergenceTracker()

@router.post("/emergence/{agent_id}")
def record_emergence(agent_id: str, pattern: str = Query(...), context: str = ""):
    return tracker.record_emergence(agent_id, pattern, context)

@router.get("/emergence/history/{agent_id}")
def get_emergence(agent_id: str):
    return tracker.get_emergence_events(agent_id)
