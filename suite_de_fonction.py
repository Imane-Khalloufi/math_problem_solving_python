def delta (x):
    if x >=0 and x<= 1/2:
        return x
    else: return 1-x
def d(n,x):
    if n==0:
        return delta (x)
    elif 2*x<=1 and x>=0:
        return 0.5*d(n-1,2*x)
    else:
        return 0.5*d(n-1,2*x-1)
import numpy as np
import matplotlib.pyplot as plt
X=np.arange(0,1,0.001)
for i in range(6):
    Y=[d(i,x) for x in X]
    plt.plot(X,Y,label='i'+str(i))
    plt.legend()
plt.show()

def S(x):
    s=0
    for k in range(8):
        s+=d(k,x)
        return x
X=np.arange(0,1,0.01)
Y=[S(x) for x in X]
plt.plot(X,Y)
plt.show()


