\"\"\"
project_scorer.py – Scores projects based on alignment with goals, resource needs,
feasibility, and impact potential.
\"\"\"

from shared.scoring_utils import score_alignment, score_feasibility, score_impact

class ProjectScorer:
    def __init__(self):
        pass

    def score(self, project_plan: dict) -> dict:
        alignment = score_alignment(project_plan)
        feasibility = score_feasibility(project_plan)
        impact = score_impact(project_plan)

        final_score = (alignment + feasibility + impact) / 3

        return {
            "alignment": alignment,
            "feasibility": feasibility,
            "impact": impact,
            "final_score": final_score
        }
