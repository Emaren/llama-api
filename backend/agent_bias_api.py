# backend/agent_bias_api.py
# Exposes endpoints for accessing and resolving agent bias patterns.

from fastapi import APIRouter, Body
from backend.agent_bias_monitor import AgentBiasMonitor
from backend.agent_bias_reporter import AgentBiasReporter
from backend.agent_bias_resolver import AgentBiasResolver

router = APIRouter()
monitor = AgentBiasMonitor()
reporter = AgentBiasReporter()
resolver = AgentBiasResolver()

@router.post("/log_bias/{agent_id}")
def log_bias(agent_id: str, bias_vector: dict = Body(...)):
    monitor.log_bias(agent_id, bias_vector)
    return {"status": "logged"}

@router.get("/bias_report/{agent_id}")
def get_bias_report(agent_id: str):
    return reporter.generate_report(agent_id)

@router.post("/resolve_bias/{agent_id}")
def resolve_bias(agent_id: str):
    last_vector = monitor.bias_log.get(agent_id, [])[-1] if monitor.bias_log.get(agent_id) else {}
    return resolver.resolve_bias(agent_id, last_vector)
