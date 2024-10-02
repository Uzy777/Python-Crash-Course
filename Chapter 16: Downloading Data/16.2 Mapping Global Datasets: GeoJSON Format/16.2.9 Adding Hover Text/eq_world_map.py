# Downloading Date - Mapping Global Datasets: GeoJSON Format - Adding Hover Text

from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path(
    "/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/eq_data_30_day_m1.geojson"
)
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

print(mags[:10])
print(lons[:5])
print(lats[:5])


title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
