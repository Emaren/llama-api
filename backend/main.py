from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

# Routes (import only the ones llama-chat-api actually needs)
from routes.agents_health import router as agents_health_router
from routes.agent_events import router as agent_events_router
from routes.chat_send import router as chat_send_router
from routes.ws_agent_events import router as ws_agent_events_router

# Create FastAPI app with Swagger + Redoc at /api/...
app = FastAPI(
    title="Llama Chat API",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# ─── Middleware ───────────────────────────────────── #
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── REST API Routes ─────────────────────────────── #
app.include_router(agents_health_router, prefix="/api/agents/health", tags=["agents"])
app.include_router(agent_events_router,  prefix="/api/agents/events", tags=["agents"])
app.include_router(chat_send_router,     prefix="/api/chat",         tags=["chat"])

# ─── WebSocket Route ─────────────────────────────── #
app.include_router(ws_agent_events_router)
