# 03 — Accuracy Check

Same 12-image held-out test set.

| Metric | M1 PT | M2 ONNX | Change |
|---|---:|---:|---:|
| Precision | 0.91 | 0.90 | -0.01 |
| Recall | 0.88 | 0.87 | -0.01 |
| mAP@0.5 | 0.93 | 0.92 | -0.01 |
| mAP@0.5–0.95 | 0.72 | 0.70 | -0.02 |

Acceptance: mAP@0.5 loss ≤0.03, recall loss ≤0.03 and measurable latency improvement.

**Result: PASS.**
