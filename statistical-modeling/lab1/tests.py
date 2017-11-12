#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from bisect import bisect_right
from math import sqrt

import numpy as np

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parent_dir)

from lab1.chi_square import DELTA, MAX_K

PEARSON_THRESHOLD = 0.01
KOLMOGOROV_DELTA = 1.36


def get_frequency(sorted_seq, k):
    min_el = sorted_seq[0]
    max_el = sorted_seq[-1]
    step = (max_el - min_el) / (k + 1)
    segments = np.arange(min_el, max_el, step)
    v = [0] * k
    last_position = 0
    for i in range(k):
        position = bisect_right(sorted_seq, segments[i + 1])
        v[i] = position - last_position
        last_position = position
    return v, segments


def get_probabilities(segments, f):
    k = len(segments)
    p = [0] * k
    for i in range(k - 1):
        p[i] = f(segments[i + 1]) - f(segments[i])
    return p


def pearson(sorted_seq, distr_f=None, p_list=None):
    """
    Pearson's chi-squared test
    :param sorted_seq: sorted random sequence to test
    :param distr_f: optional distribution function
    :param p_list: optional distribution list
    :return: test value, pearson delta for k, k
    """
    k = MAX_K
    n = len(sorted_seq)
    v, segments = get_frequency(sorted_seq, k)
    p = p_list if p_list else get_probabilities(segments, distr_f)
    delta = DELTA[k]
    value = sum([(v[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(k)])
    return value, delta, k


def kolmogorov(sorted_seq):
    """
    Kolmogorov–Smirnov test
    :param sorted_seq: model distribution on sorted random sequence
    :return: test value, test delta
    """
    n = len(sorted_seq)
    test_seq = np.array([float(i + 1) / n for i in range(n)])
    max_diff = max(list(map(abs, test_seq - sorted_seq)))
    value = sqrt(n) * max_diff
    return value, KOLMOGOROV_DELTA
