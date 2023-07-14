# this time we don't have the key mapping so we need frequency analysis attack
# using this website https://planetcalc.com/8047/

key = "ATZMXDREBUNQIVJCLFGWPYHOSK".lower()
mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = "cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}".lower()
plain_text = ""

for i in cipher_text:
    if i in key:
        charIndex = key.find(i)
        char = mapping[charIndex]
        plain_text += char
    else:
        plain_text += i

print(plain_text)
