from math import gcd


#def computeGCD(x, y): 
#   while(y): 
#       x, y = y, x % y 
#   return x 
#print(computeGCD(66528, 52920))
#def egcd(a, b):
#    x,y, u,v = 0,1, 1,0
#    while a != 0:
#        q, r = b//a, b%a
#        m, n = x-u*q, y-v*q
#        b,a, x,y, u,v = a,r, u,v, m,n
#    gcd = b
#   return gcd, x, y

#print(egcd(26513,32321))

#flag = pow(12,65537,391)

def phi(n): 
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

p= 857504083339712752489993810776
q= 1029224947942998075080348647218
text = p*q
#flag = phi(text)
print(text)

from Crypto.PublicKey import RSA

f = open('public.pem','r')
key = RSA.importKey(f.read())
print(key.n)
print(key.e)

#openssl x509 -in 2048b-rsa-example-cert.der -inform der -text -noout -modulus