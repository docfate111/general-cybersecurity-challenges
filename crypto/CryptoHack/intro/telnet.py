#!/usr/bin/env python3
# sending json for challenge:  https://cryptohack.org/challenges/introduction/
import json
from pwn import *
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.send(request)
r = remote('socket.cryptohack.org', 11112)
def readline():
     return r.recvline().decode('utf-8')
for i in range(4):
    print(readline())
request = {
    "buy": "flag"
}
json_send(request)
log.info(readline())
