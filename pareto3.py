import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pareto
from parreto_vyborky import get_data


xs = np.linspace(1,2,50)
d = {}
array = get_data(200)[0]
for k in array:
    for i in range(len(xs)-1):
        if xs[i] <= k < xs[i+1]:
            if (xs[i]+xs[i+1])/2 in d.keys():
                d[(xs[i]+xs[i+1])/2] += 1
            else:
                d[(xs[i]+xs[i+1])/2] = 1
d1 = dict(sorted(d.items(), key=lambda a: a[0]))
d2 = {}
for elem in d1.items():
    d2[elem[0]] = elem[1]/max(d1.values())*11
plt.bar(d2.keys(),d2.values(), width = 0.05)

xs = np.linspace(0.5,2,1000)
ytrue = pareto.pdf(xs,11)

plt.plot(xs,ytrue, color = "red")
plt.legend(["real","sample"])
plt.show( )
