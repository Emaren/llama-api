# backend/agent_contextual_adaptation_api.py
# API endpoints to manage agent contextual adaptation.

from fastapi import APIRouter, Query
from backend.agent_contextual_adaptation import AgentContextualAdaptation

router = APIRouter()
context_adapt = AgentContextualAdaptation()

@router.post("/context/update/{agent_id}")
def update_context(agent_id: str, context_key: str = Query(...), context_value: str = Query(...)):
    context_adapt.update_context(agent_id, context_key, context_value)
    return {"status": "context updated"}

@router.get("/context/get/{agent_id}")
def get_context(agent_id: str, context_key: str = Query(...)):
    value = context_adapt.get_context(agent_id, context_key)
    return {"context_key": context_key, "context_value": value}

@router.post("/context/adapt_behavior/{agent_id}")
def adapt_behavior(agent_id: str, base_behavior: str = Query(...)):
    adapted = context_adapt.adapt_behavior(agent_id, base_behavior)
    return {"adapted_behavior": adapted}
