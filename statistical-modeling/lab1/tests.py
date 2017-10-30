#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from math import sqrt

import numpy as np

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parent_dir)

from lab1.chi_square import DELTA, MAX_K
from lab1.utils import get_test_result, TEST_TEMPLATE

PEARSON_THRESHOLD = 0.01
KOLMOGOROV_DELTA = 1.36


def get_frequency(seq, p):
    k = 0
    while k < MAX_K and p[k] > PEARSON_THRESHOLD:
        k += 1
    v = [0] * (k + 1)
    for el in seq:
        i = el if el < k else k
        v[i] += 1
    return k, v


def pearson(seq, p, n):
    """
    Pearson's chi-squared test
    """
    k, v = get_frequency(seq, p)
    delta = DELTA[k]
    value = sum([(v[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(k)])
    return value, delta, k


def kolmogorov(seq):
    """
    Kolmogorov–Smirnov test
    """
    n = len(seq)
    sort_seq = np.array(sorted(seq))
    test_seq = np.array([float(i + 1) / n for i in range(n)])
    max_diff = max(list(map(abs, test_seq - sort_seq)))
    value = sqrt(n) * max_diff
    sign, result = get_test_result(value, KOLMOGOROV_DELTA)
    return TEST_TEMPLATE.format(value=value, sign=sign, delta=KOLMOGOROV_DELTA, result=result)
