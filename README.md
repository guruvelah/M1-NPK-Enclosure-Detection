# M1 — Range Finder Enclosure Detection

This repository follows the six-part M1 assessment structure supplied for the Edge AI & Embedded Vision Systems assignment.

## Assessment mapping

| Task | Marks | Folder |
|---|---:|---|
| Camera and repository | 2 | [01_camera_and_repo](01_camera_and_repo/) |
| OpenCV pipeline | 4 | [02_opencv_pipeline](02_opencv_pipeline/) |
| Baseline speed | 3 | [03_baseline_speed](03_baseline_speed/) |
| Dataset v1 | 4 | [04_dataset_v1](04_dataset_v1/) |
| Correct split | 2 | [05_correct_split](05_correct_split/) |
| Train and run detector | 5 | [06_train_and_run_detector](06_train_and_run_detector/) |
| **M1 total** | **20** | |

## Detection classes

- `top_part`
- `bottom_part`
- `range_finder_enclosure`

## Dataset actually included

An 18-image source-derived dataset is documented under `04_dataset_v1/` and `dataset/`. It uses the three enclosure-view images supplied for this assignment plus five controlled variants per source image.

The split is leakage-safe by source-image group:

| Split | Images | Source group |
|---|---:|---|
| Train | 6 | physical_01 |
| Validation | 6 | physical_02 |
| Test | 6 | physical_03 |

The supplied source images contain a presentation overlay and explicitly describe the displayed FPS/latency/confidence as illustrative rather than live inference. Therefore those values are **not** reported as Raspberry Pi measurements.

## Raspberry Pi evidence

Run these on the actual target device:

```bash
python 01_camera_and_repo/camera_test.py
python 01_camera_and_repo/capture_frame.py
python 03_baseline_speed/benchmark.py --source 0 --frames 100
```

The benchmark produces mean/median latency and FPS for the configured OpenCV path. For the final detector benchmark, use the same protocol around the trained detector.

## Detector training

The repository includes a YOLO training/validation entry point. Install the detector runtime on the Raspberry Pi or training machine, then train and validate using the included `dataset/data.yaml`.

Ultralytics distinguishes quantitative validation on labeled data from prediction on new images: validation reports precision/recall/mAP metrics, while prediction produces annotated outputs for qualitative inspection. citeturn150850search0turn150850search2

## Submission integrity

No Raspberry Pi FPS, latency, confidence, model size, mAP, precision or recall values are fabricated in this repository. Those values must come from the actual hardware/detector run.

See `reports/ASSIGNMENT_STATUS.md` for the exact remaining hardware evidence checklist.
