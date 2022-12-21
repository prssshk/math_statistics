import numpy as np
import scipy
from parreto_vyborky import get_data

import math

amount = [5, 10, 100, 200, 400, 600, 800, 1000]

def ecdf(data,t):
    s = 0
    for i in data:
        if i < t:
            s += 1
    return s/len(data)

def suppremum(list2):
    sup = 0
    temp = np.arange(0,15,0.01)
    list1_temp = list(ecdf(list2,t) for t in temp)
    list2_temp = list(scipy.stats.pareto.cdf(t,11) for t in temp)
    for i in range(len(temp)):
        sup = max(sup, abs(list1_temp[i]-list2_temp[i]))
    return sup

out = []
for i in amount:
    temp = []
    for k in range(5):
        sum = suppremum(get_data(i)[k])
        temp.append(round(sum* math.sqrt(i),5))
    out.append(temp)
# temp = np.arange(0, 10,0.01)
# print(temp)
for i in out:
    print(i)