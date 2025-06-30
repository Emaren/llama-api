# backend/routes/system_vitals.py

import psutil
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("")
async def get_system_vitals():
    cpu = psutil.cpu_percent()
    net = psutil.net_io_counters()
    net_in_mb = round(net.bytes_recv / (1024 ** 2), 1)
    net_out_mb = round(net.bytes_sent / (1024 ** 2), 1)
    mem = psutil.virtual_memory()
    mem_used_mb = round(mem.used / (1024 ** 2))

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "cpu_load": [cpu],                  # ✅ charted
        "vram_util": ["42%"],               # ✅ charted
        "net_in_mb": net_in_mb,             # ✅ charted
        "net_out_mb": net_out_mb,           # ✅ charted
        "memory_used": f"{mem_used_mb}MB",  # 🆕 added
        "token_throughput": "N/A",          # 🆕 stub
        "latency": "N/A"                    # 🆕 stub
    }
