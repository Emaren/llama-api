class TeamPerformanceMonitor:
    def __init__(self, agents):
        self.agents = agents
        self.performance_log = {}

    def log_performance(self, agent_name, metric, value):
        if agent_name not in self.performance_log:
            self.performance_log[agent_name] = {}
        self.performance_log[agent_name][metric] = value

    def get_performance(self, agent_name):
        return self.performance_log.get(agent_name, {})

    def summarize_performance(self):
        summary = {}
        for agent_name, metrics in self.performance_log.items():
            summary[agent_name] = sum(metrics.values()) / len(metrics) if metrics else 0
        return summary
