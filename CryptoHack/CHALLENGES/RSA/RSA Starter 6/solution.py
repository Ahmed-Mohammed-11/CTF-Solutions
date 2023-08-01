from hashlib import sha256
from Crypto.Util.number  import bytes_to_long

message = "crypto{Immut4ble_m3ssag1ng}".encode("utf-8")
file = open("private_0a1880d1fffce9403686130a1f932b10.key" , "rb").read()
N = int(file.split(b"\n")[0].split(b"=")[1])
private_key = int(file.split(b"\n")[1].split(b"=")[1])



hashed_message = bytes_to_long(sha256(message).digest())
signed_message = pow(hashed_message, private_key, N)

print(signed_message)

