
               #TP5: Les suites numériques

#1-Présentation des suites:
 
 #1-Suites définies explicitement:
 #Exemple:

#On souhaite représenter la suite un = 1 +(−1)^n
#On utilise la fonction :
#u :N → N
#n → 1 + (−1)^n

def u(n):
    return 1+(-1)**n
#Application : On souhaite calculer les 10 premiers termes de la suite :
for k in range(1,11):
    print("Le ",k,"ème terme de la suite est:", u(k))
#Toutefois on peut calculer n’importe quel terme de la suite :
print("Le ",1000,"ème terme de la suite est:", u(1000))

  #2-Suites définies par recurrence:
  #Exemple:

#On souhaite par exemple obtenir les termes de la suite
#{un+1 =(2.un+3/un+4) ,u0 = 0}
#On représente cette suite récurrente à l’aide de la fonction :
#f :(R → R)
   # x→ 2.x+3/x+4
#Ainsi la suite récurrente est définie par :
#{un+1 = f(un),u0 = 0}

#1)-Programme de la fonction:
def f(x):
    y=(2*x+3)/(x+4)
    return y

#2)-Test avec des valeurs:
print(f(3))
print(f(5))
print(f(0))

#Apllication:
u=0
for k in range(11):
    u=f(u)
    print("Le ",k+1,"`eme terme de la suite est:", u)

#Remarque:
 #L'inconvenient de ses suites est la nécessité de passer par le calcul
 #Ceci concernant tous les termes intermediaires
 #Il est cepandant possible d'afficher uniqument le terme souhaité
    
    #Exemple:
def u(n):
    u=0
    for k in range(n):
        u=f(u)
        return u
print("Le 10 ème terme de la suite est:", u(10))

#2-Limite d'une suite:

#2.1 Cas d’une limite infinie:
    #Rappel (Définition)
# suite (un) a pour limite +∞ quand n tend vers +∞ si:
# pour tout entier naturel p, on peut trouver:
#un rang N à partir duquel tous les termes un sont supérieurs à 10p

 #illustratiin graphique:
import matplotlib.pyplot as plt

def suite_geometrique(r, n):
    suite = [1]  # On commence la suite avec 1
    for _ in range(1, n):
        suite.append(suite[-1] * r)
    return suite
raison = 2  # Raison de la suite
n_terms = 20  # Nombre de termes à générer
geom_sequence = suite_geometrique(raison, n_terms)

# Créer le graphique:
plt.figure(figsize=(10, 6))
plt.plot(range(1, n_terms + 1), geom_sequence, marker='o', linestyle='-')
plt.xlabel('N')
plt.ylabel('Valeur de la suite géométrique')
plt.title(f'Suite géométrique tendant vers l\'infini avec une raison de {raison}')
plt.grid(True)
plt.show()

#Exemple:

#Soit u la suite définie par un = 0, 5n2 − n + 1.
#On sait que cette suite admet une limite infinie en +∞.
#il va falloir déterminer un seuil à partir du quel un ≥ 10000, soit un ≥ 104

#Algorithme Seuil :

n=0
u=1
while u<10000:
    n+=1
    u=0.5*(n)**2-n+1
print(n)

#Exercice:
from math import exp
n=0
u=0
while u<10000:
    n+=1
    u=exp(n)
print(n)

#remarque:
#le seuil est petit (10);et est vite attent en exponentiel

#2.2 Cas d’une limite finie:

#Définition:
#Une suite (un) a pour limite ℓ quand n tend vers +∞ si pour tout entier naturel p, on peut trouver un:
#rang N à partir duquel tous les termes un sont à une distance de ℓ inf´erieure à 10−p

#illustration graphique:
import matplotlib.pyplot as plt

def suite_inverse(n):
    return 1/n

# Nombre d'itérations
iterations = 100

# Liste pour stocker les valeurs de la suite
valeurs_suite = []

# Calculer les valeurs de la suite
for n in range(1, iterations + 1):
    valeurs_suite.append(suite_inverse(n))

# Créer le graphique avec juste des points
plt.figure(figsize=(10, 6))
plt.plot(range(1, iterations + 1), valeurs_suite, 'o', label='Suite 1/n')

# Ajouter une ligne horizontale à y=0 pour montrer la convergence
plt.axhline(y=0, color='r', linestyle='--', label='Limite : 0')

# Étiquettes et légendes
plt.xlabel('n')
plt.ylabel('Valeur de la suite')
plt.title('Illustration de la convergence de la suite 1/n')
plt.legend()

# Afficher le graphique
plt.grid(True)
plt.show()

#Exemples:
#Soit u la suite définie pour tout n ≥ 1 par un = 3 +(−1)nn2
#• Cette suite admet pour limite 3 en +∞.
#• déterminer un seuil à partir duquel |un − 3| ≤ 10−5

n=0
u=1
while abs(u-3)> 10**-5:
    n+=1
    u=3+((-1)**n/(2)**n)
print(n,u)

#remarque:
#L’algorithme nous donne un seuil de 17,
#ie pour toute valeur de n supérieure ou égale à 17:
#la différence entre un et 3 sera inférieure à 0, 00001