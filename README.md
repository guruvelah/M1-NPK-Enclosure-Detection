# Edge AI Embedded Vision — M1 & M2

## Project
**IDRP Parts / Range Finder Enclosure Detection**

This repository contains the M1 Detect and M2 Optimize assessment deliverables for Raspberry Pi edge vision.

### Objects
- Top model
- Bottom model
- Physical 3D-printed enclosure / printed part

### M1 — Detect
Implemented:
- configurable camera input
- Ultralytics YOLO detector
- confidence threshold
- IoU threshold
- bounding-box rendering
- per-detection confidence
- measured inference latency
- evidence documentation

**Physical enclosure evidence:** three supplied viewpoints are included under `evidence/m1/`.

> The supplied screenshots are labelled as demo/mockup and illustrative-only. They are not claimed as live Raspberry Pi inference measurements.

### M2 — Optimize
Implemented:
- repeatable frame benchmark
- FPS measurement
- mean/median/min/max latency
- configurable frame count
- configurable detector input settings
- benchmark CSV output

M2 performance values must be populated from the actual Raspberry Pi run. No hardware measurements are fabricated.

### Raspberry Pi quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Place the trained YOLO weights at:

```text
models/vision_model.pt
```

Then:

```bash
python -m src.main
```

Run M2:

```BENCHMARK_FRAMES=100 python scripts/benchmark.py
```

The result is saved to:

```text
data/measurements/benchmark.csv
```

## M1 evidence
See:
- `milestones/M1_Detect.md`
- `evidence/m1/`

## M2 evidence
See:
- `milestones/M2_Optimize.md`
- `scripts/benchmark.py`
- `data/measurements/`

## Assessment integrity
Measured FPS, latency, confidence and model-size values are intentionally not invented. Run the supplied benchmark on the target Raspberry Pi and commit the generated CSV/results.
