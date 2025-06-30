class TeamCommunicationManager:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, content):
        self.messages.append({
            "sender": sender,
            "receiver": receiver,
            "content": content
        })

    def get_messages_for(self, receiver):
        return [msg for msg in self.messages if msg["receiver"] == receiver]
