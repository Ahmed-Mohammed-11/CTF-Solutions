# the idea to solve this challenge is to reset the key and encrypt your own text with the same key used to encrypt the flag
# which are the first 32 byte from the key and then start to xor the enctext with the text to retrieve the key 
# and then encrpyt the key with the encrypted flag and boom you have the flag

import pwn
from pwn import xor

enc_test_text = bytes.fromhex("1a5f2400404b24001e4824001c1a0f24001a4d24001d4e240019192224001d4e")
test_text = bytes("x" * 32, "utf-8")
enc_flag = bytes.fromhex("551e6c4c5e55644b56566d1b5100153d4004026a4b52066b4a5556383d4b0007")

key = xor(enc_test_text, test_text)
flag = xor(enc_flag, key)
print(flag)





