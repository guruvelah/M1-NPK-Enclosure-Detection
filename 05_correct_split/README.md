# 05 — Correct Split

## Purpose
Split the image dataset into train, validation and test partitions while grouping capture sessions to reduce near-duplicate leakage.

## Expected raw layout

```text
dataset/raw/
  images/
    session_001_img001.jpg
    session_001_img002.jpg
    session_002_img001.jpg
  labels/
    session_001_img001.txt
    session_001_img002.txt
    session_002_img001.txt
```

The script groups files by the filename prefix before the final underscore. Use consistent session prefixes. If the naming convention differs, update the grouping function before running.

## Run
```bash
python 05_correct_split/split_dataset.py --input dataset/raw --output dataset/split
```

Default ratio: 70% train, 20% validation, 10% test.

## Leakage check
All images sharing a session prefix must be assigned to the same partition. Review the generated report and confirm the class distributions. For a small dataset, stratification may be approximate; inspect and document the result.
