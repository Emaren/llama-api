class TeamEventLogger:
    def __init__(self):
        self.events = []

    def log_event(self, event_type, details):
        from datetime import datetime
        self.events.append({
            "type": event_type,
            "details": details,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_events(self):
        return self.events
