#pylint:disable=W0614

#p = 29
#ints = [14, 6, 11]
#for i in range(1,p):
#    for j in ints:
#        result = pow(i,2,j)
#        if result == p:
#            print(i)
#            print(j)
#            print()
#        else:
#            pass
modulus = 29
a = 6
QR = 0

#for b in range(1,((modulus-1)/2) + 1):
#    if (b ** 2) % modulus == a:
#        QR = 1
#
#if (QR == 1):
#    print("{} is a QR mod {}").format(a, modulus)
#else:
#    print("{} is a QNR mod {}").format(a, modulus)
#
s = pow(a, (modulus+1)//4 , modulus)
print(s)