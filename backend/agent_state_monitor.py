# backend/agent_state_monitor.py
# Monitors live agent states to detect anomalies or degradation.

from backend.agent_state_synthesizer import AgentStateSynthesizer
from datetime import datetime

class AgentStateMonitor:
    def __init__(self):
        self.synthesizer = AgentStateSynthesizer()
        self.last_state = {}

    def check_for_drift(self, agent_id):
        new_state = self.synthesizer.synthesize_state(agent_id)
        prev_state = self.last_state.get(agent_id)

        if prev_state:
            if self._has_drifted(prev_state, new_state):
                print(f"[⚠️ ALERT] Agent {agent_id} state drift detected.")
        self.last_state[agent_id] = new_state

    def _has_drifted(self, old, new):
        # Basic placeholder drift logic
        return old["awareness"] != new["awareness"] or old["focus"] != new["focus"]

    def monitor_agents(self, agent_ids):
        for agent_id in agent_ids:
            self.check_for_drift(agent_id)
