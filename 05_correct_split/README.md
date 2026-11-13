# 05 — Correct Split

**Marks: 2/20**

The split is **grouped by source capture**, preventing variants of the same original image from leaking into multiple partitions.

| Split | Images | Source |
|---|---:|---|
| Train | 6 | source view 1 |
| Validation | 6 | source view 2 |
| Test | 6 | source view 3 |

This is intentionally conservative because only three independent source photographs were supplied.

A larger real Raspberry Pi dataset should use a larger grouped split, for example 70/20/10 by capture session.
