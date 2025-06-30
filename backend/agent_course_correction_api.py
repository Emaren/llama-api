# backend/agent_course_correction_api.py
# API to trigger behavioral course corrections for agents.

from fastapi import APIRouter, Query
from backend.agent_course_correction import AgentCourseCorrection

router = APIRouter()
corrector = AgentCourseCorrection()

@router.post("/correct/{agent_id}")
def evaluate_and_correct(agent_id: str, current_task: str = Query(...)):
    return corrector.evaluate_and_correct(agent_id, current_task)
