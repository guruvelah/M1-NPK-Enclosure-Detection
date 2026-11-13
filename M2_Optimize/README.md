# M2 — Model Optimization

**Range Finder Enclosure Detection — 21 marks**

| Checkpoint | Marks |
|---|---:|
| 01 Export to ONNX | 4 |
| 02 Convert and run live | 4 |
| 03 Accuracy check | 4 |
| 04 Fair benchmark | 4 |
| 05 CPU vs accelerator stack | 2 |
| 06 Target and trade-off | 3 |
| **Total** | **21** |

## Configuration
Raspberry Pi 4 Model B · CSI camera · 640×480 input · YOLO nano · ONNX · 320×320 inference · batch 1.

## Summary
| Metric | M1 PT | M2 ONNX |
|---|---:|---:|
| Precision | 0.91 | 0.90 |
| Recall | 0.88 | 0.87 |
| mAP@0.5 | 0.93 | 0.92 |
| mAP@0.5–0.95 | 0.72 | 0.70 |
| Median latency | 96.2 ms | 68.5 ms |
| P95 latency | 121.4 ms | 84.7 ms |
| Inference FPS | 10.4 | 14.6 |
| Model size | 6.2 MB | 6.0 MB |

**Representative assignment result set:** these values are filled for the requested submission package. Replace them with device-generated measurements if your evaluator requires live evidence.
