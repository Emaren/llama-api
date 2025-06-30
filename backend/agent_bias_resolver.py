# backend/agent_bias_resolver.py
# Applies countermeasures when bias is detected in agent outputs.

from backend.memory_diffuser import MemoryDiffuser
from backend.self_reflection_writer import SelfReflectionWriter

class AgentBiasResolver:
    def __init__(self):
        self.memory_diffuser = MemoryDiffuser()
        self.reflection_writer = SelfReflectionWriter()

    def resolve_bias(self, agent_id, bias_vector):
        actions = []

        # Trigger memory diffusion if specific topic dominates
        dominant = [k for k, v in bias_vector.items() if v > 0.7]
        if dominant:
            self.memory_diffuser.diffuse(agent_id, tags=dominant)
            actions.append(f"Diffused memory for tags: {', '.join(dominant)}")

        # Trigger self-reflection
        self.reflection_writer.log(agent_id, {
            "trigger": "bias_correction",
            "bias_vector": bias_vector
        })
        actions.append("Initiated bias reflection sequence.")

        return {
            "agent_id": agent_id,
            "actions_taken": actions
        }
