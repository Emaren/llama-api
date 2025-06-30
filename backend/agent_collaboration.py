# backend/agent_collaboration.py
# Facilitates collaboration and communication between multiple agents

class AgentCollaboration:
    def __init__(self):
        self.collaboration_sessions = {}

    def start_session(self, session_id, agents):
        self.collaboration_sessions[session_id] = agents

    def end_session(self, session_id):
        if session_id in self.collaboration_sessions:
            del self.collaboration_sessions[session_id]

    def send_message(self, session_id, sender_id, message):
        if session_id in self.collaboration_sessions:
            for agent in self.collaboration_sessions[session_id]:
                if agent.id != sender_id:
                    agent.receive_message(message)

