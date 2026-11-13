# 01 — Export to ONNX

| Field | Result |
|---|---|
| Source model | YOLO nano trained M1 checkpoint |
| Framework | Ultralytics |
| Input dimensions | 320 × 320 |
| Batch size | 1 |
| ONNX opset | 12 |
| Export format | ONNX |
| PT model size | 6.2 MB |
| ONNX model size | 6.0 MB |
| Export status | PASS |
| Export device | Raspberry Pi 4 / development PC |

## Command

```bash
python3 scripts/export_yolo_to_onnx.py --weights ../models/best.pt --imgsz 320 --opset 12
```

## Acceptance
ONNX model loads successfully in ONNX Runtime and exposes the expected input/output tensors.
