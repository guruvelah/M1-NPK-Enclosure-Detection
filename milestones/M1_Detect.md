# M1 — Detect (20 marks)

## Objective
Demonstrate camera capture and object detection for the assessment objects on the Raspberry Pi.

## Detection targets
1. Top model
2. Bottom model
3. Physical 3D-printed enclosure / printed part

## Implemented pipeline
Camera frame → YOLO detector → bounding boxes → class label → confidence → latency measurement.

## Evidence checklist

| Requirement | Status | Evidence |
|---|---|---|
| Raspberry Pi + camera photo | Pending hardware capture | Must be captured on the target Raspberry Pi |
| Detector running on-device | Implemented in `src/detector.py` and `src/main.py` | Run on Raspberry Pi |
| Top model detection | Implemented | Capture live inference screenshot |
| Bottom model detection | Implemented | Capture live inference screenshot |
| Physical printed-part detection | Evidence supplied | `evidence/m1/printed_part_view_1.jpg`, `printed_part_view_2.jpg`, `printed_part_view_3.jpg` |
| Detection confidence recorded | Implemented in detector output | Record live value from Raspberry Pi |
| Detection latency recorded | Implemented in detector output | Record live value from Raspberry Pi |
| M1 commit | Completed | Git commit |

## Physical enclosure evidence

The supplied images show the same white rectangular enclosure from multiple viewpoints. The enclosure has rounded/chamfered corners, a visible two-piece seam and three circular openings on the front face.

The supplied screenshots contain the label:

**RANGE FINDER ENCLOSURE • DETECTED**

The screenshots themselves state that they are demo/mockup evidence and that FPS, latency and confidence are illustrative only. Therefore this repository treats them as visual enclosure evidence, not as measured live-inference performance.

## Measured values

Fill these only from the actual Raspberry Pi run:

| Metric | Result |
|---|---:|
| Detection confidence — Top | ______ % |
| Detection confidence — Bottom | ______ % |
| Detection confidence — Printed part | ______ % |
| Inference latency | ______ ms |
| FPS | ______ |

## Demonstration statement

> I can show the camera feed, the bounding box, the predicted class and the confidence value on the Raspberry Pi.

## M1 run command

```bash
python -m src.main
```
