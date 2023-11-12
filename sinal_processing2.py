import numpy as np
import matplotlib.pyplot as plt

# Task 1: Generate random values using numpy
np.random.seed(42)  # Setting a seed for reproducibility
num_points = 100
x_values = np.linspace(0, 10, num_points)  # Generating x values

# Generating three sets of random y values
y_values1 = np.random.rand(num_points)
y_values2 = np.random.rand(num_points)
y_values3 = np.random.rand(num_points)

# Task 2: Represent data using a combination of line plots
plt.figure(figsize=(10, 6))

# Plotting the first line
plt.plot(x_values, y_values1, label='Line 1', linestyle='-', marker='o', color='blue')

# Plotting the second line
plt.plot(x_values, y_values2, label='Line 2', linestyle='--', marker='s', color='green')

# Plotting the third line
plt.plot(x_values, y_values3, label='Line 3', linestyle=':', marker='^', color='red')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Combination of Line Plots with Random Data')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
