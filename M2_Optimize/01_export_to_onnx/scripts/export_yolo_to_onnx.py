import argparse
from pathlib import Path
from ultralytics import YOLO

p=argparse.ArgumentParser()
p.add_argument("--weights",required=True)
p.add_argument("--imgsz",type=int,default=320)
p.add_argument("--opset",type=int,default=12)
a=p.parse_args()

weights=Path(a.weights)
if not weights.is_file():
    raise SystemExit(f"Weights not found: {weights}")

model=YOLO(str(weights))
out=model.export(format="onnx",imgsz=a.imgsz,opset=a.opset,dynamic=False)
print(f"ONNX export: {out}")
print("Export status: PASS")
