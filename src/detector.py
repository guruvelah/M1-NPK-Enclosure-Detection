import os
import time
from dataclasses import dataclass

import yaml

try:
    from ultralytics import YOLO
except Exception:
    YOLO = None


@dataclass
class Detection:
    class_name: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int


class Detector:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        d = cfg["detector"]
        self.weights = d["weights"]
        self.conf = float(d["confidence"])
        self.iou = float(d["iou"])
        self.device = d["device"]

        if YOLO is None:
            raise RuntimeError(
                "Ultralytics is not installed. Run pip install -r requirements.txt"
            )

        if not os.path.exists(self.weights):
            raise FileNotFoundError(
                f"Model weights not found: {self.weights}. "
                "Place the trained YOLO weights there."
            )

        self.model = YOLO(self.weights)

    def predict(self, frame):
        t0 = time.perf_counter()

        result = self.model.predict(
            source=frame,
            conf=self.conf,
            iou=self.iou,
            device=self.device,
            verbose=False,
        )[0]

        latency_ms = (time.perf_counter() - t0) * 1000.0
        detections = []

        names = result.names

        if result.boxes is not None:
            for box in result.boxes:
                cls = int(box.cls.item())
                confidence = float(box.conf.item())
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                detections.append(
                    Detection(
                        class_name=names[cls],
                        confidence=confidence,
                        x1=x1,
                        y1=y1,
                        x2=x2,
                        y2=y2,
                    )
                )

        return detections, latency_ms


def draw_detections(frame, detections):
    import cv2

    for d in detections:
        cv2.rectangle(
            frame,
            (d.x1, d.y1),
            (d.x2, d.y2),
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"{d.class_name} {d.confidence:.2f}",
            (d.x1, max(20, d.y1 - 8)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

    return frame
