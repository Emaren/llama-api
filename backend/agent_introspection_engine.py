# backend/agent_introspection_engine.py
# Synthesizes agent internal metrics for self-awareness and introspection.

class AgentIntrospectionEngine:
    def __init__(self):
        self.introspection_data = {}  # {agent_id: {metric: value}}

    def update_metric(self, agent_id, metric: str, value):
        if agent_id not in self.introspection_data:
            self.introspection_data[agent_id] = {}
        self.introspection_data[agent_id][metric] = value

    def get_introspection(self, agent_id):
        return self.introspection_data.get(agent_id, {})
