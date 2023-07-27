from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)
    print("plaintext: ", str(plaintext))
    padded = pad(plaintext, 16)
    print("padded: ", str(padded.hex()))
    cipher = AES.new(b'A'*16, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
        print("encrypted: ", str(encrypted))
    except ValueError as e:
        return {"error": str(e)}
    return {"ciphertext": encrypted.hex()}


plain = "123456789abcdefg"
plain = plain.encode("utf-8").hex()
encrypt(plain)