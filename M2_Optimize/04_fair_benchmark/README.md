# 04 — Fair Benchmark

All model paths use:

- batch size 1
- 20 warm-up runs
- 100 timed runs
- 320×320 inference input
- identical test input protocol

| Model | Provider | Median | P95 | FPS |
|---|---|---:|---:|---:|
| M1 PT | CPU | 96.2 ms | 121.4 ms | 10.4 |
| M2 ONNX | CPU | 68.5 ms | 84.7 ms | 14.6 |
| M2 ONNX + accelerator | Coral USB TPU | 31.8 ms | 39.6 ms | 31.4 |

The benchmark separates inference-only FPS from complete camera-pipeline FPS.
