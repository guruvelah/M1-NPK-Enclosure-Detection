# 04 — Dataset V1

**Marks: 4/20**

Target class:

`range_finder_enclosure`

The dataset is based on the enclosure photographs supplied for the assignment. Each source image is annotated with a bounding box around the enclosure and represented in YOLO format.

### YOLO label
```
2 x_center y_center width height
```

### Dataset design

- 3 independent source views
- 5 controlled variants per source
- 18 labelled images
- no image-level duplicate is intentionally moved between train/validation/test

### Recommended next capture round

For a stronger final M2 dataset, capture at least 100 Raspberry Pi images across:
- front view
- left/right view
- different distances
- bright/dim lighting
- partial occlusion
- different backgrounds
- enclosure empty/occupied
