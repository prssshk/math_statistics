import numpy as np
import scipy
from parreto_vyborky import get_data
import matplotlib as plt
import math

amount = [5, 10, 100, 200, 400, 600, 800, 1000]
thetas = [[5.13, 16.0, 28.57, 12.5, 9.52], [16.67, 10.11, 8.65, 11.69, 10.71], [11.17, 12.45, 9.48, 12.48, 13.36], [12.33, 12.46, 10.11, 10.22, 9.89], [9.79, 11.62, 10.92, 10.87, 11.17], [10.25, 10.89, 11.06, 10.96, 10.9], [10.82, 11.01, 11.49, 10.87, 11.0], [11.38, 11.02, 11.48, 10.71, 10.88]]


def ecdf(data,t):
    s = 0
    for i in data:
        if i < t:
            s += 1
    return s/len(data)

def supp(s1, theta=11):
    x = np.linspace(0, 100, num=1000)
    f1 = list(ecdf(s1, t) for t in x)
    f2 = list(scipy.stats.pareto.cdf(t, theta) for t in x)
    s = 0
    for i in range(len(x)):
        s = max(s, abs(f1[i] - f2[i]))

    return s
def calcDn(i, k):

    return supp(get_data(i)[k], thetas[amount.index(i)][k])

out = []
for i in amount:
    temp = []
    for k in range(5):
        sum = calcDn(i,k)
        temp.append(round(sum*math.sqrt(i),5))
    out.append(temp)


for i in out:
    print(i)

