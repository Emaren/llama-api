# backend/agent_intent_disambiguator_api.py
# API endpoints for intent disambiguation and resolution.

from fastapi import APIRouter, Query
from backend.agent_intent_disambiguator import AgentIntentDisambiguator
from datetime import datetime

router = APIRouter()
disambiguator = AgentIntentDisambiguator()

@router.post("/intent/log/{agent_id}")
def log_intent(agent_id: str, intent: str = Query(...), context: str = Query(...)):
    timestamp = datetime.utcnow().isoformat()
    disambiguator.log_intent(agent_id, intent, context, timestamp)
    return {"status": "intent logged"}

@router.get("/intent/disambiguate/{agent_id}")
def disambiguate(agent_id: str, ambiguous_intent: str = Query(...)):
    return disambiguator.disambiguate(agent_id, ambiguous_intent)
