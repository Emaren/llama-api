from backend.agent_scheduler import shutdown_agents
from backend.system_monitor import log_shutdown


def stop_llama():
    """
    Cleanly shut down the LLM agent system.
    """
    print("🛑 Shutting down Llama Agent...")
    shutdown_agents()
    log_shutdown()


if __name__ == "__main__":
    stop_llama()
