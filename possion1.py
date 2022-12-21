import math
import random
import matplotlib.pyplot as plt
import numpy as np

def poisson(theta):
    r = math.exp(-theta)
    s = r
    k = 0
    x = random.uniform(0,1)
    while x > s:
        k += 1
        r *= theta/k
        s += r
    return k
data = []
for i in range(10000):
    value = poisson(22.5)
    data.append(value)


plot_data = dict((i, data.count(i) / len(data)) for i in data)
d = dict(sorted(plot_data.items(), key=lambda x: x[0]))

plt.scatter(d.keys(), d.values())
plt.show( )




