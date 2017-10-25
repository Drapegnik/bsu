#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random

from generators import mcg, mmg
from tests import pearson, kolmogorov, TEST_K, PEARSON_DELTA, KOLMOGOROV_DELTA, extrapolate

N = 1000
K = 64
M = 2.0 ** 31
alpha0 = beta = 16807.0
epsilon = 0.05

b = list(mcg(alpha0, beta, M, N + K))
bn = b[:N]
print('mcg:\t{}'.format(bn))

c = [random() for _ in range(N)]
print('random:\t{}'.format(c))

a = list(mmg(b, c, K, N))
print('mmg:\t{}'.format(a))

p = [1.0 / TEST_K] * TEST_K
chi, test_result = pearson(extrapolate(bn, TEST_K), TEST_K, p, N, PEARSON_DELTA)
chi2, test_result2 = pearson(extrapolate(a, TEST_K), TEST_K, p, N, PEARSON_DELTA)
chi3, test_result3 = pearson(extrapolate(c, TEST_K), TEST_K, p, N, PEARSON_DELTA)

print('\npearson:')
print(' chi for mcg: {0} - test {1}'.format(chi, test_result))
print(' chi for mmg: {0} - test {1}'.format(chi2, test_result2))
print(' chi for random: {0} - test {1}'.format(chi3, test_result3))

dn1, test_result = kolmogorov(bn, KOLMOGOROV_DELTA)
dn2, test_result2 = kolmogorov(a, KOLMOGOROV_DELTA)

print('\nkolmogorov:')
print(' sqrt(n)*dn for mcg: {0} - test {1}'.format(dn1, test_result))
print(' sqrt(n)*dn for mmg: {0} - test {1}'.format(dn2, test_result2))
