# backend/agent_decision_confidence_api.py
# API endpoints for managing agent decision confidence data.

from fastapi import APIRouter, Query
from backend.agent_decision_confidence import AgentDecisionConfidence

router = APIRouter()
confidence_tracker = AgentDecisionConfidence()

@router.post("/decision_confidence/log/{agent_id}")
def log_confidence(agent_id: str, decision_id: str = Query(...), score: float = Query(...)):
    confidence_tracker.log_confidence(agent_id, decision_id, score)
    return {"status": "confidence logged", "score": score}

@router.get("/decision_confidence/average/{agent_id}")
def get_average_confidence(agent_id: str):
    avg = confidence_tracker.average_confidence(agent_id)
    return {"average_confidence": avg}
