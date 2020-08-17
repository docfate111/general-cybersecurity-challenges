#!/usr/bin/python
import requests as r
flip_byte = lambda x, y: ''.join([chr(ord(i)^ord(j)) for i, j in zip(x,y)])
if __name__=='__main__':
    cookie = r.get('http://aes.cryptohack.org/flipping_cookie/get_cookie/').json()['cookie'].decode('hex')
    iv = cookie[:6]+flip_byte(cookie[6:10], 'True')+cookie[10:16]
    resp = cookie[16:]
    site = 'http://aes.cryptohack.org/flipping_cookie/check_admin/{c}/{i}/'.format(c=resp.encode('hex'), i=iv.encode('hex'))
    g = r.get(site)
    print(g.text)
