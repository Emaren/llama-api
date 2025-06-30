# backend/agent_perception_reporter.py
# Summarizes perception evolution for transparency and insight generation.

from backend.agent_perception_tracker import AgentPerceptionTracker
from backend.agent_perception_analyzer import AgentPerceptionAnalyzer

class AgentPerceptionReporter:
    def __init__(self):
        self.tracker = AgentPerceptionTracker()
        self.analyzer = AgentPerceptionAnalyzer()

    def generate_perception_report(self, agent_id):
        history = self.tracker.get_recent_perceptions(agent_id)
        if len(history) < 2:
            return f"Not enough data to generate perception report for agent {agent_id}."

        report_lines = [f"🧠 Perception Report for Agent {agent_id}:"]
        for i in range(1, len(history)):
            old_state = history[i - 1]["state"]
            new_state = history[i]["state"]
            diff = self.analyzer.compare_perceptions(old_state, new_state)
            summary = self.analyzer.summarize_shift(diff)
            timestamp = history[i]["timestamp"]
            report_lines.append(f"\n🕒 {timestamp}\n{summary}")

        return "\n".join(report_lines)
