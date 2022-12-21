import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
from poisson_vyborky import get_data


data = get_data(1000)[4]
xs = np.linspace(0,50,130)
ytrue = poisson.pmf(xs,22.5)
plt.plot(xs,ytrue,color = "red")
plot_data = dict((i, data.count(i) / len(data)) for i in data)
d = dict(sorted(plot_data.items(), key=lambda x: x[0]))
plt.bar(d.keys(), d.values())
plt.legend(["real","sample"])
plt.xlim(0,50)
plt.show( )
