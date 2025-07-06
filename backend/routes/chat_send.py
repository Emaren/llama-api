# routes/chat_send.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from agent_coordinator import AgentCoordinator
from backend.memory_engine import save_memory, memory_engine
from backend.memory_scorer import score_memory

router = APIRouter()
coordinator = AgentCoordinator()

@router.post("/send")
async def send_chat_message(req: Request):
    try:
        # 🧠 Parse and debug input JSON
        try:
            data = await req.json()
        except Exception as parse_error:
            raw = await req.body()
            print("❌ Failed to parse JSON:", raw)
            raise parse_error

        print("📨 Chat Message Received:", data)

        # 📛 Extract fields
        user_id = "demo-user"  # Replace with Firebase UID in prod
        agent_name = data.get("agent_name") or data.get("agent") or "LlamaAgent42"
        content = data.get("message", "")
        session_id = f"{agent_name}-session"  # Ensures scoped memory

        # 🧠 Score memory
        score = score_memory(content)
        print(f"🧠 Message score: {score}")
        if score >= 1.0:
            await save_memory(user_id, agent_name, content, score, session_id=session_id)
            print("💾 Memory saved.")

        # 🔎 Retrieve scoped memory
        scoped_traces = memory_engine.retrieve_scope(session_id, content)
        scoped_content = "\n".join([t.content for t in scoped_traces])
        print(f"📚 Scoped Memory:\n{scoped_content}")

        # 🧩 Final prompt
        system_prompt = f"Relevant memory:\n{scoped_content}\n\nYou are a helpful assistant."
        print(f"📝 System Prompt:\n{system_prompt}\n✉️ User Message:\n{content}")

        # 🧠 Run LLM logic
        response_text = await coordinator.handle_input(
            content,
            session_id,
            user_id=user_id,
            agent_name=agent_name,
            system_prompt_override=system_prompt
        )

        print("📬 Response from coordinator:", response_text)
        return JSONResponse(content={"response": response_text}, status_code=200)

    except Exception as e:
        print("❌ Exception in /api/chat/send:", e)
        return JSONResponse(content={"error": "Invalid or empty JSON"}, status_code=400)
