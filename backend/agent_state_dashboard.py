# backend/agent_state_dashboard.py
# Prepares agent state snapshots for frontend visualization.

from backend.agent_state_synthesizer import AgentStateSynthesizer

class AgentStateDashboard:
    def __init__(self):
        self.synthesizer = AgentStateSynthesizer()

    def get_agent_state_summary(self, agent_id):
        state = self.synthesizer.synthesize_state(agent_id)
        return {
            "agent_id": agent_id,
            "role": state["awareness"].get("role"),
            "status": state["awareness"].get("status"),
            "focus_keys": list(state["focus"].get("focus", {}).keys())[:3],
            "perceived_context": state["perception"].get("context"),
            "memory_snippet": state["memory"][:1] if isinstance(state["memory"], list) else state["memory"]
        }

    def get_bulk_state_summary(self, agent_ids):
        return [self.get_agent_state_summary(agent_id) for agent_id in agent_ids]
