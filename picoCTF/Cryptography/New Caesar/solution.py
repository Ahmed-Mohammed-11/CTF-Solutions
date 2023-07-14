import string
flag = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

LOWERCASE_OFFSET = ord("a")
# first 16 letters of alphabet lowercase  (a-p)
ALPHABET = string.ascii_lowercase[:16]

def shift(c, k):  # c is a letter in the alphabet for c in plain (a-p)
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

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


#https://www.youtube.com/watch?v=yaZP4bMn4pU
