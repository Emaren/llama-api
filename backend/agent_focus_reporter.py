# backend/agent_focus_reporter.py
# Generates human-readable reports of agent focus behavior and trends.

from backend.agent_focus_tracker import AgentFocusTracker

class AgentFocusReporter:
    def __init__(self):
        self.tracker = AgentFocusTracker()

    def generate_report(self, agent_id, limit=10):
        history = self.tracker.get_focus_history(agent_id, limit=limit)
        if not history:
            return f"No focus history found for agent {agent_id}."

        report_lines = [f"Focus Report for Agent {agent_id}:"]
        for entry in history:
            top_focus = sorted(entry["focus"].items(), key=lambda x: -x[1])[:3]
            focus_str = ", ".join([f"{k} ({v:.2f})" for k, v in top_focus])
            report_lines.append(f"- {entry['timestamp']}: {focus_str}")
        return "\n".join(report_lines)
