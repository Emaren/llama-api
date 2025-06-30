# backend/routes/ws_agent_events.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio, json
from datetime import datetime

router = APIRouter(prefix="/logs/agent-events")
connected_clients: set[WebSocket] = set()

@router.websocket("")
async def agent_events(websocket: WebSocket):
    await websocket.accept()
    print("🧠 WebSocket connection accepted")
    connected_clients.add(websocket)

    try:
        while True:
            # Prevent timeout — read from client or timeout
            try:
                await asyncio.wait_for(websocket.receive_text(), timeout=1.0)
            except asyncio.TimeoutError:
                pass  # normal behavior — just keeps connection alive

            # Simulated message (every second)
            event = {
                "agent": "GoalOptimizer",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "message": "Reprioritized tasks based on engagement."
            }
            data = json.dumps(event)
            print("📤 Broadcasting:", data)

            dead = []
            for client in connected_clients:
                try:
                    await client.send_text(data)
                except WebSocketDisconnect:
                    dead.append(client)
            for d in dead:
                connected_clients.discard(d)

    except WebSocketDisconnect:
        print("❌ Client closed WebSocket")
        connected_clients.discard(websocket)
