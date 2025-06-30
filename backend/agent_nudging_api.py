# backend/agent_nudging_api.py
# API to deliver nudges that influence agent course correction.

from fastapi import APIRouter, Query
from backend.agent_nudging_engine import AgentNudgingEngine

router = APIRouter()
nudger = AgentNudgingEngine()

@router.post("/nudge/{agent_id}")
def send_nudge(agent_id: str, message: str = Query(...)):
    return nudger.send_nudge(agent_id, message)

@router.get("/nudge/history/{agent_id}")
def get_nudges(agent_id: str):
    return nudger.get_nudges(agent_id)
