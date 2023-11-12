import numpy as np
#Creating a Matrix

# Create a 2x3 matrix with random values
matrix_a = np.random.random((2, 3))
print("Matrix A:")
print(matrix_a)

# Addition of two matrices
matrix_b = np.random.random((2, 3))
sum_matrix = matrix_a + matrix_b
print("\nSum of Matrix A and Matrix B:")
print(sum_matrix)

# Multiplication of two matrices (element-wise)
product_matrix = matrix_a * matrix_b
print("\nElement-wise Product of Matrix A and Matrix B:")
print(product_matrix)

# Matrix multiplication (dot product)
matrix_c = np.random.random((3, 2))
dot_product_matrix = np.dot(matrix_a, matrix_c)
print("\nMatrix Multiplication of Matrix A and Matrix C:")
print(dot_product_matrix)

# Access an element in the matrix
element = matrix_a[1, 2]
print("\nElement at row 2, column 3 in Matrix A:", element)

# Transpose of a matrix
transpose_matrix_a = np.transpose(matrix_a)
print("\nTranspose of Matrix A:")
print(transpose_matrix_a)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:")
print(identity_matrix)

# Create a square matrix
square_matrix = np.random.random((3, 3))

# Calculate the inverse of the matrix
inverse_matrix = np.linalg.inv(square_matrix)
print("\nInverse of Square Matrix:")
print(inverse_matrix)

