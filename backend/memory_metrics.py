\"\"\"
memory_metrics.py – Tracks and generates memory performance metrics like recall rate,
compression ratio, decay velocity, and memory retrieval latency.
\"\"\"

from typing import List
from shared.memory_types import MemoryTrace

class MemoryMetrics:
    def __init__(self):
        self.recall_attempts = 0
        self.successful_recalls = 0
        self.total_latency = 0.0
        self.access_count = 0

    def log_recall(self, success: bool, latency: float):
        self.recall_attempts += 1
        if success:
            self.successful_recalls += 1
        self.total_latency += latency
        self.access_count += 1

    def compute_metrics(self):
        recall_rate = (
            self.successful_recalls / self.recall_attempts
            if self.recall_attempts > 0 else 0.0
        )
        avg_latency = (
            self.total_latency / self.access_count
            if self.access_count > 0 else 0.0
        )
        return {
            "recall_rate": round(recall_rate, 3),
            "average_latency": round(avg_latency, 3),
            "total_recalls": self.recall_attempts,
            "successful_recalls": self.successful_recalls,
        }
