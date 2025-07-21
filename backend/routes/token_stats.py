# backend/routes/token_stats.py

from fastapi import APIRouter
from backend.state.token_tracker import last_chat_token_stats

router = APIRouter()

@router.get("/chat/stats/last")
async def get_last_chat_tokens():
    """
    Returns the most recent token usage stats from the last chat request.
    """
    return last_chat_token_stats

@router.get("/chat/stats/tokens")
async def get_global_token_usage():
    """
    Returns a simulated global token usage report. This can be expanded later to track
    cumulative stats from memory or a database.
    """
    total_cap = 100000
    used = last_chat_token_stats["total_tokens"]
    return {
        "tokens_used": used,
        "tokens_total": total_cap,
        "percentage": round((used / total_cap) * 100, 1) if total_cap else 0.0,
    }
