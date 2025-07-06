from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import random

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

# ─── Dashboard Mock Routes ───────────────────────── #

@app.get("/api/context")
async def context_scope_meter():
    return {
        "tokensUsed": 1234,
        "tokensLimit": 4096,
        "percent": 30.1
    }

@app.get("/api/context-usage")
async def context_usage():
    return {
        "tokens_used": 86381,
        "tokens_total": 100000,
        "percentage": 86.38,
        "status": "OK"
    }

@app.get("/api/stats/system")
async def system_stats():
    return {
        "cpu_pct": round(random.uniform(12, 28), 1),
        "mem_pct": round(random.uniform(30, 65), 1),
        "cpu": [round(random.uniform(12, 28), 1)],
        "mem": [round(random.uniform(30, 65), 1)],
        "memory": {
            "used_mb": 5789,
            "total_mb": 16000
        },
        "uptime": "5 days, 3 hours"
    }

@app.get("/api/stats/llm")
async def llm_stats():
    return {
        "model": "gpt-4o",
        "tokens_per_s": round(random.uniform(600, 800), 2),
        "latency_ms": random.randint(35, 50),
        "bias_vector": {
            "tone": 0.5,
            "formality": 0.7
        },
        "engagement_prediction": 0.72
    }

@app.get("/api/system-vitals")
async def system_vitals():
    return {
        "cpu_load": [round(random.uniform(10, 20), 1)],
        "vram_util": [round(random.uniform(40, 60), 1)],
        "memory_used": "10.2 / 12.6 GB",
        "token_throughput": f"{round(random.uniform(700, 800), 1)} / s",
        "latency": f"{random.randint(35, 50)} ms",
        "net_in_mb": round(random.uniform(1.0, 2.0), 1),
        "net_out_mb": round(random.uniform(0.5, 1.5), 1)
    }

@app.get("/api/query-type")
async def query_type():
    return {
        "query_type": "user_feedback"
    }

@app.get("/api/stats/trend")
async def cpu_mem_trend():
    return {
        "cpu_pct": round(random.uniform(10, 30), 1),
        "mem_pct": round(random.uniform(35, 60), 1)
    }
