# 01 — Camera and Repository

## Purpose
Verify the camera connected to the Raspberry Pi and capture a repeatable frame for the enclosure-detection workflow.

## Hardware record
Fill these fields from the physical setup; do not assume a camera model that has not been confirmed.

| Item | Value |
|---|---|
| Host board | Raspberry Pi (record exact model) |
| Camera | Record exact module / USB webcam |
| Interface | CSI / USB |
| Resolution | 640 × 480 default; update to measured setting |
| Capture backend | OpenCV VideoCapture |
| Camera index | 0 by default |

## Files
- `camera_specs.md`
- `camera_test.py`
- `capture_frame.py`

## Run
```bash
python 01_camera_and_repo/camera_test.py
python 01_camera_and_repo/capture_frame.py
```

Captured image is written to `evidence/camera/`.

## Evidence to collect
1. Photograph of Raspberry Pi and camera connection.
2. Terminal output showing successful camera open.
3. Captured frame showing the actual test scene.

Do not use the assessment-sheet screenshot as proof that the camera is operating.
