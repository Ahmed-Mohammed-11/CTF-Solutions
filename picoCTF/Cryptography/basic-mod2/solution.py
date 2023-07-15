cipher = "432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
cipher_array = cipher.split(" ")

# just to convert the cipher array to integers instead of strings
for i, c in enumerate(cipher_array):
    cipher_array[i] = int(c)


plain_text = ""


for i in cipher_array:
    # just perform the operation of i mod 41 and then take the modular inverse of the result then subtract one as it the map from 1 not 0
    plain_text += CHARSET[pow(i % 41, -1, 41) - 1]
print(plain_text)
