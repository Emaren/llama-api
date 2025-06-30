# ✏️  pseudo-code – adapt to your collectors
payload = {
    "memory_used":  f"{psutil.virtual_memory().used // 1_000_000}MB",
    "cpu_load":     f"{psutil.cpu_percent()}%",
    "vram_util":    gpu.percent if gpu else None,          # ← new
    "net_in_mb":    round(net.bytes_recv / 1_000_000, 1),  # ← new
    "net_out_mb":   round(net.bytes_sent / 1_000_000, 1),  # ← new
    "tokens_per_s": token_rate or "N/A",                   # already for LLM
    "latency_ms":   latency_ms or None                     # ← new
}
