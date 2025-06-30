class TeamPerformanceTracker:
    def __init__(self):
        self.performance_logs = {}

    def log_performance(self, agent_name, metric, value):
        if agent_name not in self.performance_logs:
            self.performance_logs[agent_name] = []
        self.performance_logs[agent_name].append({
            "metric": metric,
            "value": value
        })

    def get_performance(self, agent_name):
        return self.performance_logs.get(agent_name, [])
