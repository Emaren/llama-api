class TeamMetricsCollector:
    def __init__(self):
        self.metrics = {}

    def record_metric(self, agent_name, metric_name, value):
        if agent_name not in self.metrics:
            self.metrics[agent_name] = {}
        self.metrics[agent_name][metric_name] = value

    def get_metrics(self, agent_name):
        return self.metrics.get(agent_name, {})
