# backend/agent_alignment_api.py
# Exposes alignment checking and resolution endpoints for agent behavior.

from fastapi import APIRouter, Body
from backend.agent_alignment_interface import AgentAlignmentInterface

router = APIRouter()
alignment_interface = AgentAlignmentInterface()

@router.post("/check_alignment/{agent_id}")
def check_alignment(agent_id: str, output: str = Body(...)):
    return alignment_interface.full_alignment_check(agent_id, output)

@router.get("/alignment_report/{agent_id}")
def get_alignment_report(agent_id: str):
    return alignment_interface.reporter.generate_report(agent_id)

@router.post("/resolve_alignment/{agent_id}")
def resolve_alignment(agent_id: str):
    return alignment_interface.resolver.resolve_violations(agent_id)
