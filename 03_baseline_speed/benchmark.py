import argparse
import csv
import os
import statistics
import time
import cv2
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="0")
    p.add_argument("--weights", default="models/best.pt")
    p.add_argument("--frames", type=int, default=100)
    p.add_argument("--warmup", type=int, default=10)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--conf", type=float, default=0.25)
    args = p.parse_args()

    if args.frames < 1:
        p.error("--frames must be >= 1")
    if not os.path.isfile(args.weights):
        raise FileNotFoundError(f"Missing model weights: {args.weights}")

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.weights)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open source {args.source}")

    timings = []
    try:
        for _ in range(args.warmup):
            ok, frame = cap.read()
            if not ok:
                raise RuntimeError("Camera/video ended during warm-up")
            model.predict(frame, imgsz=args.imgsz, conf=args.conf, verbose=False)

        for _ in range(args.frames):
            ok, frame = cap.read()
            if not ok:
                raise RuntimeError("Camera/video ended before requested frame count")
            t0 = time.perf_counter()
            model.predict(frame, imgsz=args.imgsz, conf=args.conf, verbose=False)
            timings.append((time.perf_counter() - t0) * 1000.0)
    finally:
        cap.release()

    mean_ms = statistics.mean(timings)
    median_ms = statistics.median(timings)
    total_s = sum(timings) / 1000.0
    fps_inference = len(timings) / total_s if total_s else 0.0

    out = "03_baseline_speed/results"
    os.makedirs(out, exist_ok=True)
    csv_path = os.path.join(out, "baseline_benchmark.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "frames", "warmup_frames", "mean_latency_ms", "median_latency_ms",
            "min_latency_ms", "max_latency_ms", "inference_fps"
        ])
        writer.writeheader()
        writer.writerow({
            "frames": len(timings), "warmup_frames": args.warmup,
            "mean_latency_ms": mean_ms, "median_latency_ms": median_ms,
            "min_latency_ms": min(timings), "max_latency_ms": max(timings),
            "inference_fps": fps_inference,
        })

    print(f"Measured frames: {len(timings)}")
    print(f"Mean inference latency: {mean_ms:.2f} ms")
    print(f"Median inference latency: {median_ms:.2f} ms")
    print(f"Min / max latency: {min(timings):.2f} / {max(timings):.2f} ms")
    print(f"Inference FPS: {fps_inference:.2f}")
    print(f"CSV: {csv_path}")

if __name__ == "__main__":
    main()
