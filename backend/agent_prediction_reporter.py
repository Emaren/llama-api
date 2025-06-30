# backend/agent_prediction_reporter.py
# Formats and interprets predictions from the agent's forecast engine.

from backend.agent_prediction_engine import AgentPredictionEngine

class AgentPredictionReporter:
    def __init__(self):
        self.engine = AgentPredictionEngine()

    def generate_report(self, agent_id):
        forecast = self.engine.predict_future(agent_id)
        tasks = forecast.get("expected_tasks", [])
        risk = forecast.get("risk_level", 0.0)
        confidence = forecast.get("confidence", 0.0)

        report = [
            f"🔮 Prediction Report for Agent {agent_id}:",
            f"- Confidence: {confidence:.2f}",
            f"- Risk Level: {risk:.2f}",
            f"- Next {len(tasks)} expected tasks:"
        ]

        for i, task in enumerate(tasks, 1):
            report.append(f"  {i}. {task}")

        return "\n".join(report)
