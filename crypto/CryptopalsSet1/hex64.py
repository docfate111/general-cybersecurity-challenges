#code that converts a hex string to base 64:
'''
hexstr=input("Enter a string: ")
print(divnconq(hexstr))
'''
def hex2dec(c):
	#for numbers the same character in hex is in decimal
	toDec={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
	return toDec[c]
#takes 3 hex characters and returns 2 base64 characters:
def hex2b64(input):
	base64="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	nums=[0, 0, 0]
	output=[0, 0]
	#replace each hex with respective decimal through method above:
	for i in range(3):
		nums[i]=hex2dec(input[i])
        #hex digits x,y,z->64(4x+(y/4)),16(y%4)+z
	a=(nums[1]>>2)+(nums[0]<<2)
	output[0]=base64[a]
	b=(((nums[1])&3)<<4)+nums[2]
	output[1]=base64[b]
	return output
def b642hex(input):
	output=[0, 0, 0]
	base64="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	#convert base64 to decimal then to hex
	nums=[base64.find(input[0]), base64.find(input[1]), 0]
	hex="0123456789abcdef"
	nums[0], temp=divmod(nums[0], 4)
	temp2, nums[2]=divmod(nums[1], 16)
	nums[1]=temp*4+temp2
	for i in range(3):
		output[i]=hex[nums[i]]
	return output
def b(input):
	l=len(input)
	temp="str"
	output=""
	r=l-(l%3)
	a=[0, 0, 0]
	for i in range(r):
		if(i%3==0 and i>=3):
                	output+=hex2b64(a)[0]
                	output+=hex2b64(a)[1]
		a[i%3]=input[i]
	output+=''.join(hex2b64(input[-3:]))
	pad="="
	#if not length not divisible by 3 append = so that it is
	while(r!=l):
		output+=pad
		r+=1
	return output
def h(input):
	l=len(input)
	a=[0, 0, 0]
	s=[0, 0]
	output=""
	i=0
	while(i<l):
		a=input[i:i+2]
		e=''.join(b642hex(a))
		i+=2
		output+=e
	return output
#print(h(b("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")))
