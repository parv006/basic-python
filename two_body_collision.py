
import matplotlib.pyplot as plt
import numpy as np

mb=100000000
ms=1
vs=0.0
vb=-10.0
c=[] 
m=[-10000.0] 
n=[0] 
pl=[] 
pl1=[] 
pbl=[] 
kil=[] 
kfl=[]

while True:
    ki=(mb*(vb**2))+(ms*(vs**2))
    kil.append(ki)
    pb=mb*vb+ms*vs
    pbl.append(pb)
    vb=(((mb-ms)/(mb+ms))*vb)+(((2*ms)/(ms+mb))*vs)
    m.append(vb*((mb)**(1/2)))
    m.append(vb*((mb)**(1/2)))
    vs=(((ms-mb)/(mb+ms))*vs)+(((2*mb)/(ms+mb))*vb)
    n.append(vs*((ms)**(1/2))) # type: ignore
    c.append(1)
  
    p1=mb*vb+ms*vs
    pl.append(p1)
    if (vs>0 and vb>0) and vb>vs:
        break
    vs=-vs
    n.append(vs) # type: ignore
    c.append(1)
    p2=mb*vb+ms*vs
    pl1.append(p2)
    
    kf=(mb*(vb**2))+(ms*(vs**2))
    kfl.append(kf)
    if (vs>0 and vb>0) and vb>vs:
        break
   
if len(n)<len(m):
  n.append(0)
if len(pl1)<len(pl):
  pl1.append(0)
if len(pl1)<len(pbl):
  pl1.append(0)
if len(kil)<len(kfl):
  kil.append(0)
print(len(c))
plt.plot(m,n)
plt.show()
