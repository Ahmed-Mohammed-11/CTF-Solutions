from requests import *
from hashlib import md5

encrypt_url = "http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"
decrypt_url = "https://aes.cryptohack.org/passwords_as_keys/decrypt/"

# encrypt the flag
response = get(encrypt_url)
cipher_text = response.json()["ciphertext"]

wordlist_url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
wordlist = get(wordlist_url).text.splitlines()
print(f"wordlist length: {len(wordlist)}")

for i in range(len(wordlist)):
    digest = md5(wordlist[i].encode()).hexdigest()
    response = get(f"{decrypt_url}/{cipher_text}/{digest}")
    print(f"Trying {wordlist[i]} which is number {i}")
    plain_text = bytes.fromhex(response["plaintext"])
    if b'crypto' in plain_text:
        print(plain_text)
        break






