import requests
from string import printable
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
def print_in_blocks_of(s, n):
    for i in range(0, len(s), n):
        print(s[i:i+n])
if __name__ == "__main__":
    p = 'a'*46
    site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p)
    r = requests.get(site)
    saved = r.json()['ciphertext']
    print_in_blocks_of(saved, 32)
    p = 'a'*44
    for c in printable:
        site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p+c.encode('utf-8').hex())
        r = requests.get(site)
        resp = r.json()['ciphertext']
        if resp[32:38] == saved[32:38]:
            print('='*20)
            print(c)
            print_in_blocks_of(resp, 32)
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
