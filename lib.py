import numpy as np
m1 = np.array([1,2,3])
m2 = np.array([[4],[5],[6]])
sum1 = (m1+m2)
print(sum1)

prod1 = (m1*m2)
print(prod1)

m22 = np.array([[0,0],[1,1]])
print(m22)

m33 = np.array([[[0,0,0],[1,1,1],[2,2,2]],[[0],[1]]])
print(m33[[2],[1],[1]])

m14 = np.array([[0],[1],[2],[3]])
print(m14)

m42 = np.array([[0,0],[1,1],[2,2],[3,3]])
print(m42)

print(m22.ndim)

print(m33.transpose())
if(np.linalg.det(m22)==0):
    	{
 print("Inverse cannot be found")
 }
else:
            {
                print(np.linalg.inv(m22))
                }
print(m42.flatten())

#Extracting Row/Column
np.array
