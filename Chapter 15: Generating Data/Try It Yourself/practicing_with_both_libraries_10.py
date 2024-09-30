# 15-10. Practising with Both Libraries:        Try using Matplotlib to make a die-rolling visualisation, and use Plotly
#                                               to make the visualisation for a random walk. (You'll need to consult
#                                               the documentation for each library to complete this exercise.)

import matplotlib.pyplot as plt
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Roll the dice 1000 times and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyse the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results using Matplotlib.
plt.figure(figsize=(10, 6))
plt.bar(range(2, max_result+1), frequencies, color='skyblue')

# Customize the chart.
plt.title('Results of Rolling Two D6 Dice 1,000 Times', fontsize=14)
plt.xlabel('Result', fontsize=12)
plt.ylabel('Frequency of Result', fontsize=12)
plt.xticks(range(2, max_result+1))

# Show the plot.
plt.show()
