# backend/routes/stats_data.py

from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("")
async def get_data_stats():
    now = datetime.utcnow()
    points = []
    for i in range(12):
        ts = now - timedelta(seconds=(11 - i) * 5)
        points.append({
            "timestamp": ts.isoformat() + "Z",
            "itemsProcessed": round(200 + i * 15 + ((-1)**i) * 30, 0),
        })
    return {"data": points}
