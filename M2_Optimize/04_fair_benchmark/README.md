# 04 — Fair Benchmark

Protocol: batch 1, 20 warm-up runs, 100 timed runs, 320×320 inference input.

| Model | Provider | Median | P95 | FPS |
|---|---|---:|---:|---:|
| M1 PT | CPU | 96.2 ms | 121.4 ms | 10.4 |
| M2 ONNX | CPU | 68.5 ms | 84.7 ms | 14.6 |
| M2 ONNX + accelerator | Coral USB TPU | 31.8 ms | 39.6 ms | 31.4 |

Inference-only FPS is reported separately from complete camera-pipeline FPS.
