# M2 — Optimize (20 marks)

## Objective
Measure the inference pipeline on the Raspberry Pi and document the performance trade-off of a lightweight edge-vision configuration.

## Baseline

Run the benchmark using the configured detector:

```bash
BENCHMARK_FRAMES=100 python scripts/benchmark.py
```

The benchmark records:
- FPS
- mean latency
- median latency
- minimum latency
- maximum latency

Output:

```text
data/measurements/benchmark.csv
```

## Optimization strategy

The project uses a Raspberry Pi-appropriate inference pipeline:
- lightweight YOLO detector
- configurable confidence threshold
- configurable IoU threshold
- configurable detector device
- camera frame input
- repeatable benchmark loop

The benchmark measures the actual inference call rather than estimating performance theoretically.

## Results

The numerical values below must come from the target Raspberry Pi. They are deliberately not fabricated.

| Metric | Baseline | Optimized |
|---|---:|---:|
| FPS | Pending hardware run | Pending hardware run |
| Mean latency | Pending | Pending |
| Median latency | Pending | Pending |
| Model size | Pending | Pending |
| Detection metric | Pending | Pending |

## Accuracy / confidence comparison

For a valid M2 comparison, run the same evaluation images through both configurations and compare:
- detection confidence
- missed detections
- false detections
- model size
- latency
- FPS

Do not use FPS alone as the optimization criterion.

## Benchmark acceptance procedure

1. Use the same camera and test scene.
2. Use the same number of frames.
3. Warm up the detector before comparing configurations.
4. Record mean and median latency.
5. Record FPS.
6. Record model file size.
7. Compare detection quality on the same test set.
8. Commit the resulting CSV and evidence screenshots.

## M2 evidence checklist

- [x] Benchmark implementation
- [x] Repeatable CSV output
- [x] Configurable inference pipeline
- [ ] Baseline Raspberry Pi benchmark
- [ ] Optimized Raspberry Pi benchmark
- [ ] CPU/memory observation
- [ ] Model size measurement
- [ ] Accuracy/confidence comparison
- [x] M2 repository commit

## Required evidence command

```bash
BENCHMARK_FRAMES=100 python scripts/benchmark.py
```
