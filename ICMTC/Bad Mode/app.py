from flask import Flask
import os
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import codecs

KEY = os.urandom(16)
app = Flask(__name__)

@app.route('/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext_bytes = codecs.decode(ciphertext, "hex")
    decrypted = AES.new(KEY, AES.MODE_CBC, KEY).decrypt(ciphertext_bytes)
    return codecs.encode(decrypted, "hex").decode()

@app.route('/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext_bytes = codecs.decode(plaintext, "hex")
    encrypted = AES.new(KEY, AES.MODE_CBC, KEY).encrypt(plaintext_bytes)
    return codecs.encode(encrypted, "hex").decode()

@app.route('/check_key/<user_key>/')
def check_key(user_key):
    FLAG = os.environ.get("FLAG")
    FLAG = pad(FLAG.encode(), 16)
    user_key_bytes = codecs.decode(user_key, "hex")
    return codecs.encode(FLAG, "hex").decode() if user_key_bytes == KEY else "Try Again !!"

@app.route('/')
def home():
    return "Hi!"

if __name__ == "__main__":
    app.run()
