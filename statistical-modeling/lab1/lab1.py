#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random

from chi_square import MAX_K
from generators import mcg, mmg
from tests import pearson, kolmogorov
from utils import format_test_result

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
bn_result = pearson(sorted(bn), p_list=p)
c_result = pearson(sorted(c), p_list=p)
a_result = pearson(sorted(a), p_list=p)

print('\npearson, chi:')
print('\tmcg:\t' + format_test_result(*bn_result))
print('\trandom:\t' + format_test_result(*c_result))
print('\tmmg:\t' + format_test_result(*a_result))

bn_result = kolmogorov(sorted(bn))
a_result = kolmogorov(sorted(a))

print('\nkolmogorov, sqrt(n)*dn')
print('\tmcg:\t' + format_test_result(*bn_result))
print('\tmmg:\t' + format_test_result(*a_result))
