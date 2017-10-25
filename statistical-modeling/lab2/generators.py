#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# discrete random number generators

from math import exp, factorial
from random import random

MAX = 10 * 6


def poisson_distribution(lmbda, x):
    return (lmbda ** x) * exp(-lmbda) / factorial(x)


def poisson_theory(lmbda, n):
    for i in range(n):
        yield poisson_distribution(lmbda, i)


def get_next_poisson(lmbda):
    alpha = random()
    n = 0
    while alpha >= exp(-lmbda):
        alpha *= random()
        n += 1
    return n


def poisson(lmbda, n):
    for _ in range(n):
        yield get_next_poisson(lmbda)


def bernoulli(p):
    return [0 if random() > p else 1 for _ in range(MAX)]


def C(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def pascal_distribution(r, p, x):
    return C(r + x - 1, x) * p ** r * (1 - p) ** x


def get_next_pascal(r, p):
    b = bernoulli(p)
    sum = 0
    i = 0
    while sum < r and i < MAX:
        sum += b[i]
        i += 1
    return i - r


def pascal(r, p, n):
    """
    Negative binomial distribution (Pascal distribution)
    """
    for i in range(n):
        yield get_next_pascal(r, p)
