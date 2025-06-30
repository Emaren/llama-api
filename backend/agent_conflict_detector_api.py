# backend/agent_conflict_detector_api.py
# API endpoints for managing agent conflict detection records.

from fastapi import APIRouter, Query
from backend.agent_conflict_detector import AgentConflictDetector

router = APIRouter()
conflict_detector = AgentConflictDetector()

@router.post("/conflict/add/{agent_id}")
def add_conflict(agent_id: str, conflict_type: str = Query(...), details: str = Query(...)):
    conflict_detector.add_conflict(agent_id, conflict_type, details)
    return {"status": "conflict logged"}

@router.get("/conflict/list/{agent_id}")
def get_conflicts(agent_id: str):
    return conflict_detector.get_conflicts(agent_id)
