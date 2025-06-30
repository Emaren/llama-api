# backend/agent_collective_consciousness.py
# Models and manages shared mental states among agent collectives.

from datetime import datetime

class AgentCollectiveConsciousness:
    def __init__(self):
        self.shared_states = {}  # {group_id: {state: value, "last_update": timestamp}}

    def update_shared_state(self, group_id, state: str, value):
        if group_id not in self.shared_states:
            self.shared_states[group_id] = {}
        self.shared_states[group_id][state] = value
        self.shared_states[group_id]["last_update"] = datetime.utcnow().isoformat()

    def get_shared_state(self, group_id, state: str):
        return self.shared_states.get(group_id, {}).get(state)

    def get_all_states(self, group_id):
        return self.shared_states.get(group_id, {})
