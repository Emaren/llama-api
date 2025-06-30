# backend/agent_bias_reporter.py
# Summarizes bias patterns and offers suggestions for mitigation.

from backend.agent_bias_monitor import AgentBiasMonitor

class AgentBiasReporter:
    def __init__(self):
        self.monitor = AgentBiasMonitor()

    def generate_report(self, agent_id):
        bias_log = self.monitor.bias_log.get(agent_id, [])
        if not bias_log:
            return f"No bias data recorded for agent {agent_id}."

        last_vector = bias_log[-1]
        skew_detected = self.monitor.detect_skew(agent_id)
        dominant_topics = [k for k, v in last_vector.items() if v > 0.6]

        report = [f"🧠 Bias Report for Agent {agent_id}:"]
        report.append(f"- Dominant dimensions: {', '.join(dominant_topics) or 'None'}")
        report.append(f"- Skew detected: {'Yes' if skew_detected else 'No'}")
        report.append(f"- Bias sample (last vector): {last_vector}")
        return "\n".join(report)
