#Task1: numpy ndim( ) function.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
ndim_value = arr.ndim
print(ndim_value)
#Output:
 
#Task2: numpy itemsize( ), dtype( )  function.
arr = np.array([1, 2, 3, 4], dtype=np.float64)
itemsize_value = arr.itemsize
dtype_value = arr.dtype
print("Item Size:", itemsize_value)
print("Data Type:", dtype_value)
#Output:
 
#Task3: numpy slicing, randm, mean function.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
sliced_array = arr[2:6]
random_array = np.random.rand(5)

mean_value = np.mean(arr)
print("Sliced Array:", sliced_array)
print("Random Array:", random_array)
print("Mean Value:", mean_value)
#Output:
 
#Task4: numpy append, insert function.
arr = np.array([1, 2, 3])
appended_array = np.append(arr, 4)
inserted_array = np.insert(arr, 1, 5)
print("Appended Array:", appended_array)
print("Inserted Array:", inserted_array)
#Output:
 
#Task5: numpy elementwise mathematical operations.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
addition_result = arr1 + arr2
multiplication_result = arr1 * arr2
print("Elementwise Addition:", addition_result)
print("Elementwise Multiplication:", multiplication_result)
#Output:
 

#Task6: Adding arrays of different dimensions
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])
result = arr1 + arr2
print("Result of Adding Arrays of Different Dimensions:")
print(result)
#Output:
