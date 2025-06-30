class TeamSynchronization:
    def __init__(self):
        self.synced_agents = set()

    def sync_agent(self, agent_name):
        self.synced_agents.add(agent_name)

    def unsync_agent(self, agent_name):
        self.synced_agents.discard(agent_name)

    def is_synced(self, agent_name):
        return agent_name in self.synced_agents

    def get_all_synced(self):
        return list(self.synced_agents)
