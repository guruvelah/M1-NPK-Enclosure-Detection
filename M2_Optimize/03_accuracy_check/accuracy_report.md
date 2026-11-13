# 03 — Accuracy Check

The original M1 PT model and optimized ONNX model were compared on the **same 12-image held-out test set**.

| Metric | M1 PT | M2 ONNX | Change |
|---|---:|---:|---:|
| Precision | 0.91 | 0.90 | -0.01 |
| Recall | 0.88 | 0.87 | -0.01 |
| mAP@0.5 | 0.93 | 0.92 | -0.01 |
| mAP@0.5–0.95 | 0.72 | 0.70 | -0.02 |

## Acceptance decision

The predeclared acceptance rule is:

- mAP@0.5 loss ≤ 0.03
- recall loss ≤ 0.03
- measurable latency improvement

All three conditions are satisfied.

**Result: PASS.**

The optimized model is slightly less accurate but materially faster, which is the intended M2 edge-deployment trade-off.
