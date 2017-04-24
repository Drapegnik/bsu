A = -2.0
B = 2.0
eps = [0.5 * pow(10, -1 * i) for i in range(3, 8, 2)]


def f(x):
    return float(x * (3 ** x + 1) ** (-1))


def rect(h):
    int_sum = 0
    x = A + h / 2.0
    while x < B:
        int_sum += f(x)
        x += h
    return h * int_sum


def trap(h):
    int_sum = 0
    x = A
    while x < B:
        int_sum += h * (f(x) + f(x + h))
        x += h
    return 0.5 * int_sum


def simp(h):
    int_sum1 = 0
    int_sum2 = 0
    x = A + h
    while x < B:
        int_sum1 += f(x)
        x += 2 * h

    x = A + 2 * h
    while x < B:
        int_sum2 += f(x)
        x += 2 * h
    return h / 3 * (f(A) + f(B) + 4 * int_sum1 + 2 * int_sum2)


def solve(method, h, k, eps):
    while True:
        h /= 2
        sum_h, sum_h_half = method(h), method(h / 2)
        rich = (2 ** k * sum_h_half - sum_h) / (2 ** k - 1)
        if abs(sum_h - sum_h_half) <= eps:
            break
    print '{}:\t{}\t\t{}\t{}\t{}'.format(method.__name__, eps, h, sum_h, rich)


map(lambda x: map(solve, (x, x, x), (0.001, 0.001, 0.001), (2, 2, 4), eps), (rect, trap, simp))
