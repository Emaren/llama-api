# backend/agent_collective_consciousness_api.py
# API for agent collective consciousness and shared group state.

from fastapi import APIRouter, Query
from backend.agent_collective_consciousness import AgentCollectiveConsciousness

router = APIRouter()
collective = AgentCollectiveConsciousness()

@router.post("/collective_state/update/{group_id}")
def update_shared_state(group_id: str, state: str = Query(...), value: str = Query(...)):
    collective.update_shared_state(group_id, state, value)
    return {"status": "state updated"}

@router.get("/collective_state/get/{group_id}")
def get_shared_state(group_id: str, state: str = Query(...)):
    return {"value": collective.get_shared_state(group_id, state)}

@router.get("/collective_state/all/{group_id}")
def get_all_states(group_id: str):
    return collective.get_all_states(group_id)
