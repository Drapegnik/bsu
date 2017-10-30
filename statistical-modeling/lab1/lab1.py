#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random

from chi_square import MAX_K
from generators import mcg, mmg
from tests import pearson, kolmogorov
from utils import extrapolate, get_pearson_result

N = 1000
K = 64
M = 2.0 ** 31
alpha0 = beta = 16807.0

b = list(mcg(alpha0, beta, M, N + K))
bn = b[:N]
print('mcg:\t{}'.format(bn))

c = [random() for _ in range(N)]
print('random:\t{}'.format(c))

a = list(mmg(b, c, K, N))
print('mmg:\t{}'.format(a))

p = [1.0 / MAX_K] * MAX_K
bn_result = pearson(extrapolate(bn, MAX_K), p, N)
c_result = pearson(extrapolate(c, MAX_K), p, N)
a_result = pearson(extrapolate(a, MAX_K), p, N)

print('\npearsonm, chi:')
print('\tmcg:\t{}'.format(get_pearson_result(*bn_result)))
print('\trandom:\t{}'.format(get_pearson_result(*c_result)))
print('\tmmg:\t{}'.format(get_pearson_result(*a_result)))

print('\nkolmogorov, sqrt(n)*dn')
print('\tmcg:\t{}'.format(kolmogorov(bn)))
print('\tmmg:\t{}'.format(kolmogorov(a)))
