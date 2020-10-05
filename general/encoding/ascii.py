import binascii
import base64
from Crypto.Util.number import bytes_to_long,long_to_bytes


#ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125] 
#for a in ascii:
#    print(chr(a),end='')

#hex_text = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
#flag_term = chr(int(hex_text,16)) #not working
#flag = hex_text.decode('ascii') #not working
#flag = bytes.fromhex(hex_text)

#hex_text = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
#flag_bytes = bytes.fromhex(hex_text)
#flag = base64.b64encode(flag_bytes)

#text = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
#text is in decimal/numeric format aka base10 and base16 is concatenation of resp. hex values then to ascii then text.
#Above long inpleemtiation is done via long_to_bytes in pycryptodome module.
#print(base)
#flag = long_to_bytes(text)

#print(flag)