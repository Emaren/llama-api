# backend/agent_resilience_dashboard.py
# Prepares resilience stats for frontend display components.

from backend.agent_resilience_monitor import AgentResilienceMonitor

class AgentResilienceDashboard:
    def __init__(self):
        self.monitor = AgentResilienceMonitor()

    def get_dashboard_data(self, agent_id):
        score = self.monitor.calculate_resilience_score(agent_id)
        failures = self.monitor.failure_events.get(agent_id, [])
        recoveries = self.monitor.recovery_events.get(agent_id, [])

        return {
            "agent_id": agent_id,
            "resilience_score": round(score, 2),
            "failures_last_hour": len(failures),
            "recoveries_last_hour": len(recoveries),
            "trend": self._compute_trend(failures, recoveries)
        }

    def _compute_trend(self, failures, recoveries):
        if not failures:
            return "stable"
        ratio = len(recoveries) / len(failures)
        if ratio < 0.5:
            return "declining"
        elif ratio < 1.0:
            return "recovering"
        return "strong"
