import base64
from Crypto.Cipher import AES
key="YELLOW SUBMARINE"
decipher=AES.new(key, AES.MODE_ECB)
def aesecb_dec(ctxt, key):
	decipher=AES.new(key, AES.MODE_ECB)
	return decipher.decrypt(ctxt)
msg=base64.b64decode(''.join(open("7.txt", "r")))
k=b'YELLOW SUBMARINE'
#print(aesecb_dec(msg, k))
