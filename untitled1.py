#broadcasting
import numpy as np
a1 = np.array([1,2,3])
a2 = np.array([[1],[2],[3]])
sum = a1+a2
print("a1 = ",a1)
print("a2 = ",a2)
print("broadcasted sum =>")
print(sum,end='\n\n')


# numpy 2d array
print("2d array and it's funcitons ")
print('--------------------------- \n')
a22 = np.array([[1,1],[2,2]])
print('first matrix = ',end = '\n')
print(a22)
A22 = np.array([[1,1],[2,2]])
print('second matrix =',end = '\n' )
print(A22,end = '\n\n')
multiply2matrices = np.dot(a22,A22)
print('result after dot product')
print(multiply2matrices)
print('--------------------------- \n')

