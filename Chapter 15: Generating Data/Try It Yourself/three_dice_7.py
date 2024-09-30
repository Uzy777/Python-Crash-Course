# 15-7. Three Dice:     When you roll three D6 dice, the smallest number you can roll is 3
#                       and the largest number is 18. Create a visualisation that shows
#                       what happens when you roll three D6 dice.

import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyse the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
title = "Results of Rolling Three D6 Dice 100 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)

# Further customise chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)