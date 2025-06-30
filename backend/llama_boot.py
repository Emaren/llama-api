from backend.agent_loop import run_agent_loop
from backend.prompt_listener import listen_for_prompts
from backend.system_monitor import check_system_status


def start_llama():
    """
    Initialize and start the LLM agent system.
    """
    print("🚀 Booting Llama Agent...")
    check_system_status()
    listen_for_prompts()
#    run_agent_loop()


if __name__ == "__main__":
    start_llama()
