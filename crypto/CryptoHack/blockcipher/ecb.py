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
    # lets get 2 blocks
    block_size = 32
    ind = 1
    flag = ''
    while(ind<block_size):
        p = (block_size-ind)*'a'
        print(p)
        site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p.encode('utf-8').hex())
        r = requests.get(site)
        saved = r.json()['ciphertext']
        first = split_blocks(saved, block_size)
        for c in printable:
            p = (block_size-ind)*'a'+flag+c
            print(p)
            site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p.encode('utf-8').hex())
            r = requests.get(site)
            if(r.status_code==200):
                resp = r.json()['ciphertext']
                second = split_blocks(resp, block_size)
                if second[1]==first[1]:
                    print('='*20)
                    print('Found')
                    print('='*20)
                    flag += c
                    ind += 1
                    break
            else:
                print("="*20)
                print(r.text)
                print("="*20)
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
