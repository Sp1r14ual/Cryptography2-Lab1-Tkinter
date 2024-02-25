import math
import sympy
import time


def pollard(n):
    iter_count = 0
    c = 2
    i = 2

    while (True):
        m = pow(c, i, n)
        d = math.gcd((m-1), n)
        if (d > 1):
            return (d, iter_count + 1)
        i += 1
        iter_count += 1


def factorize(n):
    iter_count = 0
    start_time = time.time()

    num = n
    factors = []

    while (True):
        d, iter_count_subloop = pollard(num)
        iter_count += iter_count_subloop
        factors.append(d)
        r = int(num / d)

        if (sympy.isprime(r)):
            factors.append(r)
            break
        else:
            num = r

    end_time = time.time()
    elapsed_time = end_time - start_time

    return (factors, elapsed_time, iter_count)
