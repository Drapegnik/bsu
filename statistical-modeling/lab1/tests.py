#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt

import numpy as np

TEST_K = 30
PEARSON_DELTA = 42.577
KOLMOGOROV_DELTA = 1.36


def extrapolate(seq, k):
    return [int(el * k) for el in seq]


def get_frequency(seq, k):
    v = [0] * k
    for el in seq:
        v[el] += 1
    return v


def get_test_result(val, delta):
    return 'passed 👌' if val < delta else 'failed 😭'


def pearson(seq, k, p, n, delta):
    """
    Pearson's chi-squared test
    """
    v = get_frequency(seq, k)
    value = sum([(v[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(k)])
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
