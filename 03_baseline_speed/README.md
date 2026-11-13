# 03 — Baseline Speed

## Purpose
Measure baseline end-to-end detector performance on the target Raspberry Pi.

## Run
```bash
python 03_baseline_speed/benchmark.py --source 0 --weights models/best.pt --frames 100
```

Run on the target device. The script performs warm-up inference, measures inference time over the requested number of captured frames, and prints mean/median latency and FPS. It writes CSV results beneath `03_baseline_speed/results/`.

## System monitor
In a second terminal:
```bash
python 03_baseline_speed/system_monitor.py
```

## Evidence to collect
- Raspberry Pi model and OS
- model file size
- benchmark command
- raw terminal output
- generated CSV
- CPU and memory snapshot

Never copy benchmark results from another person's device.
