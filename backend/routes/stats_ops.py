# backend/routes/stats_ops.py

from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("")
async def get_ops_stats():
    now = datetime.utcnow()
    points = []
    for i in range(12):
        ts = now - timedelta(seconds=(11 - i) * 5)
        points.append({
            "timestamp": ts.isoformat() + "Z",
            "ops": round(50 + i * 3 + ((-1)**i) * 8, 1),
        })
    return {"data": points}
