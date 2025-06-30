class TeamMonitor:
    def __init__(self):
        self.statuses = {}

    def update_status(self, agent_name, status):
        self.statuses[agent_name] = status

    def get_status(self, agent_name):
        return self.statuses.get(agent_name)

    def get_all_statuses(self):
        return self.statuses
