#1
from numpy.polynomial import Polynomial
def euler(n):
    if n==0:
        return Polynomial([1])
    else :
        P=euler(n-1)
        Q=P.integ()
        return n*(Q-Q(0))-(n/2)*(Q(1)-Q(0))
for k in range(11):
    print (euler(k).coef)
X=Polynomial([0,1])
for i in range(11):
    P=euler(k)
    print((P+P(X+1)).coef)
#2
for i in range(11):
    print(euler(i)(0))
#3
import matplotlib.pyplot as plt
import numpy as np
for i in range(9):
    X=np.arange(0,1,0.01)
    Y=euler(i)(X)
    plt.plot(X,Y,label='euler(i)')
    plt.show()
    

    

