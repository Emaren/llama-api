"""
Dashboard-backend router registry
─────────────────────────────────
Routers that physically live under **llama-api/backend/routes/**.
"""

# telemetry / system-health
from .system_vitals      import router as system_vitals_router   # /api/system-vitals
from .stats_system       import router as stats_system_router    # /api/stats/system
from .stats_llm          import router as stats_llm_router       # /api/stats/llm
from .context_tokens     import router as context_tokens_router  # /api/context/*

# agent plumbing (demo helpers)
from .agents_health      import router as agents_health_router   # /api/agents/health
from .agent_events       import router as agent_events_router    # /api/agents/events
from .ws_agent_events    import router as ws_agent_events_router # /api/ws/agents/events
from .chat_send          import router as chat_send_router       # /api/chat/send  (mock)

# NEW: token-counters
from .chat_stats         import router as chat_stats_router      # /api/chat/stats/*

__all__: list[str] = [
    "system_vitals_router",
    "stats_system_router",
    "stats_llm_router",
    "context_tokens_router",
    "agents_health_router",
    "agent_events_router",
    "ws_agent_events_router",
    "chat_send_router",
    "chat_stats_router",
]
