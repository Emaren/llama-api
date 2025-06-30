\"\"\"
session_history.py – Maintains chronological records of messages exchanged during a session.
Used for tracking, debugging, or generating reflection summaries.
\"\"\"

class SessionHistory:
    def __init__(self):
        self.history = {}

    def log_message(self, session_id: str, message: str):
        if session_id not in self.history:
            self.history[session_id] = []
        self.history[session_id].append(message)

    def get_history(self, session_id: str) -> list[str]:
        return self.history.get(session_id, [])

    def clear_history(self, session_id: str):
        if session_id in self.history:
            del self.history[session_id]
