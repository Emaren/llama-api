# backend/agent_perception_analyzer.py
# Compares agent perception snapshots to detect inconsistency and growth signals.

class AgentPerceptionAnalyzer:
    def __init__(self):
        pass

    def compare_perceptions(self, old_state, new_state):
        differences = {}

        for key in ["context", "memory", "system"]:
            if key not in old_state or key not in new_state:
                continue
            if old_state[key] != new_state[key]:
                differences[key] = {
                    "before": old_state[key],
                    "after": new_state[key]
                }

        return differences

    def summarize_shift(self, diff):
        summary = []
        for domain, change in diff.items():
            summary.append(f"{domain.upper()} changed from {repr(change['before'])[:80]} to {repr(change['after'])[:80]}")
        return "\n".join(summary) if summary else "No significant changes."
