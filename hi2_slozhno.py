from scipy.stats import chi2
from scipy.stats import poisson
from poisson_vyborky import get_data
import pandas as pd
import numpy as np

j = 0
S = [get_data(5)[j],get_data(10)[j],get_data(100)[0],get_data(200)[j],get_data(400)[j],get_data(600)[j],get_data(800)[j],get_data(1000)[j]]
ss = [5, 10, 100, 200, 400, 600, 800, 1000]

def test_chi_b_calc_o(sample: list, sample_index: int, theta):
    s = 0

    l = list(set(sorted(sample)))

    freq = [sample.count(i) for i in l]

    for i in range(len(l)):
        prob = poisson.pmf(l[i], theta)
        s += (freq[i] - sample_index * prob) ** 2 / (sample_index * prob)

    return s


def accept_chi_b(sample, s, a):
    l = list(set(sorted(sample)))
    chi = chi2.ppf(1 - a, df=len(l) - 1)
    if s <= chi:
        return "принимается"
    else:
        return "отвергается"


p_estimates_b1 = [np.mean(S[i]) for i in range(len(S))]

test_chi_b = [test_chi_b_calc_o(S[i], ss[i], p_estimates_b1[i]) for i in range(len(S))]

crits = [0.1, 0.05, 0.01]
hyp_chi_b = [[accept_chi_b(S[i], test_chi_b[i], a) for i in range(len(S))] for a in crits]

chi_b = {'Тестовая статистика': test_chi_b, 'alpha=0.1': hyp_chi_b[0], 'alpha=0.05': hyp_chi_b[1],
         'alpha=0.01': hyp_chi_b[2]}
chi_table_b = pd.DataFrame(data=chi_b)
chi_table_b.index = ss

print(chi_table_b)