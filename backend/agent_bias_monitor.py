# backend/agent_bias_monitor.py
# Monitors agent outputs for signs of cognitive or data-driven bias.

from backend.bias_visualizer import BiasVisualizer
from backend.feedback_tracker import FeedbackTracker

class AgentBiasMonitor:
    def __init__(self):
        self.visualizer = BiasVisualizer()
        self.feedback_tracker = FeedbackTracker()
        self.bias_log = {}

    def log_bias(self, agent_id, bias_vector):
        if agent_id not in self.bias_log:
            self.bias_log[agent_id] = []
        self.bias_log[agent_id].append(bias_vector)

    def detect_skew(self, agent_id):
        logs = self.bias_log.get(agent_id, [])
        if len(logs) < 5:
            return False
        recent = logs[-5:]
        mean = self._average_vector(recent)
        return self.visualizer.is_skewed(mean)

    def _average_vector(self, vectors):
        if not vectors:
            return {}
        keys = set().union(*vectors)
        avg = {k: sum(v.get(k, 0) for v in vectors) / len(vectors) for k in keys}
        return avg
