class TeamConfidenceManager:
    def __init__(self):
        self.confidence_levels = {}

    def set_confidence(self, agent_name, level):
        self.confidence_levels[agent_name] = level

    def get_confidence(self, agent_name):
        return self.confidence_levels.get(agent_name, 0.0)
