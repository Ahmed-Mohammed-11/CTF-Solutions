import string
import base64

for i in range(10000):
    print("the char is -> " ,  chr(i) , " and the utf-8 encoding is ->" , chr(i).encode('utf-8') , " and the base64 encoding is -> " , base64.b64encode(chr(i).encode('utf-8')))


print(base64.b64encode(b'a'))
print(bytes('a', 'utf-8'))
#print binary representation of a
print(bin(ord('a')))
print(bin(97))
print(bin(32894783294))
print(base64.b64encode(bytes('ε', 'utf-8')))
print(base64.b64encode(bytes('║4', 'utf-8')))

