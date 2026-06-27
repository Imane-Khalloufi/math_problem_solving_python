              #La méthode d'Euler:
#Pour la résolution des équations differentielles

  
#1-Le principe:
 
#celui ci consiste à faire une approximation
#pour la résolution d'équations differentielles
#tout en imposant les condtions initiales

  #2-constrution:

#A partir de la valeur x0 on peut calculer dxdt (0) = x
#en calculant f(0, x0) . Comme valeur approximative xl au temps t1 = 0 + tl
#On choisit de prendre :x0 + dx = x0 + x
#Ou encore :x0 + dx = x0 + f(0, x0) . t1 (2)
#Soit alors :x1 = x0 + f(0, x0) . t1 
  
  #3-Exemple concret:
 
#1.Par la méthode d'Euler

import numpy as np
import math
import matplotlib.pyplot as plt
N=50
T=[i/N for i in range(N)]
def f(t,x) :return -2*t*x
X=[1]
x=1
for i in range(N-1) :
    x=x+f(T[i],x)*(T[i+1]-T[i])
    X.append(x)
plt.plot(T,X,color='b',linestyle='--')
plt.title("Méthode d'Euler")
plt.show()
#2.Par la méthode analytique:

d=[math.exp(-(T[i])**2) for i in range(N)]
plt.plot(T,X,color='b',linestyle='-')
plt.plot(T,d,color='g')
plt.title("Méthode analytique :")
plt.show()


#Remarque:
#On voit clairement que les deux courbes sont très similaires

#4-Généralistaion de la méthode d'Euler:

#D'une maniere plus générale (En choisissant n'importe quelle fonction)
#On définit la fonction :
def Euler(f,t0,tf,x0,n) :
    h=(tf-t0)/n
    x=x0
    t=t0
    X=[x0]
    T=[t0]
    for k in range(n) :
        x=x+f(t,x)*h
        t=t+h
        X.append(x)
        T.append(t)
        plt.plot(T,X)
plt.show()

   #5-Méthode d'Euler a deux variables:

#On considère maintenant le système S :
#x'(t) = 0.08x(t) − 0.004x(t)y(t)
#y'(t) = −0.06y(t) + 0.002x(t)y(t)
#Le principe est simple aussi
#C'est de la meme manière mais ne pas oublier d'ajouter une nouvelle variable
#notée m afin de laisser le "x" intact tout en le dupliquant

#Appliaction:

import numpy as np
import matplotlib.pyplot as plt

h = 200/1000

T = [0]
X = [40] # x0 = 40
Y = [20] # y0 = 20

t = 0
x = 40
y = 20

for i in range(999):
    m = x
    x = x + h*(0.08*x -0.004*x*y)
    y = y + h*(-0.06*y + 0.002*m*y)
    X.append(x)
    Y.append(y)
    T.append(i*h)
    

plot1 = plt.subplot2grid((2,3),(0,0))
plot2 = plt.subplot2grid((2,3),(0,1))
plot3 = plt.subplot2grid((2,3),(0,2))
plot4 = plt.subplot2grid((2,3),(1,0), colspan = 3 )

plot1.plot(T,X,color='b',linestyle='--')
plot1.set_title("Evolution lapin :")
plot1.grid(True)

plot2.plot(T,Y,color='r',linestyle='--')
plot2.set_title("Evolution renards :")
plot2.grid(True)

plot3.plot(Y,X,color='g')
plot3.set_title("Evolution Lapins/renards : ")
plot3.grid(True)

plot4.plot(T,X,color='b')
plot4.plot(T,Y,color='r',linestyle='--')
plot4.set_title("Evolution renards et lapins : ")
plot4.grid(True)


plt.show()



