# backend/agent_feedback_api.py
# API for providing feedback to agents and reviewing history.

from fastapi import APIRouter, Query
from backend.agent_feedback_integration import AgentFeedbackIntegration

router = APIRouter()
feedback = AgentFeedbackIntegration()

@router.post("/feedback/{agent_id}")
def submit_feedback(agent_id: str, message: str = Query(...), feedback_type: str = "general", source: str = "human"):
    return feedback.submit_feedback(agent_id, message, feedback_type, source)

@router.get("/feedback/history/{agent_id}")
def get_feedback(agent_id: str):
    return feedback.get_feedback_history(agent_id)
