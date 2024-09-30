# 15-9. Die Comprehensions:     For clarity, the listings in this section use the long form of for loops.
#                               If you're comfortable using list comprehensions, try writing a comprehension
#                               for one or both of the loops in each of these programs.

import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]


# Analyse the results.
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualise the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customise chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)
