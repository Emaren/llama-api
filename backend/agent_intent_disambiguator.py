# backend/agent_intent_disambiguator.py
# Clarifies ambiguous intents by leveraging context and historical data.

class AgentIntentDisambiguator:
    def __init__(self):
        self.intent_log = {}  # {agent_id: [ {intent, context, timestamp} ]}

    def log_intent(self, agent_id, intent: str, context: str, timestamp: str):
        if agent_id not in self.intent_log:
            self.intent_log[agent_id] = []
        self.intent_log[agent_id].append({
            "intent": intent,
            "context": context,
            "timestamp": timestamp
        })

    def disambiguate(self, agent_id, ambiguous_intent: str):
        # Placeholder: returns the most frequent matching intent from history
        intents = [entry["intent"] for entry in self.intent_log.get(agent_id, []) if ambiguous_intent in entry["intent"]]
        if not intents:
            return {"resolved": False, "reason": "No matching history"}
        from collections import Counter
        most_common = Counter(intents).most_common(1)[0][0]
        return {"resolved": True, "resolved_intent": most_common}
