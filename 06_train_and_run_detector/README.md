# 06 — Train and Run Detector

## Before training
1. Collect real images on the target camera.
2. Label every visible target in YOLO format.
3. Run the group-aware split from task 05.
4. Review label files and class distribution.
5. Install dependencies.

## Train
```bash
python 06_train_and_run_detector/train.py --data 04_dataset_v1/data.yaml --epochs 100 --imgsz 640
```

## Detect from camera
```bash
python 06_train_and_run_detector/detect.py --source 0 --weights runs/detect/rangefinder/weights/best.pt
```

## Detect from image
```bash
python 06_train_and_run_detector/detect.py --source path/to/test_image.jpg --weights runs/detect/rangefinder/weights/best.pt
```

## Evaluation
Record the Ultralytics validation metrics and inspect test-set predictions. Do not claim a trained model or performance score until the dataset is labelled and training has actually run.
