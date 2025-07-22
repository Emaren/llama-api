# backend/main.py
"""
Llama-Dashboard API (metrics / support)
───────────────────────────────────────
This service powers **token-scope, system-vitals, agent-health, etc.**
It no longer owns the `/api/chat/stats/*` endpoints – those now live
inside the *chat* backend (`llama-chat-api`).

Run locally:

    # pick a free port (default 8005)
    BACKEND_PORT=8005 uvicorn backend.main:app --reload --port $BACKEND_PORT
"""

from __future__ import annotations

import os
import sys
import random
from datetime import datetime

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

# ── make “backend.routes.*” import-resolvable no matter the CWD ────────────
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# ── FastAPI app ────────────────────────────────────────────────────────────
app = FastAPI(
    title="Llama Dashboard API",
    version="0.3.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# ── CORS / dev security ────────────────────────────────────────────────────
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])  # dev-only
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # tighten for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── ROUTERS ────────────────────────────────────────────────────────────────
# chat / demo helpers
from backend.routes.chat_send        import router as chat_send_router
from backend.routes.chat_stats       import router as chat_stats_router
from backend.routes.agent_events     import router as agent_events_router
from backend.routes.agents_health    import router as agents_health_router
from backend.routes.ws_agent_events  import router as ws_agent_events_router

# telemetry / dashboard
from backend.routes.system_vitals    import router as system_vitals_router
from backend.routes.stats_system     import router as stats_system_router
from backend.routes.stats_llm        import router as stats_llm_router
from backend.routes.context_tokens   import router as context_tokens_router

# ---------- attach ----------
app.include_router(chat_send_router,       prefix="/api/chat",           tags=["chat"])
app.include_router(chat_stats_router,      prefix="/api/chat/stats",     tags=["chat"])
app.include_router(agent_events_router,    prefix="/api/agents/events",  tags=["agents"])
app.include_router(agents_health_router,   prefix="/api/agents/health",  tags=["agents"])
app.include_router(ws_agent_events_router,                             tags=["agents"])

app.include_router(system_vitals_router,   prefix="/api/system-vitals",  tags=["system"])
app.include_router(stats_system_router,    prefix="/api/stats/system",   tags=["system"])
app.include_router(stats_llm_router,       prefix="/api/stats/llm",      tags=["system"])
app.include_router(context_tokens_router,  prefix="/api/context",        tags=["context"])

# ── Root + favicon ─────────────────────────────────────────────────────────
@app.get("/", tags=["meta"])
async def root():
    return {
        "status": "llama-dashboard-api running",
        "port": int(os.getenv("BACKEND_PORT", 8005)),
    }

@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)

# ── Mock endpoints expected by dashboard (temporary) ───────────────────────
@app.get("/api/context")
async def context_scope_meter():
    return {"tokensUsed": 1234, "tokensLimit": 4096, "percent": 30.1}

@app.get("/api/context-usage")
async def context_usage():
    return {
        "tokens_used": 86381,
        "tokens_total": 100000,
        "percentage": 86.38,
        "status": "OK",
    }

@app.get("/api/stats/system")
async def system_stats():
    return {
        "cpu_pct": round(random.uniform(12, 28), 1),
        "mem_pct": round(random.uniform(30, 65), 1),
        "cpu": [round(random.uniform(12, 28), 1)],
        "mem": [round(random.uniform(30, 65), 1)],
        "memory": {"used_mb": 5789, "total_mb": 16000},
        "uptime": "5 days, 3 hours",
    }

@app.get("/api/stats/llm")
async def llm_stats():
    return {
        "model": "gpt-4o",
        "tokens_per_s": round(random.uniform(600, 800), 2),
        "latency_ms": random.randint(35, 50),
        "bias_vector": {"tone": 0.5, "formality": 0.7},
        "engagement_prediction": 0.72,
    }

@app.get("/api/system-vitals")
async def system_vitals():
    return {
        "cpu_load":       [round(random.uniform(10, 20), 1)],
        "vram_util":      [round(random.uniform(40, 60), 1)],
        "memory_used":    "10.2 / 12.6 GB",
        "token_throughput": f"{round(random.uniform(700, 800), 1)} / s",
        "latency":        f"{random.randint(35, 50)} ms",
        "net_in_mb":      round(random.uniform(1.0, 2.0), 1),
        "net_out_mb":     round(random.uniform(0.5, 1.5), 1),
    }

@app.get("/api/query-type")
async def query_type():
    return {"query_type": "user_feedback"}
