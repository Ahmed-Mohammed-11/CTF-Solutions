

######## I made the changes to this file ########

import json
import codecs
import base64

from pwnlib.tubes.remote import remote

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


# solution starts here
# while loop to keep receiving and sending data and
# break when the flag is received

received = json_recv()
while received:

    print(received)

    if "flag" in received:
        print(received["flag"])
        break

    # Initialize the decoded variable to fill it later
    decoded = ""

    # Check the encoding type and decode accordingly
    if received['type'] == "base64":
        decoded = base64.b64decode(received['encoded']).decode()
    elif received['type'] == "hex":
        decoded = bytes.fromhex(received['encoded']).decode()
    elif received['type'] == "rot13":
        decoded = codecs.encode(received['encoded'], 'rot_13')
    elif received['type'] == "bigint":
        # sorry this silly way is the only way I could get it to work as Crypto library is not available
        number_of_bytes = len(received['encoded'][2:]) // 2
        decoded = (int(received['encoded'], 16)).to_bytes(number_of_bytes, 'big').decode()
    elif received['type'] == "utf-8":
        decoded = "".join([chr(b) for b in received['encoded']])

    print("Decoded value: ")
    print(decoded)
    to_send = {
        "decoded": decoded
    }

    json_send(to_send)
    received = json_recv()

