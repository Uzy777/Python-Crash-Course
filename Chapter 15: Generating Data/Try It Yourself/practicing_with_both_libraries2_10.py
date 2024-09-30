# 15-10. Practising with Both Libraries:        Try using Matplotlib to make a die-rolling visualisation, and use Plotly
#                                               to make the visualisation for a random walk. (You'll need to consult
#                                               the documentation for each library to complete this exercise.)

import random
import plotly.express as px

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate points for the walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """Determine the direction and distance of a step."""
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2, 3, 4])
        return direction * distance

# Make a random walk and plot the points using Plotly.
random_walk = RandomWalk()
random_walk.fill_walk()

# Visualize the walk using Plotly.
fig = px.scatter(x=random_walk.x_values, y=random_walk.y_values,
                 title="Random Walk Visualization", labels={'x': 'X', 'y': 'Y'},
                 width=800, height=800)

# Show the plot.
fig.show()
