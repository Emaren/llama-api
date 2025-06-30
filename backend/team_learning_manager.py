class TeamLearningManager:
    def __init__(self):
        self.learning_logs = {}

    def log_learning(self, agent_name, topic, details):
        if agent_name not in self.learning_logs:
            self.learning_logs[agent_name] = []
        self.learning_logs[agent_name].append({
            "topic": topic,
            "details": details
        })

    def get_learning_log(self, agent_name):
        return self.learning_logs.get(agent_name, [])
