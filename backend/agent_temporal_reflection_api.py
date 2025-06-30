# backend/agent_temporal_reflection_api.py
# API for querying temporal introspection insights for agents.

from fastapi import APIRouter
from backend.agent_temporal_reflection import AgentTemporalReflection

router = APIRouter()
reflector = AgentTemporalReflection()

@router.get("/temporal_reflection/{agent_id}")
def temporal_reflection(agent_id: str):
    return reflector.reflect(agent_id)
