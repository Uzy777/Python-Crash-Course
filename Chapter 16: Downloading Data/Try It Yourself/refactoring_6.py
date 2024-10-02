# 16-6. Refactoring:        The loop that pulls data from 'all_eq_dicts' uses variables for the magnitude, longitude, latitude,
#                           and little of each earthquake before appending these values to their appropriate lists.
#                           This approach was chosen for clarity in how to pull data from a GeoJSON file, but it's not necessary in your code.
#                           Instead of using these temporary variables, pull each value from eq_dict and append it to the appropriate list in one line.
#                           Doing so should shorten the body of this loop to just four lines.

from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

print(mags[:10])
print(lons[:5])
print(lats[:5])