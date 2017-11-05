import os
from math import log, exp

from generators import \
    gauss, gauss_distribution, \
    lognormal, lognormal_distribution, \
    exponential, exponential_distribution

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parent_dir)

from lab2.utils import run

N = 1000
M = 1
S = 3
LAMBDA = 2

run(
    title='Gauss',
    generator=gauss,
    distr=gauss_distribution,
    args=[M, S],
    mean=M,
    var=S ** 2,
    size=N,
    enable_pearson=False
)

mu = log(M)
lognormal_mean = exp(mu + (S ** 2) / 2)
lognormal_var = (exp(S ** 2) - 1) * exp(2 * mu + S ** 2)
run(
    title='Lognormal',
    generator=lognormal,
    distr=lognormal_distribution,
    args=[M, S],
    mean=lognormal_mean,
    var=lognormal_var,
    size=N,
    enable_pearson=False
)

run(
    title='Exponential',
    generator=exponential,
    distr=exponential_distribution,
    args=[LAMBDA],
    mean=LAMBDA ** (-1),
    var=LAMBDA ** (-2),
    size=N,
    enable_pearson=False
)
