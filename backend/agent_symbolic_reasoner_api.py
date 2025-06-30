# backend/agent_symbolic_reasoner_api.py
# API for interacting with the symbolic reasoning engine.

from fastapi import APIRouter, Query
from backend.agent_symbolic_reasoner import AgentSymbolicReasoner

router = APIRouter()
reasoner = AgentSymbolicReasoner()

@router.post("/reasoner/fact/{agent_id}")
def add_fact(agent_id: str, fact: str = Query(...)):
    reasoner.add_fact(agent_id, fact)
    return {"status": "fact added", "fact": fact}

@router.get("/reasoner/check/{agent_id}")
def has_fact(agent_id: str, fact: str = Query(...)):
    return {"exists": reasoner.has_fact(agent_id, fact)}

@router.post("/reasoner/infer/{agent_id}")
def infer(agent_id: str, premise_a: str = Query(...), premise_b: str = Query(...), conclusion: str = Query(...)):
    return reasoner.infer(agent_id, premise_a, premise_b, conclusion)
