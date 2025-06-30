class TeamTaskAllocator:
    def __init__(self, agents):
        self.agents = agents

    def allocate_tasks(self, tasks):
        allocation = {}
        for task in tasks:
            suitable_agents = [agent for agent in self.agents.values() if agent.can_handle(task)]
            if suitable_agents:
                allocation[task['id']] = suitable_agents[0]  # simple assign first suitable
        return allocation
