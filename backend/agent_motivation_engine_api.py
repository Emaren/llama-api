# backend/agent_motivation_engine_api.py
# API endpoints for managing agent motivation logs and queries.

from fastapi import APIRouter, Query
from backend.agent_motivation_engine import AgentMotivationEngine

router = APIRouter()
motivation_engine = AgentMotivationEngine()

@router.post("/motivation/log/{agent_id}")
def log_motivation(agent_id: str, type: str = Query(...), intensity: float = Query(...), reason: str = Query(...)):
    motivation_engine.log_motivation(agent_id, type, intensity, reason)
    return {"status": "motivation logged"}

@router.get("/motivation/latest/{agent_id}")
def get_latest(agent_id: str):
    return motivation_engine.get_latest(agent_id)

@router.get("/motivation/history/{agent_id}")
def get_history(agent_id: str):
    return motivation_engine.get_history(agent_id)
