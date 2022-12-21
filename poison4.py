from poisson_vyborky import get_data

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


out2 = []
for i in amount:
    temp = []
    for k in range(5):
        sum = 0
        for s in range(i):
           sum += (get_data(i)[k][s]-out[amount.index(i)][k])**2
        temp.append(round(sum/i,4))
    out2.append(temp)

for i in range(len(out2)):
    for k in range(len(out2[i])):
        out2[i][k] = round((out2[i][k]-0.012)/0.012*100,2)

for i in out:
    print(i)