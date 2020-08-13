from Crypto.Cipher import AES
import hashlib
import requests
# r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
# ctxt = r.json()['ciphertext']
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return {"plaintext": decrypted}
# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
for i in words:
    KEY = hashlib.md5(i.encode()).hexdigest()
    ctxt = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
    ans = decrypt(ctxt, KEY)
    ans = ans['plaintext']
    # ans = bytes.fromhex(ans['plaintext'][2:])
    if b'cry' in ans or b'CRY' in ans:
        print(ans)
    # result = decrypt('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66', KEY)
    # if b'cry' in result or b'CRY' in result:
    #     print(result, KEY)
