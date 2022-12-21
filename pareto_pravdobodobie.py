from parreto_vyborky import get_data
import math

amount = [5, 10, 100, 200, 400, 600, 800, 1000]

out = []
for i in amount:
    temp = []
    for k in range(5):
        sum = 0
        for s in range(i):
           sum += math.log(get_data(i)[k][s])
        t = (i-1)/round(sum,2)
        temp.append(round(t,2))
    out.append(temp)

print(out)


