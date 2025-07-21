# backend/state/token_tracker.py

from typing import Optional
from datetime import datetime

last_chat_token_stats = {
    "model": None,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "cost_usd": 0.0,
    "timestamp": None,
}
