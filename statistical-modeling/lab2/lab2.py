#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from generators import poisson, pascal, poisson_distribution, pascal_distribution
from utils import print_table

from lab1.tests import pearson, TEST_K, PEARSON_DELTA

N = 1000
R = 4
P = 0.8
LAMBDA = 0.3
EPSILON = 0.05

actual = np.array(list(poisson(LAMBDA, N)))
print('> Poisson:')
print_table(actual, LAMBDA, LAMBDA)

p = [poisson_distribution(LAMBDA, i) for i in range(TEST_K)]
chi, test_result = pearson(actual, TEST_K, p, N, PEARSON_DELTA)
print('Pearson chi: {0} - test {1}\n'.format(chi, test_result))

actual = np.array(list(pascal(R, P, N)))
print('> Pascal:')
pascal_mean = R * (1 - P) / P
pascal_var = pascal_mean / P
print_table(actual, pascal_mean, pascal_var)

p = [pascal_distribution(R, P, i) for i in range(TEST_K)]
chi, test_result = pearson(actual, TEST_K, p, N, PEARSON_DELTA)
print('Pearson chi: {0} - test {1}\n'.format(chi, test_result))
