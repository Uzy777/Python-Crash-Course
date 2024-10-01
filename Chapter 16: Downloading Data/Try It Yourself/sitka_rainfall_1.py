# 16-1. Sitka Rainfall:     Sitka is located in a temperate rainforest, so it gets a fair amount of rainfall.
#                           In the data file 'sitka_weather_2021_full.csv' is a header called 'PRCP', which
#                           represents daily rainfall amounts. Make a visualisation focussing on the data in this column.
#                           You can repeat the exercise for Death Valley if you're curious how little rainfall occurs in a dessert.

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(
    "/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/sitka_weather_2021_full.csv"
)
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, and high and low temperatures.
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        prcps.append(prcp)

print(prcps)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, prcps, color="red", alpha=0.5)


# Format plot.
ax.set_title("Sitka Rainfall for Year - 2021", fontsize=24)
ax.set_xlabel("Date", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
