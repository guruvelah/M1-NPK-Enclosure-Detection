import os
import platform
import time

try:
    import psutil
except ImportError:
    psutil = None

print("System snapshot")
print(f"OS: {platform.platform()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor() or 'not reported'}")
if psutil:
    print(f"CPU cores: {psutil.cpu_count(logical=True)}")
    print(f"Memory total: {psutil.virtual_memory().total / (1024**3):.2f} GiB")
    print(f"Memory used: {psutil.virtual_memory().percent:.1f}%")
    print(f"CPU usage: {psutil.cpu_percent(interval=1):.1f}%")
else:
    print("Install psutil to report CPU and memory usage: pip install psutil")
