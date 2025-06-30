\"\"\"
interaction_logger.py – Logs all message-level interactions including user inputs,
agent outputs, token usage, timestamps, and sentiment metadata.
\"\"\"

import time
from backend.sentiment_parser import SentimentParser
from shared.utils import get_token_count

class InteractionLogger:
    def __init__(self):
        self.logs = {}
        self.sentiment_parser = SentimentParser()

    def log(self, session_id: str, user_input: str, agent_response: str):
        timestamp = time.time()
        sentiment = self.sentiment_parser.analyze(user_input)
        tokens_used = get_token_count(user_input + agent_response)

        entry = {
            "timestamp": timestamp,
            "input": user_input,
            "response": agent_response,
            "sentiment": sentiment,
            "tokens": tokens_used,
        }

        if session_id not in self.logs:
            self.logs[session_id] = []

        self.logs[session_id].append(entry)
        print(f"[Logger] Logged interaction for session {session_id} at {timestamp}")

    def get_session_log(self, session_id: str):
        return self.logs.get(session_id, [])
