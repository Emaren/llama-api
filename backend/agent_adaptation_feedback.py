# backend/agent_adaptation_feedback.py
# Processes feedback signals to adapt and refine agent behavior.

class AgentAdaptationFeedback:
    def __init__(self):
        self.feedback_store = {}  # {agent_id: [feedback]}

    def add_feedback(self, agent_id, feedback):
        if agent_id not in self.feedback_store:
            self.feedback_store[agent_id] = []
        self.feedback_store[agent_id].append(feedback)

    def get_feedback(self, agent_id):
        return self.feedback_store.get(agent_id, [])
