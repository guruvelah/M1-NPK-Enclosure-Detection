import argparse
import time
import cv2

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None

p = argparse.ArgumentParser()
p.add_argument("--source", default="0")
p.add_argument("--weights", default="models/best.pt")
args = p.parse_args()

if YOLO is None:
    raise RuntimeError("Install ultralytics first: pip install ultralytics")

source = int(args.source) if args.source.isdigit() else args.source
model = YOLO(args.weights)
cap = cv2.VideoCapture(source, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    raise RuntimeError("Could not open Raspberry Pi camera")

prev = time.perf_counter()

while True:
    ok, frame = cap.read()
    if not ok:
        break

    t0 = time.perf_counter()
    result = model.predict(frame, imgsz=320, conf=0.40, verbose=False)[0]
    latency_ms = (time.perf_counter() - t0) * 1000
    fps = 1000 / latency_ms if latency_ms > 0 else 0

    annotated = result.plot()
    cv2.putText(annotated, f"Inference: {latency_ms:.1f} ms",
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX, .6, (0,255,0), 2)
    cv2.putText(annotated, f"FPS: {fps:.1f}",
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, .6, (0,255,0), 2)

    cv2.imshow("Range Finder Enclosure", annotated)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
