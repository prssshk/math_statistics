from poisson_vyborky import get_data
import numpy as np
amount = [5, 10, 100, 200, 400, 600, 800, 1000]

out = []
for i in amount:
    temp = []
    for k in range(5):
        sum = 0
        for s in range(i):
           sum += get_data(i)[k][s]
        temp.append(round(sum/i,2))
    out.append(temp)
t = []
for i in amount:
    sum = []
    for k in range(5):
        sum.append(np.mean(get_data(i)[k]))
    t.append(sum)
get_theta = [[20.2, 21.4, 21.8, 21.8, 25.6], [24.6, 19.7, 25.1, 21.5, 21.0], [22.65, 22.26, 22.72, 23.76, 22.19], [22.27, 23.07, 21.89, 22.89, 22.69], [22.42, 22.43, 22.56, 22.85, 22.53], [22.42, 22.48, 22.36, 22.66, 22.32], [22.5, 22.8, 22.46, 22.52, 22.2], [22.5, 22.92, 22.63, 22.33, 22.75]]


print(t)