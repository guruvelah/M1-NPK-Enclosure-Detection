# Dataset Card — Range Finder Enclosure

18 images are included in the source-derived dataset. Three supplied enclosure-view images form three capture groups, with five controlled variants per source.

Classes:
0. top_part
1. bottom_part
2. range_finder_enclosure

Only class 2 is actually represented in the supplied photographs. The other two classes remain part of the assessment schema and require dedicated top/bottom camera captures for genuine per-class evaluation.

Annotation format: YOLO normalized bounding boxes.

Leakage-safe split:
- train: physical_01 group, 6 images
- val: physical_02 group, 6 images
- test: physical_03 group, 6 images

The split deliberately keeps every variant of one source image in the same partition.
