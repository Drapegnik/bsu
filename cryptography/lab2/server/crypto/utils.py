"""
Helper multiply functions in finite field (Galois field) GF(2^8)
"""


def mul_by_02(num):
    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b
    return res % 0x100


def mul_by_03(num):
    return mul_by_02(num) ^ num


def mul_by_09(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


def mul_by_0b(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


def mul_by_0d(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


def mul_by_0e(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)


def state_to_list(state):
    n, m = len(state), len(state[0])
    output = [None for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            output[i + n * j] = state[i][j]
    return output
