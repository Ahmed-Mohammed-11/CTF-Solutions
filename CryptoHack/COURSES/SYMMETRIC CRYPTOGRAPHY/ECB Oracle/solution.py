from requests import get
from Crypto.Util.Padding import pad

#lets construct the full script by bruteforcing the whole 16bytes

encrypt_url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
counter = 1
prepend = '00'*8
last_payload = ''
plain_text = ""

while counter < 19 :
    response1 = get(encrypt_url + prepend)
    last_block = response1.json()["ciphertext"][-32:] if counter < 16 else response1.json()["ciphertext"][-64:-32]
    prepend += '00'
    counter += 1
    for i in range(128):
        payload = str(hex(i)[2:]).zfill(2) + last_payload
        payload_padded = str((pad(bytes.fromhex(payload), 16)).hex())
        print("trying this payload -> " , payload_padded)
        response2 = get(encrypt_url + payload_padded)
        first_block = response2.json()["ciphertext"][:32]
        if(first_block == last_block):
            print("found the byte -> ", chr(i))
            last_payload = str(hex(i)[2:]).zfill(2) + last_payload
            plain_text =  chr(i) + plain_text
            break

print("the plain text is -> crypto{" + plain_text)
