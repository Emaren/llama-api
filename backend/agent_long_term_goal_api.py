# backend/agent_long_term_goal_api.py
# API to set, update, and fetch long-term goal progress for agents.

from fastapi import APIRouter, Query
from backend.agent_long_term_goal_monitor import AgentLongTermGoalMonitor

router = APIRouter()
goal_monitor = AgentLongTermGoalMonitor()

@router.post("/goal/set/{agent_id}")
def set_goal(agent_id: str, goal: str = Query(...)):
    goal_monitor.set_goal(agent_id, goal)
    return {"status": "goal set", "goal": goal}

@router.post("/goal/milestone/{agent_id}")
def add_milestone(agent_id: str, milestone: str = Query(...)):
    goal_monitor.add_milestone(agent_id, milestone)
    return {"status": "milestone added", "milestone": milestone}

@router.post("/goal/complete/{agent_id}")
def complete_goal(agent_id: str):
    goal_monitor.complete_goal(agent_id)
    return {"status": "goal marked as complete"}

@router.get("/goal/status/{agent_id}")
def get_goal_status(agent_id: str):
    return goal_monitor.get_goal_status(agent_id)
