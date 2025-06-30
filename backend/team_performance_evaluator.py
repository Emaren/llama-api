class TeamPerformanceEvaluator:
    def __init__(self):
        self.evaluations = {}

    def add_evaluation(self, agent_name, score):
        if agent_name not in self.evaluations:
            self.evaluations[agent_name] = []
        self.evaluations[agent_name].append(score)

    def get_average_score(self, agent_name):
        scores = self.evaluations.get(agent_name, [])
        if scores:
            return sum(scores) / len(scores)
        return None
