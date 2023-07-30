from requests import get


encrypt_url = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
decrypt_url = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
response = get(encrypt_url)
cipher_text = response.json()["ciphertext"]
plain_text = ""


for i in range(32, 96, 32):
    intermediary = get(f"{decrypt_url}/{cipher_text[i:i+32]}").json()["plaintext"]
    plain_text += hex(int(intermediary, 16) ^ int(cipher_text[i-32 : i], 16))[2:]


print(bytes.fromhex(plain_text))


