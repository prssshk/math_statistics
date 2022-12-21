import math
import random
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import pareto

def parreto(theta):
    a = random.uniform(0,1)
    xi = a**(-1/theta)
    return xi
def ecdf(data,t):
    s = 0
    for i in data:
        if i < t:
            s += 1
    return s/len(data)


data = [ ]
for i in range(1000):
    value = parreto(11)
    data.append(value)

xs = np.linspace(1,3,100)
y = [ecdf(data,t) for t in xs]
#plt.step(xs,y)

ytrue = pareto.pdf(xs,11)
plt.plot(xs,ytrue)
plt.hist(data,density=True)


plt.xlim(0.5,2)
plt.show( )