class TeamTaskCoordinator:
    def __init__(self):
        self.tasks = {}

    def assign_task(self, agent_name, task):
        if agent_name not in self.tasks:
            self.tasks[agent_name] = []
        self.tasks[agent_name].append(task)

    def get_tasks(self, agent_name):
        return self.tasks.get(agent_name, [])

    def complete_task(self, agent_name, task):
        if agent_name in self.tasks and task in self.tasks[agent_name]:
            self.tasks[agent_name].remove(task)
