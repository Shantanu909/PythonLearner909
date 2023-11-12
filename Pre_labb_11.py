
#Create a user deifned Array 
import numpy as np
n = (int)(input("Please enter the number of row of a square matrix\n"))
print(n)
mat1 = np.zeros((n,n))
print("Please enter the elements of given dimensions:")
for i in range(0,n,1):
    print("Please enter the elements of row: ",end='')
    print(i)
    for j in range(0,n,1):
        w=1
        while(w>0):
            print("Please enter the ",end='')
            print(j,end='')
            print("th element")
            s = (int)(input())
            if(s<2):
                print("invalid input, please enter number within 2:10")
            elif(s>10):
                    print("Invalid input")
                    print("invalid input, please enter number within 2:10")
            else:
                mat1[i][j] = s
                w =0
print(mat1)


#Change the element ar a particular index in a vector
n = (int)(input("Please enter the length of your vector\n"))
mat2 = np.zeros(n)
print("Please enter the position you want to exchange ",end='')
temp_n = (int)(input())
print("Please enter the new number")
temp_a = int(input())
mat2[temp_n] = temp_a        
print(mat2)


#Checkboard fashioned output
n = (int)(input("Please enter the number of row of a square matrix\n"))
print(n)
mat3 = np.zeros((n,n))
count = False
for i in range(0,n,1):
    count = not(count)
    for j in range(0,n,1):  
        count = not(count)
        if(count == False):
            mat3[i][j] = 0 
        else:
            mat3[i][j] = 1
print(mat3)
