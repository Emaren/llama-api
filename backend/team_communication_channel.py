class TeamCommunicationChannel:
    def __init__(self):
        self.channels = {}

    def add_channel(self, channel_name, participants):
        self.channels[channel_name] = participants

    def send_message(self, channel_name, sender, message):
        if channel_name not in self.channels:
            raise ValueError("Channel does not exist")
        # In a real system, this would route message properly
        print(f"Message from {sender} to {channel_name}: {message}")

    def get_participants(self, channel_name):
        return self.channels.get(channel_name, [])
