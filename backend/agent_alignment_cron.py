# backend/agent_alignment_cron.py
# Background job to monitor alignment status across agents on a schedule.

import time
from backend.agent_alignment_dashboard import AgentAlignmentDashboard
from backend.agent_alignment_recommender import AgentAlignmentRecommender

class AgentAlignmentCron:
    def __init__(self, agent_ids, interval_seconds=3600):
        self.agent_ids = agent_ids
        self.interval = interval_seconds
        self.dashboard = AgentAlignmentDashboard()
        self.recommender = AgentAlignmentRecommender()

    def run_once(self):
        for agent_id in self.agent_ids:
            summary = self.dashboard.get_dashboard_summary(agent_id)
            recommendations = self.recommender.recommend(agent_id)
            self._log(summary, recommendations)

    def start_loop(self):
        while True:
            print("[⏱️ ALIGNMENT CRON] Running alignment audit loop...")
            self.run_once()
            time.sleep(self.interval)

    def _log(self, summary, recommendations):
        print(f"\n[🧠 Alignment Summary] Agent: {summary['agent_id']}")
        print(f"Violations: {summary['violation_count']} | Bias: {summary['bias_keys']}")
        print(f"Recommendations: {recommendations['suggestions']}\n")
