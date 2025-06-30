# backend/agent_coordinator.py
# Central coordinator to manage and orchestrate agents

# import ollama  # Add this import

class AgentCoordinator:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_id, agent):
        self.agents[agent_id] = agent

    def unregister_agent(self, agent_id):
        if agent_id in self.agents:
            del self.agents[agent_id]

    def send_command(self, agent_id, command):
        if agent_id in self.agents:
            self.agents[agent_id].execute_command(command)

    def broadcast(self, message):
        for agent in self.agents.values():
            agent.receive_message(message)

    def initialize_system(self):
        print("[AgentCoordinator] System initialized.")

    def handle_input(self, user_input, session_id):
        print(f"[AgentCoordinator] Handling input: '{user_input}' for session: {session_id}")

        try:
            response = ollama.chat(
                model='zephyr:latest',
                messages=[{ "role": "user", "content": user_input }]
            )
            return response['message']['content']
        except Exception as e:
            print(f"[AgentCoordinator] Ollama error: {e}")
            return "❌ Error processing with Zephyr."
