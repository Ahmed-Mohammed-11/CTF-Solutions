import Crypto.Util.number
from Crypto.Util.number import *

# We know that the AES Algorithm isn't broken (yet) so we are just breaking the bad choices in implementation like key and IV choices , ...
# in AES -CBC if we choose the IV as random enough and didn't reuse it, the algorithm will be considered secure
# if we choose to decrypt a made up cipher text of all zeros the output of the decryption function would be the same but then xored with different intermediates
# so we just need a cipher text of 32 bytes long to use 2 decryption functions
# if we performed the following plain(0) xor plain(1) =
#                                                                                   (IV xor decrypted(0)) xor (cipher(0) xor decrypted(1))
# and since the decrypted(0) = decrypted(1) the xoring of them is 0
#                                                                                    (IV) xor cipher(0)) and cipher(0) is all zeros so the result of this xoring is the IV
# We just need to decrypt a cipher of 32 bytes of zeros and xor the 2 resulting plain-text chuncks

c1 = "0" * 32
p1 = "8485b912712a1dc4bffecdfe33852cc7"
c2 = "0" * 32
p2 = "905b08a5e2eb094efc3ab1bd7e1df7c5"


p1 = int(p1, 16)
p2 = int(p2, 16)


key = p1 ^ p2
print(
    key.to_bytes(16, "big").hex()
)  # this is the IV in hex check with check_key function provided by the flask app


# The key is correct and we got the flag of 98 hex chars with 30 hex chars padding
flag = "4547434552547b39616631346430303539623763323939376366353565316232623365336664305f65313661323136307d"
flag = int(flag, 16)

print(long_to_bytes(flag).decode())
