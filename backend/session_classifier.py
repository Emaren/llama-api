\"\"\"
session_classifier.py – Classifies the type of session based on recent message history,
such as debug sessions, casual chats, or goal-oriented dialogues.
\"\"\"

from shared.session_types import SESSION_TYPES

class SessionClassifier:
    def classify(self, conversation_history: list[str]) -> str:
        if not conversation_history:
            return "unknown"

        recent = " ".join(conversation_history[-5:]).lower()
        if any(word in recent for word in ["fix", "bug", "debug"]):
            return "debug"
        elif any(word in recent for word in ["goal", "objective", "milestone"]):
            return "goal-oriented"
        elif any(word in recent for word in ["hi", "what's up", "how are you"]):
            return "casual"
        else:
            return "general"
