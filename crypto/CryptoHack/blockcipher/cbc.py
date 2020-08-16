import requests as r
# xor 2 hex strings
hexor = lambda a, b: hex(int(a, 16)^int(b,16))[2:]
# divide block into 3
split_block = lambda s: [s[i:i+32] for i in range(0, len(s), 32)]
# decrypt the ciphertext
decrypt = lambda x: r.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ctxt}/'.format(ctxt=x)).json()['plaintext']
if __name__ == '__main__':
    ciphertext = r.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/').json()['ciphertext']
    cblocks = split_block(ciphertext)
    plaintext = ''
    for i in range(2):
        plaintext += hexor(cblocks[i], decrypt(cblocks[i+1]))
    print(bytes.fromhex(plaintext).decode('utf-8'))
