import time

class TeamScheduler:
    def __init__(self, coordinator):
        self.coordinator = coordinator
        self.task_queue = []

    def add_task(self, task):
        self.task_queue.append(task)

    def run(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            results = self.coordinator.delegate_task(task)
            self.process_results(results)
            time.sleep(0.1)  # throttle

    def process_results(self, results):
        # Example: merge or log results
        for agent_name, output in results.items():
            print(f"Agent {agent_name} completed task with output: {output}")
