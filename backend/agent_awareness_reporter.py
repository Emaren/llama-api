# backend/agent_awareness_reporter.py
# Produces structured summaries of agent self-awareness trends and transitions.

from backend.agent_awareness_tracker import AgentAwarenessTracker

class AgentAwarenessReporter:
    def __init__(self):
        self.tracker = AgentAwarenessTracker()

    def generate_report(self, agent_id):
        history = self.tracker.get_history(agent_id)
        if not history:
            return f"No awareness history found for agent {agent_id}."

        lines = [f"🧭 Awareness Report for Agent {agent_id}:"]
        for entry in history:
            state = entry["state"]
            lines.append(
                f"- {entry['timestamp']}: role={state['role']}, context={state['context']}, status={state['status']}"
            )
        return "\n".join(lines)

    def detect_fluctuations(self, agent_id):
        if self.tracker.detect_conflict(agent_id):
            return f"⚠️ Role/context fluctuation detected for agent {agent_id}."
        return f"✓ No major awareness shifts detected for agent {agent_id}."
