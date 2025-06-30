# backend/agent_routine_planner.py
# Schedules structured routines to guide agent behavior and reduce drift.

from datetime import datetime, timedelta

class AgentRoutinePlanner:
    def __init__(self):
        self.routines = {}  # {agent_id: [ {time, task} ]}

    def plan_daily_routine(self, agent_id, tasks):
        now = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
        schedule = []

        for i, task in enumerate(tasks):
            scheduled_time = now + timedelta(hours=i)
            schedule.append({
                "time": scheduled_time.isoformat(),
                "task": task
            })

        self.routines[agent_id] = schedule
        return schedule

    def get_routine(self, agent_id):
        return self.routines.get(agent_id, [])

    def clear_routine(self, agent_id):
        if agent_id in self.routines:
            del self.routines[agent_id]
