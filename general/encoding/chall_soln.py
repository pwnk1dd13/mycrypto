# pylint: disable=W0614
from pwn import * # pip install pwntools
import json
from Crypto.Util.number import long_to_bytes
import base64
import codecs


def rot13(message, shift): 
    decipher = '' 
    for letter in message: 
        if(letter != '_'): 
            num = ( ord(letter) - shift + 26) % 26
            decipher += chr(num) 
        else: 
            # adds space 
            decipher += '_'
    return decipher 

def solve(type_chall,encoded):
    if type_chall == "utf-8":
        print(encoded)
        flag = ""
        #res = ''.join(map(chr, ini_list)) #return str(res)
        for val in encoded:
            flag = flag + chr(val)
        return str(flag)
    if type_chall == "hex":
        flag = bytes.fromhex(encoded)
        flag = flag.decode('ascii')
        return flag
    if type_chall == "rot13":
        #abc = "abcdefghijklmnopqrstuvwxyz"
        #secret = "".join([abc[(abc.find(c)-13)%26] for c in cipher])
        #flag = rot13(encoded,13)
        #flag = flag.decode('ascii')
        flag = codecs.encode(encoded,'rot13')
        return flag
    if type_chall == "bigint":
        flag = bytes.fromhex(encoded[2:])
        #flag = long_to_bytes(flag)
        flag = flag.decode('ascii')
        return flag
    if type_chall == "base64":
        flag_bytes = encoded.encode('ascii')
        flag_bytes = base64.b64decode(flag_bytes)
        flag = flag_bytes.decode('ascii')
        return flag



r = remote('socket.cryptohack.org', 13377)
#r = remote('socket.cryptohack.org', 13377, level = 'debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

counter = 1
while True:
    received = json_recv()
    print(received)

    print("Received type: ",end='')
    type_chall = received["type"]
    print(type_chall)
    print("Received encoded value: ",end='')
    encoded = received["encoded"]
    print(encoded)

    payload = solve(type_chall,encoded)
    #to_send = '{"decoded": "{0}"}'.format(payload)
    to_send = {"decoded": payload}
    print("Payload Sent: ",end='')
    print(to_send)

    json_send(to_send)
    print("Level Passed: ",end='')
    print(counter)
    print()
    print()
    counter += 1
    #if counter >= 99:
        #boom = json_recv()
        #print(boom)
    #else:
        #pass
    #json_recv()
    #r.interactive()