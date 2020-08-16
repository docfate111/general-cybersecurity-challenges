import requests as r
#r.get('http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/')
# def check_admin(cookie, iv):
#     cookie = bytes.fromhex(cookie)
#     iv = bytes.fromhex(iv)
#     try:
#         cipher = AES.new(KEY, AES.MODE_CBC, iv)
#         decrypted = cipher.decrypt(cookie)
#         unpadded = unpad(decrypted, 16)
#     except ValueError as e:
#         return {"error": str(e)}
#     if b"admin=True" in unpadded.split(b";"):
#         return {"flag": FLAG}
#     else:
#         return {"error": "Only admin can read the flag"}
# def get_cookie():
#     expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
#     cookie = f"admin=False;expiry={expires_at}".encode()
#     iv = os.urandom(16)
#     padded = pad(cookie, 16)
#     cipher = AES.new(KEY, AES.MODE_CBC, iv)
#     encrypted = cipher.encrypt(padded)
#     ciphertext = iv.hex() + encrypted.hex()
#     return {"cookie": ciphertext}
if __name__=='__main__':
    cookie = r.get('http://aes.cryptohack.org/flipping_cookie/get_cookie/').json()['cookie']
    iv = cookie[:32]
