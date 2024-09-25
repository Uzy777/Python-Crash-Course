# 15-3. Molecular Motion:       Modify 'rw_visual'.py by replacing 'ax.scatter()' with 'ax.plot()'.
#                               To simulate the path of a pollen grain on the surface of a drop of water,
#                               pass in the 'rw.x_values' and 'rw.y_values', and include a 'linewidth' argument.
#                               Use 5,000 instead of 50,000 points to keep the plot from being too busy.

import matplotlib.pyplot as plt
from random_walk import RandomWalk  # Assuming you have a RandomWalk class defined

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk with 5,000 points instead of 50,000.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=100)
    
    # Use ax.plot() to plot the path with linewidth.
    ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')

    # Emphasize the first and last points.
    ax.plot(0, 0, marker='o', c='green', markersize=10)  # First point
    ax.plot(rw.x_values[-1], rw.y_values[-1], marker='o', c='red', markersize=10)  # Last point

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
