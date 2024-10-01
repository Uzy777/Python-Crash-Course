# 16-4. Automatic Indexes:      In this section, we hardcoded the indexes corresponding to the 'TMIN' and 'TMAX' columns.
#                               Use the header row to determine the indexes for these values, so your program can work
#                               for Sitka or Death Valley. Use the station name to automatically generate an appropriate
#                               title for your graph as well.


from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Path to the weather data (modify as needed).
path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding="utf-8").splitlines()

# Read the CSV file.
reader = csv.reader(lines)
header_row = next(reader)

# Automatically find the indexes for 'TMIN' and 'TMAX' and the station name.
tmin_index = header_row.index('TMIN')
tmax_index = header_row.index('TMAX')
station_name = header_row[1]  # Assuming the station name is in the second column.

# Extract dates and temperature data.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")  # Assuming date is in column 3.
    try:
        high = int(row[tmax_index])
        low = int(row[tmin_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title(f"Daily High and Low Temperatures, 2021\n{station_name}", fontsize=24)
ax.set_xlabel("Date", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
