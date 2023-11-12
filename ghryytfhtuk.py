import matplotlib.pyplot as plt
import numpy as np




# Generate some sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, label='Sine Wave', linestyle='--', color='b')

# Add labels and a title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Basic Plot')

# Add a legend
ax.legend()

# Customize the axes limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Add grid lines
ax.grid(True)

# Add text annotation
ax.text(2, 0.5, 'Annotation Example', fontsize=12, color='r')



# Add arrow annotation
ax.annotate('Arrow Annotation', xy=(3, 0), xytext=(4, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Add a subplot
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, np.cos(x), label='Cosine Wave', color='g')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_title('Second Plot')
ax2.legend()

# Save the figure as an image
plt.savefig('basic_plot.png')

# Show the plot
plt.show()
