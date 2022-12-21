from scipy.stats import chi2
from scipy.stats import pareto
import math
import pandas as pd
from parreto_vyborky import get_data

j = 0
S_m = [get_data(5)[j],get_data(10)[j],get_data(100)[0],get_data(200)[j],get_data(400)[j],get_data(600)[j],get_data(800)[j],get_data(1000)[j]]
ss = [5, 10, 100, 200, 400, 600, 800, 1000]

def test_chi_m_calc(sample: list, sample_index: int):
    s = 0

    l = list(sorted(sample))

    freq = []
    N = 50

    delta = (math.floor(l[-1]) + 1 - round(l[0])) / N

    lb, rb = math.floor(l[0]), math.floor(l[0]) + delta
    c = 0
    i = 0
    x = []

    while i <= len(l):
        if i == len(l):
            x.append(lb + delta / 2)
            freq.append(c)
            break
        elif lb <= l[i] < rb:
            c += 1
            i += 1
        else:
            x.append(lb + delta / 2)
            freq.append(c)
            c = 0
            lb, rb = rb, rb + delta

    for i in range(len(x) - 1):
        prob = pareto.cdf(x[i + 1] - delta / 2, 11) - pareto.cdf(x[i] - delta / 2, 11)
        s += (freq[i] - sample_index * prob) ** 2 / (sample_index * prob)

    prob = pareto.cdf(x[-1] + delta / 2, 11) - pareto.cdf(x[-1] - delta / 2,11)

    s += (freq[-1] - sample_index * prob) ** 2 / (sample_index * prob)

    return s


def accept_chi_m(sample, s, a):
    l = list(set(sample))
    chi = chi2.ppf(1 - a, df=len(l) - 1)
    if s <= chi:
        return "H0 принимается"
    else:
        return "H0 отвергается"


test_chi_m = [test_chi_m_calc(S_m[i], ss[i]) for i in range(len(S_m))]

crits = [0.1, 0.05, 0.01]
hyp_chi_m = [[accept_chi_m(S_m[i], test_chi_m[i], a) for i in range(len(S_m))] for a in crits]

chi_m = {'Тестовая статистика': test_chi_m, 'alpha=0.1': hyp_chi_m[0], 'alpha=0.05': hyp_chi_m[1],
         'alpha=0.01': hyp_chi_m[2]}
chi_table_m = pd.DataFrame(data=chi_m)
chi_table_m.index = ss
#print(chi_table_m)

# for i in test_chi_m:
#     print(round(i,3))