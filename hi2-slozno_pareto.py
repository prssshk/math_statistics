from scipy.stats import chi2
from scipy.stats import pareto
from parreto_vyborky import get_data
from hi2_pareto import test_chi_m
import pandas as pd
import math
import numpy as np
j = 0
S_m = [get_data(5)[j],get_data(10)[j],get_data(100)[0],get_data(200)[j],get_data(400)[j],get_data(600)[j],get_data(800)[j],get_data(1000)[j]]
ss = [5, 10, 100, 200, 400, 600, 800, 1000]

def test_chi_m_calc_o(sample: list, sample_index: int, theta_m):
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

    prob = pareto.cdf(x[-1] + delta / 2, 11) - pareto.cdf(x[-1] - delta / 2, 11)

    s += (freq[-1] - sample_index * prob) ** 2 / (sample_index * prob)

    return s


def accept_chi_m_o(sample, s, a):
    l = list(set(sample))
    chi = chi2.ppf(1 - a, df=len(l) - 2)
    if s <= chi:
        return " принимается"
    else:
        return "отвергается"

tml_estimates_m = [[5.13, 16.0, 28.57, 12.5, 9.52], [16.67, 10.11, 8.65, 11.69, 10.71], [11.17, 12.45, 9.48, 12.48, 13.36], [12.33, 12.46, 10.11, 10.22, 9.89], [9.79, 11.62, 10.92, 10.87, 11.17], [10.25, 10.89, 11.06, 10.96, 10.9], [10.82, 11.01, 11.49, 10.87, 11.0], [11.38, 11.02, 11.48, 10.71, 10.88]]

test_chi_m_o = [test_chi_m_calc_o(S_m[i], ss[i], tml_estimates_m[i][j]) for i in range(len(S_m))]

crits = [0.1, 0.05, 0.01]
hyp_chi_m_o = [[accept_chi_m_o(S_m[i], test_chi_m[i], a) for i in range(len(S_m))] for a in crits]

chi_m_o = {'Тестовая статистика': test_chi_m_o, 'alpha=0.1': hyp_chi_m_o[0], 'alpha=0.05': hyp_chi_m_o[1],
           'alpha=0.01': hyp_chi_m_o[2]}
chi_table_m = pd.DataFrame(data=chi_m_o)
chi_table_m.index = ss
print(chi_table_m)
# for i in test_chi_m_o:
#     print(round(i,3))