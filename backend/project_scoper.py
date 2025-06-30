\"\"\"
project_scoper.py – Determines the boundaries, focus areas, and constraints
of a project based on objectives and system context.
\"\"\"

from shared.config_loader import load_project_goals
from shared.system_constants import DEFAULT_SCOPE_LIMITS

class ProjectScoper:
    def __init__(self):
        self.goals = load_project_goals()
        self.scope_limits = DEFAULT_SCOPE_LIMITS

    def define_scope(self, goal_id: str):
        goal = self.goals.get(goal_id, {})
        focus_area = goal.get("focus_area", "general")
        constraints = self.scope_limits.get(focus_area, {})
        return {
            "goal_id": goal_id,
            "focus_area": focus_area,
            "constraints": constraints
        }
