# backend/agent_emergent_intelligence_api.py
# API for emergent intelligence event tracking.

from fastapi import APIRouter, Query
from backend.agent_emergent_intelligence import AgentEmergentIntelligence
import json

router = APIRouter()
emergent = AgentEmergentIntelligence()

@router.post("/emergent_intelligence/log")
def log_event(description: str = Query(...), involved_agents: str = Query(...), metric: float = Query(...)):
    # involved_agents must be passed as JSON-encoded list
    agent_list = json.loads(involved_agents)
    event = emergent.log_event(description, agent_list, metric)
    return {"status": "event logged", "event": event}

@router.get("/emergent_intelligence/events")
def get_events():
    return emergent.get_events()

@router.get("/emergent_intelligence/events_by_agent/{agent_id}")
def get_events_by_agent(agent_id: str):
    return emergent.get_events_by_agent(agent_id)
