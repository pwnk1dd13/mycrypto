from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


msg = "???"

with open('21.key') as f:
    key = RSA.importKey(f.read())

cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(msg)

with open('21.ciphertext', 'w') as f:
    f.write(ciphertext.hex())

