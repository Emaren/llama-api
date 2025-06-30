# backend/agent_role_evolution_api.py
# API endpoints for managing and evolving agent roles.

from fastapi import APIRouter, Query
from backend.agent_role_evolution import AgentRoleEvolution

router = APIRouter()
evolution = AgentRoleEvolution()

@router.post("/role/record/{agent_id}")
def record_role(agent_id: str, role: str = Query(...), reason: str = "manual"):
    evolution.record_role(agent_id, role, reason)
    return {"status": "recorded"}

@router.get("/role/history/{agent_id}")
def get_role_history(agent_id: str):
    return evolution.get_role_history(agent_id)

@router.get("/role/suggest/{agent_id}")
def suggest_next_role(agent_id: str):
    return {"suggested_role": evolution.suggest_next_role(agent_id)}
