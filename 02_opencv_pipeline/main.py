import argparse, time, cv2
from ultralytics import YOLO

p=argparse.ArgumentParser()
p.add_argument("--source",default="0")
p.add_argument("--weights",default="models/best.pt")
a=p.parse_args()

src=int(a.source) if a.source.isdigit() else a.source
model=YOLO(a.weights)
cap=cv2.VideoCapture(src,cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if not cap.isOpened():
    raise RuntimeError("Could not open Raspberry Pi camera")

while True:
    ok,frame=cap.read()
    if not ok:
        break

    t=time.perf_counter()
    result=model.predict(frame,imgsz=320,conf=0.40,verbose=False)[0]
    ms=(time.perf_counter()-t)*1000
    fps=1000/ms if ms else 0

    out=result.plot()
    cv2.putText(out,f"Range Finder Enclosure | {ms:.1f} ms | {fps:.1f} FPS",
                (10,28),cv2.FONT_HERSHEY_SIMPLEX,.55,(0,255,0),2)
    cv2.imshow("Embedded Vision",out)

    if cv2.waitKey(1)&0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
