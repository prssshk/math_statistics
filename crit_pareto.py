import numpy as np
from scipy.stats import gamma
from parreto_vyborky import get_data

amount = [5, 10, 100, 200, 400, 600, 800, 1000]
j = 0
array = [get_data(5)[j],get_data(10)[j],get_data(100)[0],get_data(200)[j],get_data(400)[j],get_data(600)[j],get_data(800)[j],get_data(1000)[j]]


tmp = []
theta0 = 11
theta1 = 13

for i in range(8):
    tmp.append(list(map(np.log, array[i])))

c = [gamma.ppf(0.9, a=i, scale=theta0) for i in amount]
sums = np.zeros(8)
data = ["Accept {}" for i in range(8)]

#таблица 1
for i in range(8):
    sums[i] = sum(tmp[i])
    theta = theta0 if sums[i] < c[i] else theta1

    data[i] = data[i].format(theta)
#таблица 2
data = [gamma.cdf(c[i], a=amount[i], scale=theta1) for i in range(8)]

for i in data:
    print(round(i,6))
