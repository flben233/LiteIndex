import os
import time

import psutil
from fastapi import APIRouter
from pydantic import BaseModel

app = APIRouter()


class PerformanceInfo(BaseModel):
    cpu_usage: float
    memory_total: float
    memory_usage: float
    temperature: float
    net_upload: float
    net_download: float


@app.get("/api/performance/")
async def get_performance_info():
    # temperature
    result = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()

    # network
    sent_before = psutil.net_io_counters().bytes_sent
    recv_before = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = (sent_now - sent_before) / 1024
    recv = (recv_now - recv_before) / 1024

    return PerformanceInfo(
        cpu_usage=psutil.cpu_percent(),
        memory_total=psutil.virtual_memory().total,
        memory_usage=psutil.virtual_memory().used,
        temperature=float(result) / 1000,
        net_upload=sent,
        net_download=recv)
