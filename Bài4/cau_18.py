print("Le Van An")
print("235752021610044")
def primes_less_than_one_million_sieve():
    limit = 1000000
    is_prime = [True] * limit
    primes = []
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
    return tuple(primes)
P = primes_less_than_one_million_sieve()
print(P)
