# backend/agent_temporal_reflection.py
# Analyzes temporal patterns for introspective insights.

from backend.agent_temporal_context import AgentTemporalContext

class AgentTemporalReflection:
    def __init__(self):
        self.context = AgentTemporalContext()

    def reflect(self, agent_id):
        state = self.context.get_temporal_state(agent_id)
        insights = []

        if state["last_active_seconds"] is None:
            insights.append("🕒 No activity logged yet.")
        elif state["last_active_seconds"] > 3600:
            insights.append("⚠️ Agent has been idle for over an hour.")
        else:
            insights.append("✅ Agent is active.")

        if state["last_failure_seconds"] is not None and state["last_failure_seconds"] < 300:
            insights.append("⛔ Recent failure detected — monitor recovery.")

        if state["last_goal_set_seconds"] is None:
            insights.append("⚠️ No recent goal set.")
        elif state["last_goal_set_seconds"] > 1800:
            insights.append("💤 Goal may be outdated — consider refreshing.")

        return {
            "agent_id": agent_id,
            "reflections": insights,
            "raw_state": state
        }
