# the same thing as substitution1

key = "TKZBFVRAXJDPGLQSIYENWUMOHC".lower()
mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = "sxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}".lower()
plain_text = ""

for i in cipher_text:
    if i in key:
        charIndex = key.find(i)
        char = mapping[charIndex]
        plain_text += char
    else:
        plain_text += i

print(plain_text)