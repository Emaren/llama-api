# backend/routes/chat_stats.py
"""
backend.routes.chat_stats
─────────────────────────
GET  /api/chat/stats/tokens   – global usage
GET  /api/chat/stats/last     – last request
POST /api/chat/stats/update   – push new usage (from chat backend)
"""

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from fastapi import APIRouter, Response, status
from pydantic import BaseModel, Field

router = APIRouter()

# ────────── data models ──────────
class GlobalStats(TypedDict):
    tokens_used:  int
    tokens_total: int
    percentage:   float          # 0–100 %

class LastStats(TypedDict):
    model:             Optional[str]
    prompt_tokens:     int
    completion_tokens: int
    total_tokens:      int
    cost_usd:          float

class UsageIn(BaseModel):
    prompt_tokens:     int   = Field(ge=0)
    completion_tokens: int   = Field(ge=0)
    model_name:        str
    cost_usd:          float = Field(ge=0.0)


# ────────── in‐memory store ──────────
GLOBAL: GlobalStats = {
    "tokens_used":  0,
    "tokens_total": 100_000,
    "percentage":   0.0,
}

LAST: LastStats = {
    "model":             None,
    "prompt_tokens":     0,
    "completion_tokens": 0,
    "total_tokens":      0,
    "cost_usd":          0.0,
}

def _recalc_pct() -> None:
    total = GLOBAL["tokens_total"]
    if total > 0:
        GLOBAL["percentage"] = round(
            GLOBAL["tokens_used"] / total * 100,
            2
        )

def bump_usage(
    prompt_tokens:     int,
    completion_tokens: int,
    model_name:        str,
    cost_usd:          float,
) -> None:
    total = prompt_tokens + completion_tokens
    GLOBAL["tokens_used"] += total
    _recalc_pct()
    LAST.update(
        model             = model_name,
        prompt_tokens     = prompt_tokens,
        completion_tokens = completion_tokens,
        total_tokens      = total,
        cost_usd          = round(cost_usd, 6),
    )


# ────────── endpoints ──────────
@router.get("/tokens", response_model=GlobalStats, tags=["stats"])
async def get_global_stats() -> GlobalStats:
    """
    Return cumulative token usage and percentage of quota used.
    """
    _recalc_pct()
    return GLOBAL


@router.get("/last", response_model=LastStats, tags=["stats"])
async def get_last_stats() -> LastStats:
    """
    Return the stats (tokens + cost) from the very last chat request.
    """
    return LAST


@router.post(
    "/update",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["stats"],
)
async def push_usage(body: UsageIn) -> Response:
    """
    Receive a UsageIn payload and update global + last stats.
    Used by your chat backend after each OpenAI call.
    """
    bump_usage(
        prompt_tokens     = body.prompt_tokens,
        completion_tokens = body.completion_tokens,
        model_name        = body.model_name,
        cost_usd          = body.cost_usd,
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
