import argparse
import os
import time
import cv2
from ultralytics import YOLO

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="0", help="Camera index or video/image path")
    p.add_argument("--weights", default="models/best.pt")
    p.add_argument("--conf", type=float, default=0.25)
    p.add_argument("--imgsz", type=int, default=640)
    return p.parse_args()

def main():
    args = parse_args()
    if not os.path.isfile(args.weights):
        raise FileNotFoundError(
            f"Model weights not found: {args.weights}. Train the model first."
        )

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.weights)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError(f"Unable to open source: {args.source}")

    previous = time.perf_counter()
    fps = 0.0

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("End of stream or camera frame unavailable.")
                break

            start = time.perf_counter()
            result = model.predict(frame, conf=args.conf, imgsz=args.imgsz, verbose=False)[0]
            latency_ms = (time.perf_counter() - start) * 1000.0

            annotated = result.plot()
            now = time.perf_counter()
            dt = now - previous
            previous = now
            if dt > 0:
                fps = 0.9 * fps + 0.1 * (1.0 / dt) if fps else 1.0 / dt

            cv2.putText(annotated, f"Inference: {latency_ms:.1f} ms",
                        (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0,255,0), 2)
            cv2.putText(annotated, f"Pipeline FPS: {fps:.1f}",
                        (10, 52), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0,255,0), 2)

            cv2.imshow("Range Finder Enclosure Detection", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
