# backend/routes/context_tokens.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_context_usage():
    """
    Returns a stub of how many context tokens have been used vs. the limit.
    """
    used = 1234
    limit = 4096
    return {
        "tokensUsed": used,
        "tokensLimit": limit,
        "percent": round(used / limit * 100, 1),
    }
