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

from fastapi import FastAPI
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
from backend.routes.chat_stats       import router as chat_stats_router   # ★ add
from backend.routes.agent_events     import router as agent_events_router
from backend.routes.agents_health    import router as agents_health_router
from backend.routes.ws_agent_events  import router as ws_agent_events_router

# telemetry / dashboard
from backend.routes.system_vitals    import router as system_vitals_router
from backend.routes.stats_system     import router as stats_system_router
from backend.routes.stats_llm        import router as stats_llm_router
from backend.routes.context_tokens   import router as context_tokens_router

# ---------- attach ----------
app.include_router(chat_send_router,   prefix="/api/chat",           tags=["chat"])
app.include_router(chat_stats_router,  prefix="/api/chat/stats",     tags=["chat"])  # ★ add
app.include_router(agent_events_router,   prefix="/api/agents/events", tags=["agents"])
app.include_router(agents_health_router,  prefix="/api/agents/health", tags=["agents"])
app.include_router(ws_agent_events_router,                            tags=["agents"])

app.include_router(system_vitals_router,  prefix="/api/system-vitals", tags=["system"])
app.include_router(stats_system_router,   prefix="/api/stats/system",  tags=["system"])
app.include_router(stats_llm_router,      prefix="/api/stats/llm",     tags=["system"])
app.include_router(context_tokens_router, prefix="/api/context",       tags=["context"])

# ── liveness probe ────────────────────────────────────────────────────────
@app.get("/", tags=["meta"])
async def root():
    """Quick sanity ping so `curl localhost:$BACKEND_PORT/` returns JSON."""
    return {
        "status": "llama-dashboard-api running",
        "port": int(os.getenv("BACKEND_PORT", 8005)),
    }
