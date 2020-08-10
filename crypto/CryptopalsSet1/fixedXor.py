from hex64 import hex2dec
#xors 2 hex strings
def hexor(a, b):
        l=len(a)
        hex="0123456789abcdef"
        output=[]
        for j in range(l):
                output+=hex[(hex2dec(a[j]))^(hex2dec(b[j]))]
        return ''.join(output)
def hexXor(a, b):
	return bytes([x^y for x,y in zip(a, b)])
'''
str=input("Enter a hex string: ")
str2=input("Enter another hex string: ")
print(hexor(str, str2))
'''

