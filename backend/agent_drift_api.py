# backend/agent_drift_api.py
# API to detect behavioral drift in agents.

from fastapi import APIRouter, Query
from backend.agent_drift_detector import AgentDriftDetector

router = APIRouter()
drift_detector = AgentDriftDetector()

@router.get("/drift/{agent_id}")
def detect_drift(agent_id: str, current_task: str = Query(...)):
    return drift_detector.detect_drift(agent_id, current_task)
