
#Task1: Matrix flattening.
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_array = matrix.flatten()
print("Flattened Array:", flattened_array)
#Output: 
 
#Task2: Numpy array iterating.
arr = np.array([1, 2, 3, 4, 5])
for element in arr:
    print(element)
#Output: 
 

#Task3: Dimensions of an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
dimensions = arr.shape
print("Dimensions of the Array:", dimensions)
#Output: 
 
#Task4: Item size and random and mean in an array
arr = np.array([1, 2, 3, 4, 5])
item_size = arr.itemsize
random_values = np.random.rand(5)
mean_value = np.mean(arr)
print("Item Size:", item_size)
print("Random Values:", random_values)
print("Mean Value:", mean_value)
#Output: 
