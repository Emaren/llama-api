# backend/agent_resilience_reporter.py
# Summarizes resilience metrics and recovery patterns over time.

from backend.agent_resilience_monitor import AgentResilienceMonitor

class AgentResilienceReporter:
    def __init__(self):
        self.monitor = AgentResilienceMonitor()

    def generate_report(self, agent_id):
        score = self.monitor.calculate_resilience_score(agent_id)
        failures = len(self.monitor.failure_events.get(agent_id, []))
        recoveries = len(self.monitor.recovery_events.get(agent_id, []))

        report = [
            f"🛡️ Resilience Report for Agent {agent_id}:",
            f"- Failures logged: {failures}",
            f"- Recoveries logged: {recoveries}",
            f"- Resilience Score (past 60 min): {score:.2f}",
        ]

        if score < 0.5:
            report.append("⚠️ Low resilience detected. Consider support routines.")
        elif score < 0.8:
            report.append("🟡 Moderate resilience. Monitor closely.")
        else:
            report.append("🟢 Resilient agent. No action needed.")

        return "\n".join(report)
