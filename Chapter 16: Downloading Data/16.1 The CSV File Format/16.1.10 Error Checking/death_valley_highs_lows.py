# Downloading Data - The CSV File Format - Error Checking

from pathlib import Path
import csv

path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)