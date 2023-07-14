import string

LOWERCASE_OFFSET = ord("a")
# first 16 letters of alphabet lowercase  (a-p)
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def shift(c, k):  # c is a letter in the alphabet for c in plain (a-p)
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = "redacted"
key = "redacted"

# k is in alphabet for k in key (k is a letter in the alphabet for k in key) (a-p)
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1  # key is 1 letter long

b16 = b16_encode("aaaaaaaaaaaa")
enc = ""

for i, c in enumerate(b16):
    print(i, c)
    enc += shift(c, key[i % len(key)])
print(enc)




def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        first = "{0:04b}".format(ALPHABET.index(enc[i]))
        second = "{0:04b}".format(ALPHABET.index(enc[i + 1]))
        plain += chr(int(first + second, 2))
    return plain


for key in ALPHABET:
    flag_clear = ""
    for c in flag:
        flag_clear += shift(c, key)
    print(b16_decode(flag_clear))
