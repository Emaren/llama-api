from fastapi import APIRouter
router = APIRouter(prefix="/api")

@router.get("/context")         # dashboard expects JSON with the chat context
def ctx():        return {"messages": [], "summary": ""}

@router.get("/stats/system")    # <-- tiny placeholder until you wire real data
def sys():        return {"cpu_pct": 0, "mem_pct": 0}

@router.get("/stats/llm")       # <-- ditto
def llm():        return {"tokens_per_s": 0, "latency_ms": 0}

@router.get("/agents/health")   # <-- dashboard shows the red ‘offline’ pill
def ag():         return {"agents": [], "status": "offline"}
