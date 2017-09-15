from random import random

from generators import mcg, mmg
from tests import pearson, kolmogorov

N = 1000
K = 64
TEST_K = 30
PEARSON_DELTA = 42.577
KOLMOGOROV_DELTA = 1.36
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

chi, test_result = pearson(bn, TEST_K, N, PEARSON_DELTA)
chi2, test_result2 = pearson(a, TEST_K, N, PEARSON_DELTA)

print('\npearson:')
print(' chi for mcg: {0} - test {1}'.format(chi, test_result))
print(' chi for mmg: {0} - test {1}'.format(chi2, test_result2))

dn1, test_result = kolmogorov(bn, KOLMOGOROV_DELTA)
dn2, test_result2 = kolmogorov(a, KOLMOGOROV_DELTA)

print('\nkolmogorov:')
print(' sqrt(n)*dn for mcg: {0} - test {1}'.format(dn1, test_result))
print(' sqrt(n)*dn for mmg: {0} - test {1}'.format(dn2, test_result2))
