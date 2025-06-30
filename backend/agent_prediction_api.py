# backend/agent_prediction_api.py
# Exposes forecast endpoints for agent future states and behavior.

from fastapi import APIRouter
from backend.agent_prediction_engine import AgentPredictionEngine
from backend.agent_prediction_reporter import AgentPredictionReporter

router = APIRouter()
engine = AgentPredictionEngine()
reporter = AgentPredictionReporter()

@router.get("/predict_future/{agent_id}")
def get_future_prediction(agent_id: str):
    return engine.predict_future(agent_id)

@router.get("/prediction_report/{agent_id}")
def get_prediction_report(agent_id: str):
    return reporter.generate_report(agent_id)
