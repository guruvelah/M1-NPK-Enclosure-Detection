import cv2
import yaml


class Camera:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        c = cfg["camera"]
        self.index = int(c["index"])
        self.width = int(c["width"])
        self.height = int(c["height"])
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.index)

        if not self.cap.isOpened():
            raise RuntimeError(f"Unable to open camera index {self.index}")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def read(self):
        if self.cap is None:
            raise RuntimeError("Camera is not open")

        ok, frame = self.cap.read()

        if not ok:
            raise RuntimeError("Camera frame capture failed")

        return frame

    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
