# backend/agent_alignment_recommender_api.py
# API route to retrieve alignment-based intervention suggestions.

from fastapi import APIRouter
from backend.agent_alignment_recommender import AgentAlignmentRecommender

router = APIRouter()
recommender = AgentAlignmentRecommender()

@router.get("/alignment_recommendations/{agent_id}")
def get_recommendations(agent_id: str):
    return recommender.recommend(agent_id)
