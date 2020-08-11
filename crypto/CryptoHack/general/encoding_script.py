import base64
import binascii
import json
import codecs
import pwn
ascii = lambda x: ''.join([chr(i) for i in x])
unhex = lambda x: bytes.fromhex(x).decode('utf-8')
b64 = lambda x: base64.b64decode(x).decode('utf-8')
bigint_to_str = lambda x: binascii.unhexlify(hex(int(x, 16))[2:]).decode('utf-8')
rot13 = lambda x: codecs.decode(x, 'rot13')
r = pwn.remote('socket.cryptohack.org', 13377)
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.send(request)
for i in range(101):
    s = r.recvline(timeout=1)
    print(s.decode('utf-8'))
    json_response = json.loads(s)
    if 'flag' in json_response.keys() or 'error' in json_response.keys():
        break
    else:
        encoded = json_response['encoded']
        ans = ''
        if(json_response['type']=='bigint'):
            ans = bigint_to_str(encoded)
        elif(json_response['type']=='hex'):
            ans = unhex(encoded)
        elif(json_response['type']=='utf-8'):
            ans = ascii(encoded)
        elif(json_response['type']=='rot13'):
            ans = rot13(encoded)
        else:
            ans = b64(encoded)
        response = {'decoded':ans}
        print(response)
        json_send(response)
# pwn.log.info('Flag: '+json_response['flag'])
