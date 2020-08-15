import requests
from string import printable
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def oracle(chosen):
    secret = ("a"*46) + chosen # target to decrypt
    secret = getPadding(secret)
    if display:
        displaySecret(secret) # For illustrative purposes
    ct = cipher.encrypt(secret)
    return ct

def getPadding(secret):
    pl = len(secret)
    mod = pl % 16
    if mod != 0:
        padding = 16 - mod
        secret += "X" * padding
    return secret

def displaySecret(secret):
    split = split_len(secret, 16)
    display = ""
    for i in split:
        for j in split_len(i, 1):
            display += j + " "
        display += " "
    print("pt: %s" % display)

def displayCiphertext(ct):
    split = split_len(ct, 16)
    display = ""
    for i in split:
        display += i.encode('hex') + " "
    print("ct: %s" % (display))

if __name__ == "__main__":
    p = 'a'*46
    each_letter = {}
    for c in printable:
        site = 'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/'.format(plaintext=p+c.encode('utf-8').hex())
        r = requests.get(site)
        if(r.status_code==200):
            resp = r.json()['ciphertext']
            each_letter[c] = resp
        else:
            print(r.text)
    for i in each_letter.keys():
        print(each_letter, each_letter[i])
    chosen = sys.argv[1]
    ct = oracle(chosen)
    if display:
        displayCiphertext(ct)
    else:
        print(ct.hex())
