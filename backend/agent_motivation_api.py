# backend/agent_motivation_api.py
# API endpoints to manage agent motivation states.

from fastapi import APIRouter, Query
from backend.agent_motivation_engine import AgentMotivationEngine

router = APIRouter()
motivation_engine = AgentMotivationEngine()

@router.post("/motivation/set/{agent_id}")
def set_motivation(agent_id: str, motivation: str = Query(...), level: float = Query(...)):
    motivation_engine.set_motivation(agent_id, motivation, level)
    return {"status": "motivation set", "motivation": motivation, "level": level}

@router.get("/motivation/get/{agent_id}")
def get_motivation(agent_id: str, motivation: str = Query(...)):
    level = motivation_engine.get_motivation(agent_id, motivation)
    return {"motivation": motivation, "level": level}

@router.get("/motivation/all/{agent_id}")
def get_all_motivations(agent_id: str):
    return motivation_engine.get_all_motivations(agent_id)
