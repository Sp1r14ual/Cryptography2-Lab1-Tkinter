def trial_division(n):

    divisors = []

    while n % 2 == 0:
        divisors.append(2)
        n //= 2

    f = 3

    while f * f <= n:
        if n % f == 0:
            divisors.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        divisors.append(n)

    return True if len(divisors) == 1 else False
