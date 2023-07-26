from hashlib import md5
from Crypto.Cipher import AES
from requests import *

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return {"plaintext": decrypted.hex()}


wordlist_url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
wordlist = get(wordlist_url).text.splitlines()
print(f"wordlist length: {len(wordlist)}")

encrypt_url = "http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"

# encrypt the flag
response = get(encrypt_url)
cipher_text = response.json()["ciphertext"]

for i in range(len(wordlist)):
    digest = md5(wordlist[i].encode()).hexdigest()
    plain_hex = decrypt(cipher_text, digest)
    print(f"Trying {wordlist[i]} which is number {i}")
    plain_text = bytes.fromhex(plain_hex["plaintext"])
    if b'crypto' in plain_text:
        print(plain_text)
        break
