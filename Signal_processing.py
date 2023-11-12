import matplotlib.pyplot as plt
import numpy as np

# Task 1: Adding Title to Subplots Using set_title() method
fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title("Subplot 1")
axs[0, 1].set_title("Subplot 2")
axs[1, 0].set_title("Subplot 3")
axs[1, 1].set_title("Subplot 4")

# Task 2: Using title.set_text() method
axs[0, 0].title.set_text("New Title for Subplot 1")

# Task 3: Using plt.gca().set_title() method
plt.gca().set_title("Title for Current Axes")

# Task 4: Using plt.gca().title.set_text() method
plt.gca().title.set_text("New Title for Current Axes")

# Task 5: Setting a Single Title for All the Subplots Example - 1
fig.suptitle("Common Title for All Subplots")

# Task 6: Setting a Single Title for All the Subplots Example - 2
fig.suptitle("Common Title for All Subplots", fontsize=16, color='red')

# Task 7: Turn Off the Axes for Subplots Using matplotlib.axes.Axes.axis()
axs[0, 0].axis('off')

# Task 8: Turn Off the Axes for Subplots Using matplotlib.pyplot.axis()
plt.axis('off')

# Task 9: Create Different Subplot Sizes in Matplotlib subplot2grid
fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax1.set_title("Subplot 1")
ax2.set_title("Subplot 2")
ax3.set_title("Subplot 3")
ax4.set_title("Subplot 4")
ax5.set_title("Subplot 5")

# Task 10: Create Different Subplot Sizes in Matplotlib subplot2grid with additional customization
fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax1.set_title("Subplot 1")
ax2.set_title("Subplot 2")
ax3.set_title("Subplot 3")
ax4.set_title("Subplot 4")
ax5.set_title("Subplot 5")

# Task 11: Using tight_layout() to set spacing between subplots
fig, axs = plt.subplots(2, 2)
plt.tight_layout(pad=2.0)

# Task 12: Using pad to set spacing between subplots
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(hspace=0.4, wspace=0.4)

plt.show()
