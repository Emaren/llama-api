# backend/agent_self_transcendence_api.py
# API for agent self-transcendence and meta-goal tracking.

from fastapi import APIRouter, Query
from backend.agent_self_transcendence_tracker import AgentSelfTranscendenceTracker

router = APIRouter()
transcendence_tracker = AgentSelfTranscendenceTracker()

@router.post("/self_transcendence/log/{agent_id}")
def log_event(agent_id: str, event: str = Query(...), description: str = Query(...)):
    transcendence_tracker.log_event(agent_id, event, description)
    return {"status": "event logged"}

@router.get("/self_transcendence/events/{agent_id}")
def get_events(agent_id: str):
    return transcendence_tracker.get_events(agent_id)
