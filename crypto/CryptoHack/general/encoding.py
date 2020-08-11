import base64
import binascii
# ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
#
# Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
ascii = lambda a: ''.join([chr(i) for i in a])
print(ascii(a))
# When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.
#
# Included below is a the flag encoded as a hex string. Decode this back into bytes to get the flag.
h = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
print(bytes.fromhex(h).decode('utf-8'))
# Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters. One character of a Base64 string encodes 6 bits, and so 4 characters of Base64 encodes three 8-bit bytes.
#
# Base64 is most commonly used online, where binary data such as images can be easy included into html or css files.
#
# Take the below hex string, decode it into bytes and then encode it into Base64.
b = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
b = bytes.fromhex(b)
print(base64.b64encode(b))
# Convert the following integer back into a message:
h = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(binascii.unhexlify(hex(h)[2:]).decode('utf-8'))
