\"\"\"
memory_loader.py – Loads memory traces from persistent storage and prepares
them for use in active memory systems.
\"\"\"

import json
from shared.memory_types import MemoryTrace

class MemoryLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_memory(self) -> list[MemoryTrace]:
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            traces = [MemoryTrace(**item) for item in data]
            print(f"[MemoryLoader] Loaded {len(traces)} memory traces from {self.filepath}")
            return traces
        except Exception as e:
            print(f"[MemoryLoader] Error loading memory: {e}")
            return []
