from pwn import xor
import string
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(data)
print(data)
flag = b""

for i in range(256):
    flag = xor(data, i)
    if flag.startswith(b'crypto'):
        print(flag)
        break


# another solution
byte = data[0] ^ ord('c')
print(byte)
flag = xor(data, byte)
print(flag)


