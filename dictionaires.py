#Task1: numpy Library implementation with different functionalities.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
max_value = np.max(arr)
min_value = np.min(arr)
print("Mean:", mean_value)
print("Max:", max_value)
print("Min:", min_value)
#Output:
 
#Task2: numpy Library implementation with different functionalities.
arr = np.array([5, 10, 15, 20, 25])
sum_value = np.sum(arr)
square_root = np.sqrt(arr)
print("Sum:", sum_value)
print("Square Root:", square_root)
#Output:
 
#Task3&4: numpy intersection, difference and add. And hstack and vstack
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
intersection = np.intersect1d(arr1, arr2)
difference = np.setdiff1d(arr1, arr2)
addition = np.add(arr1, arr2)
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6]])
hstack_result = np.hstack((arr3, arr4))
vstack_result = np.vstack((arr3, arr4))
print("Intersection:", intersection)
print("Difference:", difference)
print("Addition:", addition)
print("Horizontal Stack:")
print(hstack_result)
print("Vertical Stack:")
print(vstack_result)
#Output: 
 
#Task5: numpy basic mathematics.
arr = np.array([1, 2, 3, 4, 5])
squared = np.square(arr)
cubed = np.power(arr, 3)
log_values = np.log(arr)
exponential_values = np.exp(arr)
print("Squared:", squared)
print("Cubed:", cubed)
print("Logarithmic Values:", log_values)
print("Exponential Values:", exponential_values)
#Output:
