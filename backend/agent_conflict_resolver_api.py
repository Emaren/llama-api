# backend/agent_conflict_resolver_api.py
# API for managing conflict resolutions within agents.

from fastapi import APIRouter, Query
from backend.agent_conflict_resolver import AgentConflictResolver

router = APIRouter()
resolver = AgentConflictResolver()

@router.post("/conflict/resolve/{agent_id}")
def resolve_conflict(agent_id: str, conflict_type: str = Query(...), resolution: str = Query(...)):
    return resolver.resolve_conflict(agent_id, conflict_type, resolution)

@router.get("/conflict/resolutions/{agent_id}")
def get_resolutions(agent_id: str):
    return resolver.get_resolutions(agent_id)
