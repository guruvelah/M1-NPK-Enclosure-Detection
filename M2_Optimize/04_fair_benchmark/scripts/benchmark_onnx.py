import argparse,time,statistics
import numpy as np
import onnxruntime as ort

p=argparse.ArgumentParser()
p.add_argument("--model",required=True)
p.add_argument("--runs",type=int,default=100)
p.add_argument("--warmup",type=int,default=20)
a=p.parse_args()

s=ort.InferenceSession(a.model,providers=["CPUExecutionProvider"])
inp=s.get_inputs()[0]
shape=[1,3,320,320]
x=np.zeros(shape,dtype=np.float32)
feed={inp.name:x}

for _ in range(a.warmup): s.run(None,feed)

times=[]
for _ in range(a.runs):
    t=time.perf_counter()
    s.run(None,feed)
    times.append((time.perf_counter()-t)*1000)

median=statistics.median(times)
p95=sorted(times)[int(.95*len(times))-1]
print(f"Runs: {a.runs}")
print(f"Median latency: {median:.2f} ms")
print(f"P95 latency: {p95:.2f} ms")
print(f"Inference FPS: {1000/median:.2f}")
