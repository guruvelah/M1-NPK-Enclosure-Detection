# M1 + M2 — Range Finder Enclosure Detection

Edge AI & Embedded Vision Systems assignment.

## Assessment structure

| ID | Task | Marks |
|---|---|---:|
| 01 | Camera and repository | 2 |
| 02 | OpenCV pipeline | 4 |
| 03 | Baseline speed | 3 |
| 04 | Dataset V1 | 4 |
| 05 | Correct split | 2 |
| 06 | Train and run detector | 5 |
| | **M1 Total** | **20** |

## Target
Detect the **range finder enclosure** from a Raspberry Pi camera using OpenCV and a compact YOLO detector.

## Hardware
Raspberry Pi + CSI camera. The pipeline is configured for 640×480 capture and uses OpenCV/V4L2 for the camera path.

## Evidence
- Camera test: `01_camera_and_repo/camera_test.py`
- Live detector: `02_opencv_pipeline/main.py`
- Baseline benchmark: `03_baseline_speed/benchmark.py`
- Dataset documentation: `04_dataset_v1/README.md`
- Split protocol: `05_correct_split/README.md`
- Training/validation: `06_train_and_run_detector/`

## Important
The supplied reference screenshots explicitly state that their FPS, latency and confidence are illustrative and not live inference. This repository therefore does **not** misrepresent those values as measured Pi results. Run the supplied benchmark on the Pi to produce the actual device numbers.

Repository URL:
https://github.com/guruvelah/M1-NPK-Enclosure-Detection
