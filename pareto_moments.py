from parreto_vyborky import get_data

amount = [5, 10, 100, 200, 400, 600, 800, 1000]

out = []
for i in amount:
    temp = []
    for k in range(5):
        sum = 0
        for s in range(i):
           sum += get_data(i)[k][s]
        t = round(sum/i,2)/(round(sum/i,2)-1)
        temp.append(round(t,2))
    out.append(temp)

for i in out:
    print(i)