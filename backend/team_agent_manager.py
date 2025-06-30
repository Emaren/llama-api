class TeamAgentManager:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name, agent_object):
        self.agents[agent_name] = agent_object

    def get_agent(self, agent_name):
        return self.agents.get(agent_name)

    def unregister_agent(self, agent_name):
        if agent_name in self.agents:
            del self.agents[agent_name]
