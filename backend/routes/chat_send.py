# backend/routes/chat_send.py
"""
Single-endpoint wrapper that receives a chat message, calls the agent
coordinator, and records the token usage via bump_usage().
"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from agent_coordinator         import AgentCoordinator
from backend.memory_engine     import save_memory, memory_engine
from backend.memory_scorer     import score_memory
from backend.routes.chat_stats import bump_usage          # ← use new tracker

router      = APIRouter()
coordinator = AgentCoordinator()


@router.post("/send")
async def send_chat_message(req: Request):
    try:
        data = await req.json()
        print("📨 /chat/send payload:", data)

        # ---- extract ---------------------------------------------------
        user_id      = "demo-user"                 # swap for Firebase uid
        agent_name   = data.get("agent") or "LlamaAgent42"
        content      = data.get("message", "")
        session_id   = f"{agent_name}-session"

        # ---- memory scoring / storage ----------------------------------
        score = score_memory(content)
        if score >= 1.0:
            await save_memory(user_id, agent_name, content, score, session_id)

        # ---- retrieve scoped memory for prompt -------------------------
        scoped_traces  = memory_engine.retrieve_scope(session_id, content)
        scoped_context = "\n".join(t.content for t in scoped_traces)
        system_prompt  = f"Relevant memory:\n{scoped_context}\n\nYou are a helpful assistant."

        # ---- run the agent ---------------------------------------------
        response_text = await coordinator.handle_input(
            content,
            session_id,
            user_id=user_id,
            agent_name=agent_name,
            system_prompt_override=system_prompt,
        )

        # ---- token usage -----------------------------------------------
        usage = getattr(coordinator, "last_token_usage", None)
        if usage:
            bump_usage(
                prompt_tokens     = usage.get("prompt_tokens", 0),
                completion_tokens = usage.get("completion_tokens", 0),
                model_name        = usage.get("model", "unknown"),
                cost_usd          = usage.get("cost_usd", 0.0),
            )

        return JSONResponse(content={"response": response_text}, status_code=200)

    except Exception as exc:
        print("❌ /api/chat/send error:", exc)
        return JSONResponse({"error": "invalid request"}, status_code=400)
