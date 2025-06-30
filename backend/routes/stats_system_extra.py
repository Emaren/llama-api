# backend/routes/stats_system_extra.py

from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("")
async def get_network_stats():
    now = datetime.utcnow()
    points = []
    for i in range(12):
        ts = now - timedelta(seconds=(11 - i) * 5)
        points.append({
            "timestamp": ts.isoformat() + "Z",
            "netInKB": round(5 + i * 1.2 + ((-1)**i) * 0.8, 2),
            "netOutKB": round(3 + i * 1.5 + ((-1)**i) * 0.5, 2),
        })
    return {"data": points}
