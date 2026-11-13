# 05 — CPU vs Accelerator Stack

| Item | CPU path | Accelerator path |
|---|---|---|
| Hardware | Raspberry Pi 4 CPU | Raspberry Pi 4 + Coral USB TPU |
| Runtime | ONNX Runtime | Edge accelerator runtime |
| Median latency | 68.5 ms | 31.8 ms |
| P95 latency | 84.7 ms | 39.6 ms |
| FPS | 14.6 | 31.4 |
| CPU utilization | 69% | 31% |
| Accelerator utilization | 0% | 72% |
| Temperature | 58°C | 55°C |
| mAP@0.5 | 0.92 | 0.91 |

## Stack
Camera → OpenCV → resize/normalize → inference runtime → post-processing → bounding box → display.
