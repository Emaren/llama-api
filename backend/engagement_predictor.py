\"\"\"
engagement_predictor.py – Predicts how engaging the last response was
based on content length, emoji usage, tone shifts, and response variety.
\"\"\"

import random

class EngagementPredictor:
    def __init__(self):
        pass

    def score_response(self, response: str) -> float:
        length_score = min(len(response) / 1000, 1.0)
        emoji_score = response.count("🔥") + response.count("😅") + response.count("💡")
        tone_score = 0.3 if any(kw in response.lower() for kw in ["great", "awesome", "interesting"]) else 0

        noise = random.uniform(-0.05, 0.05)
        total = min(1.0, max(0.0, 0.6 * length_score + 0.3 * emoji_score + tone_score + noise))
        print(f"[Engagement] score: {round(total, 3)}")
        return round(total, 3)
