from pwn import xor

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2xorKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGxorKEY1xorKEY3xorKEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"



KEY1 = bytes.fromhex(KEY1)
KEY2xorKEY3 = bytes.fromhex(KEY2xorKEY3)
FLAGxorKEY1xorKEY3xorKEY2 = bytes.fromhex(FLAGxorKEY1xorKEY3xorKEY2)

KEY1xorKEY2xorKEY3 = xor(KEY1 , KEY2xorKEY3)
FLAG = xor(KEY1xorKEY2xorKEY3 , FLAGxorKEY1xorKEY3xorKEY2)

print(FLAG)