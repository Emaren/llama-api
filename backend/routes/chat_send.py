# routes/chat_send.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/send")
async def send_chat_message(req: Request):
    try:
        data = await req.json()
        print("📨 Chat Message Received:", data)
    except Exception as e:
        print("❌ JSON parse error:", e)
        return JSONResponse(content={"error": "Invalid or empty JSON"}, status_code=400)

    return JSONResponse(content={"status": "received"}, status_code=200)
