import argparse,time,statistics
import numpy as np
import onnxruntime as ort
p=argparse.ArgumentParser()
p.add_argument("--model",required=True); p.add_argument("--runs",type=int,default=100); p.add_argument("--warmup",type=int,default=20)
a=p.parse_args()
s=ort.InferenceSession(a.model,providers=["CPUExecutionProvider"])
inp=s.get_inputs()[0]; x=np.zeros((1,3,320,320),dtype=np.float32); feed={inp.name:x}
for _ in range(a.warmup): s.run(None,feed)
t=[]
for _ in range(a.runs):
    t0=time.perf_counter(); s.run(None,feed); t.append((time.perf_counter()-t0)*1000)
med=statistics.median(t); p95=sorted(t)[int(.95*len(t))-1]
print(f"Median: {med:.2f} ms"); print(f"P95: {p95:.2f} ms"); print(f"FPS: {1000/med:.2f}")
