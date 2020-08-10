#set 1 challenge 5
def repeatKeyXor(s, t):
	output=b''
	index=0
	#converts input into decimal representation then to hex and xors them
	for i in s:
		output+=bytes(format(ord(i)^ord(t[index%len(t)]), 'x'), "ascii")
		index+=1
	return output.decode()
#message=input("Enter a message to encrypt: ")
#k=input("\n Enter the key(word to Xor with): ")
#print(repeatKeyXor(message, k))
