import argparse
from pathlib import Path
from ultralytics import YOLO
p=argparse.ArgumentParser()
p.add_argument("--weights",required=True); p.add_argument("--imgsz",type=int,default=320); p.add_argument("--opset",type=int,default=12)
a=p.parse_args()
w=Path(a.weights)
if not w.is_file(): raise SystemExit(f"Weights not found: {w}")
out=YOLO(str(w)).export(format="onnx",imgsz=a.imgsz,opset=a.opset,dynamic=False)
print("ONNX export:",out)
print("Status: PASS")
