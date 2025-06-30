\"\"\"
scoring_engine.py – Computes scores for sessions, memories, projects,
or user responses using configurable weight matrices and algorithms.
\"\"\"

from shared.scoring_utils import weighted_score, normalize_score
from shared.constants import MEMORY_SCORE_WEIGHTS, PROJECT_SCORE_WEIGHTS

class ScoringEngine:
    def score_memory(self, memory_data: dict) -> float:
        score = weighted_score(memory_data, MEMORY_SCORE_WEIGHTS)
        return normalize_score(score)

    def score_project(self, project_data: dict) -> float:
        score = weighted_score(project_data, PROJECT_SCORE_WEIGHTS)
        return normalize_score(score)

    def score_session(self, session_metrics: dict) -> float:
        score = (
            session_metrics.get("engagement", 0) * 0.4 +
            session_metrics.get("accuracy", 0) * 0.3 +
            session_metrics.get("retention", 0) * 0.3
        )
        return normalize_score(score)
