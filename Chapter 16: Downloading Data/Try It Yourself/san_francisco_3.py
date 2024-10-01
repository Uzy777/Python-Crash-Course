# 16-3. San Francisco:      Are temperatures in San Francisco more like temperatures in Sitka or temperatures in Death Valley?
#                           Download some data for San Francisco, and generate a high-low temperature plot for San Francisco to make a comparison. 

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Load Sitka weather data.
sitka_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/sitka_weather_2021_simple.csv')
sitka_lines = sitka_path.read_text(encoding="utf-8").splitlines()

sitka_reader = csv.reader(sitka_lines)
sitka_header_row = next(sitka_reader)

sitka_dates, sitka_highs, sitka_lows = [], [], []
for row in sitka_reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for Sitka {current_date}")
    else:
        sitka_dates.append(current_date)
        sitka_highs.append(high)
        sitka_lows.append(low)

# Load Death Valley weather data.
dv_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/death_valley_2021_simple.csv')
dv_lines = dv_path.read_text(encoding="utf-8").splitlines()

dv_reader = csv.reader(dv_lines)
dv_header_row = next(dv_reader)

dv_dates, dv_highs, dv_lows = [], [], []
for row in dv_reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for Death Valley {current_date}")
    else:
        dv_dates.append(current_date)
        dv_highs.append(high)
        dv_lows.append(low)



# Load San Francisco weather data.
sf_path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/san_francisco_weather_2021.csv')
sf_lines = sf_path.read_text(encoding="utf-8").splitlines()

sf_reader = csv.reader(sf_lines)
sf_header_row = next(sf_reader)

sf_dates, sf_highs, sf_lows = [], [], []
for row in sf_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    try:
        high = float(row[3])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for San Francisco {current_date}")
    else:
        sf_dates.append(current_date)
        sf_highs.append(high)
        sf_lows.append(low)

# Plot all datasets.
plt.style.use("seaborn-v0_8")
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Plot Sitka temperatures.
ax1.plot(sitka_dates, sitka_highs, color="red", alpha=0.5)
ax1.plot(sitka_dates, sitka_lows, color="blue", alpha=0.5)
ax1.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.1)
ax1.set_title("Daily High and Low Temperatures - 2021\nSitka, AK", fontsize=20)
ax1.set_ylabel("Temperature (F)", fontsize=16)
ax1.tick_params(labelsize=12)

# Plot Death Valley temperatures.
ax2.plot(dv_dates, dv_highs, color="red", alpha=0.5)
ax2.plot(dv_dates, dv_lows, color="blue", alpha=0.5)
ax2.fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.1)
ax2.set_title("Daily High and Low Temperatures - 2021\nDeath Valley, CA", fontsize=20)
ax2.set_xlabel("Date", fontsize=16)
ax2.set_ylabel("Temperature (F)", fontsize=16)
ax2.tick_params(labelsize=12)

# Plot San Francisco temperatures.
ax3.plot(sf_dates, sf_highs, color='red', alpha=0.5)
ax3.plot(sf_dates, sf_lows, color='blue', alpha=0.5)
ax3.fill_between(sf_dates, sf_highs, sf_lows, facecolor='blue', alpha=0.1)
ax3.set_title("Daily High and Low Temperatures - 2021\nSan Francisco, CA", fontsize=20)
ax3.set_xlabel("Date", fontsize=16)
ax3.set_ylabel("Temperature (F)", fontsize=16)
ax3.tick_params(labelsize=12)

# Set identical y-axis limits for both plots.
ax1.set_ylim(0, 80)  # You can adjust these limits based on the temperature range.
ax2.set_ylim(0, 130)
ax3.set_ylim(0, 30)

# Automatically format the date labels for better readability.
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
