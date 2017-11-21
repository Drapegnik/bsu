#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# cryptographically secure pseudorandom number generators

def mcg(alpha, beta, m, n):
    """
    Multiplicative congruential generator (MCG)
    """
    for i in range(n):
        alpha = (beta * alpha) % m
        yield alpha / m


def mmg(b, c, k, n):
    """
    MacLaren-Marsaglia generator (MMG)
    """
    v = b[:k]
    for i in range(n):
        s = int(c[i] * k)
        yield v[s]
        v[s] = b[i + k]
