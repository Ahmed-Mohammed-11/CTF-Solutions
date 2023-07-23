from sympy.ntheory import discrete_log
import math
from math import gcd

a = 288260533169915
p = 1007621497415251

# we now that each element of the cipher is either n or p-n
# so we can just try to compute the discrete log of each element considering it is n and hence append 1 to the plain text
# if it fails, it means it is p-n and we append 0 to the plain text


cipher = open('output_80fc6398d2fd9f272186d0af510323f9.txt', 'r')
cipher = cipher.read()[1:len(cipher.read())-2].split(', ')


cipher_list = []
for i in cipher:
    cipher_list.append(int(i))

plain = ''

for i in cipher_list:
    print(i)
    try :
        discrete_log(p, i, a)
        plain += '1'
    except:
        plain += '0'

plain_list = [(plain[i:i+8]) for i in range(0, len(plain), 8)]
print(''.join(chr(int(i, 2)) for i in plain_list))






