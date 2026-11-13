# 02 — OpenCV Pipeline

## Purpose
Implement the camera-to-detector pipeline with OpenCV, displaying detections for the three project classes.

## Pipeline
Camera frame → model inference → bounding-box overlay → FPS and latency display.

## Run
```bash
python 02_opencv_pipeline/main.py
```

## Requirements
- OpenCV camera access
- Trained weights at `models/best.pt`
- Ultralytics installed from `requirements.txt`

Press `q` to exit.

## Evidence to collect
Capture a real Raspberry Pi screenshot showing:
- live camera feed
- detected object class
- bounding box
- confidence value
- measured FPS / inference latency

The provided mockup images are not live inference evidence.
