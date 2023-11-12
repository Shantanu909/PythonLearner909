import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()

ax.plot(x, y, label='Sine Wave', linestyle='--', color='b')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Basic Plot')
ax.legend()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)
ax.grid(True)
ax.text(2, 0.5, 'Annotation Example', fontsize=12, color='r')
ax.annotate('Arrow Annotation', xy=(3, 0), xytext=(4, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, np.cos(x), label='Cosine Wave', color='g')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_title('Second Plot')
ax2.legend()

plt.savefig('basic_plot.png')
plt.show()
