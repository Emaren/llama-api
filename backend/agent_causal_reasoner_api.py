# backend/agent_causal_reasoner_api.py
# API endpoints for agent causal reasoning.

from fastapi import APIRouter, Query
from backend.agent_causal_reasoner import AgentCausalReasoner

router = APIRouter()
causal = AgentCausalReasoner()

@router.post("/causal/add/{agent_id}")
def add_causal_relation(agent_id: str, cause: str = Query(...), effect: str = Query(...)):
    causal.add_causal_relation(agent_id, cause, effect)
    return {"status": "causal relation added"}

@router.get("/causal/effects/{agent_id}")
def get_effects(agent_id: str, cause: str = Query(...)):
    return {"effects": causal.get_effects(agent_id, cause)}

@router.get("/causal/causes/{agent_id}")
def get_causes(agent_id: str, effect: str = Query(...)):
    return {"causes": causal.get_causes(agent_id, effect)}
