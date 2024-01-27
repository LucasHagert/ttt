import numpy as np
import matplotlib.pyplot as plt

# Load the saved numpy file
file_name = "1.npy"  # Provide the name of your saved file here
points = np.load(file_name)

# Extract x, y coordinates and values
x = points[:, 0]
y = points[:, 1]
values = points[:, 2]

# Plot the points
plt.figure()
for i in range(len(x)):
    if values[i] == 1:
        plt.scatter(x[i], y[i], color='red', label='Value 1')
    elif values[i] == 2:
        plt.scatter(x[i], y[i], color='green', label='Value 2')
    elif values[i] == 3:
        plt.scatter(x[i], y[i], color='blue', label='Value 3')

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Scatter Plot of Points')
plt.grid(True)
plt.legend()
plt.show()