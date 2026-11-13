# 03 — Baseline Speed

**Marks: 3/20**

Baseline is measured on the Raspberry Pi before optimization.

### Measurement procedure

- Resolution: 640×480
- Warm-up frames: 10
- Measured frames: 100
- Same camera and lighting used for comparison
- FPS calculated from measured inference latency

Run:

```bash
python3 03_baseline_speed/benchmark.py --source 0 --frames 100
```

Example report format:

| Metric | Baseline |
|---|---:|
| Resolution | 640×480 |
| Frames | 100 |
| Mean inference | record from Pi |
| Median inference | record from Pi |
| FPS | record from Pi |

**Important:** the supplied assessment screenshot says its FPS/latency values are illustrative. Therefore this repository does not claim those screenshot numbers as measured Raspberry Pi results.
