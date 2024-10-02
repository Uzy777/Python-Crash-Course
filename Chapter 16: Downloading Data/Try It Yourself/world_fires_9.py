# 16-9. World Fires:        In the resources for this chapter, you'll find a file called 'world_fires_1_day.csv'.
#                           This file contains information about fires burning in different locations around the globe,
#                           including the latitude, longitude, and brightness of each fire. Using the data-processing work from
#                           the first part of this chapter and the mapping work from this section, make a map that shows which parts of the world are affected by fires.
#
#                           You can download more recent versions of this data at https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data
#                           You can find links to the data in CSV format in the SHP, KML, and TXT Files section.

from pathlib import Path
import csv

import plotly.express as px

# Path to CSV file
path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/world_fires_1_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract required data from CSV.
latitudes, longitudes, brightnesses = [], [], []
for row in reader:
    latitude = float(row[0])
    longitude = float(row[1])
    brightness = float(row[2])

    latitudes.append(latitude)
    longitudes.append(longitude)
    brightnesses.append(brightness)

print(latitudes[:10])
print(longitudes[:10])
print(brightnesses[:10])


title = 'Map of Global Fires Around the World'
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightnesses, color=brightnesses)
fig.show()



# USE BRIGHTNESS TO DICTATE THE COLOUR STRENGTH FOR EACH PLOT!!!!!!



# # Read data as a string and convert to a Python object.
# path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/eq_data_1_day_m1.geojson')
# contents = path.read_text(encoding='utf-8')
# all_eq_data = json.loads(contents)

# # Examine all earthquakes in the dataset.
# all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)



# title = 'Global Earthquakes'
# fig = px.scatter_geo(lat=lats, lon=lons, title=title)
# fig.show()
