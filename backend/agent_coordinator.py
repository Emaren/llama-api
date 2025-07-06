# backend/agent_coordinator.py
# Central coordinator to manage and orchestrate agents

import ollama  # Ensure this is uncommented
import asyncio
from memory_loader import load_memories

# Initialize Ollama client with local HTTP endpoint (no SSL context issues)
client = ollama.Client(host='http://localhost:11434')

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

    async def handle_input(self, user_input, session_id, user_id="demo-user", agent_name="LlamaAgent42"):
        print(f"[AgentCoordinator] Handling input: '{user_input}' for session: {session_id}")

        try:
            # Load relevant memories
            memories = await load_memories(user_id, agent_name)
            memory_lines = "\n".join(f"- {m}" for m in memories)
            memory_block = f"Here is what you already know about the user:\n{memory_lines}\n\n"

            messages = [
                {
                    "role": "system",
                    "content": memory_block + "You are a helpful agent. Stay in character and be consistent with known facts."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]

            response = await client.acompletion(
                model='zephyr:latest',
                messages=messages,
                stream=False,
            )
            return response['choices'][0]['message']['content']

        except Exception as e:
            print(f"[AgentCoordinator] Ollama error: {e}")
            return "❌ Error processing with Zephyr."
