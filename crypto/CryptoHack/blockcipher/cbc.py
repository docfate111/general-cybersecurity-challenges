import requests as r
# xor 2 hex strings
hexor = lambda a, b: hex(int(a, 16)^int(b,16))[2:]
# divide block into 3
split_block = lambda s: [s[i:i+32] for i in range(0, len(s), 32)]
# decrypt the ciphertext
decrypt = lambda x: r.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ctxt}/'.format(ctxt=x.encode('utf-8').hex())).json()['plaintext']
if __name__ == '__main__':
    ciphertext = r.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/').json()['ciphertext']
    cblocks = split_block(ciphertext)
    plaintext = hexor(cblocks[0], decrypt(cblocks[1]))
    plaintext +=  hexor(cblocks[1], decrypt(cblocks[2]))
    print(plaintext)
