# backend/agent_feedback_integration.py
# Handles incoming feedback to adapt agent behavior.

from datetime import datetime

class AgentFeedbackIntegration:
    def __init__(self):
        self.feedback_log = {}  # {agent_id: [ {type, message, source, timestamp} ]}

    def submit_feedback(self, agent_id, message: str, feedback_type: str = "general", source: str = "human"):
        entry = {
            "type": feedback_type,
            "message": message,
            "source": source,
            "timestamp": datetime.utcnow().isoformat()
        }
        if agent_id not in self.feedback_log:
            self.feedback_log[agent_id] = []
        self.feedback_log[agent_id].append(entry)
        return entry

    def get_feedback_history(self, agent_id):
        return self.feedback_log.get(agent_id, [])
