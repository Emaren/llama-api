class TeamTrainingManager:
    def __init__(self, agents):
        self.agents = agents

    def train_agents(self, training_data):
        for agent in self.agents.values():
            agent.train(training_data)

    def evaluate_agents(self, test_data):
        results = {}
        for name, agent in self.agents.items():
            results[name] = agent.evaluate(test_data)
        return results
