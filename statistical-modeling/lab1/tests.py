from math import sqrt

import numpy as np


def get_frequency(seq, k):
    v = [0] * k
    step = 1.0 / k
    bound = step
    seq.sort()
    i, j = 0, 0
    while j < k:
        while i < len(seq) and seq[i] < bound:
            v[j] += 1
            i += 1
        bound += step
        j += 1
    return v


def get_test_result(val, delta):
    return 'passed 👌' if val < delta else 'failed 😭'


def pearson(seq, k, n, delta):
    """
    Pearson's chi-squared test
    """
    v = get_frequency(seq, k)
    p = 1.0 / k
    value = sum([(v[i] - n * p) ** 2 / (n * p) for i in range(k)])
    return value, get_test_result(value, delta)


def kolmogorov(seq, delta):
    """
    Kolmogorov–Smirnov test
    """
    n = len(seq)
    sort_seq = np.array(sorted(seq))
    test_seq = np.array([float(i + 1) / n for i in range(n)])
    max_diff = max(list(map(abs, test_seq - sort_seq)))
    value = sqrt(n) * max_diff
    return value, get_test_result(value, delta)
