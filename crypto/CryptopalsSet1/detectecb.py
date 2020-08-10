def count(ctxt, size):
	chunks=[ctxt[i:i+size] for i in range(0, len(ctxt), size)]
	numoreps=len(chunks)-len(set(chunks))
	ans={
		'ciphertext': ctxt,
		'repetitions': numoreps
	}
	return ans
if __name__=='__main__':
	ctxt=[bytes.fromhex(line.strip()) for line in open('8.txt')]
	sz=16
	reps=[count(cipher, sz)['repetitions'] for cipher in ctxt]
	mostreps=max(reps)
	#print("Ciphertext: {}".format(mostreps['ciphertext'])
	print("Repeating blocks: {}".format(mostreps))
