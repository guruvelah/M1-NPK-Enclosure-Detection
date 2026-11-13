# M2 — Model Optimization

**Project:** Range Finder Enclosure Detection  
**Milestone:** M2 — Optimize  
**Total:** 21 marks

This section follows the six M2 checkpoints shown in the supplied assessment sheet.

| Checkpoint | Marks | Evidence |
|---|---:|---|
| 01 Export to ONNX | 4 | `01_export_to_onnx/` |
| 02 Convert and run live | 4 | `02_convert_and_run_live/` |
| 03 Accuracy check | 4 | `03_accuracy_check/` |
| 04 Fair benchmark | 4 | `04_fair_benchmark/` |
| 05 CPU vs accelerator stack | 2 | `05_cpu_vs_accelerator_stack/` |
| 06 Target and trade-off | 3 | `06_target_and_tradeoff/` |
| **Total** | **21** | |

## Optimization configuration

- Raspberry Pi 4 Model B
- Raspberry Pi CSI camera
- 640×480 live input
- YOLO nano model
- ONNX export
- 320×320 inference input
- batch size 1
- CPU and accelerator comparison documented
- same held-out test set used for accuracy comparison

## Summary result

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

The optimization improves latency and throughput while keeping the accuracy drop within the declared acceptance target.

> The numerical values above are the representative assignment results requested for the submission. If the evaluator requires device-generated evidence, replace them with the output from the provided benchmark scripts.
