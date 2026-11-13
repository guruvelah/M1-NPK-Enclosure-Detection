import csv
import os
import statistics
import time

from src.camera import Camera
from src.detector import Detector


def main():
    n = int(os.getenv("BENCHMARK_FRAMES", "100"))

    camera = Camera()
    detector = Detector()

    camera.open()

    latencies = []

    # Warm-up frames are intentionally excluded from the reported statistics.
    warmup = int(os.getenv("BENCHMARK_WARMUP", "10"))

    for _ in range(warmup):
        frame = camera.read()
        detector.predict(frame)

    start = time.perf_counter()

    for _ in range(n):
        frame = camera.read()
        _, latency_ms = detector.predict(frame)
        latencies.append(latency_ms)

    elapsed = time.perf_counter() - start
    camera.release()

    fps = n / elapsed
    mean_latency = statistics.mean(latencies)
    median_latency = statistics.median(latencies)

    os.makedirs("data/measurements", exist_ok=True)

    output = "data/measurements/benchmark.csv"

    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "frames",
            "elapsed_s",
            "fps",
            "mean_latency_ms",
            "median_latency_ms",
            "min_latency_ms",
            "max_latency_ms",
        ])
        writer.writerow([
            n,
            elapsed,
            fps,
            mean_latency,
            median_latency,
            min(latencies),
            max(latencies),
        ])

    print(f"FPS={fps:.3f}")
    print(f"Mean latency={mean_latency:.3f} ms")
    print(f"Median latency={median_latency:.3f} ms")
    print(f"Min latency={min(latencies):.3f} ms")
    print(f"Max latency={max(latencies):.3f} ms")
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
