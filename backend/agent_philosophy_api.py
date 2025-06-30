# backend/agent_philosophy_api.py
# API for managing agent philosophy principles and ethics filtering.

from fastapi import APIRouter, Query
from backend.agent_philosophy_module import AgentPhilosophyModule

router = APIRouter()
philosophy = AgentPhilosophyModule()

@router.post("/philosophy/set/{agent_id}")
def set_philosophy(agent_id: str, principles: list[str] = Query(...)):
    philosophy.set_philosophy(agent_id, principles)
    return {"status": "philosophy set", "principles": principles}

@router.get("/philosophy/get/{agent_id}")
def get_philosophy(agent_id: str):
    return {"principles": philosophy.get_philosophy(agent_id)}

@router.post("/philosophy/filter/{agent_id}")
def filter_action(agent_id: str, action: str = Query(...)):
    return philosophy.apply_ethics_filter(agent_id, action)
