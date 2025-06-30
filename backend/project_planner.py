\"\"\"
project_planner.py – Converts project goals into structured modular plans,
including milestones, dependencies, and execution order.
\"\"\"

from backend.project_scoper import ProjectScoper
from backend.prompt_composer import PromptComposer
from shared.config_loader import load_goal_config

class ProjectPlanner:
    def __init__(self):
        self.scoper = ProjectScoper()
        self.composer = PromptComposer()
        self.goal_config = load_goal_config()

    def plan_project(self, goal_id: str):
        scope = self.scoper.define_scope(goal_id)
        milestones = self._generate_milestones(scope)
        tasks = self._generate_tasks(scope, milestones)
        prompts = self.composer.compose_for_tasks(tasks)
        return {
            "goal_id": goal_id,
            "milestones": milestones,
            "tasks": tasks,
            "prompts": prompts
        }

    def _generate_milestones(self, scope):
        return [f"{scope}-milestone-{i}" for i in range(3)]

    def _generate_tasks(self, scope, milestones):
        return [{"milestone": m, "task": f"task_for_{m}"} for m in milestones]
