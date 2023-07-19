# Fermat's little theorem
# a^(p-1) = 1 mod p
# a^p = a mod p
#
# examples:
# print(pow(3, 17, 17))  -> result is 3
# print(pow(5, 17, 17))  -> result is 5
# print(pow(7, 17 , 17)) -> result is 7
# print(pow(7, 16 , 17)) -> result is 1

# square and multiply algorithm
def square_and_multiply(x, c, n):
    y = 1
    for i in range(c.bit_length()):
        if c & (1 << i):
            y = (y * x) % n
        x = (x * x) % n
    return y

print(square_and_multiply(273246787654 , 65536, 65537))

# and you can simply use pow() function applying Fermat's little theorem and get the result = 1
# as this question obeys the formula a^(p-1) = 1 mod p
print(pow(273246787654 , 65536, 65537))