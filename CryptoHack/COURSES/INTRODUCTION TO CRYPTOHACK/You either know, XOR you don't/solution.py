from pwn import xor
data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data = bytes.fromhex(data)
flag_part = b"crypto{"
print(xor(data[:7], flag_part)) #this results in this byte sting b'myXORke'
#it seems like the key is 8 bytes (myXORkey) long and we have the first 7 bytes

for i in range(256):
    flag_part = b"crypto{" + bytes([i])
    # print(i , "-> ", bytes([i]))
    key = xor(flag_part , data[:8])
    if key == b'myXORkey':
        print(flag_part)
        break


print(xor(data, key))





