# backend/agent_self_repair_api.py
# API for managing autonomous self-repair logs and retrieval.

from fastapi import APIRouter, Query
from backend.agent_self_repair import AgentSelfRepair

router = APIRouter()
repair = AgentSelfRepair()

@router.post("/self_repair/log/{agent_id}")
def log_repair(agent_id: str, issue: str = Query(...), action: str = Query(...)):
    return repair.log_repair(agent_id, issue, action)

@router.get("/self_repair/history/{agent_id}")
def get_repair_history(agent_id: str):
    return repair.get_repair_history(agent_id)
