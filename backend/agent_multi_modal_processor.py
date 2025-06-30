# backend/agent_multi_modal_processor.py
# Processes multi-modal inputs and outputs (text, image, audio, etc.)

class AgentMultiModalProcessor:
    def __init__(self):
        self.input_history = {}  # {agent_id: [ {modality, content, timestamp} ]}

    def log_input(self, agent_id, modality: str, content: str, timestamp: str):
        if agent_id not in self.input_history:
            self.input_history[agent_id] = []
        self.input_history[agent_id].append({
            "modality": modality,
            "content": content,
            "timestamp": timestamp
        })

    def get_history(self, agent_id):
        return self.input_history.get(agent_id, [])

    def get_latest_by_modality(self, agent_id, modality: str):
        history = self.input_history.get(agent_id, [])
        filtered = [item for item in history if item["modality"] == modality]
        return filtered[-1] if filtered else None
