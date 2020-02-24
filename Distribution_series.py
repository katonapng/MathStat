import math
import random as rand
from random import random
import matplotlib.pyplot as plt
import seaborn as sns
pi = 3.141592653589793238462
e = 2.7182818284590452353602
L = 10
STEP = 500
a = -math.sqrt(3)
b = math.sqrt(3)

sample1 = 10
sample2 = 50
sample3 = 1000

def Normal():
    s = 0
    while s > 1 or s == 0:
        x = rand.uniform(-1,1)
        y = rand.uniform(-1,1)
        s = pow(x,2)+pow(y,2)
    
    f = math.sqrt(-2*math.log(s)/s)
    return x*f

def NormalDensity(x):
    return math.pow(e,-math.pow(x,2)/2)/(math.sqrt(2*pi))
    
def Cauchy():
    y = 0
    x = 1
    while pow(x,2)+pow(y,2) > 1 or y == 0:
        x = rand.uniform(-1,1)
        y = rand.uniform(-1,1)
    return x/y

def CauchyDensity(x):
    return 1/(pi*(1+pow(x,2)))

def Poisson():
    k = 0
    p = pow(e,-L)
    s = p 
    u = rand.uniform(0,1)
    while u > s:
        k = k + 1
        p = p * L / k
        s = s + p
    return k

def PoissonProbability(k):
    return pow(e,-L)*pow(L, k)/math.factorial(k)

def Laplace():
    e1 = -1/math.sqrt(2)*math.log(random())
    e2 = -1/math.sqrt(2)*math.log(random())
    return e1-e2

def LaplaceDensity(x):
    return 1/math.sqrt(2)*pow(e,-math.sqrt(2)*abs(x))

def Uniform():
    return rand.uniform(a,b)

def UniformDensity(x):
    return 1/(b-a)

def RunDistribution(distribution, probability):
    x = []
    density_x = []
    for _ in range(sample2):
        x.append(distribution())
    x.sort()
    for element in x:
        density_x.append(probability(element))
    plt.plot(x,density_x,'r')
    plt.ylabel("f(X)")
    plt.xlabel("X")
    plt.grid()
    sns.distplot(x)
    plt.show()


if __name__ == "__main__":
    RunDistribution(Normal, NormalDensity)
    RunDistribution(Cauchy, CauchyDensity)
    RunDistribution(Laplace, LaplaceDensity)
    RunDistribution(Poisson, PoissonProbability)
    RunDistribution(Uniform, UniformDensity)
 

    