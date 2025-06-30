# backend/agent_knowledge_drift_api.py
# API endpoints for managing knowledge drift tracking.

from fastapi import APIRouter, Query
from backend.agent_knowledge_drift import AgentKnowledgeDrift

router = APIRouter()
drift_tracker = AgentKnowledgeDrift()

@router.post("/knowledge_drift/record/{agent_id}")
def record_snapshot(agent_id: str, snapshot_hash: str = Query(...)):
    drift_tracker.record_snapshot(agent_id, snapshot_hash)
    return {"status": "snapshot recorded"}

@router.get("/knowledge_drift/calculate/{agent_id}")
def calculate_drift(agent_id: str):
    drift = drift_tracker.calculate_drift(agent_id)
    return {"agent_id": agent_id, "drift_ratio": drift}
