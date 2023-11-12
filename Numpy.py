#Task1: Matrix 4X4 checkerboard.
import numpy as np
checkerboard = np.zeros((4, 4), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print("4x4 Checkerboard Matrix:")
print(checkerboard)
#Output:
 
#Task2: Using nditer and split function.
arr = np.array([[1, 2], [3, 4], [5, 6]])
for x in np.nditer(arr):
    print(x, end=' ')
split_arrays = np.split(arr, 3)
print("\nSplit Arrays:")
for split_arr in split_arrays:
    print(split_arr)
#Output:
 
#Task3: Searching and sorting arrays.
arr = np.array([3, 1, 4, 2, 5])
element_to_search = 4
index = np.where(arr == element_to_search)
sorted_arr = np.sort(arr)
print("Index of", element_to_search, ":", index)
print("Sorted Array:", sorted_arr)
#Output:
 
#Task4: File handling.
arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)
loaded_arr = np.load('my_array.npy')
print("Loaded Array:", loaded_arr)
#Output:
 

