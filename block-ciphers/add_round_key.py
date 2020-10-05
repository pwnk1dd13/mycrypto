state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

import numpy as np

a = np.bitwise_xor(state,round_key)

#def add_round_key(s, k):
#    #flag = ""
#    for i in range(0,4):
#        for k in range(0,4):
#            a = s[i][k]
#            b = k[i][k]
#            #flag += s[i][k] ^ k[i][k]
#            print(a,b)



#def matrix2bytes(matrix):
#    return bytes(sum(matrix, []))
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    flag = ""
    for i in range(0, 4):
        for k in range(0,4):
            flag += chr(matrix[i][k])
        
    return flag

#print(add_round_key(state, round_key))
#print(str(matrix2bytes(matrix).decode('utf-8')))
print(a)
print(matrix2bytes(a))