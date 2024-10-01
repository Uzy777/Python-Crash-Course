# Downloading Data - The CSV File Format - Downloading Your Own Data

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(
    "/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/cardiff-bute-park.csv"
)
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, max temperatures, min temperatures, and rainfall.
years, months, tmax, tmin, rain = [], [], [], [], []
for row in reader:
    row = [item.strip() for item in row]  # Remove leading/trailing spaces from each row

    try:
        # Parse the data
        year = int(row[0])  # Parse the year
        month = int(row[1])  # Parse the month
        max_temp = float(row[2]) if row[2] != "---" else None  # Handle missing data
        min_temp = float(row[3]) if row[3] != "---" else None  # Handle missing data
        rainfall = float(row[5]) if row[5] != "---" else None  # Handle missing data

        # Append parsed data to the respective lists
        years.append(year)
        months.append(month)
        tmax.append(max_temp)
        tmin.append(min_temp)
        rain.append(rainfall)

    except ValueError:
        # Skip rows with invalid data
        print(f"Skipping row: {row}")

# Create a list of datetime objects for plotting
dates = [datetime(year, month, 1) for year, month in zip(years, months)]


# Plotting the temperatures (max and min)
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, tmax, color="green", label="Max Temp (°C)")
ax.plot(dates, tmin, color="red", label="Min Temp (°C)")

# Format plot.
ax.set_title("Cardiff Bute Park - Temperature Over Time", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

# Show the plot
plt.show()
