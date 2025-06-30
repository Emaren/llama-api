\"\"\"
logic_tuner.py – Refines inference chains and evaluates logical soundness
to prevent hallucination and optimize reasoning.
\"\"\"

from shared.utils import trace_reasoning_path
from shared.constants import LOGIC_CONFIDENCE_THRESHOLD

class LogicTuner:
    def __init__(self, reasoning_engine):
        self.engine = reasoning_engine

    def tune_inference(self, query, response):
        trace = trace_reasoning_path(query, response)
        issues = []

        for step in trace:
            if step.get("confidence", 1.0) < LOGIC_CONFIDENCE_THRESHOLD:
                issues.append(step)

        return {
            "total_steps": len(trace),
            "low_confidence_steps": len(issues),
            "recommendations": self.suggest_fixes(issues)
        }

    def suggest_fixes(self, issues):
        suggestions = []
        for issue in issues:
            if "fallback" in issue:
                suggestions.append(f"Use fallback: {issue['fallback']}")
            else:
                suggestions.append("Recompute step with clearer inputs.")
        return suggestions
