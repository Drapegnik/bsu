#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from generators import poisson, poisson_distribution, pascal, pascal_distribution
from utils import run

N = 1000
R = 4
P = 0.8
LAMBDA = 0.3

run(
    title='Poisson',
    generator=poisson,
    distr=poisson_distribution,
    args=[LAMBDA],
    mean=LAMBDA,
    var=LAMBDA,
    size=N,
    enable_kolmogorov=False
)

pascal_mean = R * (1 - P) / P
pascal_var = pascal_mean / P
run(
    title='Pascal',
    generator=pascal,
    distr=pascal_distribution,
    args=[R, P],
    mean=pascal_mean,
    var=pascal_var,
    size=N,
    enable_kolmogorov=False
)
