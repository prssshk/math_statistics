import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pareto
from parreto_vyborky import get_data


def ecdf(data,t):
    s = 0
    for i in data:
        if i < t:
            s += 1
    return s/len(data)

def suppremum(list1,list2):
    sup = 0
    temp = np.arange(0, max(len(list1),len(list2),0.01))
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
        data1 = get_data(n)[4]
        data2 = get_data(i)[4]
        data_temp.append(round(Dmn(data1,data2),5))
    a.append(data_temp)
for i in a:
    print(i)

colors = ["olive", "grey", "black", "blue", "green", "yellow", "violet", "orange"]
''''
xs = np.linspace(1,3,100)
amount = [5, 10, 100, 200, 400, 600, 800, 1000]
for k in amount:
    data = get_data(k)[4]
    y = [ecdf(data,t) for t in xs]
    plt.step(xs,y, color = colors[amount.index(k)])

ytrue = pareto.cdf(xs,11)
plt.plot(xs,ytrue, color = "red")


plt.legend([*amount,"cdf"])
plt.grid()
plt.xlim(1,2)
plt.show( )
'''


