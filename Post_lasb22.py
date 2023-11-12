import random as rs
import numpy as np
n = int(input("Please enter the length fo your vector\n"))
mat1 = np.zeros(n)
for i in range(0,n,1):
    w=1
    while(w>0):
        d = int(rs.randint(1,5))
        if(d>5):
            w=1
        elif(d<1):
            w=1
        else:
            mat1[i] = d
            w=0
print(mat1)

import numpy as np
n = (int)(input("Please enter the number of row of your matrix\n"))
k = (int)(input("Please enter the number of column of your matrix\n"))
mat2 = np.zeros((n,k))
print("Please enter the elements of given dimensions:")
for i in range(0,n,1):
    print("Please enter the elements of row: ",end='')
    print(i)
    for j in range(0,k,1):
            print("Please enter the ",end='')
            print(j,end='')
            print("th element")
            s = (int)(input())
            mat2[i][j] = s

for i in range(0,k,1):
    print(mat2[n-1][i])