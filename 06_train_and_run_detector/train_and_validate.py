from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    project="runs/detect",
    name="rangefinder",
)
metrics = model.val(
    data="dataset/data.yaml",
    split="test",
)
print("mAP50-95:", metrics.box.map)
print("mAP50:", metrics.box.map50)
print("Precision:", metrics.box.mp)
print("Recall:", metrics.box.mr)
