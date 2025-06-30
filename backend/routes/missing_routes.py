from fastapi import APIRouter
router = APIRouter(prefix="/api")

@router.get("/stats/llm")
def llm_stats():
    return {"tokens_per_s": 0, "latency_ms": 0}

@router.get("/stats/system")
def sys_stats():
    return {"cpu_pct": 0, "mem_pct": 0}

@router.get("/agents/health")
def agent_health():
    return {"agents": [], "status": "offline"}
