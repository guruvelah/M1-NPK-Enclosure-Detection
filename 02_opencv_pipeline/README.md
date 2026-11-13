# 02 — OpenCV Pipeline

**Marks: 4/20**

The pipeline is designed for a Raspberry Pi camera at 640×480. It captures frames, performs detector inference and overlays:

- bounding box
- class name
- confidence
- inference latency
- FPS

Run:

```bash
python3 02_opencv_pipeline/main.py --source 0 --weights models/best.pt
```

The pipeline fails cleanly if the trained checkpoint is missing instead of displaying fabricated detections.
