class TeamCommunication:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, content):
        self.messages.append({
            "from": sender,
            "to": receiver,
            "content": content,
            "timestamp": self._current_time()
        })

    def receive_messages(self, receiver):
        return [msg for msg in self.messages if msg["to"] == receiver]

    def _current_time(self):
        import datetime
        return datetime.datetime.utcnow().isoformat()
