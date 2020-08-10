import base64
from hex64 import h
from hex64 import b
#cryptopals set 1 challenge 6 decrypt base64 xored ciphertext
#this method returns the hamming distance between 2 strings
#which is the number of different bits
def ham(s, t):
	sum=0
	for i in range(len(s)):
		#replaced bin() with format(,08b) so strings are the same length
		a, b=format(ord(s[i]), '08b'), format(ord(t[i]), '08b')
		for k in range(len(a)):
			if(a[k]!=b[k]):
				sum+=1
			#counts bytes that are the same(could be done with xor)
	return sum
def findKeySize(filename):
	input=''.join(open(filename, "r"))
	#convert file into big string without "\n" symbols
	while(input.find('\n')!=-1):
		input=input.replace('\n', '')
	#let keysize be between 2 and 40
	ks=2
	max=0
	for kl in range(2, 41):
		dist=float(ham(input[:5*kl], input[5*kl:10*kl]))/float(kl)
		if(dist>max):
			max=dist
			res=kl
	return res
def transpose(filename):
	key=findKeySize(filename)
	bigStr=''.join(open(filename, "r"))
	#convert file into big string without "/n" symbols
	while(bigStr.find('\n')!=-1):
		bigStr=bigStr.replace('\n', '')
	e=[]
	i=0
	#divide big string into chunks of keysize(in hex):
	print(bigStr)
	ans=[]
	return ans
print(transpose('6.txt'))
