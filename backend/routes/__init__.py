from .system_vitals import router as system_vitals_router
from .ws_agent_events import router as ws_agent_events
from .stats_system import router as stats_system_router
from .stats_llm import router as stats_llm_router
from .agents_health import router as agents_health_router        # 👈 NEW
from .context_tokens import router as context_tokens_router                    # 👈 NEW

__all__ = [
    "system_vitals_router",
    "ws_agent_events",
    "stats_system_router",
    "stats_llm_router",
    "agents_health_router",
    "context_tokens_router",
]
