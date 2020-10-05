import binascii
from pwn import xor 
from Crypto.Util.number import bytes_to_long,long_to_bytes
import struct

#text = "label"
#flag = ""
#for ch in text:
#    cy = ord(ch)
#    cy = cy ^ 13
#    flag = flag + chr(cy)

#hidden_flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" #FLAG ^ KEY1 ^ KEY3 ^ KEY2
#key2key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" #KEY2 ^ KEY3
#key1key2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" #KEY2 ^ KEY1
#key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" #KEY1
#def xor(text1,text2):
#    text = int(text1,16) ^ int(text2,16) #outputs integer
#    return text
##key2 = int(key1key2,16) ^ int((key1),16)
#key2 = xor(key1key2, key1)
#print(key2)
#key3 = int(key2key3,16) ^ key2
#print(key3)
#flag = xor(xor(xor(hidden_flag, key2), key3), key1)
#flag_3 = int(hidden_flag, 16) ^ key2
#print(flag_3)
#flag_2 = flag_3 ^ key3
#print(flag_2)
#flag_1 = flag_2 ^ int(key1,16)
#flag = long_to_bytes(flag_1)

fav_byte = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
sec_byte = ""
decode_msg = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
#ord('c') ^ 0x73 = 16
#byte = 16
flag = ""

for b in decode_msg:
    flag += chr(b ^ 16)

print(decode_msg)
print(flag)