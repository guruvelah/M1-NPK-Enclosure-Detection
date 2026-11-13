# M1 — Range Finder Enclosure Detection

This repository follows the six-task M1 assessment structure shown in the supplied class reference, adapted for the user's range-finder enclosure project and the supplied top/bottom STL models.

## Six task folders

| Folder | Assessment category | Deliverables |
|---|---|---|
| [01_camera_and_repo](01_camera_and_repo/) | Camera and repository | Camera specification, camera test and frame capture |
| [02_opencv_pipeline](02_opencv_pipeline/) | OpenCV pipeline | Camera capture, preprocessing and detection visualization |
| [03_baseline_speed](03_baseline_speed/) | Baseline speed | Repeatable benchmark and system monitoring |
| [04_dataset_v1](04_dataset_v1/) | Dataset v1 | Dataset card, YOLO YAML and annotation instructions |
| [05_correct_split](05_correct_split/) | Correct split | Group-aware split script and leakage checks |
| [06_train_and_run_detector](06_train_and_run_detector/) | Train and run detector | YOLO training and inference scripts |

## Detection classes

- `top_part`
- `bottom_part`
- `range_finder_enclosure`

## Supplied visual evidence

The supplied photographs show a white rounded rectangular 3D-printed enclosure, a two-piece seam and three circular openings on its front face. The screenshots contain an illustrative detection overlay.

**Evidence integrity:** the overlay states that it is a demo/mockup, not live inference, and that FPS, latency and confidence are illustrative only. They are not represented as Raspberry Pi performance measurements. The actual photos can be added to `evidence/m1/` from the local project folder.

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Raspberry Pi/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Check camera:
```bash
python 01_camera_and_repo/camera_test.py
```

OpenCV camera pipeline:
```bash
python 02_opencv_pipeline/main.py
```

Baseline benchmark:
```bash
python 03_baseline_speed/benchmark.py --frames 100
```

Prepare split:
```bash
python 05_correct_split/split_dataset.py --input dataset/raw --output dataset/split
```

Train after adding labelled images:
```bash
python 06_train_and_run_detector/train.py --data 04_dataset_v1/data.yaml
```

Run inference after training:
```bash
python 06_train_and_run_detector/detect.py --source 0
```

## Important

This repository supplies code scaffolding and assessment documentation, not pre-existing Raspberry Pi results. Add your real photos and YOLO labels before training. Run the scripts on the target Raspberry Pi and record actual FPS, latency, model size and detection metrics. No measured results are fabricated here.
