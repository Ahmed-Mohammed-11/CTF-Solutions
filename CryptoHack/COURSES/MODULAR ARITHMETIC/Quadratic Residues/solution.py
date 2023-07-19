def is_quadratic_residue(n, p):
    return pow(n, (p-1)//2, p) == 1


def find_square_root(n, p):
    if not is_quadratic_residue(n, p):
        return "Not a quadratic residue"
    set = []
    for i in range(p):
        if i*i % p == n:
            set.append(i)
    return "set of square roots -> " + str(set)

p = 29
number = [14, 6, 11]
for n in number:
    print(find_square_root(n, p))


# another solution

def quadratic_residue(n, p):
    # simple solution
    set = []
    for i in range(p):
        if i * i % p == n:
            set.append(i)

    if len(set) == 0:
        return "Not a quadratic residue"
    else:
        return "set of square roots -> " + str(set)

for n in number:
    print(quadratic_residue(n, p))

