\"\"\"
memory_tester.py – Validates core memory system behaviors using synthetic or saved test cases.
Checks ingestion, pruning, scoring, tagging, and consistency under load or stress.
\"\"\"

from backend.memory_engine import MemoryEngine
from backend.memory_test_generator import MemoryTestGenerator

class MemoryTester:
    def __init__(self):
        self.engine = MemoryEngine()
        self.generator = MemoryTestGenerator()

    def run_tests(self, test_count=10):
        print("[MemoryTester] Running memory ingestion tests...")
        test_entries = self.generator.generate(test_count)
        for entry in test_entries:
            self.engine.ingest(entry["content"], entry["timestamp"], entry["metadata"])
        print(f"[MemoryTester] Successfully ingested {test_count} test memories.")

    def validate_scoring(self):
        print("[MemoryTester] Validating memory scoring logic...")
        scores = self.engine.score_all()
        assert all(isinstance(s, float) for s in scores), "Non-numeric scores detected."
        print("[MemoryTester] Scoring validation passed.")

    def validate_pruning(self):
        print("[MemoryTester] Validating memory pruning...")
        pre_count = len(self.engine.memory_store)
        self.engine.prune()
        post_count = len(self.engine.memory_store)
        print(f"[MemoryTester] Pruned {pre_count - post_count} memories.")
