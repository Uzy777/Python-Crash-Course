# Generating Data - Rolling Dice with Plotly - Making a Histogram

import plotly.express as px

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyse the results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
fig = px.bar(x=poss_results, y=frequencies)
fig.show()


print(frequencies)
