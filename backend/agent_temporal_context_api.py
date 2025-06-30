# backend/agent_temporal_context_api.py
# API for querying and updating temporal context of agents.

from fastapi import APIRouter, Query
from backend.agent_temporal_context import AgentTemporalContext

router = APIRouter()
temporal = AgentTemporalContext()

@router.post("/temporal/update/{agent_id}")
def update_timestamp(agent_id: str, key: str = Query(...)):
    temporal.update_timestamp(agent_id, key)
    return {"status": "timestamp updated", "key": key}

@router.get("/temporal/state/{agent_id}")
def get_temporal_state(agent_id: str):
    return temporal.get_temporal_state(agent_id)
