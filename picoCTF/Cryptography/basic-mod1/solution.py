cipher = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
cipher_array = cipher.split(" ")

#just to convert the cipher array to integers instead of strings
for i, c in enumerate(cipher_array):
    cipher_array[i] = int(c)

plain_text = ""
for i in cipher_array:
    plain_text += CHARSET[i % 37]

print(plain_text)
