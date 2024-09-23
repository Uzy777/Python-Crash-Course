# 15-1. Cubes:      A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5,000 cubic numbers.

import matplotlib.pyplot as plt

x_values_1 = range(1, 6)
y_values_1 = [x**3 for x in x_values_1]

x_values_2 = range(1, 5001)
y_values_2 = [x**3 for x in x_values_2]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color='red', s=10)
ax.scatter(x_values_1, y_values_1, color='blue', s=10)
ax.scatter(x_values_2, y_values_2, color='red', s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()