class TeamMemorySync:
    def __init__(self, agents):
        self.agents = agents

    def sync_memories(self):
        base_memory = self.agents[next(iter(self.agents))].get_memory_snapshot()
        for name, agent in self.agents.items():
            if agent.get_memory_snapshot() != base_memory:
                agent.update_memory(base_memory)
