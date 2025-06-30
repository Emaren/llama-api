# backend/agent_influence_propagator_api.py
# API for influence propagation in agent social networks.

from fastapi import APIRouter, Query
from backend.agent_influence_propagator import AgentInfluencePropagator

router = APIRouter()
influencer = AgentInfluencePropagator()

@router.post("/influence/set/{agent_id}")
def set_influence(agent_id: str, peer_id: str = Query(...), strength: float = Query(...)):
    influencer.set_influence(agent_id, peer_id, strength)
    return {"status": "influence set"}

@router.post("/influence/propagate/{agent_id}")
def propagate(agent_id: str, strength: float = Query(1.0)):
    result = influencer.propagate(agent_id, strength)
    return {"propagated": result}

@router.get("/influence/get/{agent_id}")
def get_influence(agent_id: str):
    return influencer.get_influence(agent_id)
