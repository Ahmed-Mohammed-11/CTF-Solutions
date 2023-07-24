# from Crypto.Cipher import AES
#
#
# KEY = ?
# FLAG = ?
#
#
# @chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
# def decrypt(ciphertext):
#     ciphertext = bytes.fromhex(ciphertext)
#
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         decrypted = cipher.decrypt(ciphertext)
#     except ValueError as e:
#         return {"error": str(e)}
#
#     return {"plaintext": decrypted.hex()}
#
#
# @chal.route('/block_cipher_starter/encrypt_flag/')
# def encrypt_flag():
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     encrypted = cipher.encrypt(FLAG.encode())
#
#     return {"ciphertext": encrypted.hex()}

# you can use the website directly to decrypt the ciphertext
# or using agent like postman
# or using python script
