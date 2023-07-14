# Description
# In RSA, a small e value can be problematic, but what about N?
# Can you decrypt this?

# c: 421345306292040663864066688931456845278496274597031632020995583473619804626233684
# n: 631371953793368771804570727896887140714495090919073481680274581226742748040342637
# e: 65537


# Solution
import math

# We can use factordb to factorize N
# https://factordb.com

p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809
e = 65537
d = pow(e, -1, (p-1)*(q-1))
c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
m = pow(c, d, p*q)
print(m)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big').decode())

# m.bit_length(): This part calculates the number of bits required to represent the integer value m. 
# The bit_length() method returns the minimum number of bits needed to represent a non-negative integer. 
# For example, if m is 10, its binary representation is '1010', which requires 4 bits.
# + 7: This adds 7 to the bit length. The purpose of adding 7 is to ensure that the number of bits is always rounded up to the nearest multiple of 8. 
# This is done to ensure that the number of bits can be divided evenly into bytes.
# // 8: This performs integer division by 8, which effectively converts the number of bits to the number of bytes required. 
# Integer division discards the remainder, so the result will be the number of whole bytes needed to represent the value.
# m.to_bytes(...): This method converts the integer m to its byte representation. 
# The method to_bytes() takes two arguments: the first argument specifies the number of bytes required to represent the value, 
# and the second argument specifies the byte order. In this case, the first argument is (m.bit_length() + 7) // 8, 
# which is the calculated number of bytes, and the second argument is 'big', which indicates that the most significant byte should be placed first.
# .decode(): This method converts the byte representation of the integer into a string. 
# The decode() method is used to convert a sequence of bytes into a string using a specified encoding. 
# In this case, no encoding is explicitly specified, so it will use the default encoding (usually UTF-8) to convert the bytes into a string.


# another way
# def factorize(n):
#     factors = []
#     limit = int(math.sqrt(n)) + 1

#     for i in range(2, limit):
#         if n % i == 0:
#             factors.append((i, n // i))
#             break

#     if len(factors) == 0:
#         factors.append((1, n))

#     return factors

# # Example usage
# N = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
# result = factorize(N)
# print(result)

# if len(result) > 0:
#     print(f"The factors of {N} are: {result[0][0]} and {result[0][1]}")
# else:
#     print(f"{N} is a prime number")