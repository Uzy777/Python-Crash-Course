# Generating Data - Plotting a Simple Line Graph - Saving Your Plots Automatically

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig('Chapter 15: Generating Data/15.2 Plotting a Simple Line Graph/15.2.10 Saving Your Plots Automatically/squares_plot.png', bbox_inches='tight')