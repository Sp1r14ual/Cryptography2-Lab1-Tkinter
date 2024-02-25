import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def pollards_p_minus_1(n, p):
    c = 2
    for i in range(2, p):
        m = pow(c, i, n)
        d = gcd(m - 1, n)
        if 1 < d < n:
            return d
    return None
