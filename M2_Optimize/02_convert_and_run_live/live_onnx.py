import argparse,time,cv2
import numpy as np
import onnxruntime as ort

p=argparse.ArgumentParser()
p.add_argument("--model",required=True)
p.add_argument("--source",default="0")
a=p.parse_args()

session=ort.InferenceSession(a.model,providers=["CPUExecutionProvider"])
inp=session.get_inputs()[0]
name=inp.name
shape=inp.shape
h=int(shape[2]) if isinstance(shape[2],int) else 320
w=int(shape[3]) if isinstance(shape[3],int) else 320

src=int(a.source) if a.source.isdigit() else a.source
cap=cv2.VideoCapture(src,cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if not cap.isOpened():
    raise RuntimeError("Camera unavailable")

while True:
    ok,frame=cap.read()
    if not ok: break
    x=cv2.resize(frame,(w,h))
    x=cv2.cvtColor(x,cv2.COLOR_BGR2RGB).astype(np.float32)/255.0
    x=np.transpose(x,(2,0,1))[None,...]

    t=time.perf_counter()
    session.run(None,{name:x})
    ms=(time.perf_counter()-t)*1000

    cv2.putText(frame,f"ONNX latency {ms:.1f} ms | FPS {1000/ms:.1f}",
                (10,28),cv2.FONT_HERSHEY_SIMPLEX,.55,(0,255,0),2)
    cv2.imshow("M2 ONNX Live",frame)
    if cv2.waitKey(1)&0xFF==ord("q"): break

cap.release()
cv2.destroyAllWindows()
