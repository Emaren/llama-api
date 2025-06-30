\"\"\"
memory_test_generator.py – Generates synthetic memory entries and edge-case scenarios
for use in testing memory ingestion, tagging, pruning, scoring, and querying.
\"\"\"

import random
from datetime import datetime, timedelta

TEMPLATES = [
    "User asked about {topic}.",
    "A conversation about {topic} occurred.",
    "System responded emotionally about {topic}.",
]

TOPICS = ["self-improvement", "AI ethics", "project deadlines", "user feedback", "reflection"]

class MemoryTestGenerator:
    def __init__(self, seed=42):
        random.seed(seed)

    def generate(self, count=10):
        memory_entries = []
        for _ in range(count):
            content = random.choice(TEMPLATES).format(topic=random.choice(TOPICS))
            timestamp = datetime.utcnow() - timedelta(minutes=random.randint(1, 1000))
            memory_entries.append({
                "content": content,
                "timestamp": timestamp.isoformat(),
                "metadata": {
                    "generated": True
                }
            })
        return memory_entries
