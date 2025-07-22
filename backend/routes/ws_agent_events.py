# Web-Socket endpoint: /logs/agent-events

from __future__ import annotations
import asyncio, json
from datetime import datetime
from typing import Set

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()
clients: Set[WebSocket] = set()

@router.websocket("/logs/agent-events")
async def agent_events(ws: WebSocket) -> None:
    await ws.accept()
    clients.add(ws)
    print("🧠 WS client connected")

    try:
        while True:
            # ignore any inbound text; broadcast every ~0.75 s
            try:
                await asyncio.wait_for(ws.receive_text(), timeout=0.75)
            except asyncio.TimeoutError:
                pass

            payload = {
                "agent": "GoalOptimizer",
                "timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
                "message": "Reprioritized tasks based on engagement.",
            }
            dead = []
            for c in clients:
                try:
                    await c.send_text(json.dumps(payload))
                except WebSocketDisconnect:
                    dead.append(c)
            for d in dead:
                clients.discard(d)

    except WebSocketDisconnect:
        print("❌ WS client disconnected")
        clients.discard(ws)
