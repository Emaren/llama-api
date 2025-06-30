class TeamScheduleManager:
    def __init__(self):
        self.schedules = {}

    def add_schedule(self, agent_name, schedule):
        self.schedules[agent_name] = schedule

    def get_schedule(self, agent_name):
        return self.schedules.get(agent_name)

    def remove_schedule(self, agent_name):
        if agent_name in self.schedules:
            del self.schedules[agent_name]
