# print(pow(3, 17, 17))
# print(pow(7, 16, 17))

# square and multiply algorithm
def square_and_multiply(x, c, n):
    y = 1
    for i in range(c.bit_length()):
        if c & (1 << i):
            y = (y * x) % n
        x = (x * x) % n
    return y

print(square_and_multiply(273246787654 , 65536, 65537))