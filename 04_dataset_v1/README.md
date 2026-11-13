# 04 — Dataset v1

## Classes
0. top_part
1. bottom_part
2. range_finder_enclosure

The supplied STL files describe top and bottom geometry. Physical photographs show the assembled enclosure. They are different views/objects and should be labelled consistently with the annotation policy below.

## Data organization

```text
dataset/
  raw/
    images/
    labels/
  split/
    images/
      train/
      val/
      test/
    labels/
      train/
      val/
      test/
```

For YOLO detection, each image has a text label file with rows:

```text
class_id x_center y_center width height
```

Coordinates must be normalized to 0..1. Boxes must be tight and visible objects only.

## Data integrity
- Include different camera angles, distances, backgrounds and lighting.
- Avoid near-duplicate frames in different splits.
- Keep all frames from the same capture session in one split group.
- Do not create empty labels for images containing the target object.
- Maintain a separate test set not used for training or threshold tuning.

## Current status
The directory contains configuration and documentation only. The real image dataset and labels must be added before training. The three supplied visual mockups should not be treated as original training photos or verified inference outputs.
