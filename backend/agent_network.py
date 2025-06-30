class AgentNetwork:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def broadcast(self, message):
        for agent in self.agents.values():
            agent.receive_message(message)

    def gather_responses(self, query):
        responses = {}
        for name, agent in self.agents.items():
            responses[name] = agent.respond(query)
        return responses
