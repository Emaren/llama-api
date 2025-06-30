\"\"\"
memory_tagger.py – Assigns tags to memory entries based on content, emotional tone,
contextual relevance, or predefined schema.
\"\"\"

from shared.tone_utils import detect_tone
from shared.context_filters import extract_keywords

class MemoryTagger:
    def __init__(self, tagging_rules=None):
        self.rules = tagging_rules or {
            "reflective": lambda m: "I think" in m.content,
            "emotional": lambda m: detect_tone(m.content) in ["sad", "angry", "joyful"],
            "goal-related": lambda m: "goal" in m.content.lower()
        }

    def tag(self, memory_entry):
        tags = []
        for tag, rule in self.rules.items():
            if rule(memory_entry):
                tags.append(tag)
        keywords = extract_keywords(memory_entry.content)
        tags.extend([f"kw:{kw}" for kw in keywords])
        memory_entry.tags = list(set(tags))
        return memory_entry
