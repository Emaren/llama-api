from fastapi import APIRouter
import random

router = APIRouter()
_latency = [random.uniform(0.6, 1.4) for _ in range(60)]
_tokens  = [random.randint(20, 60)    for _ in range(60)]

@router.get("/", tags=["stats"])
def get_llm():
    _latency.append(random.uniform(0.6, 1.4)); _latency.pop(0)
    _tokens.append(random.randint(20, 60));    _tokens.pop(0)
    return {"lat_ms": _latency, "tok_s": _tokens}

__all__ = ["router"]
