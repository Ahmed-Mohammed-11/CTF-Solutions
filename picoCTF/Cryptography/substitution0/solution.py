# refer to https://www.sciencedirect.com/topics/computer-science/substitution-cipher for more information about substitution cipher

key = "OHNFUMWSVZLXEGCPTAJDYIRKQB".lower()
#just a mapping of the alphabet
mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = "pvncNDM{5YH5717Y710G_3I0XY710G_03055505}".lower()
plain_text = ""

for i in cipher_text:
    if i in key:
        charIndex = key.find(i)
        char = mapping[charIndex]
        plain_text += char
    else:
        plain_text += i

print(plain_text)

