# backend/agent_decision_confidence.py
# Records and analyzes confidence scores for agent decisions.

class AgentDecisionConfidence:
    def __init__(self):
        self.confidence_log = {}  # {agent_id: [ {decision_id, confidence_score} ]}

    def log_confidence(self, agent_id, decision_id, score: float):
        if agent_id not in self.confidence_log:
            self.confidence_log[agent_id] = []
        self.confidence_log[agent_id].append({
            "decision_id": decision_id,
            "confidence_score": score
        })

    def average_confidence(self, agent_id):
        scores = [entry["confidence_score"] for entry in self.confidence_log.get(agent_id, [])]
        if not scores:
            return None
        return sum(scores) / len(scores)
