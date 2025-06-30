\"\"\"
memory_simulator.py – Simulates memory scenarios and alternate trace evolutions
to model hypothetical system outcomes or memory alignment paths.
\"\"\"

from shared.memory_types import MemoryTrace
import random
import copy

class MemorySimulator:
    def __init__(self, variation_factor=0.1):
        self.variation_factor = variation_factor

    def simulate_alternatives(self, trace: MemoryTrace, num_variants=3):
        variants = []
        for _ in range(num_variants):
            simulated = copy.deepcopy(trace)
            simulated.metadata["relevance"] *= self._vary()
            simulated.metadata["engagement"] *= self._vary()
            simulated.metadata["rephrased"] = True
            variants.append(simulated)
        return variants

    def _vary(self):
        # Apply a small random variation to simulate natural uncertainty
        return 1 + random.uniform(-self.variation_factor, self.variation_factor)
