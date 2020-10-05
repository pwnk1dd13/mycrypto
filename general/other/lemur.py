#f = open('flag.png', 'rb')
#input_bytes = f.read()
#f.close()
#
#from pwn import xor
#
#def determine_key(cipher_text : bytearray, plain_text : str):
#    key = ''
#    for i in range(len(plain_text)):
#        print(chr(cipher_text[i]))
#        print(ord(plain_text))
#        key += chr(cipher_text[i] ^ ord(plain_text[i]))
#    return key
#
#
#def get_flag(encrypted_msg : bytearray, key):
#    
#    flag = ''
#    key_length = len(key)
#    for i in range(len(encrypted_msg)):
#        # i%key_length helps avoiding out of range
#        flag += chr(encrypted_msg[i] ^ ord(key[i%key_length]))
#    flag = bytes(flag, 'utf-8') 
#    f = open('decrypted2.png', 'wb')
#    f.write(flag)
#    f.close()
#key = determine_key(h, known_plain_text) + 'y' # based on the pattern we now now the key value.
#print(key)
#get_flag(h, key)

#z = xor(inpur_bytes,known_plain_text.encode())
#print(z)
#print(determine_key(input_bytes,known_plain_text))
#print(input_bytes)

#gmic flag.png lemur.png -blend xor -o xor.png
