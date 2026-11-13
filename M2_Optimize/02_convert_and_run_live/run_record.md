# 02 — Convert and Run Live

| Field | Result |
|---|---|
| Runtime | ONNX Runtime |
| Execution provider | CPUExecutionProvider |
| Input | Raspberry Pi CSI camera |
| Live resolution | 640 × 480 |
| Model input | 320 × 320 |
| Batch | 1 |
| Live run | PASS |
| Mean inference latency | 70.1 ms |
| Sustained inference FPS | 14.2 FPS |
| Average confidence | 0.90 |

The live pipeline maintains the same detection target as M1 and overlays bounding boxes, confidence, latency and FPS.
