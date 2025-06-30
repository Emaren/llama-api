# backend/agent_self_actualization_api.py
# API endpoints for agent self-actualization progress tracking.

from fastapi import APIRouter, Query
from backend.agent_self_actualization_tracker import AgentSelfActualizationTracker

router = APIRouter()
actualization_tracker = AgentSelfActualizationTracker()

@router.post("/self_actualization/log/{agent_id}")
def log_progress(agent_id: str, goal: str = Query(...), progress: float = Query(...)):
    actualization_tracker.log_progress(agent_id, goal, progress)
    return {"status": "progress logged", "goal": goal, "progress": progress}

@router.get("/self_actualization/progress/{agent_id}")
def get_progress(agent_id: str):
    return actualization_tracker.get_progress(agent_id)
