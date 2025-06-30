# backend/agent_behavioral_trends_api.py
# API endpoints for managing behavioral trends tracking.

from fastapi import APIRouter, Query
from backend.agent_behavioral_trends import AgentBehavioralTrends

router = APIRouter()
behavior_trends = AgentBehavioralTrends()

@router.post("/behavior/log/{agent_id}")
def log_behavior(agent_id: str, behavior: str = Query(...)):
    behavior_trends.log_behavior(agent_id, behavior)
    return {"status": "behavior logged"}

@router.get("/behavior/trends/{agent_id}")
def get_behavior_trends(agent_id: str):
    return behavior_trends.get_behavior_trends(agent_id)
