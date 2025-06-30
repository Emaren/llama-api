class TeamFeedbackManager:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self, agent_name, feedback):
        self.feedbacks.append({
            "agent": agent_name,
            "feedback": feedback
        })

    def get_feedbacks(self):
        return self.feedbacks
