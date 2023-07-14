import Crypto.Util.number
from Crypto.Util.number import *
import os

flag_enc = "61bade96f3f7f36d90c29b92d1bb7b8aa9ba9692e61da2c9e3fefbb876dce0"
first_part_of_decrypted_flag = b"EGCERT{"
key = bytes_to_long(first_part_of_decrypted_flag) ^ int(flag_enc[0:14], 16)

# check the key is valid (Done)

bytes_key = long_to_bytes(key)
flag = [0 for i in range(31)]
k = 0
for i in range(0, len(flag_enc), 2):
    flag[k] = int(flag_enc[i : i + 2], 16) ^ bytes_key[k % 7]
    k += 1

dec_flag = b""
for i in flag:
    dec_flag += long_to_bytes(i)

#from bytes to string
print(dec_flag.decode("utf-8"))
