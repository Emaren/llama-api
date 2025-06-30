# backend/agent_hierarchical_reflection.py
# Supports hierarchical, recursive, and meta-reflection in agents.

class AgentHierarchicalReflection:
    def __init__(self):
        self.reflections = {}  # {agent_id: [ {level, content, timestamp} ]}

    def log_reflection(self, agent_id, level: int, content: str):
        from datetime import datetime
        entry = {
            "level": level,
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        }
        if agent_id not in self.reflections:
            self.reflections[agent_id] = []
        self.reflections[agent_id].append(entry)
        return entry

    def get_reflections(self, agent_id, level: int = None):
        logs = self.reflections.get(agent_id, [])
        if level is not None:
            logs = [entry for entry in logs if entry["level"] == level]
        return logs
