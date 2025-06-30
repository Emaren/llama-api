\"\"\"
message_ranker.py – Assigns scores to user/assistant messages based on clarity, coherence, relevance,
and emotional weight. Can be used to improve engagement, memory scoring, and summarization.
\"\"\"

from shared.vector_math import cosine_similarity
from shared.constants import MESSAGE_SCORING_WEIGHTS

class MessageRanker:
    def __init__(self):
        self.weights = MESSAGE_SCORING_WEIGHTS

    def score(self, message_embedding, goal_embedding, context_embedding):
        goal_score = cosine_similarity(message_embedding, goal_embedding)
        context_score = cosine_similarity(message_embedding, context_embedding)
        final_score = (
            self.weights["goal"] * goal_score +
            self.weights["context"] * context_score
        )
        return final_score

    def rank(self, messages, goal_embedding, context_embedding):
        scored = [
            (msg, self.score(msg["embedding"], goal_embedding, context_embedding))
            for msg in messages
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
