import argparse
import time
import statistics
import cv2

p = argparse.ArgumentParser()
p.add_argument("--source", default="0")
p.add_argument("--frames", type=int, default=100)
a = p.parse_args()

src = int(a.source) if a.source.isdigit() else a.source
cap = cv2.VideoCapture(src, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    raise RuntimeError("Camera could not be opened")

latencies = []

for _ in range(10):
    ok, _ = cap.read()
    if not ok:
        raise RuntimeError("Warm-up capture failed")

for _ in range(a.frames):
    ok, frame = cap.read()
    if not ok:
        raise RuntimeError("Capture failed")

    t0 = time.perf_counter()
    _ = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    latency = (time.perf_counter() - t0) * 1000
    latencies.append(latency)

cap.release()

mean_ms = statistics.mean(latencies)
median_ms = statistics.median(latencies)

print("BASELINE BENCHMARK")
print(f"Frames: {len(latencies)}")
print(f"Mean latency: {mean_ms:.3f} ms")
print(f"Median latency: {median_ms:.3f} ms")
print(f"FPS: {1000/mean_ms:.2f}")
