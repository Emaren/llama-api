# backend/agent_performance_predictor.py
# Uses historical data to predict agent performance and identify risks.

class AgentPerformancePredictor:
    def __init__(self):
        self.performance_data = {}  # {agent_id: [performance_scores]}

    def add_performance_score(self, agent_id, score: float):
        if agent_id not in self.performance_data:
            self.performance_data[agent_id] = []
        self.performance_data[agent_id].append(score)

    def predict_performance(self, agent_id):
        scores = self.performance_data.get(agent_id, [])
        if not scores:
            return {"prediction": "insufficient data"}
        avg_score = sum(scores) / len(scores)
        risk = "low" if avg_score > 0.7 else "high" if avg_score < 0.4 else "medium"
        return {"average_score": round(avg_score, 3), "risk_level": risk}
