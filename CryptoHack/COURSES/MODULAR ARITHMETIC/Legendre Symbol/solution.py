p = int(open('output_479698cde19aaa05d9e9dfca460f5443.txt' , 'r').readline().split('= ')[1])

#read array of numbers from file
numbers = []
numbers = open('output_479698cde19aaa05d9e9dfca460f5443.txt' , 'r').readlines()[2:]
numbers = numbers[0][8:-2].split(', ')

for a in numbers:
    if(pow(int(a), (p - 1) // 2, p) == 1):
        print("The Quadratic Residue is -> " , a, end = ' ')

QR = numbers[5]
print()

# from the hint p ≡ 3 mod 4
# so ( p + 1 ) // 4 is an integer
# and if we tried to square
# (a ^ (( p + 1 ) // 4 )) ^ 2 % p
# (a ^ (( p + 1 ) // 2 )) % p
# (a ^ ( p + 1 -2 + 2 ) // 2) % p
# (a ^ ( p - 1 ) // 2) * a % p
# the first portion ≡ 1 from legendre symbol
# so the result is a % p or QR mod p
# meaning that the square roots of QR mod p is
# a ^ (( p + 1 ) // 4 ) , -a ^ (( p + 1 ) // 4 )

print("The greater square root is -> " , max(pow(int(QR), (p + 1) // 4, p), pow(- int(QR), (p + 1) // 4, p)))
