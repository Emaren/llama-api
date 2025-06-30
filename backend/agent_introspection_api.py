# backend/agent_introspection_api.py
# API endpoints to interact with the agent introspection engine.

from fastapi import APIRouter, Query
from backend.agent_introspection_engine import AgentIntrospectionEngine

router = APIRouter()
introspection = AgentIntrospectionEngine()

@router.post("/introspection/update/{agent_id}")
def update_metric(agent_id: str, metric: str = Query(...), value: str = Query(...)):
    introspection.update_metric(agent_id, metric, value)
    return {"status": "metric updated", "metric": metric, "value": value}

@router.get("/introspection/get/{agent_id}")
def get_introspection(agent_id: str):
    return introspection.get_introspection(agent_id)
