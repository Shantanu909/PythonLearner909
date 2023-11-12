import numpy as np
arr = np.array([1,3,3,4,5,3,7,8,3])
print(arr)

arr2 = np.array([0,10,10,5,0,0,0,0,0])
"""
arr2d = np.array([[1,2,3],[0,9,1,2],[0,1,2,3,4]],dtype=object)
print(f"hi\n{arr2d}"),

rando = np.random.randint(0,1000000)
print(rando)

arr3 = np.vstack(arr)
print(arr3)
arr4 = np.hstack(arr)
print(arr4)"""

arr6 = np.intersect1d(arr, arr2)
print(arr6)
arr7 = np.setdiff1d(arr, arr2)
print(arr7)

