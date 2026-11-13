# 06 — Train and Run Detector

**Marks: 5/20**

Training command:

```bash
python3 -m pip install ultralytics
yolo detect train model=yolo26n.pt data=dataset/data.yaml epochs=100 imgsz=640 project=runs/detect name=rangefinder
```

Validation:

```bash
yolo detect val model=runs/detect/rangefinder/weights/best.pt data=dataset/data.yaml split=test
```

Inference:

```bash
yolo detect predict model=runs/detect/rangefinder/weights/best.pt source=dataset/split/images/test save=True
```

### Required reported metrics

- Precision
- Recall
- mAP50
- mAP50-95
- inference latency
- FPS

The numbers must be copied from the actual Pi/model run. No screenshot-only value is presented as a measured model result.
