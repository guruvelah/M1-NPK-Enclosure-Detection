import argparse
import os
import cv2
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="0")
    p.add_argument("--weights", default="runs/detect/rangefinder/weights/best.pt")
    p.add_argument("--conf", type=float, default=0.25)
    p.add_argument("--imgsz", type=int, default=640)
    args = p.parse_args()

    if not os.path.isfile(args.weights):
        raise FileNotFoundError(f"Trained weights not found: {args.weights}")

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.weights)
    results = model.predict(source=source, conf=args.conf, imgsz=args.imgsz, show=True)
    print(f"Processed {len(results)} result frame(s).")

if __name__ == "__main__":
    main()
