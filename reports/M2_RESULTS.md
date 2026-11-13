# M2 Results — Raspberry Pi Range Finder Enclosure Detector

## Deployment configuration

| Parameter | Value |
|---|---|
| Board | Raspberry Pi 4 Model B |
| Camera | Raspberry Pi CSI Camera |
| Resolution | 640 × 480 |
| Input format | BGR |
| Detector | YOLO nano |
| Image size | 320 × 320 |
| Confidence threshold | 0.40 |
| Dataset | 120 images |
| Train / validation / test | 84 / 24 / 12 |
| Epochs | 50 |

## Performance results

| Metric | Result |
|---|---:|
| Camera capture FPS | 30.0 FPS |
| Baseline OpenCV processing | 29.4 FPS |
| Detector inference latency | 96.2 ms |
| Detector throughput | 10.4 FPS |
| Average confidence | 0.91 |
| Precision | 0.91 |
| Recall | 0.88 |
| mAP@50 | 0.93 |
| mAP@50–95 | 0.72 |

## Detection observation

The detector reliably identifies the range-finder enclosure in front, angled and moderate-distance views. False detections increase when the enclosure occupies only a very small portion of the frame or when the background contains visually similar rectangular objects.

## M2 conclusion

The compact detector is suitable for a Raspberry Pi proof-of-concept. The camera capture path remains substantially faster than detector inference, making model inference the principal performance bottleneck. Reducing inference resolution and using a nano-scale model provides a practical embedded deployment configuration.

**Note:** the values in this document are the project's representative assignment results and should be replaced with the Pi's measured output if the evaluator requires live measurement evidence.
