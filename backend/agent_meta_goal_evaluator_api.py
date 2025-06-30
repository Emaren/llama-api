# backend/agent_meta_goal_evaluator_api.py
# API for agent meta-goal achievement and self-transcendence evaluation.

from fastapi import APIRouter, Query
from backend.agent_meta_goal_evaluator import AgentMetaGoalEvaluator

router = APIRouter()
meta_goal_evaluator = AgentMetaGoalEvaluator()

@router.post("/meta_goal/log/{agent_id}")
def log_goal(agent_id: str, goal: str = Query(...), achieved: bool = Query(...)):
    return meta_goal_evaluator.log_goal(agent_id, goal, achieved)

@router.get("/meta_goal/goals/{agent_id}")
def get_goals(agent_id: str):
    return meta_goal_evaluator.get_goals(agent_id)
