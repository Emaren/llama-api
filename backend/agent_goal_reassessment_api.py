# backend/agent_goal_reassessment_api.py
# API endpoints to manage agent goal reassessment.

from fastapi import APIRouter, Query
from backend.agent_goal_reassessment import AgentGoalReassessment

router = APIRouter()
reassessment = AgentGoalReassessment()

@router.post("/goal_reassessment/request/{agent_id}")
def request_reassessment(agent_id: str, reason: str = Query(...)):
    return reassessment.request_reassessment(agent_id, reason)

@router.get("/goal_reassessment/history/{agent_id}")
def get_reassessments(agent_id: str):
    return reassessment.get_reassessments(agent_id)
