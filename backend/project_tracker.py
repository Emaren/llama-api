\"\"\"
project_tracker.py – Tracks ongoing projects, their statuses, milestones,
and updates for health monitoring and reflection.
\"\"\"

from datetime import datetime

class ProjectTracker:
    def __init__(self):
        self.projects = {}

    def start_project(self, project_id: str, metadata: dict):
        self.projects[project_id] = {
            "metadata": metadata,
            "status": "active",
            "milestones": [],
            "updates": [],
            "start_time": datetime.utcnow()
        }

    def update_status(self, project_id: str, status: str):
        if project_id in self.projects:
            self.projects[project_id]["status"] = status

    def add_milestone(self, project_id: str, milestone: str):
        if project_id in self.projects:
            self.projects[project_id]["milestones"].append({
                "milestone": milestone,
                "timestamp": datetime.utcnow()
            })

    def log_update(self, project_id: str, update: str):
        if project_id in self.projects:
            self.projects[project_id]["updates"].append({
                "update": update,
                "timestamp": datetime.utcnow()
            })

    def get_summary(self, project_id: str) -> dict:
        return self.projects.get(project_id, {})
