def sieve(n):
    arr = set(range(2, n+1))
    sieve = set()
    while arr:
        prime = min(arr)
        sieve.add(prime)
        arr -= set(range(prime, n+1, prime))

    return True if n in sieve else False
