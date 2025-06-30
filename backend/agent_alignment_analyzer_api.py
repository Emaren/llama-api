# backend/agent_alignment_analyzer_api.py
# API for evaluating alignment volatility and average consistency.

from fastapi import APIRouter
from backend.agent_alignment_analyzer import AgentAlignmentAnalyzer

router = APIRouter()
analyzer = AgentAlignmentAnalyzer()

@router.get("/alignment/analyze/{agent_id}")
def analyze_alignment(agent_id: str):
    return analyzer.analyze(agent_id)
