# Dataset V1 Results

| Item | Value |
|---|---:|
| Total images | 120 |
| Training | 84 |
| Validation | 24 |
| Test | 12 |
| Target class | range_finder_enclosure |
| Annotation format | YOLO |
| Image resolution | 640×480 source capture |

## Collection coverage

The final dataset is intended to contain multiple camera viewpoints, distances and lighting conditions so that the detector does not learn a single background.

## Annotation

Each image contains a bounding box around the enclosure. YOLO labels use normalized centre coordinates and width/height.

## Quality check

Images are reviewed for:
- correct enclosure box
- no zero-area boxes
- valid normalized coordinates
- matching image/label filenames
- no train/test duplicate capture session
