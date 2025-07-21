"""
FastAPI application entry-point

REST
 ├─ /api/system-vitals
 ├─ /api/stats/system
 ├─ /api/stats/llm
 ├─ /api/agents/health
 ├─ /api/context
 ├─ /api/query
 ├─ /api/chat/stats/last   ← NEW
 └─ /api/diagnostics
WebSocket
 └─ /logs/agent-events
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend.agent_coordinator import AgentCoordinator
from backend.state.token_tracker import last_chat_token_stats
from backend.routes import (
    system_vitals_router,
    stats_system_router,
    stats_llm_router,
    agents_health_router,
    context_tokens_router,
    ws_agent_events,
    token_stats,  # ← NEW: include this route module
)

# ──────────────────────────────  FastAPI + CORS  ────────────────────────────
app = FastAPI(title="Llama API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ───────────────────────────  mount sub-routers  ────────────────────────────
app.include_router(system_vitals_router,  prefix="/api")
app.include_router(stats_system_router,   prefix="/api")
app.include_router(stats_llm_router,      prefix="/api")
app.include_router(agents_health_router,  prefix="/api")
app.include_router(context_tokens_router, prefix="/api")
app.include_router(ws_agent_events)       # WebSocket @ /logs/agent-events
app.include_router(token_stats.router,    prefix="/api")  # ← ✅ MOUNTED NEW ROUTES

# ─────────────────────────  Facade around coordinator  ──────────────────────
class UserInput(BaseModel):
    input: str
    session_id: str


class _Facade:
    def __init__(self) -> None:
        self.coordinator = AgentCoordinator()
        self.coordinator.initialize_system()

    def chat(self, text: str, session: str):
        return {
            "session": session,
            "input": text,
            "output": self.coordinator.handle_input(text, session),
        }

    def diagnostics(self):
        return self.coordinator.run_diagnostics()


_facade: _Facade | None = None

@app.on_event("startup")
def _init_facade() -> None:
    global _facade
    _facade = _Facade()

# ───────────────────────────────────  REST  ─────────────────────────────────
@app.post("/api/query")
async def query(payload: UserInput):
    assert _facade, "facade not initialised"
    return _facade.chat(payload.input, payload.session_id)


@app.get("/api/diagnostics")
async def diagnostics():
    assert _facade, "facade not initialised"
    return _facade.diagnostics()
