import argparse
import random
import shutil
from collections import defaultdict
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def group_key(path: Path) -> str:
    # Expected filename: sessionID_frameID.jpg
    # All frames from one session remain in a single split.
    return path.stem.rsplit("_", 1)[0] if "_" in path.stem else path.stem

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="dataset/raw")
    p.add_argument("--output", default="dataset/split")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--train", type=float, default=0.70)
    p.add_argument("--val", type=float, default=0.20)
    args = p.parse_args()

    if args.train <= 0 or args.val <= 0 or args.train + args.val >= 1:
        p.error("train and val must be positive and sum to less than 1")

    root = Path(args.input)
    images_dir, labels_dir = root / "images", root / "labels"
    if not images_dir.is_dir() or not labels_dir.is_dir():
        raise FileNotFoundError("Expected input/images and input/labels directories")

    groups = defaultdict(list)
    for img in images_dir.iterdir():
        if img.is_file() and img.suffix.lower() in IMAGE_EXTS:
            label = labels_dir / f"{img.stem}.txt"
            if not label.is_file():
                raise FileNotFoundError(f"Missing label file for {img.name}")
            groups[group_key(img)].append((img, label))

    keys = sorted(groups)
    if len(keys) < 3:
        raise ValueError("Need at least 3 distinct capture groups for train/val/test")

    random.Random(args.seed).shuffle(keys)
    n = len(keys)
    n_train = max(1, round(n * args.train))
    n_val = max(1, round(n * args.val))
    if n_train + n_val >= n:
        n_train = n - 2
        n_val = 1

    partitions = {
        "train": keys[:n_train],
        "val": keys[n_train:n_train+n_val],
        "test": keys[n_train+n_val:],
    }

    for split, split_groups in partitions.items():
        for sub in ("images", "labels"):
            (Path(args.output) / sub / split).mkdir(parents=True, exist_ok=True)

        for key in split_groups:
            for img, label in groups[key]:
                shutil.copy2(img, Path(args.output) / "images" / split / img.name)
                shutil.copy2(label, Path(args.output) / "labels" / split / label.name)

    membership = {}
    for split, split_groups in partitions.items():
        for key in split_groups:
            if key in membership:
                raise RuntimeError(f"Group leakage detected: {key}")
            membership[key] = split

    print(f"Groups: {n}")
    print(f"Images: {sum(len(v) for v in groups.values())}")
    for split, split_groups in partitions.items():
        count = sum(len(groups[k]) for k in split_groups)
        print(f"{split}: {len(split_groups)} groups, {count} images")
    print("Group leakage check: PASS")

if __name__ == "__main__":
    main()
