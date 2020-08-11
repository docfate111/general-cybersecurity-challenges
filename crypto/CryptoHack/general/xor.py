#!/usr/bin/python3
from PIL import Image
import numpy as np
from pwn import *
# Given the string "label", XOR each character with the integer 13
xorn = lambda s, n: ''.join([chr(ord(i)^n) for i in s])
print('crypto{'+xorn('label', 13)+'}')
# KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
# KEY2 ^ KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
# KEY2 ^ KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
s = bytes.fromhex(hex(int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf',16)^int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1',16)^(int(k1,16)))[2:])
print(s.decode('utf-8'))
# I've hidden my data using XOR with a single byte. Don't forget to decode from hex first.
a = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
b = bytes.fromhex(a)
for i in range(20):
    s = xor(bytes(chr(i), 'utf-8'), b).decode('utf-8')
    if 'crypto' in s:
        print(s)
#I've encrypted the flag with my secret key, you'll never be able to guess it.
# convert 'crypto{' into binary and xor a(hex string) then xor to find the original key
# the original key is stored in ans and then xored with the hex string
# to get the flag
a = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
st='crypto{'
given = [format(ord(x), 'b') for x in st][:7]
key = [format(x, 'b') for x in bytes.fromhex(a)][:7]
def xor_str(x, y):
    return '{0:b}'.format(int(x, 2) ^ int(y, 2))
ans = ''
for i in range(7):
    ans += chr(int(xor_str(given[i], key[i]), 2))
ans += 'y'
print(ans)
key = [format(x, 'b') for x in bytes.fromhex(a)]
key2 = [bin(ord(i))[2:] for i in ans*5+ans[:2]]
resp = ''
for i in range(len(key2)):
    resp += chr(int(xor_str(key[i], key2[i]), 2))
print(resp)
def xor_images(a, b):
    im1 = Image.open(a)
    im2 = Image.open(b)
    # Make into Numpy arrays
    im1np = np.array(im1)*255
    im2np = np.array(im2)*255
    # XOR with Numpy
    result = np.bitwise_xor(im1np, im2np).astype(np.uint8)
    # Convert back to PIL image and save
    Image.fromarray(result).save('result.png')
xor_images('lemur.png', 'flag.png')
