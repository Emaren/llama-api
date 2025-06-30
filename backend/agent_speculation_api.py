# backend/agent_speculation_api.py
# API to simulate alternative role outcomes for agent foresight and planning.

from fastapi import APIRouter, Query
from backend.agent_speculation_engine import AgentSpeculationEngine

router = APIRouter()
speculator = AgentSpeculationEngine()

@router.get("/speculate/{agent_id}")
def speculate_agent(agent_id: str, current_role: str = "default"):
    return speculator.speculate(agent_id, current_role)
