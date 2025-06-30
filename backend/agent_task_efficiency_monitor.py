# backend/agent_task_efficiency_monitor.py
# Tracks how efficiently agents perform tasks relative to resources used.

class AgentTaskEfficiencyMonitor:
    def __init__(self):
        self.task_logs = {}  # {agent_id: [ {task_id, duration_sec, resources_used} ]}

    def log_task(self, agent_id, task_id, duration_sec, resources_used):
        if agent_id not in self.task_logs:
            self.task_logs[agent_id] = []
        self.task_logs[agent_id].append({
            "task_id": task_id,
            "duration_sec": duration_sec,
            "resources_used": resources_used
        })

    def calculate_efficiency(self, agent_id):
        logs = self.task_logs.get(agent_id, [])
        if not logs:
            return {"efficiency": None, "message": "No task data"}

        total_duration = sum(log["duration_sec"] for log in logs)
        total_resources = sum(log["resources_used"] for log in logs)
        if total_resources == 0:
            return {"efficiency": None, "message": "Resources usage zero"}

        efficiency = total_duration / total_resources
        return {"efficiency": efficiency}
