\"\"\"
agent_scheduler.py – Schedules and executes tasks across agents.
Handles immediate execution and deferred task queues.
\"\"\"

from typing import Any

class AgentScheduler:
    def __init__(self):
        self.queue = []

    def schedule(self, agent_name: str):
        print(f"[AgentScheduler] Queuing agent: {agent_name}")
        self.queue.append(agent_name)

    def execute(self, task: dict, session_id: str) -> Any:
        agent = task.get("agent")
        payload = task.get("payload", {})
        print(f"[AgentScheduler] Executing task for agent: {agent}")
        return self._run_agent(agent, payload, session_id)

    def _run_agent(self, agent_name: str, payload: dict, session_id: str):
        try:
            module = __import__(f"backend.{agent_name}", fromlist=[""])
            AgentClass = getattr(module, agent_name_to_class(agent_name))
            agent_instance = AgentClass()
            return agent_instance.run(payload, session_id)
        except Exception as e:
            print(f"[AgentScheduler] Error executing {agent_name}: {e}")
            return {"error": str(e)}

def agent_name_to_class(name: str) -> str:
    return ''.join(part.capitalize() for part in name.split('_'))
