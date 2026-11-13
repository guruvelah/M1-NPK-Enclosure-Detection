import cv2
import sys

CAMERA_INDEX = 0
WIDTH = 640
HEIGHT = 480

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print(f"ERROR: Could not open camera index {CAMERA_INDEX}")
        print("Check CSI/USB connection, permissions and camera configuration.")
        return 1

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    ok, frame = cap.read()
    if not ok or frame is None:
        print("ERROR: Camera opened but frame capture failed.")
        cap.release()
        return 2

    h, w = frame.shape[:2]
    print("CAMERA TEST: PASS")
    print(f"Camera index: {CAMERA_INDEX}")
    print(f"Captured resolution: {w}x{h}")
    print(f"Frame dtype: {frame.dtype}")
    print(f"Frame shape: {frame.shape}")
    cap.release()
    return 0

if __name__ == "__main__":
    sys.exit(main())
