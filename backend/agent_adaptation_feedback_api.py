# backend/agent_adaptation_feedback_api.py
# API endpoints for managing agent adaptation feedback.

from fastapi import APIRouter, Query
from backend.agent_adaptation_feedback import AgentAdaptationFeedback

router = APIRouter()
adaptation_feedback = AgentAdaptationFeedback()

@router.post("/adaptation_feedback/add/{agent_id}")
def add_feedback(agent_id: str, feedback: str = Query(...)):
    adaptation_feedback.add_feedback(agent_id, feedback)
    return {"status": "feedback added", "feedback": feedback}

@router.get("/adaptation_feedback/get/{agent_id}")
def get_feedback(agent_id: str):
    return adaptation_feedback.get_feedback(agent_id)
