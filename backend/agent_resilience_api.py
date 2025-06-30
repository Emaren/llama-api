# backend/agent_resilience_api.py
# API for resilience event tracking and score analysis.

from fastapi import APIRouter
from backend.agent_resilience_monitor import AgentResilienceMonitor

router = APIRouter()
resilience = AgentResilienceMonitor()

@router.post("/resilience/failure/{agent_id}")
def log_failure(agent_id: str):
    resilience.log_failure(agent_id)
    return {"status": "failure logged"}

@router.post("/resilience/recovery/{agent_id}")
def log_recovery(agent_id: str):
    resilience.log_recovery(agent_id)
    return {"status": "recovery logged"}

@router.get("/resilience/score/{agent_id}")
def get_resilience_score(agent_id: str):
    score = resilience.calculate_resilience_score(agent_id)
    return {"agent_id": agent_id, "resilience_score": round(score, 2)}
