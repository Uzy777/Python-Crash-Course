# 15-8. Multiplication:     When you roll two dice, you usually add the two numbers together to get the result.
#                           Create a visualisation that shows what happens if you multiply these numbers by each other instead.

import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results.
frequencies = []
max_results = die_1.num_sides * die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
title = "Results of Rolling Two D6 Dice 1,000 Times Using Multiplication"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)

# Further customise chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)