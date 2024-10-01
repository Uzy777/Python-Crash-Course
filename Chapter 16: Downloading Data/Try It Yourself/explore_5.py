# 16-5. Explore:        Generate a few more visualisation that examine any other weather aspect you're interested in for any locations you're curious about.

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Load Cardiff weather data.
cardiff_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/cardiff_weather_2023.csv')
cardiff_lines = cardiff_path.read_text(encoding="utf-8").splitlines()

cardiff_reader = csv.reader(cardiff_lines)
cardiff_header_row = next(cardiff_reader)

cardiff_dates, cardiff_highs, cardiff_lows = [], [], []
for row in cardiff_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    try:
        high = float(row[3])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for Cardiff {current_date}")
    else:
        cardiff_dates.append(current_date)
        cardiff_highs.append(high)
        cardiff_lows.append(low)

# Load London weather data.
london_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/london_weather_2023.csv')
london_lines = london_path.read_text(encoding="utf-8").splitlines()

london_reader = csv.reader(london_lines)
london_header_row = next(london_reader)

london_dates, london_highs, london_lows = [], [], []
for row in london_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    try:
        high = float(row[3])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for London {current_date}")
    else:
        london_dates.append(current_date)
        london_highs.append(high)
        london_lows.append(low)



# Load Birmingham weather data.
birmingham_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/birmingham_weather_2023.csv')
birmingham_lines = birmingham_path.read_text(encoding="utf-8").splitlines()

birmingham_reader = csv.reader(birmingham_lines)
birmingham_header_row = next(birmingham_reader)

birmingham_dates, birmingham_highs, birmingham_lows = [], [], []
for row in birmingham_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    try:
        high = float(row[3])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for Birmingham {current_date}")
    else:
        birmingham_dates.append(current_date)
        birmingham_highs.append(high)
        birmingham_lows.append(low)

# Plot all datasets.
plt.style.use("seaborn-v0_8")
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Plot Cardiff temperatures.
ax1.plot(cardiff_dates, cardiff_highs, color="red", alpha=0.5)
ax1.plot(cardiff_dates, cardiff_lows, color="blue", alpha=0.5)
ax1.fill_between(cardiff_dates, cardiff_highs, cardiff_lows, facecolor="blue", alpha=0.1)
ax1.set_title("Daily High and Low Temperatures - 2023\nCardiff", fontsize=20)
ax1.set_ylabel("Temperature (C)", fontsize=16)
ax1.tick_params(labelsize=12)

# Plot London temperatures.
ax2.plot(london_dates, london_highs, color="red", alpha=0.5)
ax2.plot(london_dates, london_lows, color="blue", alpha=0.5)
ax2.fill_between(london_dates, london_highs, london_lows, facecolor="blue", alpha=0.1)
ax2.set_title("Daily High and Low Temperatures - 2023\nLondon", fontsize=20)
ax2.set_xlabel("Date", fontsize=16)
ax2.set_ylabel("Temperature (C)", fontsize=16)
ax2.tick_params(labelsize=12)

# Plot Birmingham temperatures.
ax3.plot(birmingham_dates, birmingham_highs, color='red', alpha=0.5)
ax3.plot(birmingham_dates, birmingham_lows, color='blue', alpha=0.5)
ax3.fill_between(birmingham_dates, birmingham_highs, birmingham_lows, facecolor='blue', alpha=0.1)
ax3.set_title("Daily High and Low Temperatures - 2023\nBirmingham", fontsize=20)
ax3.set_xlabel("Date", fontsize=16)
ax3.set_ylabel("Temperature (C)", fontsize=16)
ax3.tick_params(labelsize=12)

# Set identical y-axis limits for both plots.
ax1.set_ylim(-10, 35)  # You can adjust these limits based on the temperature range.
ax2.set_ylim(-10, 35)
ax3.set_ylim(-10, 35)

# Automatically format the date labels for better readability.
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
