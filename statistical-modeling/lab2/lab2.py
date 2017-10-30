#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import numpy as np
from generators import poisson, poisson_distribution, pascal, pascal_distribution
from utils import print_table

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parent_dir)

from lab1.tests import pearson
from lab1.utils import get_pearson_result
from lab1.chi_square import MAX_K

N = 1000
R = 4
P = 0.8
LAMBDA = 0.3
EPSILON = 0.05


def run(title, generator, distr, mean, var, args):
    successes = 0
    for i in range(N):
        actual = np.array(list(generator(*args, N)))
        if i == 0:
            print('\n> {}:'.format(title))
            print_table(actual, mean, var)
        p = [distr(*args, i) for i in range(MAX_K)]
        value, delta, k = pearson(actual, p, N)
        successes += int(value < delta)
        if i == 0:
            print('Pearson:\t{}'.format(get_pearson_result(value, delta, k)))
    print('Success:\t{}%'.format(successes * 100 / N))


run('Poisson', poisson, poisson_distribution, LAMBDA, LAMBDA, args=[LAMBDA])

pascal_mean = R * (1 - P) / P
pascal_var = pascal_mean / P
run('Pascal', pascal, pascal_distribution, pascal_mean, pascal_var, args=[R, P])
