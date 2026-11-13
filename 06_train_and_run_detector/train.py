import argparse
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="04_dataset_v1/data.yaml")
    p.add_argument("--model", default="yolov8n.pt")
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=8)
    args = p.parse_args()

    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        project="runs/detect",
        name="rangefinder",
        exist_ok=True,
    )

if __name__ == "__main__":
    main()
