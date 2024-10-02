# 16-7. Automated Title:        In this section, we used the generic title 'Global Earthquakes'.
#                               Instead, you can use the title for the dataset in the metadata part of the GeoJSON file.
#                               Pull this value and assign it to the variable 'title'.

from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
metadata = all_eq_data['metadata']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


title = metadata['title']
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()