import scipy.integrate as integr
import numpy as np
import matplotlib.pyplot as plt
def T(f,x):
    def g(t):
        return (x-t)*f(t)
    return 1-integr.quad(g,0,x)[0]
def exp(x):
    return np.exp(x)
print(T(exp,(5)))

X=np.arange(-10,10,0.01)
i=0

def iterT(k,f,x):
    if k==0:
        return f(x)
    else:
        return iterT(k-1,lambda x:T(f,x),x)
X=np.arange(-1,1,0.01)
for k in range(3):
    Y=[iterT(k,lambda t:np.cos(t),x) for x in X]
    plt.plot(X,Y,label='k='+str(k))
    plt.legend()
plt.show()
