import math
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import poisson
from parreto_vyborky import get_data

def ecdf(data,t):
    s = 0
    for i in data:
        if i < t:
            s += 1
    return s/len(data)

def suppremum(list1,list2):
    sup = 0
    temp = np.arange(0, 10,0.01)
    list1_temp = list(ecdf(list2,t) for t in temp)
    list2_temp = list(ecdf(list1, t) for t in temp)
    for i in range(len(temp)):
        sup = max(sup, abs(list1_temp[i]-list2_temp[i]))
    return sup

def Dmn(list1,list2):
    m = len(list1)
    n = len(list2)
    return math.sqrt(m * n / (m + n ))*suppremum(list1,list2)

amount = [5, 10, 100, 200, 400, 600, 800, 1000]
a = []
values = list(range(30))
for i in amount:
    data_temp = []
    for n in amount:
        data1 = get_data(n)[0]
        data2 = get_data(i)[0]
        t_n_m = 1.22
        data_temp.append(round(Dmn(data1,data2),5) < t_n_m)
    a.append(data_temp)

for i in a:
    print(i)

