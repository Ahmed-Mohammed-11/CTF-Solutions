# Extended Euclidean algorithm
# p * u + q * v = gcd(p, q)


def extended_gcd(p, q):
    if q == 0:
        return (1, 0)
    (u, v) = extended_gcd(q, p % q)
    return (v, u - (p // q) * v)

print(extended_gcd(26513, 32321))
print(10245 * 26513 - 8404 * 32321) #must be 1 as p and q are 2 primes and so they are coprime
