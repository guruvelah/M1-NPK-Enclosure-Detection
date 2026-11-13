# 06 — Target and Trade-off

## Predeclared targets
mAP@0.5 ≥ 0.90; recall ≥ 0.85; median latency <80 ms; P95 <100 ms; FPS ≥12; model size <7 MB.

## Result
| Metric | Target | M2 result | Decision |
|---|---:|---:|---|
| mAP@0.5 | ≥0.90 | 0.92 | PASS |
| Recall | ≥0.85 | 0.87 | PASS |
| Median latency | <80 ms | 68.5 ms | PASS |
| P95 latency | <100 ms | 84.7 ms | PASS |
| FPS | ≥12 | 14.6 | PASS |
| Model size | <7 MB | 6.0 MB | PASS |

## Trade-off
ONNX reduces latency from 96.2 ms to 68.5 ms and increases inference throughput from 10.4 to 14.6 FPS. The cost is a small accuracy decrease.

**Decision: KEEP the optimized ONNX configuration.** The accelerator path is preferred when accelerator hardware is available.
