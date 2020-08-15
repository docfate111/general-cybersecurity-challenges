import requests
from string import printable
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
def split_blocks(s, n):
    l = []
    for i in range(0, len(s), n):
        l.append(''.join(s[i:i+n]))
    return l
def print_blocks(n):
    for i in n:
        print(i)
if __name__ == "__main__":
    block_size = 32
    p = 'a'*12
    site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p)
    r = requests.get(site)
    saved = r.json()['ciphertext']
    b12 = split_blocks(saved, block_size)
    print_blocks(b12)
    p = 'a'*14
    for c in printable:
        site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p+c.encode('utf-8').hex())
        r = requests.get(site)
        resp = r.json()['ciphertext']
        b14 = split_blocks(resp, block_size)
        if b14[0]== b12[0]:
            print('='*20)
            print(c)
            print_blocks(b14)
            print('='*20)
    # by testing the length of input and output we determined that the input
    # must be an even length and that the blocks are 16 bytes
    # for i in range(2, 120, 2):
    #     p = 'a'*i
    #     site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p)
    #     r = requests.get(site)
    #     if(r.status_code==200):
    #         print(len(p), len(r.json()['ciphertext']))
    #     else:
    #         print(r.text)
