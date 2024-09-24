# 15-2. Coloured Cubes:     Apply a colourmap to your cubes plot.

import matplotlib.pyplot as plt

x_values_1 = range(1, 6)
y_values_1 = [x**3 for x in x_values_1]

x_values_2 = range(1, 5001)
y_values_2 = [x**3 for x in x_values_2]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color='red', s=10)
ax.scatter(x_values_1, y_values_1, c=y_values_1, cmap=plt.cm.Blues, s=50, label="First 5 Cubic Numbers")
ax.scatter(x_values_2, y_values_2, c=y_values_2, cmap=plt.cm.Reds, s=10, label="First 5000 Cubic Numbers")

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 5100, 0, 130_000_000_000])  # Adjusted to fit the large cubic values
ax.legend()
plt.show()