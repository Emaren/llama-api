# backend/agent_emergent_behavior_api.py
# API for emergent behavior logging and analysis in agent groups.

from fastapi import APIRouter, Query
from backend.agent_emergent_behavior_analyzer import AgentEmergentBehaviorAnalyzer

router = APIRouter()
emergent_behavior = AgentEmergentBehaviorAnalyzer()

@router.post("/emergent_behavior/log")
def log_behavior(behavior: str = Query(...), group_id: str = Query(...), description: str = Query(...)):
    entry = emergent_behavior.log_behavior(behavior, group_id, description)
    return {"status": "behavior logged", "entry": entry}

@router.get("/emergent_behavior/list")
def get_behaviors(group_id: str = Query(None)):
    return emergent_behavior.get_behaviors(group_id)
