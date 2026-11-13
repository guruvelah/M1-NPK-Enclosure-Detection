# 01 — Export to ONNX

| Field | Result |
|---|---|
| Source model | YOLO nano trained M1 checkpoint |
| Framework | Ultralytics |
| Input | 320×320 |
| Batch | 1 |
| ONNX opset | 12 |
| PT size | 6.2 MB |
| ONNX size | 6.0 MB |
| Status | PASS |

Command:
```bash
python3 scripts/export_yolo_to_onnx.py --weights ../models/best.pt --imgsz 320 --opset 12
```
