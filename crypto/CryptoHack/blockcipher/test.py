from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from datetime import datetime, timedelta
import os
flip_byte = lambda x, y: ''.join([chr(i^j) for i, j in zip(x,y)])
KEY = 'key'+'b'*13
FLAG = 'crypto{}'+'a'*8
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)
    try:
        cipher = AES.new(KEY.encode(), AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        print(unpadded.split(b';'))
        return {"error": "Only admin can read the flag"}
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()
    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY.encode(), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()
    return {"cookie": ciphertext}
if __name__=='__main__':
    cookie = bytes.fromhex(get_cookie()['cookie'])
    iv = cookie[:16]
    resp = cookie
    print(check_admin(resp.hex(), iv.hex()))
    resp = cookie[16:23]+flip_byte(b'True', cookie[23:27]).encode()+cookie[27:]
    print(check_admin(resp.hex(), iv.hex()))
