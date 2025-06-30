# backend/agent_state_logger.py
# Logs synthesized agent state snapshots for long-term tracking.

import json
from datetime import datetime
from backend.agent_state_synthesizer import AgentStateSynthesizer

class AgentStateLogger:
    def __init__(self, log_path="data/agent_state_log.jsonl"):
        self.synthesizer = AgentStateSynthesizer()
        self.log_path = log_path

    def log_state(self, agent_id):
        state = self.synthesizer.synthesize_state(agent_id)
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent_id": agent_id,
            "state": state
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def tail_log(self, n=5):
        try:
            with open(self.log_path, "r") as f:
                lines = f.readlines()[-n:]
            return [json.loads(line) for line in lines]
        except FileNotFoundError:
            return []
