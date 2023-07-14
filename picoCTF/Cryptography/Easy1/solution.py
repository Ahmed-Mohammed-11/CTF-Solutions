enc_flag = "UFJKXQZQUNB"
key = "SOLVECRYPTO"
flag = ""
for i in range(len(enc_flag)):
    flag += chr((ord(enc_flag[i]) - ord(key[i])) % 26 + ord("A"))
print(flag)
