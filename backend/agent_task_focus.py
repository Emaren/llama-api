# backend/agent_task_focus.py
# Adjusts agent task focus based on system priorities and attention signals.

from backend.context_engine import ContextEngine
from backend.attention_bias_trainer import AttentionBiasTrainer
from backend.project_scorer import ProjectScorer

class AgentTaskFocus:
    def __init__(self):
        self.context_engine = ContextEngine()
        self.bias_trainer = AttentionBiasTrainer()
        self.project_scorer = ProjectScorer()

    def determine_focus(self, agent_id, context):
        analysis = self.context_engine.analyze(context)
        score = self.project_scorer.score_context(analysis)
        bias = self.bias_trainer.apply_bias(agent_id, analysis)
        focus = self._merge_signals(score, bias)
        return focus

    def _merge_signals(self, score, bias):
        merged = {}
        for key in set(score) | set(bias):
            merged[key] = score.get(key, 0) * 0.6 + bias.get(key, 0) * 0.4
        return dict(sorted(merged.items(), key=lambda x: x[1], reverse=True))
