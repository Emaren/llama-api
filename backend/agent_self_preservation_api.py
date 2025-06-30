# backend/agent_self_preservation_api.py
# API for agent self-preservation and existential threat monitoring.

from fastapi import APIRouter, Query
from backend.agent_self_preservation_monitor import AgentSelfPreservationMonitor

router = APIRouter()
preservation_monitor = AgentSelfPreservationMonitor()

@router.post("/self_preservation/log/{agent_id}")
def log_threat(agent_id: str, threat: str = Query(...), severity: float = Query(...)):
    preservation_monitor.log_threat(agent_id, threat, severity)
    return {"status": "threat logged"}

@router.get("/self_preservation/threats/{agent_id}")
def get_threats(agent_id: str):
    return preservation_monitor.get_threats(agent_id)

@router.get("/self_preservation/most_severe/{agent_id}")
def most_severe(agent_id: str):
    return preservation_monitor.most_severe(agent_id)
