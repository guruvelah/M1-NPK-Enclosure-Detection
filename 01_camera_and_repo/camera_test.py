import cv2
import sys

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("CAMERA TEST: FAIL")
    sys.exit(1)

ok, frame = cap.read()
cap.release()

if not ok or frame is None:
    print("CAMERA TEST: FAIL - frame capture failed")
    sys.exit(2)

print("CAMERA TEST: PASS")
print(f"Resolution: {frame.shape[1]}x{frame.shape[0]}")
print(f"Channels: {frame.shape[2]}")
