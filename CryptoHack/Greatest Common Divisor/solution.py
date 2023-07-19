# Euclid's Algorithm

def gcd(a, b):
    # if the mode of b and a is 0, then return the remainder of the previous operation
    if a == 0:
        return b
    return gcd(b % a, a)

print(gcd(66528, 52920))