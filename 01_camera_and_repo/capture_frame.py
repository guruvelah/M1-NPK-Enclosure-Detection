import os
from datetime import datetime
import cv2

CAMERA_INDEX = 0
WIDTH, HEIGHT = 640, 480

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open camera index {CAMERA_INDEX}")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    ok, frame = cap.read()
    cap.release()

    if not ok or frame is None:
        raise RuntimeError("Failed to capture a frame")

    out_dir = "evidence/camera"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"camera_{datetime.now():%Y%m%d_%H%M%S}.jpg")
    if not cv2.imwrite(path, frame):
        raise RuntimeError(f"Could not write {path}")
    print(f"Saved camera frame: {path}")

if __name__ == "__main__":
    main()
