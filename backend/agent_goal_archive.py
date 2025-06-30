# backend/agent_goal_archive.py
# Archives historical goals for analysis and long-term learning.

import json
from datetime import datetime

class AgentGoalArchive:
    def __init__(self, archive_path="data/archived_goals.json"):
        self.archive_path = archive_path
        self._load_archive()

    def _load_archive(self):
        try:
            with open(self.archive_path, "r") as f:
                self.archive = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.archive = []

    def archive_goal(self, agent_id, goal, status, notes=None):
        entry = {
            "agent_id": agent_id,
            "goal": goal,
            "status": status,
            "notes": notes,
            "archived_at": datetime.utcnow().isoformat()
        }
        self.archive.append(entry)
        self._save_archive()

    def _save_archive(self):
        with open(self.archive_path, "w") as f:
            json.dump(self.archive, f, indent=2)

    def get_archived_goals(self, agent_id=None):
        if agent_id:
            return [g for g in self.archive if g["agent_id"] == agent_id]
        return self.archive
