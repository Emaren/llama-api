class TeamTaskScheduler:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks.clear()
