from fastapi import APIRouter
import psutil, threading, time
from collections import deque

router = APIRouter()
_WINDOW = 60

cpu_hist = deque(maxlen=_WINDOW)
mem_hist = deque(maxlen=_WINDOW)

def _sample():
    cpu_hist.append(psutil.cpu_percent())
    mem_hist.append(psutil.virtual_memory().percent)

@router.on_event("startup")
def _start():
    threading.Thread(target=lambda: (_sample() or time.sleep(1)) or _start(), daemon=True).start()

@router.get("/", tags=["stats"])
def get_stats():
    return {"cpu": list(cpu_hist), "mem": list(mem_hist)}

__all__ = ["router"]
