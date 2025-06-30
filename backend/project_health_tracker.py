\"\"\"
project_health_tracker.py – Monitors project status using key metrics like progress,
scope stability, engagement, and error frequency.
\"\"\"

from backend.project_tracker import ProjectTracker
from backend.health_checker import HealthChecker
from shared.scoring_utils import compute_health_score

class ProjectHealthTracker:
    def __init__(self):
        self.tracker = ProjectTracker()
        self.health_checker = HealthChecker()

    def evaluate_project(self, project_id: str):
        progress = self.tracker.get_progress(project_id)
        stability = self.tracker.get_scope_stability(project_id)
        errors = self.health_checker.get_error_metrics(project_id)
        score = compute_health_score(progress, stability, errors)
        return {
            "project_id": project_id,
            "progress": progress,
            "stability": stability,
            "errors": errors,
            "health_score": score
        }
