import numpy as np
from scipy.stats import poisson
from poisson_vyborky import get_data

amount = [5, 10, 100, 200, 400, 600, 800, 1000]
j = 0
array = [get_data(5)[j],get_data(10)[j],get_data(100)[0],get_data(200)[j],get_data(400)[j],get_data(600)[j],get_data(800)[j],get_data(1000)[j]]

theta0 = 22.5
theta1 = 23.5


c = [poisson.ppf(0.9, theta0*i) for i in amount]
sums = np.zeros(8)
data = ["Accept {}" for i in range(8)]
#таблица 1
for i in range(len(array)):
    sums[i] = sum(array[i])
    theta = theta0 if sums[i] < c[i] else theta1
    data[i] = theta

#таблица 2
data = [poisson.cdf(c[i], theta1*amount[i]) for i in range(8)]


