# backend/agent_performance_predictor_api.py
# API endpoints for agent performance prediction.

from fastapi import APIRouter, Query
from backend.agent_performance_predictor import AgentPerformancePredictor

router = APIRouter()
predictor = AgentPerformancePredictor()

@router.post("/performance_score/add/{agent_id}")
def add_score(agent_id: str, score: float = Query(...)):
    predictor.add_performance_score(agent_id, score)
    return {"status": "score added", "score": score}

@router.get("/performance_predict/{agent_id}")
def predict_performance(agent_id: str):
    return predictor.predict_performance(agent_id)
