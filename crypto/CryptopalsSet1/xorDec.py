def charXor(input, n):
	#input is hex string n is ASCII character as number
	input=bytes.fromhex(input)
	output=b''
	for i in input:
		output+=bytes([i^n])
	return output
def score(input):
	count=0
	freqchars=" uldrhsnioate"
	#most frequent English letters will be most similar to english
	s=str(input, encoding='ascii', errors='ignore')
	for i in range(len(s)):
		for j in range(len(freqchars)):
			if(s[i]==freqchars[j]):
				count+=j
	return count
def findEnglish(s):
		output=""
		max=0
		for i in range(256):
			if(max<score(charXor(s, i))):
				max=score(charXor(s, i))
				output=charXor(s, i)
		return output, max
#for set 1 part 3:
#print(findEnglish("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
#for set 1 part 4:
def checkFile(name):
	f=open(name, 'r')
	max=0
	output=""
	#combing through hex file and returning most English like output
	for c in f.read().split('\n'):
			if(findEnglish(c)[1]>max):
				max=findEnglish(c)[1]
				output=findEnglish(c)[0]
	return output.decode()
#print("Loading ...")
#print(checkFile("hex.txt"))

